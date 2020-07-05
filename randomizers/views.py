from django.shortcuts import render
from django.views.generic import TemplateView


class WorksheetView(TemplateView):
    template_name = 'randomizers/worksheet.html'
