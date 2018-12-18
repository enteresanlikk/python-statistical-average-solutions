##Basit seride
basitXi = [4, 5, 7, 8, 16]
basitToplam = 0
basitNi = len(basitXi)

for ni in basitXi:
    basitToplam += ni

basitSonuc = float(basitToplam / basitNi)

print("Basit Seride Sonuç =", basitSonuc)

##Sınıflanmış seride
siniflanmisDegerler = [(2, 3), (3, 2), (4, 1), (5, 4)]
siniflanmisToplam = 0
siniflanmisNi = 0

for (xi, ni) in siniflanmisDegerler:
    siniflanmisNi = siniflanmisNi + ni
    siniflanmisToplam += (xi*ni)

siniflanmisSonuc = float(siniflanmisToplam / siniflanmisNi)

print("Sınıflanmış Seride Sonuç =", siniflanmisSonuc)

##Gruplanmış seride
gruplanmisSiniflar = [((1, 3), 3), ((3, 5), 3), ((5, 7), 4)]
gruplanmisNi = 0
gruplanmisToplam = 0
for ((mini, maxi), ni) in gruplanmisSiniflar:
    gruplanmisToplam += ni
    ortaNokta = (maxi+mini)/2
    gruplanmisNi += ni*ortaNokta

gruplanmisSonuc = float(gruplanmisNi / gruplanmisToplam)

print("Gruplanmış Seride Sonuç =", gruplanmisSonuc)