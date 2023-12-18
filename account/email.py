import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings


def sendOTP(email):
    Subject = "Email verification"
    otp_code = random.randint(1000, 9999)
    user = User.objects.get(email=email)
    # current_site = 'myAuth.com'
    email_body = f'Hi, thanks for signing up. Please verify your email with the passcode {otp_code} '

    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code = otp_code)

    send_email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to = [email])
    send_email.send(fail_silently=True)
