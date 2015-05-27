from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings

def get_all_emails():
	emails_list = []
	emails = User.objects.all().values("email")
	for i in emails:
		emails_list.append(i['email'])
	return emails_list

def new_live_class(**kw):
	subject = "Clase en vivo"
	message = "Unete a nuestra clase" 
	+ kw['name'] + "en vivo :DD /n link: http://localhost:8000/classroom/room?n="
	+ kw['n']
	host_email = settings.EMAIL_HOST_USER
	to_list = get_all_emails()
	try:
		mail = EmailMessage(subject,message,host_email, to_list)
		mail.send()
	except:
		print ("Se murio :c")