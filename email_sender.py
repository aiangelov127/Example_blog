import smtplib
my_email = "blago82bt@gmail.com"
password = "123465Zxcvnb"

def email_sender(func):
    def wrapper(*args):
        func(args[0], args[1], args[2], args[3])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="naskoia7@gmail.com",
                                msg=f"Message from Kosmonavt ({args[0]}"
                                    "\n\n "
                                    f"Name: {args[1]}, phone {args[2]}, message: \n {args[3]}"
                                )
    return wrapper
