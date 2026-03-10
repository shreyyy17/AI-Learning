import smtplib
from email.message import EmailMessage
email_content = '''
Dear Sir/Madam,

I am sending you an e-mail with python.I hope you like it,

Kind regards,

Jose
'''

email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'you@gmail.com'
email['To'] = 'shreyvalorent@gmail.com'


smpt_connector = smtplib.SMTP('smtp.gmail.com', 587)
smpt_connector.starttls()
smpt_connector.login('you@gmail.', 'password')