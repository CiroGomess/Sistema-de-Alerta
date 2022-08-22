# Contação do dolar for menor que 5.20

import requests
import smtplib
import email.message

# Pegando informação

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
# jwelliton3@gmail.com
emails = ['ciro.ggj@gmail.com', 'dev.ggjs@gmail.com']

req = requests.get(url)
req_dicionario = req.json()


contacao = float(req_dicionario['USDBRL']['bid'])


# Enviar um aviso

def enviar_email(contacao):  
    corpo_email = f"""
    <p>Dólar está abaixo de R$5.20. Contação atual: R${contacao}</p>
    """
    count = 0
    for i in range(len(emails)):

        if count != len(emails):
            msg = email.message.Message()
            msg['Subject'] = "Dólar abaixo de R$5.20"
            msg['From'] = 'dev.ggjs@gmail.com'
            msg['To'] = emails[i]
            password = 'xawckozaqjyumkpn' 
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email )

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print('Email enviado')
            count = count + 1
if contacao < 5.20:
   enviar_email(contacao)




# Deploy - heroku