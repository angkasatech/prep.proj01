"""
Tipe data dictionary sekedar menghubungkan antara KEY dan Value
KVP = Key Value Pair
dictionary ~ kamus
"""
kamus_id_en = {}
kamus_id_en['anak'] = 'son'
kamus_id_en['ibu'] = 'mother'
kamus_id_en['bapak'] = 'father'

# kamus_id_en = {'anak': 'son', 'ibu': 'mother', 'bapak': 'father'} #sama seperti diatas lebih simpel

print(kamus_id_en)
print(kamus_id_en['ibu'])
print(kamus_id_en['bapak'])

# Case Study "gojek"
print('\nData ini dikirimkan oleh server gojek, untuk informasi driver disekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '17-10-2020',
    'driver_list': [{'nama':'ujang', 'jarak': 13}, {'nama':'mang oleh','jarak': 5}, {'nama':'atep','jarak':'22'}, {'nama':'tisna','jarak':'14'}]
}

print(data_dari_server_gojek)
print(f"\ndriver disekitar sini{data_dari_server_gojek['driver_list']}")
print(f"driver pertama {data_dari_server_gojek['driver_list'][0]}")
print(f"driver keempat {data_dari_server_gojek['driver_list'][3]}")

print(f"Jarak driver ketiga (terdekat) {data_dari_server_gojek['driver_list'][1]['jarak']} meter")