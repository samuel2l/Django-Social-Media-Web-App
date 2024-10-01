from django import template
from social.models import Notification
register = template.Library()


@register.inclusion_tag('show_notifications.html', takes_context=True)
def show_notifications(context):
	current_user = context['request'].user
	notifications = Notification.objects.filter(receiver=current_user).exclude(seen=True).order_by('-date')
	return {'notifications': notifications}




