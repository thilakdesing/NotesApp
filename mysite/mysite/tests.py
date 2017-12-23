from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import pytest
from _pytest.monkeypatch import monkeypatch
from transactional_manager import TransactionalManager
from notes_dao import NotesDAO
from notes_handler import NotesHandler
import datetime

client = Client()
# Django tests
class TestNotesView(TestCase):
	def test_page_render(self):
		response = self.client.get('/notes/')
		self.assertEqual(response.status_code, 200)
	def test_page_template(self):
		response = self.client.get('/notes/')
		self.assertTemplateUsed(response, 'views_home.html')

#Python tests
class TestNotesHandler():
	def test_get_active_notes_success(self,monkeypatch):
		def mock_fetch_active_notes(self):
			return [{'note_id':5,'note_title':'test','note_content':'test content','status':1,'created_datetime':'2017-05-05','modified_datetime':'2017-05-05'}]
		monkeypatch.setattr(NotesDAO,'fetch_active_notes',mock_fetch_active_notes)
		result=NotesHandler().get_active_notes()
		assert result['notes'][0]['note_id']==5	
	
	def test_get_active_notes_failure(self,monkeypatch):
		def mock_fetch_active_notes_exception(self):
			raise
		monkeypatch.setattr(NotesDAO,'fetch_active_notes',mock_fetch_active_notes_exception)
		with pytest.raises(Exception) as exception:
			result=NotesHandler().get_active_notes()
	def test_get_new_note_id_success(self,monkeypatch):
		def mock_get_new_note_id(self,note_dict):
			return 6
		monkeypatch.setattr(NotesDAO,'insert_note',mock_get_new_note_id)
		result=NotesHandler().get_new_note_id()
		assert result['note_id']==6
	
	def test_get_new_note_id_failure(self,monkeypatch):
		def mock_get_new_note_id_exception(self,note_dict):
			raise
		monkeypatch.setattr(NotesDAO,'insert_note',mock_get_new_note_id_exception)
		with pytest.raises(Exception) as exception:
			result=NotesHandler().get_new_note_id()
	def test_update_note_success(self,monkeypatch):
		def mock_create_note_history(self,note_dict):
			pass
		def mock_update_note(self,note_dict):
			pass
		monkeypatch.setattr(NotesDAO,'create_note_history',mock_create_note_history)
		monkeypatch.setattr(NotesDAO,'update_note',mock_update_note)
		result=NotesHandler().update_note({'note_title':'test title','note_content':'test content','note_id':55})
		assert result=='SUCCESS'
	
	def test_pdate_note_failure(self,monkeypatch):
		def mock_create_note_history(self,note_dict):
			pass
		def mock_update_note(self,note_dict):
			raise
		monkeypatch.setattr(NotesDAO,'create_note_history',mock_create_note_history)
		monkeypatch.setattr(NotesDAO,'update_note',mock_update_note)
		result=NotesHandler().update_note({'note_title':'test title','note_content':'test content','note_id':55})
		assert result=='FAILURE'
		
	def test_remove_note_success(self,monkeypatch):
		def mock_create_note_history(self,note_dict):
			pass
		def mock_delete_note(self,note_dict):
			pass
		monkeypatch.setattr(NotesDAO,'create_note_history',mock_create_note_history)
		monkeypatch.setattr(NotesDAO,'delete_note',mock_delete_note)
		result=NotesHandler().remove_note({'note_title':'test title','note_content':'test content','note_id':55})
		assert result=='SUCCESS'
	
	def test_remove_note_failure(self,monkeypatch):
		def mock_create_note_history(self,note_dict):
			pass
		def mock_delete_note(self,note_dict):
			raise
		monkeypatch.setattr(NotesDAO,'create_note_history',mock_create_note_history)
		monkeypatch.setattr(NotesDAO,'delete_note',mock_delete_note)
		result=NotesHandler().remove_note({'note_title':'test title','note_content':'test content','note_id':55})
		assert result=='FAILURE'
	
	def test_get_history_success(self,monkeypatch):
		def mock_fetch_history(self,note_dict):
			return [{'note_id':5,'note_title':'test','note_content':'test content','status':1,'created_datetime':datetime.datetime.now(),'modified_datetime':datetime.datetime.now()}]
		monkeypatch.setattr(NotesDAO,'fetch_history',mock_fetch_history)
		result=NotesHandler().get_history(note_id=55)
		assert result[0]['note_id']==5
	
	def test_get_history_failure(self,monkeypatch):
		def mock_fetch_history(self,note_dict):
			raise
		monkeypatch.setattr(NotesDAO,'fetch_history',mock_fetch_history)
		result=NotesHandler().get_history(note_id=55)
		assert result=='FAILURE'
	
	def test_get_history_content_success(self,monkeypatch):
		def mock_fetch_history_content(self,note_dict):
			return [{'note_id':55,'note_title':'test','note_content':'test content','status':1,'created_datetime':datetime.datetime.now(),'modified_datetime':datetime.datetime.now()}]
		monkeypatch.setattr(NotesDAO,'fetch_history_content',mock_fetch_history_content)
		result=NotesHandler().get_history_content(note_history_id=55)
		assert result[0]['note_id']==55
	
	def test_get_history_content_failure(self,monkeypatch):
		def mock_fetch_history_content(self,note_dict):
			raise
		monkeypatch.setattr(NotesDAO,'fetch_history_content',mock_fetch_history_content)
		result=NotesHandler().get_history_content(note_history_id=55)
		assert result=='FAILURE'
			
	
	