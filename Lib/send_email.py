from redmail import EmailSender

# Configure the sender
email = EmailSender(host="localhost", port=0)

def send_email(title, txt):
    # Send the email
    email.send(
        subject=title,
        sender="remi.lapointe@free.fr",
        receivers=['remi.lapointe@gmail.com'],
        text=txti #,
#        html="<h1>" + txt + "</h1>"
    )

