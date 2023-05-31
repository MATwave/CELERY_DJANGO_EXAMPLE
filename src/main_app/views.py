from smtplib import SMTPSenderRefused

from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .service import EmailSender


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact.html'

    def form_valid(self, form):
        form.save()
        try:
            EmailSender.send_email(form.instance.email)
        except SMTPSenderRefused:
            form.add_error(None, 'Не удалось отправить сообщение')
            return self.form_invalid(form)
        return super().form_valid(form)
