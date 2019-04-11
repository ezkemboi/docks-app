from rest_framework import serializers
from docusion.template.models import Template

class TemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

