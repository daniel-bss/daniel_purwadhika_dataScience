def gambar_segitiga():
    a = int(input('Masukkan Jumlah Baris : '))

    print(' '*(a-1) + '***' + ' '*(a-1))
    for i in range(a-2,0,-1):
        spasi = ' ' * i
        bintang = '**'
        print(spasi + bintang + (' '*(a*2 + 1 - 2*len(spasi) - 2*len(bintang))) + bintang + spasi)

    print('*' * (2*a + 1))

gambar_segitiga()
