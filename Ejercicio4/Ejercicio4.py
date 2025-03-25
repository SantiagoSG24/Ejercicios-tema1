from collections import deque

class Mision:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __repr__(self):
        return f"Mision({self.nombre})"

class ColaDeMisiones:
    def __init__(self):
        self.cola = deque()

    def agregar_mision(self, mision):
        self.cola.append(mision)
        self.cola = deque(sorted(self.cola, key=lambda x: x.dificultad))

    def obtener_mision(self):
        return self.cola.popleft() if self.cola else None

    def mostrar_misiones(self):
        for mision in self.cola:
            print(mision)

# Ejemplo de uso
cola_misiones = ColaDeMisiones()
cola_misiones.agregar_mision(Mision("Rescatar al prisionero", 3))
cola_misiones.agregar_mision(Mision("Recolectar suministros", 1))
cola_misiones.agregar_mision(Mision("Defender la base", 2))

cola_misiones.mostrar_misiones()