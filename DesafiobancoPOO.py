import textwrap
from datetime import datetime
from abc import ABC, abstractmethod

# ------------------ Histórico ------------------
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def listar(self):
        return self.transacoes


# ------------------ Interface Transação ------------------
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


# ------------------ Conta ------------------
class Conta:
    BANCO = "ABMS"

    def __init__(self, numero, cliente, agencia="0001"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor: float) -> bool:
        if valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False
        elif valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


# ------------------ Conta Corrente ------------------
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False
        elif self._saques_realizados >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        if super().sacar(valor):
            self._saques_realizados += 1
            return True
        return False


# ------------------ Transações ------------------
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(
                f"Depósito:\tR$ {self._valor:.2f}"
            )


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(
                f"Saque:\t\tR$ {self._valor:.2f}"
            )


# ------------------ Cliente ------------------
class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf


# ------------------ Funções auxiliares ------------------
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


def validar_data(data):
    try:
        return datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        return None


def preencher_endereco():
    endereco = {}
    endereco["rua"] = input("Rua: ").strip()
    endereco["numero"] = input("Número: ").strip()
    endereco["bairro"] = input("Bairro: ").strip()
    endereco["cidade"] = input("Cidade: ").strip()
    endereco["estado"] = input("Estado (sigla): ").strip().upper()

    if all(endereco.values()):
        return endereco
    else:
        print("\n@@@ Todos os campos do endereço são obrigatórios! @@@")
        return preencher_endereco()


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [l]\tLogin
    [o]\tLogout
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    return cliente.contas[0]


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.listar()

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(transacao)

    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


# ------------------ Main ------------------
def main():
    clientes = []
    contas = []
    usuario_logado = None

    while True:
        opcao = menu()

        if opcao == "d":
            if not usuario_logado:
                print("\n@@@ Nenhum usuário logado! Faça login. @@@")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            conta = recuperar_conta_cliente(usuario_logado)
            if conta:
                usuario_logado.realizar_transacao(conta, transacao)

        elif opcao == "s":
            if not usuario_logado:
                print("\n@@@ Nenhum usuário logado! Faça login. @@@")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            conta = recuperar_conta_cliente(usuario_logado)
            if conta:
                usuario_logado.realizar_transacao(conta, transacao)

        elif opcao == "e":
            if not usuario_logado:
                print("\n@@@ Nenhum usuário logado! Faça login. @@@")
                continue

            conta = recuperar_conta_cliente(usuario_logado)
            if conta:
                exibir_extrato(conta)

        elif opcao == "nu":
            cpf = input("Informe o CPF (somente números): ")

            if not validar_cpf(cpf):
                print("\n@@@ CPF inválido! @@@")
                continue

            cliente = filtrar_cliente(cpf, clientes)
            if cliente:
                print("\n@@@ Já existe usuário com esse CPF! @@@")
                continue

            nome = input("Informe o nome completo: ")

            data_nascimento = None
            while not data_nascimento:
                data_input = input("Informe a data de nascimento (dd/mm/aaaa): ")
                data_nascimento = validar_data(data_input)
                if not data_nascimento:
                    print("\n@@@ Data inválida! Tente novamente. @@@")

            print("\n=== Endereço ===")
            endereco = preencher_endereco()

            cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
            clientes.append(cliente)

            print("=== Usuário criado com sucesso! ===")

        elif opcao == "nc":
            if not usuario_logado:
                print("\n@@@ Nenhum usuário logado! Faça login. @@@")
                continue

            numero_conta = len(contas) + 1
            conta = ContaCorrente.nova_conta(usuario_logado, numero_conta)
            contas.append(conta)
            usuario_logado.adicionar_conta(conta)

            print(f"\n=== Conta criada com sucesso no banco {Conta.BANCO}! Limite de saque: R$500,00 ===")

        elif opcao == "lc":
            for conta in contas:
                print("=" * 100)
                print(f"Banco:\t\t{Conta.BANCO}")
                print(f"Agência:\t{conta.agencia}")
                print(f"C/C:\t\t{conta.numero}")
                print(f"Titular:\t{conta.cliente.nome}")

        elif opcao == "l":
            cpf = input("Informe o CPF: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente:
                usuario_logado = cliente
                print(f"\n=== Login realizado com sucesso! Bem-vindo, {cliente.nome}. ===")
            else:
                print("\n@@@ Cliente não encontrado! @@@")

        elif opcao == "o":
            if usuario_logado:
                print(f"\n=== Logout realizado: {usuario_logado.nome} ===")
                usuario_logado = None
            else:
                print("\n@@@ Nenhum usuário logado! @@@")

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida! @@@")


# executa
main()
