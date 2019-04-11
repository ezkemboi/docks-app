from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from docusion.template import views

urlpatterns = [
    path('template/', views.TemplateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
