import requests as Req

p = input("Por Favor , informe Qual produto você quer ver? ")
url = "http://127.0.0.1:7000/produtos/" + p
retorno = Req.api.get(url).json()
print(retorno)