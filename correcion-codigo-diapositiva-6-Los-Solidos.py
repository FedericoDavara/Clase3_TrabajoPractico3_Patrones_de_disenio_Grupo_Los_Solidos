from abc import ABC, abstractmethod
class FabricaMercado(ABC):
    @abstractmethod
    def crear_moneda(self): ...
    @abstractmethod
    def crear_documento(self): ...
class FabricaArgentina(FabricaMercado):
    def crear_moneda(self): return "ARS"
    def crear_documento(self): return "DNI"
class FabricaEuropa(FabricaMercado):
    def crear_moneda(self): return "EUR"
    def crear_documento(self): return "Pasaporte"
def formulario(fabrica): return f"{fabrica.crear_documento()} en {fabrica.crear_moneda()}"

print(formulario(FabricaEuropa()))

class FabricaBrasil(FabricaMercado):
    def crear_moneda(self): return "BRL"
    def crear_documento(self): return "CPF"