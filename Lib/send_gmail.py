from redmail import gmail

# Configure the sender
gmail.username = "remi.lapointe@gmail.com"
gmail.password = "sucatohgoqklwpfa"

def send_gmail(title, txt):
    # Send the email
    gmail.send(
        subject=title,
        sender='remi.lapointe@free.fr',
        receivers=['remi.lapointe@gmail.com'],
        text=txt#,
#        html="<h1>" + txt + "</h1>"
    )

