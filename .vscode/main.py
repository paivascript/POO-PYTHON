class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Saldo inválido.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Saldo insuficiente.")


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial, juros):
        super().__init__(titular, saldo_inicial)
        self.juros = juros

    def aplicar_juros(self):
        self.saldo = self.saldo + (self.saldo * self.juros)
        print(f"Juros aplicados. Novo saldo: R${self.saldo}")


class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        total = valor + taxa
        if total <= self.saldo:
            self.saldo = self.saldo - total
            print("Taxa de R$2 aplicada ao saque (Conta Corrente).")
            print(f"Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente para saque + taxa.")


c1 = ContaBancaria("João", 1000)
c2 = ContaPoupanca("Maria", 1500, 0.10)
c3 = ContaCorrente("Pedro", 2000)

print(c1.saldo)
c1.depositar(500)
c1.sacar(200)
c2.aplicar_juros()
c3.sacar(300)
