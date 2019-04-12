from docusion.template.models import Template
from docusion.template.serializers import TemplateSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TemplateList(APIView):
    # Create and get all templates
    def get(self, request, format=None):
        # Get all templates
        templates = Template.objects.all()
        serializer = TemplateSerializers(templates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a template
        # Will write a kwargs and args function for this validation to avoid long checks
        if 'name' not in request.data['title'] or 'style' not in request.data['title']:
            return Response({"message": "Title must contain name and style"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TemplateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)