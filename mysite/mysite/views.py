import json
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from notes_handler import NotesHandler
import logging
logging.basicConfig(filename='notes.log', filemode='w', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class NotesView(View):
    """
    :brief This class handles the request for
    rendering the Notes templates and its content """
    def get(self, request, *args, **kwargs):
        """
        :brief Get method to identify the request
        and render the requisite along with its context"""
        try:
            logging.info('received %s'%request.GET)
            action = kwargs.get('action')
            notes_obj=NotesHandler()
            if action=='view_history':
                note_id=int(request.GET.get('note_id'))
                context= notes_obj.get_history(note_id)
                return HttpResponse(json.dumps(context))
            if action=='get_note_id':
                context=notes_obj.get_new_note_id()
                return HttpResponse(json.dumps(context))
            if action=='get_history_content':
                note_history_id=int(request.GET.get('note_history_id'))
                context=notes_obj.get_history_content(note_history_id)
                return HttpResponse(json.dumps(context))
            context_dict=notes_obj.get_active_notes()
            response = render(request, 'notes_home.html',context_dict)
            return response
        except Exception as ex:
            logging.info("Encountered exception in get method %s"%ex)
            raise

    def post(self, request, *args, **kwargs):
        """
        :brief Post method to handle data received.
        
        """
        try:
            logging.info('POST received %s'%request.POST)
            action = kwargs.get('action')
            note_dict={
                        'note_id':int(request.POST.get('note_id')),
                        'note_title':request.POST.get('note_title'),
                        'note_content':request.POST.get('note_content')
                       }
            notes_obj=NotesHandler()
            if action=='update':
                return HttpResponse(notes_obj.update_note(note_dict))
            if action=='delete':
                return HttpResponse(notes_obj.remove_note(note_dict))
            
        except Exception as ex:
            logging.info("Encountered exception in post method %s"%ex)
            raise