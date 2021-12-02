namalist = []
kursilist = []
ulang = 0

while (ulang < 1):
    nama = input("Masukkan nama: ")

    if nama == "STOP":
        break

    kursi = int(input("Masukkan nomor kursi {} : " .format(nama)))
        
    if kursi in kursilist:  
        print("Mohon maaf kursi tersebut telah terisi!")

    if kursi not in kursilist:
        namalist.append(nama)
        kursilist.append(kursi)

print("List kursi yang telah terisi : ")

for i in range(0,len(kursilist),1):
    print("Kursi nomor {} telah diisi oleh {}" .format(kursilist[i], namalist[i]))