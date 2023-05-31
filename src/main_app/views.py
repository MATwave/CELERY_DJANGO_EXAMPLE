from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
