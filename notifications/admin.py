from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from notifications.models import SMSNotifications, EmailBlasts


@admin.register(SMSNotifications)
class SMSNotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_content', 'media_url', 'city', 'send_link')

    def send_link(self, obj):
        url = reverse("trigger_text_send", kwargs={"notification_id":obj.id})
        return mark_safe("<a href = '{}'> send message </a>".format(url))

@admin.register(EmailBlasts)
class EmailBlastsAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_email', 'subject', 'body', 'email_link')

    def email_link(self, obj):
        url = reverse("trigger_email_send", kwargs={"blast_id": obj.id})
        return mark_safe("<a href = '{}'> send message </a>".format(url))
