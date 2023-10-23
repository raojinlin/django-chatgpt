import json

from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse, StreamingHttpResponse
from django.http.request import HttpRequest
from api.completion import completion

# Create your views here.


def hello(request: HttpRequest):
    return render(request=request, template_name='index.html')
    # return HttpResponse(status=200, content='hello')


def generate(request: HttpRequest): 
    print(request.GET)
    question = request.GET.get('question')
    if not question:
        return JsonResponse(status=400)

    return JsonResponse(status=200, data=completion(question), safe=False)


class Event:
    def __init__(self, event='', data='', id='', retry=0):
        self.event = event
        self.data = data
        self.id = id
        self.retry = retry

    def to_string(self):
        event = ""
        if self.event != "":
            event += "event: " + self.event + "\n"

        if self.data != "":
            event += "data: " + self.data + "\n"

        if self.id != "":
            event += "id: " + self.id + "\n"

        if self.retry > 0:
            event += "retry: " + str(self.retry) + "\n"

        return event + "\n"

    def __str__(self):
        return self.to_string()


def chunk_to_event(chunk):
    return Event(data=json.dumps(chunk)).to_string()


def generate_stream(request: HttpRequest):
    chat_completion_stream = completion(request.GET.get('question'), stream=True)
    return StreamingHttpResponse(
        streaming_content=(chunk_to_event(chunk) for chunk in chat_completion_stream),
        content_type='text/event-stream'
    )
