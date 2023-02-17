from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    """Home Page"""

    template_name = "repository/index.html"


class DataView(LoginRequiredMixin, TemplateView):
    """Display SMARTER datasets"""

    template_name = "repository/data.html"
