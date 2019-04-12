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
    introduction = serializers.JSONField(
        required=False,
        error_messages={
            'required': "Introduction should be a valid json of name and style"
        }
    )
    abstract = serializers.JSONField(
        required=False,
        error_messages={
            'required': "Abstract should be valid json of name and style"
        }
    )
    literaturereview = serializers.JSONField(
        required=False,
        error_messages={
            'required': "Literature review should be valid json of name and style"
        }
    )
    conclusion = serializers.JSONField(
        required=False,
        error_messages={
            'required': "Conclusion should be valid json of name and style"
        }
    )
    references = serializers.JSONField(
        required=False,
        error_messages={
            'required': "References should be valid json of name and style"
        }
    )
    class Meta:
        model = Template
        fields = '__all__'
