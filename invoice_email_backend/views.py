from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings

from .models import InvoiceEmail
from .serializers import *

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def sendEmail(mainData):
    name = mainData["name"]
    toEmail = mainData["toEmail"]
    mSubject = mainData["subject"]

    html_content = render_to_string("invoice_template.html")
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject= mSubject,
        body= "Invoice from : " + name,
        from_email= settings.EMAIL_HOST_USER,
        to= [toEmail],
    )

    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)
    print("Working", end="\n\n")


@api_view(['GET', 'POST'])
def invoiceEmail_list(request):
    if request.method == 'GET':
        data = InvoiceEmail.objects.all()

        serializer = InvoiceEmailSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceEmailSerializer(data=request.data)
        if serializer.is_valid():
            sendEmail(request.data)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def students_detail(request, pk):
    try:
        invoice = InvoiceEmail.objects.get(pk=pk)
    except InvoiceEmail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    invoice.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)