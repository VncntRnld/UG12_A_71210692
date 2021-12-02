kata = str(input("Input : "))
jmlhkata = len(kata)

print("Output :")

for i in range(0, jmlhkata):

    for j in range(0, i):
        print(kata[j], end="")
    print("")

for i in range(jmlhkata, 0, -1):

    for j in range(0, i):
        print(kata[j], end="")
    print("")