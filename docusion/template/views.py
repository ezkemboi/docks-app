from docusion.template.models import Template
from docusion.template.serializers import TemplateSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from io import BytesIO
from pdfdocument.document import PDFDocument

def convert_to_pdf(docs):
    f = BytesIO()
    pdf = PDFDocument(f)
    pdf.init_report()
    pdf.h1(docs["title"])
    pdf.p(docs["title"]["name"])
    pdf.h3(docs["abstract"])
    pdf.p(docs["abstract"]["name"])
    pdf.h3(docs["literaturereview"])
    pdf.p(docs["literaturereview"]["name"])
    pdf.h3(docs["conclusion"])
    pdf.p(docs["conclusion"]["name"])
    pdf.h3(docs["references"])
    pdf.p(docs["references"]["name"])
    pdf.generate()
    return f.getvalue()

# Create your views here.

class TemplateList(APIView):
    # Create and get all templates
    def get(self, request, format=None):
        # Get all templates
        templates = Template.objects.all()
        serializer = TemplateSerializers(templates, many=True)
        print('------------------------->',serializer.data[0])
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

class TemplateSingle(APIView):
    # Create and get all templates
    def get(self, request, format=None):
        # Get single templates
        template = Template.objects.get(slug="Th898ydusjdioshiwojhju-hsh766757687")
        serializer = TemplateSerializers(template)
        return Response(serializer.data)
