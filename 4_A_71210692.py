jmlh = int(input("Input : "))
print("Output : ")

baris = 0
bintang = 0

for i in range(jmlh):
#spasi kiri
    for j in range(jmlh-1):
        print(" ", end="")

#bintang inti
    print("*", end="")

#spasi tengah
    if jmlh != 1:
        if bintang == 1:
            for a in range(baris):
                print(" ", end="")
                bintang += 1
        else:
            for a in range(baris-1):
                print("  ", end="")
            print(" ", end="")
    else:
        for a in range(baris-1):
            print(" *", end="")
        


#bintang kanan
    if jmlh != 1:
        if bintang >= 1:  
            print("*", end="")
        else:
            bintang += 1
    else:
        print (" *")


#spasi kanan
        for j in range(jmlh-1):
            print(" ", end="")

#tambahan
    baris += 1
    jmlh -= 1
    print("")

tutup = 0

#while tutup = jmlh:
    #print("* ", end="")
    #tutup += 1
