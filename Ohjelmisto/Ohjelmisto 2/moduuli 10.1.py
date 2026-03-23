


class Hissi:

    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self,kohde):
        while self.nykyinen_kerros < kohde:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde:
            self.kerros_alas()
    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1


    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -=1


h = Hissi(1, 10)

h.siirry_kerrokseen(5)

print(h.nykyinen_kerros)
h.siirry_kerrokseen(1)

print(h.nykyinen_kerros)