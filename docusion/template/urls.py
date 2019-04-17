from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from docusion.template import views

urlpatterns = [
    path('templates', views.TemplateList.as_view()),
    path('template/<slug:slug>', views.TemplateSingle.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
