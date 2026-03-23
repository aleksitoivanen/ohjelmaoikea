


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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm

        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja(self, hissin_numero, kohde):

        hissi = self.hissit[hissin_numero -1]
        hissi.siirry_kerrokseen(kohde)




talo = Talo(1, 10, 3)
talo.aja(1,5)
print(talo.hissit[0].nykyinen_kerros)
talo.aja(2, 8 )
print(talo.hissit[1].nykyinen_kerros)
