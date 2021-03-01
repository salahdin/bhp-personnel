from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django_q.tasks import schedule
from django.contrib.auth.models import User

from edc_sms.classes import MessageSchedule

from . import Consultant, Contract, ContractExtension, Employee, Pi


@receiver(post_save, weak=False, sender=Employee,
          dispatch_uid='employee_on_post_save')
def employee_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw and created:
        try:
            User.objects.get(email=instance.email)
        except User.DoesNotExist:
            User.objects.create_user(username=instance.email,
                                     email=instance.email,
                                     password=str.lower(
                                         instance.first_name + '@2021'),
                                     first_name=instance.first_name,
                                     last_name=instance.last_name,
                                     is_staff=True,)


@receiver(post_save, weak=False, sender=Pi,
          dispatch_uid='pi_on_post_save')
def pi_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        if created:
            User.objects.create_user(username=instance.
                                     first_name[0]+''+instance.last_name,
                                     email=instance.email,
                                     password=instance.first_name+'@2020',
                                     first_name=instance.first_name,
                                     last_name=instance.last_name,
                                     is_staff=True,
                                     )


@receiver(post_save, weak=False, sender=Contract,
          dispatch_uid='contract_on_post_save')
def contract_on_post_save(sender, instance, raw, created, **kwargs):
    """
    Schedule email and sms reminder for 3months before contract end
    date.
    """
    if not raw:
        if created:
            schedule_email_notification(instance)
            schedule_sms_notification(instance)


@receiver(post_save, weak=False, sender=ContractExtension,
          dispatch_uid='contractextension_on_post_save')
def contractextension_on_post_save(sender, instance, raw, created, **kwargs):
    """
    Reschedule an email and sms reminder for 3months before contract end
    date after extension.
    """
    if not raw:
        if created:
            schedule_email_notification(instance, ext=True)
            schedule_sms_notification(instance, ext=True)


def schedule_email_notification(instance=None, ext=False):
    """
    Schedule email notification for contract expiration
    @param contract: instance of the contract
    """
    if instance:
        identifier = instance.contract.identifier if ext else instance.identifier
        end_date = (instance.end_date).strftime('%Y/%m/%d')
        user = get_user(identifier=identifier)

        schedule(
            'contract.tasks.contract_end_email_notification',
            user.first_name,
            user.last_name,
            user.email,
            user.supervisor.email,
            end_date,
            schedule_type='O',
            next_run=reminder_datetime(contract=instance))


def schedule_sms_notification(instance=None, ext=False):
    """
    Schedule sms notification for contract expiration
    @param contract: instance of the contract
    """
    user = None
    if instance:
        identifier = instance.contract.identifier if ext else instance.identifier
        user = get_user(identifier=identifier)

    msg = (f'Dear+{user.first_name},+Please+be+aware+that+your+contract+'
           f'is+ending+on+the+{instance.end_date}.+Please+notify+your+'
           'supervisor+of+your+renewal+intent+within+the+month.+Have+a+good+'
           'day+:).')

    MessageSchedule().schedule_message(
        message_data=msg,
        recipient_number=user.cell,
        sms_type='reminder',
        schedule_datetime=reminder_datetime(contract=instance))


def reminder_datetime(contract=None):
    """
    Returns datetime when the reminder should be scheduled.
    """
    if contract:
        reminder_date = contract.end_date - relativedelta(months=3)
        return datetime.combine(reminder_date, time.fromisoformat('10:00:00'))


def get_user(identifier=None):
    """
    Contract owner object getter
    @param identifier: unique identifier for the owner
    """
    try:
        return Employee.objects.get(identifier=identifier)
    except Employee.DoesNotExist:
        try:
            return Pi.objects.get(identifier=identifier)
        except Pi.DoesNotExist:
            try:
                return Consultant.objects.get(identifier=identifier)
            except Consultant.DoesNotExist:
                raise ValidationError(
                    f'Contract owner for identifier {identifier} does not exist.')
