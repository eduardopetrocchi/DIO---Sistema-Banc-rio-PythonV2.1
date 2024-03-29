from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print(
                "\n === Você excedeu o número de transações permitidas para o dia! ==="
            )
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nasc, cpf, endereco) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

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

    def sacar(self, valor):
        saldo = self.saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:
            print(
                f"Operação não realizada: Saldo insuficiente. Saldo atual: R${self._saldo}"
            )
        elif valor > 0:
            self._saldo -= valor
            print(
                f"Saque no valor de R${valor} realizado com sucesso. Saldo atual: R${self._saldo}"
            )
            return True
        else:
            print("Operação inválida")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(
                f"Depósito no valor de R${valor} realizado com sucesso. Saldo atual: R${self._saldo}"
            )

        else:
            print("Valor invalido!")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )
        execedeu_limite = valor > self.limite
        execeu_saques = numero_saques >= self.limite_saques

        if execedeu_limite:
            print(f"O valor execede o limite de saque.")
        elif execeu_saques:
            print(f"Execede quantidade de saques/mês.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        return f"""\
            Agência: \t{self.agencia}
            C\C: \t\t{self.numero}
            Titular: \t{self.cliente.nome}
        """


class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
