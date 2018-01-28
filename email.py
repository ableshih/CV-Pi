
# from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart


# from email import Encoders, Utils
from email.utils import formatdate, make_msgid

    # mail['Date'] = Utils.formatdate(localtime=1)
    mail['Date'] = formatdate(localtime=1)

    # mail['Message-ID'] = Utils.make_msgid()
    mail['Message-ID'] = make_msgid()

    # s = smtplib.SMTP(smtp_server, smtp_port)
    s = smtplib.SMTP_SSL(smtp_server, smtp_port)
