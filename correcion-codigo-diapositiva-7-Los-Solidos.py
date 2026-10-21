from abc import ABC, abstractmethod

class Pasaje(ABC):
    def __init__(self, origen, destino, precio):
        if precio < 0: raise ValueError("precio negativo")
        self._origen, self._destino, self._precio = origen, destino, precio
    @property
    def precio(self): return self._precio
    @abstractmethod
    def mostrar_info(self): ...
class PasajeAvion(Pasaje):
    def __init__(self, o, d, p, aerolinea): super().__init__(o, d, p); self._aerolinea = aerolinea
    def mostrar_info(self): print(f"AVION {self._origen}-{self._destino} {self._aerolinea}: {self._precio}")
class PasajeMicro(Pasaje):
    def mostrar_info(self): print(f"MICRO {self._origen}-{self._destino}: {self._precio}")
class PasajeTren(Pasaje):
    def mostrar_info(self): print(f"TREN {self._origen}-{self._destino}: {self._precio}")

class CreadorPasaje(ABC):
    @abstractmethod
    def crear_pasaje(self, origen, destino, precio): ...
    def registrar_pasaje(self, origen, destino, precio):
        p = self.crear_pasaje(origen, destino, precio)
        p.mostrar_info()
        return p
class CreadorAvion(CreadorPasaje):
    def __init__(self, aerolinea): self._aerolinea = aerolinea
    def crear_pasaje(self, o, d, p): return PasajeAvion(o, d, p, self._aerolinea)
class CreadorMicro(CreadorPasaje):
    def crear_pasaje(self, o, d, p): return PasajeMicro(o, d, p)
class CreadorTren(CreadorPasaje):
    def crear_pasaje(self, o, d, p): return PasajeTren(o, d, p)

# ---------- Builder ----------
class Reserva:
    def __init__(self): self.pasajes=[]; self.tasa=0; self.equipaje=0; self.seguro=0
    def subtotal(self): return sum(p.precio for p in self.pasajes)
    def calcular_total(self): return self.subtotal()+self.tasa+self.equipaje+self.seguro
class ReservaBuilder:
    def __init__(self): self.reiniciar()
    def reiniciar(self): self._r = Reserva()
    def set_pasajes(self, ps): self._r.pasajes = list(ps)
    def set_tasa(self): self._r.tasa = 10
    def set_equipaje(self): self._r.equipaje = 30
    def set_seguro(self): self._r.seguro = self._r.subtotal()*0.03
    def build(self):
        r = self._r; self.reiniciar(); return r
class DirectorReserva:
    def __init__(self, builder): self._b = builder
    def set_builder(self, b): self._b = b
    def construir_simple(self, ps):
        self._b.set_pasajes(ps); self._b.set_tasa(); return self._b.build()
    def construir_completa(self, ps):
        self._b.set_pasajes(ps); self._b.set_tasa(); self._b.set_equipaje(); self._b.set_seguro()
        return self._b.build()

p = CreadorMicro().crear_pasaje("MDZ","COR",200.0)
d = DirectorReserva(ReservaBuilder())
reserva = d.construir_completa([p])
print(f"Subtotal: {reserva.subtotal()} Total: {reserva.calcular_total()}")

