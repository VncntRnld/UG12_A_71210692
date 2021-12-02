lst = list(input("Masukkan deret angka : ").split(","))

ngt = []

print("Total: ", end="")
for i in lst:
    if int(i) % 2 != 0:
        Mns = int(i) * (-1)
        ngt.append(Mns)
        print(" - ", i, end="")

    if int(i) % 2 == 0:
        pls = int(i)      
        ngt.append(pls)
        print(" + ",pls, end="")

print("\nHasil Perhitungan diatas ialah ", sum(ngt))
