class Conta:
  
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
      print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
      
    def depositar(self, valor):
      self.__saldo += valor
      
    def __pode_sacar(self, valor_a_sacar):
      valor_disponivel_a_sacar = self.__saldo + self.__limite
      return valor_a_sacar <= valor_disponivel_a_sacar
      
    def sacar(self, valor):
      if(self.__pode_sacar(valor)):
        self.__saldo -= valor
      else:
        print("O valor {} passou o limite".format(valor))
      
    def transferir(self, valor, destino):
      self.sacar(valor)
      destino.depositar(valor)
    
    @property
    def saldo(self):
      return self.__saldo
    
    @property
    def titular(self):
      return self.__titular
    
    @property
    def limite(self):
      return self._limite
    
    @limite.setter
    def set_limite(self, limite):
      self.__limite = limite
    
    @staticmethod
    def codigoa_banco():
      return "001"
    
    @staticmethod
    def codigos_bancos():
      return {'BB': '001', 'Caixa':'104', 'Bradesco':'237'}