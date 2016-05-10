
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, request
import sendgrid
from customers.models import CustomerProfile
from notifications.models import EmailBlasts, SMSNotifications
from twilio.rest import TwilioRestClient
from django.conf import settings

def get_email_list():

    customer_mailing_list = CustomerProfile.objects.filter(want_emails=True,
                                                email_address__isnull=False)

    return customer_mailing_list

def trigger_email_send(request, notification_id):
    client = sendgrid.SendGridClient(settings.SENDGRID_API_KEY)


    for customer in get_email_list():
        message = sendgrid.Mail()
        message.add_to(customer.email_address)
        message.set_html("")
        message.set_from("")
        client.send(message)
        # TODO: Define this in settings later
    return HttpResponse('ok')

    # for customer in customer_mailing_list:
    #     # str = customer.email_address + ", "
    #     # emails.append(str)
    #     jsonlist = {}
    #     jsonlist['email']=customer.email_address
    #
    #     result.append(jsonlist)
    #
    # return HttpResponse(result)


def get_text_list():

    customer_text_list = CustomerProfile.objects.filter(want_texts=True,
                                             mobile_number__isnull=False)
    return customer_text_list

def trigger_text_send(request, notification_id):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID,
                              settings.TWILIO_AUTH_TOKEN)

    notification = SMSNotifications.objects.get(id=notification_id)

    for customer in get_text_list():
        message = client.messages.create(
            body= notification.text_content,
            to = '17023018118',
            # to=customer.mobile_number,
            from_="17029601952"
        )
            #TODO: Define this in settings later
    return HttpResponse('ok')


# message = client.messages.create(body="This is a test message. Jenny please?! I love you <3",
#     to="+17023018118",    # Replace with your phone number
#     from_="+17029601952") # Replace with your Twilio number
# print(message.sid)
