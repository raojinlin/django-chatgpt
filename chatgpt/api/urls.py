from django.urls import include, path
from api.views import hello, generate, generate_stream

urlpatterns = [
    path('chat', hello),
    path('generate', generate),
    path('generate/stream', generate_stream),
]