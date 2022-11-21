from email.quoprimime import quote
import smtplib
import random
import datetime as dt
my_email = "degercandeger42@gmail.com"
password ="rqzesopxcphtfjgl"




#connection = smtplib.SMTP("smtp.gmail.com", 587)
#connection.starttls()#Secure Connection
#connection.login(user=my_email,password=password)
#connection.sendmail(from_addr=my_email, to_addrs="degercandeger1@gmail.com", msg="Metal Gear Solid.")
#connection.close()

now = dt.datetime.now()
weekday= now.weekday()

if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readline()
        quote=random.choice(all_quotes)
    print(quote)
    
    with  smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()#Secure Connection
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="degercandeger1@gmail.com", 
            msg=f"Subject:Metal Gear Solid.\n\n{quote}"
            )
        