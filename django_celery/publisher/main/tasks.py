# -*- coding: utf-8 -*-

import logging
import time
import datetime

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from celery.schedules import crontab
from publisher.celery_app import app
from publisher.settings import EMAIL_HOST_USER

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(60, send_email_at_times.s(), expires=5)
#
#     sender.add_periodic_task(
#         crontab(hour=23, minute=25),
#         send_email_at_times.s(),
#     )
#
#     sender.add_periodic_task(
#         crontab(hour=15, minute=25),
#         send_email_at_times.s(),
#     )

@app.task
def send_verification_email(user_id):
    # use this sleeping is just because this task execute so fast
    # that the real db record in not stored at all.
    # logging.warning("sleeping...")
    # time.sleep(5)

    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your QuickPublisher account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s" % user_id)

@app.task
def send_deletion_warning_email(email):
    try:
        send_mail(
            'Delete your account warning',
            'your account {email} is deleted, byebye'.format(email=email),
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        logging.warning(e)
        logging.warning("Send notification email fail: %s" % email)

@app.task
def send_email_at_times(*args, **kwargs):
    logging.warning("begin sending email...")
    send_mail(
        'Hello, dude!',
        'This is a time alarm email, current is {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        EMAIL_HOST_USER,
        ['konmyn@163.com'],
        fail_silently=False,
    )
    logging.warning("finish sending email.")
