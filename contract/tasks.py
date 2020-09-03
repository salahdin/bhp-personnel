from Crypto import Random
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from smtplib import SMTPException


def contract_end_email_notification(first_name=None, email=None, end_date=None):
    """
    Send email notification to employee for contract expiration.
    """
    Random.atfork()

    msg = (f'Dear {first_name}, \n \n Please be notified that your '
           f'contract is ending on the {end_date}. For renewal '
           'draft a letter for your supervisor to indicate renewal intent'
           ' or otherwise. \n \n Have a good day :).')
    try:
        send_mail(
            f'Contract expiration notification ({end_date})',
            msg,
            'BHP HR <bhp.se.dmc@gmail.com>',
            [email],
            fail_silently=False)
    except SMTPException as e:
        raise ValidationError(f'There was an error sending an email: {e}')
