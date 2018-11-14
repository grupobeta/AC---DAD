import requests as Req

p = input("Por Favor, informe Qual produto você quer deletar? ")
url = "http://127.0.0.1:7000/produtos/" + p
retorno = Req.api.delete(url).json()
print(retorno)