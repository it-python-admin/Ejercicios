import smtplib
import logging
#logging.getLogger().setLevel(logging.DEBUG)
remitente="pruebas.email.python@gmail.com"
password="ITTIPython@2021"
destinatario="pruebas.email.python@gmail.com"
asunto="Prueba"
mensaje="Subject:{}\n{}".format("El otro asunto...","El mensaje")
try:
    logging.debug("Step 1")
    server = smtplib.SMTP('smtp.gmail.com',587)
    logging.debug("Step 2")
    #server.ehlo()
    logging.debug("Step 3")
    server.starttls()
    logging.debug("Step 4")
    server.login(remitente, password)
    logging.debug("Step 5")
    server.sendmail(remitente, destinatario, mensaje)
    logging.debug("Step 6")
    server.quit()
    logging.debug("Step END")
except Exception as e:
    print(e)
