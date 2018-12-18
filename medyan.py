def medyanDegeri(dizi, medyanNi):
    terim = int(((medyanNi+1) / 2))
    if medyanNi%2==0:
        islem = (dizi[terim-1]+dizi[terim])/2
        print("Değer = {}\n".format(islem))
    else:
        print("Değer = {}\n".format(dizi[terim-1]))
## Basit seride
basitMedyanDegerleri = [12, 23, 36, 49]
basitMedyanNi = len(basitMedyanDegerleri)

print("Basit Seri")
medyanDegeri(basitMedyanDegerleri, basitMedyanNi)

## Sıralanmış seride
##siralanmisDegerler = [(11, 2), (22, 3), (34, 4), (45, 2)]
siralanmisDegerler = [(13, 3), (24, 6), (37, 4), (48, 5)]
yeniSiralanmisDegerler = []
for (x,i) in siralanmisDegerler:
    for j in range(i):
        yeniSiralanmisDegerler.append(x)
        
print("Sıralanmış Seri")
medyanDegeri(yeniSiralanmisDegerler, len(yeniSiralanmisDegerler) )

## Gruplanmış seride

def medyanSinifiIndex(dizi, frekans):
    hangiNIcinde = 0
    index = 0
    for ((mini, maxi), n) in dizi:
        hangiNIcinde += n
        if hangiNIcinde > frekans:
            return index
        index += 1
    return -1

gruplanmisDegerler = [((0, 2), 4), ((2, 4), 3), ((4, 6), 1), ((6, 8), 2)]
##gruplanmisDegerler = [((4, 7), 8), ((7, 10), 5), ((10, 13), 2)]

gruplanmisNToplami = 0
for ((mini, maxi), n) in gruplanmisDegerler:
    gruplanmisNToplami += n

toplamFrekansinYarisi = float(gruplanmisNToplami/2)
medyanSinifi = gruplanmisDegerler[medyanSinifiIndex(gruplanmisDegerler, toplamFrekansinYarisi)]

L = medyanSinifi[0][0]
S = medyanSinifi[0][1]-medyanSinifi[0][0]

birOncekiMedyanSinifiFrekansi = gruplanmisDegerler[medyanSinifiIndex(gruplanmisDegerler, toplamFrekansinYarisi)-1][1] if medyanSinifiIndex(gruplanmisDegerler, toplamFrekansinYarisi)-1 != -1 else 0

sonuc = L + (S * ( toplamFrekansinYarisi - birOncekiMedyanSinifiFrekansi ) / medyanSinifi[1])

print("Gruplanmış Seri")
print("Değer = {}".format(sonuc))