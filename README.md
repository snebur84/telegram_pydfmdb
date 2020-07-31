### Chatbot Telegram

Este app é um chatbot para Telegram feito em Python, que utiliza o Dialogflow do GCP para gerar as respostas e as registra em uma base MongoDB.

##Instruções:</br>
Antes de iniciar será necessário criar dois arquivos:
- config.py - que deverá conter as seguintes variáveis:
	- api_key_telegram = "Token de acesso a API do Telegram"
	- lang = "pt-br"
	- dburl = "URL de acesso ao MongoDB"

- credentials.json - arquivo json com as credenciais do DialogFlow da GCP.

## Links
`<link>` :<https://core.telegram.org/bots> - Como criar bots no Telegram </br>
`<link>` :<https://docs.mongodb.com/manual/reference/connection-string/> - Como obter a url de conexão ao MongoDB</br>
`<link>` : <https://cloud.google.com/dialogflow/docs/quick/setup?hl=pt-br> - Como criar o agente no DialogFlow e baixar o arquivo credentials.json</br>
