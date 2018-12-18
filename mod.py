## Sınıflanmış seride
siniflanmisDegerler = [(2, 3), (3, 6), (6, 4), (7, 5)]
siniflanmisMaxIndex = 0
siniflanmisMaxN = siniflanmisDegerler[0][1]
for index, (xi, n) in enumerate(siniflanmisDegerler):
    if siniflanmisMaxN < n:
        siniflanmisMaxN = n
        siniflanmisMaxIndex = index
    
print("""
Sınıflanmış Seride
Xi\tN
{}\t{}

Mod = {}
""".format(siniflanmisDegerler[siniflanmisMaxIndex][0], siniflanmisDegerler[siniflanmisMaxIndex][1], siniflanmisDegerler[siniflanmisMaxIndex][0] ))
## Gruplanmış seride

gruplanmisDegerler = [((0, 2), 3), ((2, 4), 2), ((4, 6), 4), ((6, 8), 1)]
##gruplanmisDegerler = [((90, 100), 50), ((85, 89), 60), ((80, 84), 40), ((75, 79), 50), ((70, 74), 100), ((60, 69), 50), ((50, 59), 60), ((40, 49), 40), ((0, 39), 50)]

gruplanmisMaxIndex = 0
gruplanmisMaxN = gruplanmisDegerler[0][1]

for index, ((mini, maxi), n) in enumerate(gruplanmisDegerler):
    if gruplanmisMaxN < n:
        gruplanmisMaxN = n
        gruplanmisMaxIndex = index

birOncekiModSinifi = gruplanmisDegerler[gruplanmisMaxIndex-1]
modSinifi = gruplanmisDegerler[gruplanmisMaxIndex]
birSonrakiModSinifi = gruplanmisDegerler[gruplanmisMaxIndex+1]

modSinifininAltSiniri = modSinifi[0][0]
modSinifininAraligi = modSinifi[0][1] - modSinifi[0][0]

delta1 = abs(modSinifi[1] - birOncekiModSinifi[1])
delta2 = abs(modSinifi[1] - birSonrakiModSinifi[1])

sonuc = modSinifininAltSiniri + ( modSinifininAraligi * ( delta1 / (delta1 + delta2) ) )

print("""
Gruplanmış Seride
Sınıf\tN
{}-{}\t{}

Mod = {}
""".format(modSinifi[0][0], modSinifi[0][1], modSinifi[1], sonuc))