from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django_q.tasks import schedule
from edc_sms.classes import MessageSchedule

from . import Consultant, Contract, Employee, Pi


@receiver(post_save, weak=False, sender=Contract,
          dispatch_uid='contract_on_post_save')
def contract_on_post_save(sender, instance, raw, created, **kwargs):
    """
    Schedule email and sms reminder for 3months before contract end
    date.
    """
#     if not raw:
#         if created:
    schedule_email_notification(instance)
    schedule_sms_notification(instance)


def schedule_email_notification(contract=None):
    """
    Schedule email notification for contract expiration
    @param contract: instance of the contract
    """
    if contract:
        end_date = (contract.end_date).strftime('%Y/%m/%d')
        user = get_user(identifier=contract.identifier)

        schedule(
            'contract.tasks.contract_end_email_notification',
            user.first_name,
            user.email,
            end_date,
            schedule_type='O',
            next_run=reminder_datetime(contract=contract))


def schedule_sms_notification(contract=None):
    """
    Schedule sms notification for contract expiration
    @param contract: instance of the contract
    """
    user = None
    if contract:
        user = get_user(identifier=contract.identifier)

    msg = (f'Dear+{user.first_name},+Please+be+aware+that+your+contract+'
           f'is+ending+on+the+{contract.end_date}.+Please+notify+your+'
           'supervisor+of+your+renewal+intent+within+the+month.+Have+a+good+'
           'day+:).')

    MessageSchedule().schedule_message(
        message_data=msg,
        recipient_number=user.cell,
        sms_type='reminder',
        schedule_datetime=reminder_datetime(contract=contract))


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
        user = Employee.objects.get(identifier=identifier)
    except Employee.DoesNotExist:
        user = Pi.objects.get(identifier=identifier)
    except Pi.DoesNotExist:
        user = Consultant.objects.get(identifier=identifier)
    except Consultant.DoesNotExist:
        raise ValidationError(
            f'Contract owner for identifier {identifier} does not exist.')
    else:
        return user
