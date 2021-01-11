Nilai_theory= float(input("masukan nilai ujian teori:"))
Nilai_praktek= float(input("masukan nilai ujian praktek:"))

if Nilai_praktek >= 70 and Nilai_theory >= 70:
    print("Selamat, anda lulus!")
elif Nilai_praktek >= 70 and Nilai_theory < 70:
    print("Anda harus mengulang ujian teori")
elif Nilai_praktek < 70 and Nilai_theory >= 70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")
