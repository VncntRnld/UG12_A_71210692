lst = list(input("Masukkan deret angka : ").split(","))

ngt = []
jgn = []
pertama = 0

print("Total: ", end="")
for i in lst:
    while (pertama < 1):
        jgn.append(int(i))

        if int(i) % 2 != 0:
            Mns = int(i) * (-1)
            ngt.append(Mns)
            print(" - ", i, end="")
            

        if int(i) % 2 == 0:
            pls = int(i)      
            ngt.append(pls)           
            print(" + ",pls, end="")
            
        pertama = pertama + 1

#==================================================>

    if int(i) in jgn:
        continue

    if int(i) % 2 != 0:
        Mns = int(i) * (-1)
        ngt.append(Mns)
        print(" - ", i, end="")
            

    if int(i) % 2 == 0:
        pls = int(i)      
        ngt.append(pls)           
        print(" + ",pls, end="")

print("\nHasil Perhitungan diatas ialah ", sum(ngt))
