import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Definir a chave API como uma variável de ambiente ou usar um método seguro
api_key = ""  # Substitua pela sua chave API

# Definir o template de prompt
template_mensagem = ChatPromptTemplate.from_messages(
    [
        ("system", "Traduza o texto a seguir para {idioma}"),
        ("user", "{texto}")
    ]
)

# Criar o modelo com a chave API
modelo = ChatOpenAI(model="gpt-4", api_key=api_key)

# Gerar o prompt usando o template
#prompt = template.format(idioma="ingles", texto="De um like e comente no vídeo")

# Invocar o modelo com o prompt gerado
#resposta = modelo.invoke(prompt)

chain = template_mensagem | modelo 

# Imprimir a resposta
 
