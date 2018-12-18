from math import sqrt
##Basit seride
basitXi = [4, 5, 7, 8, 16]
basitNi = len(basitXi)
basitToplam = 0
for xi in basitXi:
    basitToplam += xi**2

basitSonuc = sqrt(float(basitToplam / basitNi))

print("Basit Seride Sonuç =", basitSonuc)

##Sınıflanmış seride
siniflanmisDegerler = [(2, 3), (3, 2), (4, 1), (5, 4)]
siniflanmisNi = 0
siniflanmisNiXi = 0

for (xi, ni) in siniflanmisDegerler:
    siniflanmisNi += ni
    siniflanmisNiXi += ni*(xi**2)

siniflanmisSonuc = sqrt(float(siniflanmisNiXi / siniflanmisNi))

print("Sınıflanmış Seride Sonuç =", siniflanmisSonuc)

##Gruplanmış seride
gruplanmisDegerler = [((1, 3), 3), ((3, 5), 3), ((5, 7), 4)]
gruplanmisNi = 0
gruplanmisNiMi = 0
for ((mini, maxi), ni) in gruplanmisDegerler:
    gruplanmisNi +=ni
    ortaNokta = (maxi+mini)/2
    ortaNoktaKaresi = ortaNokta**2
    gruplanmisNiMi += ni*ortaNoktaKaresi

gruplanmisSonuc = sqrt(float(gruplanmisNiMi / gruplanmisNi))

print("Gruplanmış Seride Sonuç =", gruplanmisSonuc)