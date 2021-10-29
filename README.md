# Python-Email-Manager

First We have to install the smtplib module which will help us to send the email through GMAIL.

Then we have to make a new file.

Inside of it import the smtplib(send email) and the tkinter module(used to make a simple GUI)

add the title Python Email Manager

then add some labels :- Your email, Password, Subject, Message, Reciever Email
then add some entry's for the corresponding
then add the button for submitting
<!--  GUI is Ready -->

Now we have to make a function called send_mail()  which wil help us to send the email

First we will intialize the variable called server as written in code. (server = smtplib.SMTP('smtp.gmail.com', 587))
Then do server.starttls().
Then login To server
And Send the Mail
Then connect the buttons  and entry to this mail. (server.login(entry_1.get(), entry_3.get()) , server.sendmail(entry_1.get(), entry_5.get(), f"Subject:{entry_6.get()}\n\n {entry_2.get()}"))
And now when you enter the details and try to send the email .
You'll se that it's Working
WOOHOO we did it 👍👍
