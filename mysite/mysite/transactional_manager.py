import MySQLdb
import logging
logging.basicConfig(filename='notes.log', filemode='w', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    
class DBManager(object):
    """
    :brief This class is to perfor DB operations 
    """
    def __init__(self,conn):
        self.cursor = conn.cursor(MySQLdb.cursors.DictCursor)
            
    def processquery(self,query,returnprimarykey=None):
        logging.debug("Executing query %s"%query)
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        logging.debug("Query Result %s" %str(result))
        if returnprimarykey:
            return self.cursor.lastrowid
        return list(result)
    
class TransactionalManager(object):
    """
    :brief This class is primarily used to get DB connection object
    """
    def __init__(self,db='notes'):
        self.conn = MySQLdb.connect (host = "localhost",
                                user = "root",
                                db = db)
        
    def get_database_connection(self):
        db_obj=DBManager(self.conn)
        return db_obj  
    
    def save(self):
        self.conn.commit()
        
    def revertback(self):
        self.conn.rollback() 
        
    def end(self):
        self.conn.close()