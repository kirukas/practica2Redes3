
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
 
class MAIL:
    def __init__(self):
        self.myEmail = "eherme90@gmail.com"
        self.myPassword = "Eherme123"
        self.mailServer = "smtp.gmail.com:587"
       
    def send(self,toEmail,subject,Image):
        # create message object instance
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.myEmail
        msg['To'] = toEmail
        ## loading  image
        fp = open(Image, 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
         # create server
        server = smtplib.SMTP(self.mailServer)
        try:
           
            server.starttls()
            server.login(self.myEmail,self.myPassword)
            server.sendmail(self.myEmail,toEmail,msg.as_string())
            print("Mail send successful")
        except Exception:
            print ("Error: unable to send email")
        server.quit()
    def setMyEmail(self, myEmail):
        self.myEmail = myEmail
    def setMyPasword(self,p):
        self.myPassword = p
    def getMyEmail(self):
        return self.myEmail
    
