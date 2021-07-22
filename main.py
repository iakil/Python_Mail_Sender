# @author akil bhuiyan
# @since 11/28/2020
# @Version 1
# @description every time we run this, it will send emails to the selected recipients.

from smtplib import SMTP
from credentials import *
with SMTP("smtp.gmail.com") as connection: 
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs= others_email,
        msg="Subject:subject\n\n body"
    )

