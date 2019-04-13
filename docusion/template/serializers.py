from rest_framework import serializers
from docusion.template.models import Template


class TemplateSerializers(serializers.ModelSerializer):
    # Create serializers for JSON fields
    title = serializers.JSONField(
        required=True,
        error_messages={
            'required': "Title required and it is json of name and style"
        }
    )
    # Add fields in the document e.g List of Dictionaries
    documentfieldsitems = serializers.DictField(
        required=True,
        error_messages={
            'required': "You must specify the JSON fields for the document"
        }
    )

    class Meta:
        model = Template
        fields = '__all__'
