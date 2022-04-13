import weasyprint
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models.signals import post_save
from .models import Receipt, ReceiptFile


def create_pdfs(sender, instance, created, **kwargs):
    html = render_to_string('pdf.html', {'receipt': instance})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{instance.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(
                                               settings.STATIC_ROOT + 'css/pdf.css')])
    return response
    pass


post_save.connect(create_pdfs, sender=Receipt)
