from django.shortcuts import render
from django.views.generic.edit import FormView #ознакомиться с моделей FormView

from .forms import FeedbackForm


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = "cervicedesk/qr.html"
