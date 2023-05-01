from rest_framework import serializers
from .models import InvoiceEmail

class InvoiceEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceEmail 
        fields = ('pk', 'name', 'toEmail', 'subject')