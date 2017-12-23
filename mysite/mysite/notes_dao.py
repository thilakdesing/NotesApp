import os
import sys
import datetime
import logging
logging.basicConfig(filename='notes.log', filemode='w', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class NotesDAO(object):
    """
    :brief Data Access object class which talks with Database to perform storage operations
    """
    def __init__(self,db_conn=None):
        
        self.db_conn=db_conn
        
    def fetch_active_notes(self):
        """
        :brief Fetches active notes from table
        """
        try:
            query="select * from notes_master where status=1 order by created_datetime desc"
            response = self.db_conn.processquery(query)
            return response
        except Exception as ex:
            logging.info("Exception encountered on DB operation "+ str(ex))
            raise ex
        
    def insert_note(self,note_dict):
        """
        :brief Inserts New note details. Also returns last inserted primarykey
        :param note_dict: Dictionary containing note details
        :type note_dict : Dictionary
        """
        try:
            query="insert into notes_master (note_title,note_content,created_datetime,modified_datetime) values ('%s','%s',now(),now())"%(note_dict['note_title'],
                                                                                     note_dict['note_content'])
            response = self.db_conn.processquery(query,returnprimarykey=True)
            return response
        except Exception as ex:
            logging.info("Exception encountered on DB operation "+ str(ex))
            raise ex

    def update_note(self,note_dict):
        """
        :brief Updates existing note details.
        :param note_dict: Dictionary containing note details
        :type note_dict : Dictionary
        """
        try:
            query="update notes_master SET note_title='%s',note_content='%s',modified_datetime=now() where note_id='%s'"%(note_dict['note_title'],
                                                                                                 note_dict['note_content'],
                                                                                                 note_dict['note_id'])
            response = self.db_conn.processquery(query)
            return response
        except Exception as ex:
            logging.info("Exception encountered on DB operation "+ str(ex))
            raise ex
    
    def delete_note(self,note_id):
        """
        :brief Updates notes table with status flag as 0 (Inactive note)
        :param note_id: Unique id of a note
        :type note_id : Integer
        """
        try:
            query="update notes_master SET status=0 where note_id=%s"%note_id
            response = self.db_conn.processquery(query)
            return response
        except Exception as ex:
            logging.info("Exception encountered while inserting Notes "+ str(ex))
            raise ex

    def create_note_history(self,note_id):
        """
        :brief Creates history record by selecting entries from master table and inserting in history table
        :param note_id: Unique id of a note
        :type note_id : Integer
        """
        try:
            query="INSERT INTO notes_master_history(note_id,note_title,note_content,status,\
            created_datetime) select note_id,note_title,note_content,status,modified_datetime\
            from notes_master where note_id=%s"%note_id
            response = self.db_conn.processquery(query)
            return response
        except Exception as ex:
            logging.info("Exception encountered on DB operation "+ str(ex))
            raise ex
        
    def fetch_history(self,note_id):
        """
        :brief Fetched historical version updated of a particular note
        :param note_id: Unique id of a note
        :type note_id : Integer
        """
        try:
            query="select note_history_id,created_datetime from notes_master_history where note_id=%s order by\
             created_datetime desc "%note_id
            response = self.db_conn.processquery(query)
            return response
        except Exception as ex:
            logging.info("Exception encountered on DB operation "+ str(ex))
            raise ex
        
    def fetch_history_content(self,note_history_id):
        """
        :brief Fetched historical note details for a particular historical note
        :param note_history_id: Unique id of a historical note
        :type note_history_id : Integer
        """
        try:
            query="select note_title,note_content from notes_master_history where note_history_id=%s"%note_history_id
            response = self.db_conn.processquery(query)
            return response
        except Exception as ex:
            logging.info("Exception encountered on DB operation "+ str(ex))
            raise ex