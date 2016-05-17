from django.http import HttpResponse
import sendgrid
from customers.models import CustomerProfile
from notifications.models import EmailBlasts, SMSNotifications
from twilio.rest import TwilioRestClient
from django.conf import settings

# ============== send email blasts via Sendgrid ================== #

def get_email_list():

    customer_mailing_list = CustomerProfile.objects.filter(want_emails=True,
                                                email_address__isnull=False)

    return customer_mailing_list

def trigger_email_send(request, blast_id):
    client = sendgrid.SendGridClient('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')

    email = EmailBlasts.objects.get(id=blast_id)

    customers = get_email_list()
    results = [settings.SENDGRID_API_KEY]
    for customer in customers:
        message = sendgrid.Mail()
        message.add_to(customer.email_address)
        message.set_html(email.body)
        message.set_subject(email.subject)
        message.set_from("dhblodgett@gmail.com")
        status,msg = client.send(message)
        results.append((status, msg))
        # TODO: Define this in settings later
    return HttpResponse(results)
        # '{} messages sent'.format(customers.count()))

# ===================== Send texts via Twilio ======================= #

def get_text_list(city=None):

    customer_text_list = CustomerProfile.objects.filter(want_texts=True,
                                             mobile_number__isnull=False)
    if city:
        customer_text_list=customer_text_list.filter(city=city)
    return customer_text_list

def trigger_text_send(request, notification_id):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID,
                              settings.TWILIO_AUTH_TOKEN)

    notification = SMSNotifications.objects.get(id=notification_id)

    customers = get_text_list(notification.city)


    for customer in customers:

        message = client.messages.create(
            body= notification.text_content,
            to=customer.mobile_number,
            from_="17029601952",
            media_url=notification.media_url

        )  #TODO: Define this in settings later
    return HttpResponse('{} messages sent'.format(customers.count()))






# message = client.messages.create(body="This is a test message. Jenny please?! I love you <3",
#     to="+17023018118",    # Replace with your phone number
#     from_="+17029601952") # Replace with your Twilio number
# print(message.sid)


# for customer in customer_mailing_list:
#     # str = customer.email_address + ", "
#     # emails.append(str)
#     jsonlist = {}
#     jsonlist['email']=customer.email_address
#
#     result.append(jsonlist)
#
# return HttpResponse(result)
