from django.urls import include, path
from api.views import generate, generate_stream

urlpatterns = [
    path('generate', generate),
    path('generate/stream', generate_stream),
]