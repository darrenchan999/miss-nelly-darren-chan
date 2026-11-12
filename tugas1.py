print("=== TUGAS INFORMATIKA: NILAI SISWA ===")

jml = 0
while jml < 20:
  jml = int(input("Mau masukin berapa nilai (minimal 20)? "))
  if jml < 20:
    print("Kurang banyak bro, minimal 20 ya!")

data = []
i = 1
while len(data) < jml:
  nilai = int(input("Masukin nilai ke-" + str(i) + ": "))
  if nilai in data:
    print("Nilainya udah ada, ganti yang lain!")
  else:
    data.append(nilai)
    i = i + 1

data.sort()
data.reverse()

tertinggi = data
terendah = data[len(data) - 1]

total = 0
for x in data:
  total = total + x
rata = total / jml

print("==================================")
print("Urutan nilai dari yang paling tinggi:")
nomor = 1
for x in data:
  print(str(nomor) + ". " + str(x))
  nomor = nomor + 1

print("----------------------------------")
print("Nilai paling tinggi :", tertinggi)
print("Nilai paling rendah :", terendah)
print("Rata-rata nilai     :", round(rata, 2))
