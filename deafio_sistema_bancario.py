import textwrap as tw

from classes import PessoaFisica
from classes import  ContaCorrente, Saque, Deposito

def menu():
    menu_text = """
    ╔═════════════════════════ MENU ═════════════════════════╗
    ║ [1] Depositar                                          ║
    ║ [2] Sacar                                              ║
    ║ [3] Extrato                                            ║
    ║ [4] Cadastrar cliente                                  ║
    ║ [5] Criar contas                                       ║
    ║ [6] Listar contas                                      ║
    ║ [0] Sair                                               ║
    ╚════════════════════════════════════════════════════════╝

    DIGITE A OPÇÃO DESEJADA:
    """
    return input(tw.dedent(menu_text))

def depositar(clientes):
    cpf = input("Digite o CPF do titular da conta: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n ══════Cliente não encontrado══════")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta: 
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Digite o CPF do titular da conta: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n ══════Cliente não encontrado══════")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
def exibir_extrato(clientes):
    cpf = input("Digite o CPF do titular da conta: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n ══════Cliente não encontrado══════")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n══════════════════EXTRATO══════════════════")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\tR${transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo: \n\n R$ {conta.saldo:.2f}")
    print("═══════════════════════════════════════════")
    
def criar_cliente(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n Cliente já cadastrado")
        return
    
    nome = input("Informe o nome completo do clinte: ")
    data_nasc = input("Data de nascimento: ")
    endereco = input("Endereço: ")
    
    cliente = PessoaFisica(nome=nome, data_nasc=data_nasc, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    
    print("\n Cliente cadastrado com sucesso!!!")

def listar_contas(contas):
    for conta in contas:
        print("="*100)
        print(tw.dedent(str(conta)))

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o CPF do titular da conta: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n Cliente não encontrado")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print(f"\n══════CONTA CRIADA COM SUCESSO!!!══════ \nBem-vindo {cliente.nome}")
    

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui nenhuma conta cadastrada.")
        return
    return cliente.contas[0]

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()        
        if opcao == "1":
            depositar(clientes)            
        elif opcao == "2":
            sacar(clientes)               
        elif opcao == "3":
            exibir_extrato(clientes)              
        elif opcao == "4":
            criar_cliente(clientes)     
        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)     
        elif opcao == "6":
            listar_contas(contas)                
        elif opcao == "0":
            print("Obrigado pela atenção!")
            break 
        else:
            print("Insira uma opção válida")
            
main()