from django.shortcuts import render
from django.conf import settings
from watson_developer_cloud import ConversationV1
from .forms import ChatForm
import json

# Create your views here.

def chat(request):
	conversation = ConversationV1(
		username = settings.USERNAME,
		password = settings.PASSWORD,
		version = '2018-02-16'
		) 
	result = ''
	if request.method == 'POST':
		form = ChatForm(request.POST)
		if form.is_valid():
			response = conversation.message(
				workspace_id = settings.WORKSPACE_ID,
				input = {
					'text':	form.cleaned_data['message']
				}
				)
			
		result += json.dumps(response, indent=2)
	else:
		form = ChatForm()
	return render(request, 'chat.html', {'form': form, 'result': result})
