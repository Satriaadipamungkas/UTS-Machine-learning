data_set_mahasiswa = [
  {"HARI":"Senin", "DATANG": 2, "BIAYA": 30000 * 2, "MAHASISWA": "Ani"},
  {"HARI":"Selasa", "DATANG": 3, "BIAYA": 35000 * 3, "MAHASISWA": "Budi"},
  {"HARI":"Rabu", "DATANG": 4, "BIAYA": 25000 * 4, "MAHASISWA": "Jono"},
  {"HARI":"Kamis", "DATANG": 1, "BIAYA": 15000 * 1, "MAHASISWA": "Lono"},
  {"HARI":"Jumat", "DATANG": 2, "BIAYA": 20000 * 2, "MAHASISWA": "Joni"},
  {"HARI":"Sabtu", "DATANG": 5, "BIAYA": 30000 * 5, "MAHASISWA": "Ani"},
  {"HARI":"Minggu", "DATANG": 2, "BIAYA": 35000 * 2, "MAHASISWA": "Budi"},
]

print("| HARI   | DATANG | BIAYA        | MAHASISWA |")
print("|--------|--------|--------------|-----------|")

for data in data_set_mahasiswa:
    print(f"| {data['HARI']}   | {data['DATANG']}      | {data['BIAYA']}      | {data['MAHASISWA']}       |")

print(f"\n\n")
# ------------- SOAL ------------- #

# a) Berapa rata-rata mahasiswa datang pada minggu ini?

total_datang = sum(data["DATANG"] for data in data_set_mahasiswa)
rata_datang = total_datang / len(data)
print(f"a) Rata-rata mahasiswa datang pada minggu ini : {rata_datang}")

# b) Kapan biaya tertinggi terjadi ?

biaya_tertinggi = max(data["BIAYA"] for data in data_set_mahasiswa)
hari_biaya_tertinggi = next(data["HARI"] for data in data_set_mahasiswa if data["BIAYA"] == biaya_tertinggi)
print(f"b) Biaya tertinggi terjadi pada hari {hari_biaya_tertinggi}")

# c) Hari apa yang lebih dari 110000 ?

hari_biaya_lebih_dari_110000 = [data["HARI"] for data in data_set_mahasiswa if data["BIAYA"] > 110000]
print(f"c) Hari-hari dimana biaya lebih dari 110000: {' ,'.join(hari_biaya_lebih_dari_110000)}")

# d) Siapa yang paling banyak datang ke kampus ?

mahasiswa_terbanyak = max(set(data["MAHASISWA"] for data in data_set_mahasiswa), key= lambda x: sum(datang["DATANG"] for datang in data_set_mahasiswa if datang["MAHASISWA"] == x))
print(f"d) {mahasiswa_terbanyak} paling banyak datang ke kampus.")

# e) Siapa yang datang pada hari minggu ?
mahasiswa_hari_minggu = [data["MAHASISWA"] for data in data_set_mahasiswa if data["HARI"] == "Minggu"]
print(f"e) Mahasiswa yang datang pada hari Minggu: {', '.join(mahasiswa_hari_minggu)}")

# f) Berapa biaya tertinggi dan terendah ?
biaya_tertinggi = max(data["BIAYA"] for data in data_set_mahasiswa)
biaya_terendah = min(data["BIAYA"] for data in data_set_mahasiswa)
print(f"f) Biaya tertinggi: Rp.{biaya_tertinggi},00 , Biaya terendah: Rp.{biaya_terendah},00")

# g) Berapa frekuensi datang tertinggi dan terendah ?
frekuensi_datang = {data["MAHASISWA"]: sum(r["DATANG"] for r in data_set_mahasiswa if r["MAHASISWA"] == data["MAHASISWA"]) for data in data_set_mahasiswa}
mahasiswa_tertinggi = max(frekuensi_datang, key=frekuensi_datang.get)
mahasiswa_terendah = min(frekuensi_datang, key=frekuensi_datang.get)
print(f"g) Mahasiswa tertinggi: {mahasiswa_tertinggi}, Frekuensi datang: {frekuensi_datang[mahasiswa_tertinggi]}, Mahasiswa terendah: {mahasiswa_terendah}, Frekuensi datang: {frekuensi_datang[mahasiswa_terendah]}" )
