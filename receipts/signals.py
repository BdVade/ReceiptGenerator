import weasyprint
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models.signals import post_save
from django.core.files.base import ContentFile
from .models import Receipt, ReceiptFile


def create_pdfs(sender, instance, created, **kwargs):
    html = render_to_string('pdf.html', {'receipt': instance})
    html = weasyprint.HTML(string=html)
    for i in range(10):
        pdf = ContentFile(html.write_pdf(stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css')]), name=f'rcpt-{instance.id}')
        ReceiptFile.objects.create(receipt=instance, file=pdf)


post_save.connect(create_pdfs, sender=Receipt)
