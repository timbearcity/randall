from django.urls import include, path

from . import views


app_name = 'randomizers'
urlpatterns = [
    path('worksheets/', views.WorksheetView.as_view(), name='worksheets'),
]
