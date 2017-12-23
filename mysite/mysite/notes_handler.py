from notes_dao import NotesDAO
from transactional_manager import TransactionalManager
from datetime import datetime,date
import logging
logging.basicConfig(filename='notes.log', filemode='w', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class NotesHandler(object):
    """
        Handler class to perform logics and computations on Notes data
    """
    def __init__(self):
        """
            Initializes connection object to handle DB operations based on logic
        """
        self.transaction_obj = TransactionalManager()
        self.db_conn = self.transaction_obj.get_database_connection()
    
    def get_active_notes(self):
        """ 
            Method to fetch all the active notes
        """
        try:
            dao_obj=NotesDAO(self.db_conn)
            note_records=dao_obj.fetch_active_notes()
            self.transaction_obj.save()
            self.transaction_obj.end()
            return {'notes':note_records}
        except Exception as ex:
            logging.exception("Exception encountered while fetching active Notes"+ str(ex))
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            raise

    def get_new_note_id(self):
        """
            Method to generate and return id for a new note
        """
        try:
            dao_obj=NotesDAO(self.db_conn)
            note_dict={'note_title':'NOTE TITLE',
                       'note_content':''
                       }
            new_note_id=dao_obj.insert_note(note_dict)
            self.transaction_obj.save()
            self.transaction_obj.end()
            return {'note_id':new_note_id}
        except Exception as ex:
            logging.info("Exception encountered while fetching New note id"+ str(ex))
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            raise
        
    def add_note(self,note_dict):
        """
        :brief Method to add a new note
        :param note_dict: Dictionary containing note details
        :type note_dict : Dictionary

        """
        
        try:
            dao_obj=NotesDAO(self.db_conn)
            note_records=dao_obj.insert_note(note_dict)
            self.transaction_obj.save()
            self.transaction_obj.end()
            return note_records
        except Exception as ex:
            logging.exception("Exception encountered while adding new Note :%s"%ex)
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            raise
        
    def update_note(self,note_dict):
        """
        :brief Method to update an existing note
        :param note_dict: Dictionary containing note details
        :type note_dict : Dictionary
        """
        try:
            dao_obj=NotesDAO(self.db_conn)
            note_id=note_dict['note_id']
            dao_obj.create_note_history(note_id)
            dao_obj.update_note(note_dict)
            self.transaction_obj.save()
            self.transaction_obj.end()
            return 'SUCCESS'
        except Exception as ex:
            print ex
            logging.exception("Exception encountered while updating existing Note :%s" %ex)
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            return 'FAILURE'
        
    def remove_note(self,note_dict):
        """
        :brief Method to delete an existing note
        :param note_dict: Dictionary containing note details
        :type note_dict : Dictionary

        """
        try:
            dao_obj=NotesDAO(self.db_conn)
            note_id=note_dict['note_id']
            dao_obj.create_note_history(note_id)
            dao_obj.delete_note(note_id)
            self.transaction_obj.save()
            self.transaction_obj.end()
            return 'SUCCESS'
        except Exception as ex:
            logging.exception("Exception encountered while fetching removing Notes: %s"%ex)
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            return 'FAILURE'
        
    def get_history(self,note_id):
        """
        :brief Method to fetch the history versions of a particular note
        :param note_id: Unique id of a note
        :type note_id : Integer
        """
        try:
            dao_obj=NotesDAO(self.db_conn)
            history_records=dao_obj.fetch_history(note_id)
            for record in history_records:
                for key,value in record.iteritems():
                    if isinstance(value, (datetime, date)):
                        record[key]=str(value)
            self.transaction_obj.save()
            self.transaction_obj.end()
            logging.info('NOTES HISTORY %s'%history_records)
            return history_records
        except Exception as ex:
            logging.exception("Exception encountered while getting version history of Notes :%s"%ex)
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            return 'FAILURE'
    
    def get_history_content(self,note_history_id):  
        """
        :brief Method to fetch Note details of a particular version
        :param note_history_id: Unique id of historical versioned note
        :type note_history_id : Integer

        """
        try:
            dao_obj=NotesDAO(self.db_conn)
            history_records=dao_obj.fetch_history_content(note_history_id)
            self.transaction_obj.save()
            self.transaction_obj.end()
            logging.info('NOTES HISTORY %s'%history_records)
            return history_records
        except Exception as ex:
            logging.exception("Exception encountered while fetching historical content of Notes: %s"%ex)
            self.transaction_obj.revertback()
            self.transaction_obj.end()
            return 'FAILURE'