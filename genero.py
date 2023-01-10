pergunta = str(input("Digite M para masculino e F para Feminino:"))
processamento="m" or "M" or 'f' or 'F'
if pergunta in ['m', 'M','f','F']:
    print("Sexo valido")
else:
    print('sexo invalido')
erro1 = str(input("Digite novamente:"))
if erro1 in ['m', 'M','f','F']:
    print("Sexo valido")
exit()