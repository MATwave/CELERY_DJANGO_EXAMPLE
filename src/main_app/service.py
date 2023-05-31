from django.core.mail import send_mail


class EmailSender:
    subject = 'Тестовое сообщение'
    message = 'Привет, это тестовое сообщение.'
    from_email = 'example_email@example.com'

    @classmethod
    def send_email(cls, email):
        send_mail(cls.subject, cls.message, email, [email])
