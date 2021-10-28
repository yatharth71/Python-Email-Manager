import smtplib

print("****** Enabling Less Secure Apps on your google account is necessary ******")

email = input("Enter your email : ")
password = input("Enter your password : ")
reciever = input("Enter the reciever's email : ")
subject = input("Enter the subject : ")
msg = input("Enter the message : ")
total = f"Subject:{subject} \n\n {msg}"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(email, password)

server.sendmail(email, reciever, total)

