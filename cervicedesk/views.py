from django.shortcuts import render
from django.views.generic.edit import FormView #ознакомиться с моделей FormView
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from .forms import FeedbackForm
from .models import QRCode


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = "cervicedesk/qr.html"
    success_url = reverse_lazy('cervicedesk:ok')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class QRListView(ListView):
    model = QRCode



