from django.views.generic import ListView

from .models import LogLine


class LogView(ListView):
    model = LogLine
    template_name = 'core/index.html'
