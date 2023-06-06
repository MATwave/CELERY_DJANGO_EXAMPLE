from smtplib import SMTPSenderRefused

from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic import View

from .forms import ContactForm
from .models import Contact
from .tasks import send_test_email
# from .service import EmailSender


class HealthCheckView(View):
    def get(self, request):
        return HttpResponse("OK", status=200)


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact.html'

    def form_valid(self, form):
        form.save()
        try:
            # EmailSender.send_email(form.instance.email) # этот способ повесит программу пока не отработает
            send_test_email.delay(form.instance.email)  # этот способ зарегистрирует задачу, а отработает потом
        except SMTPSenderRefused:
            form.add_error(None, 'Не удалось отправить сообщение')
            return self.form_invalid(form)
        return super().form_valid(form)
