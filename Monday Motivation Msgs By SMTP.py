import smtplib
import os
import random
import datetime as dt


my_email = 'You email'
now = dt.datetime.now()
week_days = now.weekday()

if week_days == 1:  #monday
    with open('Quotes.txt','r') as file:
        every_quotes = file.readlines()
        choice_quote = random.choice(every_quotes) 
        my_email = my_email
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()  #secure by ssl sequrity purpose
        connection.login(user=my_email , password="Your App password") #app password
        connection.sendmail(from_addr=my_email , 
                            to_addrs="To mail address",
                            msg=f"Subject:Monday Motivation\n\n {choice_quote}")
        connection.close() #it can be done by -with- also

