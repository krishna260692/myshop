import smtplib

from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    EMAIL_HOST_USER = 'shyamkumar260692@gmail.com'
    EMAIL_HOST_PASSWORD = 'rnycxekkkbdomnpk'

    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'shyamkumar260692@gmail.com',
                          [order.email])
    return mail_sent

