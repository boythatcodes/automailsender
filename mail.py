import time
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

send_time_in_min = 30
x = 0 

# Define to/from
recipient = 'reciever'


mail_data = [{
    'title': 'User 1 full Name',
    'name': 'user@email.com',
    'password': 'password',
    'content': """\
        <p>Hello Sir,<br>
            I think you may have forgotten about the end of my prohibition which was about a <strong style="color: red;">Month</strong> ago!<br>
            This is a formal request to review my prohibition and also my salary is due.<br>
            PS this is an automated script - Developed By: <a href="company link">Company Name</a>.
        </p>
    """
},
{
    'title': 'User 2 full Name',
    'name': 'user@email.com',
    'password': 'password',
    'content': """\
        <p>Hello Sir,<br>
            I think you may have forgotten about the end of my prohibition which was about a <strong style="color: red;">Month</strong> ago!<br>
            This is a formal request to review my prohibition and also my salary is due.<br>
            PS this is an automated script - Developed By: <a href="company link">Company Name</a>.
        </p>
    """
},
]


while True:
    for users in mail_data:
        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        # Create message
        msg = MIMEText(users['content'], 'html', 'utf-8')
        msg['Subject'] =  Header("Prohibition Mail", 'utf-8')
        msg['From'] = formataddr((str(Header(users['title'], 'utf-8')), users['name']))
        msg['To'] = recipient\

        
        server.login(users['name'], users['password'])
        server.sendmail(users['name'], [recipient], msg.as_string())
        server.quit()
    print('Message '+str(x+1)+' sent.')
    x +=1
    time.sleep(60 * send_time_in_min)
