from django.views.generic import TemplateView

class IndexView(TemplateView):
    """Home Page"""
    template_name = "repository/index.html"
