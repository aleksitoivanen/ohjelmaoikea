kuukaudet = ("joulukuu", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu","kesa", "heinakuu", "elokuu", "syyskuu", "lokakuu", "marraskuu" )
jarjestysnumero = int(input("syötä kuukauden järjestysnumero (1-12): "))
if jarjestysnumero in (12, 1, 2):
    vuodenaika = "talvi"
elif jarjestysnumero in (3, 4, 5):
    vuodenaika = "kevät"
elif jarjestysnumero in (6, 7, 8):
    vuodenaika = "kesä"
else :
    vuodenaika = "syksy"

print(f"{jarjestysnumero}. vuodenaika on", vuodenaika  )

