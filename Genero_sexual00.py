class ValidaGenero:
    def __init__(self):
        self.genero = None

    def validar_genero(self):
        while True:
            pergunta = input('Digite M para masculino e F para Feminino: ').strip().upper()
            if pergunta in ['M', 'F']:
                self.genero = pergunta
                print('Sexo válido')
                break
            else:
                print('Digite novamente.')

if __name__ == '__main__':
    genero = ValidaGenero()
    genero.validar_genero()
    print('Gênero escolhido:', genero.genero)