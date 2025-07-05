# ----------------- FUNÇOES ---------------- #
def deposita ():
    global saldo, extrato

    while True:
        valor_deposito = float(input("Qual valor deseja depositar? "))

        if (valor_deposito > 0):
            saldo += valor_deposito
            print("Depósito concluído com sucesso.")
            extrato += f"Depósito: R$ {valor_deposito:.2f} \n"
            break
        else:
            print("Valor inválido. Tente novamente")
            continue

def saca ():
    global saldo, extrato, limite_saque
    
    print(saldo)
    valor_saque = float(input("Qual valor deseja sacar? "))

    if(valor_saque > saldo):
        print("Saldo Insuficiente.")
    elif(valor_saque > 500):
        print("Limite de valor para saque excedido. Limite máximo por saque: R$500,00.")
    else:
        if(limite_saque > 0):
            saldo -= valor_saque
            print("Saque concluído.")
            extrato += f"Saque: {valor_saque:.2f} \n"
            limite_saque -= 1
        else:
            print("Você atingiu o limite de saque diário.")


def ve_extrato():
    global saldo, extrato

    if not extrato:
        print("Não foram realizadas movimentações.")
        print(f"Saldo: {saldo:.2f}")
    else:
        print(extrato)
        print(f"Saldo: {saldo:.2f}")

# ---------------- Variaveis ------------- #
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0.0
limite = 500
extrato = ""
qnt_saque = 0
limite_saque = 3

# ---------------- Main -------------- #
while True:
    print(menu)
    opcao_menu = input("Escolha uma opção: ")

    if (opcao_menu == "d"):
        deposita()
    elif (opcao_menu == "s"):
        saca()
    elif (opcao_menu == "e"):
        ve_extrato()
    elif (opcao_menu == "q"):
        break
    else:
        print("Opção Inválida")