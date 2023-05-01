from django.contrib import admin
from django.urls import path, re_path
from invoice_email_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/invoiceEmail/$', views.invoiceEmail_list),
    re_path(r'^api/invoiceEmail/([0-9])$', views.students_detail),
]