import requests
from bs4 import BeautifulSoup
from smtplib import SMTPException
import time
import smtplib
from email.mime.text import MIMEText

#This web scraper is for newegg.com, it will not work for things like Target and
#Amazon. If there isn't now, I will have an alternative download right below this
#one that can be viewed.

#f is document reading into, since html document need ot use html parser
# with open("index.html", "r") as f:

#r read mode and f stands for file

url = 'yourwebsite.com' #Here you need to put in the url of the webpage that you are on. 

result = requests.get(url)

#Here we are defining a function to check the price

doc = BeautifulSoup(result.text, "html.parser")
def check_price():
#Because of the setup of this sit, we can just find the text $
#With a site like amazon we would actually be looking for an ID
    prices = doc.find_all(text="$")
    parent = prices[0].parent
    strong = parent.find("strong")
#This is printing <strong>159<strong>
    print(strong)
#Turning it into 159
    good = strong.string
#Finally making it an integer
    goods = int(good)
    if(goods < 160):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

#Here since we're using chrome you need to either use your email, login info, or set up a two factor authentication for desktop.
    server.login('someemail@gmail.com', 'abcdefg1234567!')

    subject = "Subject line, put whatever you think is best here."
    body = "What you want in the body of your email."

    msg = f"Subject: {subject}\n\n{body}"
    recipients = [] #'email@gmail.com', here you will put the email of all the recipients.
    server.sendmail(
            #from
            'someemail@gmail.com', #Use the email your using with server.login
            #to
            recipients,
            msg
    )

    print("Email has been sent")

    server.quit()

while(True):
    check_price()
# time.sleep(43200)
    time.sleep(21600)
