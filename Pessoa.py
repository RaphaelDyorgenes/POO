#Classe Pessoa
#Classe pesoa fisica
#Classe pessoa juridica
#Classe endereço
from datetime import date, datetime

class Endereco:
    def __init__(self, logradouro = "", numero = "", endereco_comercial=False):
        #Inicializar os atributos padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial= endereco_comercial

class Pessoa:
    def __init__(self, nome = "", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco
    def calcular_imposto(self, rendimento):
        return rendimento

class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco = None, cpf="", dataNascimento=None ):
        if endereco is None:
            endereco = Endereco()
        if dataNascimento is None:
            dataNascimento = date.today()

        super().__init__(nome, endereco, rendimento)


        self.cpf = cpf
        self.datanascimento = dataNascimento
    
    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return rendimento*0.2
        elif 3500 < rendimento <= +600:
            return (rendimento / 100) * 3.5
        else: return 6000

class PessoaJuridica(Pessoa):
    pass 