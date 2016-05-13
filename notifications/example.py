import sendgrid
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# client = sendgrid.SendGridClient("SENDGRID_API_KEY")
# message = sendgrid.Mail()
#
# message.add_to("dhblodgett@gmail.com")
# message.set_from("dhblodgett@gmail.com")
# message.set_subject("Sending with SendGrid is Fun")
# message.set_html("and easy to do anywhere, even with Python")
#
# client.send(message)
#
# mail = EmailMultiAlternatives(
#   subject="Your Subject",
#   body="This is a simple text email body.",
#   from_email="David Blodgett <dhblodgett@gmail.com>",
#   to=["dhblodgett@gmail.com"],
#   headers={"Reply-To": "dhblodgett@gmail.com"}
# )
# mail.attach_alternative("<p>This is a simple HTML email body</p>", "text/html")
#
# mail.send()