def criar_conta():
    nome = input("Informe o nome do usuário: ")
    saldo_inicial = 0.0
    return {'nome': nome, 'saldo': saldo_inicial, 'extrato': '', 'numero_saques': 0}

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta['saldo']
    excedeu_limite = valor > LIMITE_SAQUE
    excedeu_saques = conta['numero_saques'] >= LIMITE_SAQUES
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
        conta['numero_saques'] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def extrato_bancario(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

def main():
    contas = []
    
    while True:
        opcao = input(menu)
        
        if opcao == "c":
            contas.append(criar_conta())
        elif opcao == "d":
            nome = input("Informe o nome do usuário: ")
            conta = next((c for c in contas if c['nome'] == nome), None)
            if conta:
                depositar(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == "s":
            nome = input("Informe o nome do usuário: ")
            conta = next((c for c in contas if c['nome'] == nome), None)
            if conta:
                sacar(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == "e":
            nome = input("Informe o nome do usuário: ")
            conta = next((c for c in contas if c['nome'] == nome), None)
            if conta:
                extrato_bancario(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

menu = """
[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

if __name__ == "__main__":
    main()
