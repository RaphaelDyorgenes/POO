# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2 - Listar pessoa Fisica / 3 - Sair
# 1 - Cadastrar Pessoa Juridica / 2 - Listar pessoa Juridica / 3 - Sair
from datetime import date, datetime
from Pessoa import PessoaFisica, Endereco

def main():
    lista_pf = []
    while True:
        opcao = int(input("Escolha uma opcao:  1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair"))
        
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar pessoa Fisica / 3 - Voltar ao menu anterior"))
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal(Digite somente numeros):"))
                    data_nascimento = input("Digite a date de nascimento (dd/mm/aaaa): ")
                    novapf.datanascimento = datetime.strptime(data_nascimento, '%d/1%m/%Y').date()
                    idade = (date.today()-novapf.datanascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue

                    novo_end_pf.logradouro = input("Digite o Logradouro")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial S/N")
                    novo_end_pf.endereco_comercial = end_comercial .strip().upper() == "S"

                    novapf.endereco = novo_end_pf
                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereço Nacimento: {cada_pf.data_Nascimento.steftime("%s%m%y")}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair")
                
                    else:
                        print("Lista Vazia")
                #sair do menu
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opção inválida, por favor digite uma das opções indicadas:")

        elif opcao == 2:
            print("Fun não implemnt")
            pass

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema")
            break

        else: print("Opção invalida, por favor digite uma das opcoes validas! ")

if __name__ == "__main__":
    main()
