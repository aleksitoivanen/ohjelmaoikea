Hytti = str(input("syötä hyttitunniste: "))
if Hytti == "A" or Hytti == "a" :
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif Hytti == "B" or Hytti == "b" :
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif Hytti == "C" or Hytti == "c" :
    print("C on ikkunaton hytti autokannen alapuolella.")

elif Hytti == "LUX" or Hytti == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")

else: print("Virheellinen hyttiluokka")
