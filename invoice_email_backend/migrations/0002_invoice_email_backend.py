from django.db import migrations

def create_data(apps, schema_editor):
    InvoiceEmail = apps.get_model('invoice_email_backend', 'InvoiceEmail')
    InvoiceEmail(name="Joe Silver", toEmail="joe@email.com", subject="Test1").save()

class Migration(migrations.Migration):

    dependencies = [
        ('invoice_email_backend', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
