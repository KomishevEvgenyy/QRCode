from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


from .views import FeedbackView, QRListView


app_name = 'cervicedesk'
urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    path('ok/', TemplateView.as_view(template_name='cervicedesk/ok.html'), name='ok'),
    path('qr/all/', QRListView.as_view()),
]
