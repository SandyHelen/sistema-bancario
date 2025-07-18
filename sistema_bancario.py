# ----------------- FUNÇOES ---------------- #
def cadastra(clientes):
    cpf = input("Digite seu CPF (somente números)")
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            print("Ja existe um cadastro para este CPF.")
            print("================================")
            return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla do estado):")

    clientes.append({"Nome": nome, "Data de nascimento": data_nascimento, "Endereço": endereco, "CPF":cpf})

def cria_conta(clientes, agencia, num_conta):
    cpf = input("Digite seu CPF (somente números)")
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            print("Conta criada com sucesso!")
            return {"Agência": agencia, "Número de conta": num_conta, "Usuário": cliente} 
    
    print("Usuário não encontrado.")
    print("================================")

def lista_conta(contas):
    for conta in contas:
        print(f"""
==================================
Agência: {conta["Agência"]}
Conta: {conta["Número de conta"]}
Titular: {conta["Usuário"]["Nome"]}
==================================
""")

def deposita (saldo, extrato):

    while True:
        valor_deposito = float(input("Qual valor deseja depositar? "))

        if (valor_deposito > 0):
            saldo += valor_deposito
            print("Depósito concluído com sucesso.")
            print("================================")
            extrato += f"Depósito: R$ {valor_deposito:.2f} \n"
            return saldo, extrato
        else:
            print("Valor inválido. Tente novamente.")
            print("================================")
            continue

def saca (*, saldo, extrato, limite_saque):
    
    print(saldo)
    valor_saque = float(input("Qual valor deseja sacar? "))

    if(valor_saque > saldo):
        print("Saldo Insuficiente.")
        print("================================")
    elif(valor_saque > 500):
        print("Limite de valor para saque excedido. Limite máximo por saque: R$500,00.")
        print("================================")
    else:
        if(limite_saque > 0):
            saldo -= valor_saque
            print("Saque concluído.")
            print("================================")
            extrato += f"Saque: {valor_saque:.2f} \n"
            limite_saque -= 1
        else:
            print("Você atingiu o limite de saque diário.")
            print("================================")
    return saldo, extrato, limite_saque


def ve_extrato(saldo,/, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
        print(f"Saldo: {saldo:.2f}")
        print("================================")
    else:
        print(extrato)
        print(f"Saldo: {saldo:.2f}")
        print("================================")

# ---------------- Variaveis ------------- #
menu = """
================================
[nu] Novo usuário
[cc] Criar conta
[lc] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
================================
"""

saldo = 0.0
limite = 500
extrato = ""
qnt_saque = 0
LIMITE_SAQUE = 3
AGENCIA = "0001"
clientes = []
contas = []

# ---------------- Main -------------- #
while True:
    print(menu)
    opcao_menu = input("Escolha uma opção: ")

    if (opcao_menu == "d"):
        saldo, extrato = deposita(saldo, extrato)
    elif (opcao_menu == "s"):
        saldo, extrato, LIMITE_SAQUE = saca(saldo=saldo, extrato=extrato, limite_saque=LIMITE_SAQUE)
    elif (opcao_menu == "e"):
        ve_extrato(saldo, extrato=extrato)
    elif (opcao_menu == "nu"):
        cadastra(clientes)
    elif (opcao_menu == "cc"):
        num_conta = len(contas)+1
        conta = cria_conta(clientes, AGENCIA, num_conta)

        if conta:
            contas.append(conta)
        print(contas)
    elif (opcao_menu == "lc"):
        lista_conta(contas)
    elif (opcao_menu == "q"):
        break
    else:
        print("Opção Inválida")