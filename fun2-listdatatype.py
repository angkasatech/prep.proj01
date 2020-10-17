# DataType

# tipe data skalar => tipe data sederhana
anak1 = 'Ukasyah'
anak2 = 'Medina'
anak3 = 'Umar'
anak4 = 'Khodijah'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

# Tipe data list/daftar/array
anak = ['Ukasyah','Medina','Umar','Khodijah']
print(anak)
anak.append('Kahfi')
print(anak)

# panggil anak ke-n
print(f'Hai {anak[0]} !')

print('panggil semua anak')
for semuaanak in anak:
    print(f'Assalamualaikum {semuaanak}!')

print('panggil semua anak: cara ribet')
for semuaanak in range(0, len(anak)):
    print(f'{semuaanak+1}. Tabarakallah {anak[semuaanak]}!')
