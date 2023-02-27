def genero():
        erro = ('==========')
        pergunta = str(input('Digite M para masculino e F para Feminino:'))
        if pergunta in ['m', 'M', 'f', 'F']:
          print('Sexo valido')

        else:

         erro: str = str(input('Digite novamente:'))
        if erro in ['m', 'M', 'f', 'F']:
           print('Sexo valido')

if __name__ == '__main__':
     genero()
