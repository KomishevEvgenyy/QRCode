from django.contrib import admin
from django.urls import path

from .views import FeedbackView


app_name = 'cervicedesk'
urlpatterns = [
    path('feetback/', FeedbackView.as_view())
]
