# @author akil bhuiyan
# @since 11/28/2020
# @Version 1
# @description every time we run this, it will send email to the selected recipient.

from smtplib import SMTP

my_email = ""
my_password =""
others_email = "", ""

with SMTP("smtp.gmail.com") as connection:   # connection = SMTP("")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs= others_email,
        msg="Subject:subject\n\n body"
    )

