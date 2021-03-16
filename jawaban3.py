def sort_odd_even(x):
    ganjil = list()
    genap = list()

    for i in x:
        if i%2 != 0:
            ganjil.append(i)
        elif i%2 == 0:
            genap.append(i)

    for i in range(len(ganjil)-1,0,-1):
        for j in range(i):
            if ganjil[j] > ganjil[j+1]:
                z = ganjil[j+1]
                ganjil[j+1] = ganjil[j]
                ganjil[j] = z

    for i in range(len(genap)-1,0,-1):
        for j in range(i):
            if genap[j] < genap[j+1]:
                z = genap[j+1]
                genap[j+1] = genap[j]
                genap[j] = z
    print(ganjil + genap)


sort_odd_even([1,3,2,2,1,5,1,24,12,124,12,21,32,15])
