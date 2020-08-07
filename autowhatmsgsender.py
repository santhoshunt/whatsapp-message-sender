#importing the module which is used to send messages

import pywhatkit
s=int(input("Enter the user's  number :"))#getting the number
hours=int(input("Enter the hour (in 24 hr format) :"))
min=int(input("Enter the minute :"))
msg=input("Enter the message you wanna send :").strip()
#the code used to send messgaes
pywhatkit.sendwhatmsg("+91"+str(s),msg,hours,min)
#the message will be sent to the user in 30 seconds python opens whatsappweb
#the message will be sent
