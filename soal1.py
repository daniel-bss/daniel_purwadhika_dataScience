def fungsi_kalimat():
    kalimat = input('Masukkan Sebuah Kalimat : ')

    if len(kalimat) > 200:
        print('Batas Karakter Maksimal Hanya 200')

    elif len(kalimat ) == 0:
        print('Masukkan Sebuah Inputan')

    elif len(kalimat) > 0 and len(kalimat) <= 200:
        kalimat_split = kalimat.split(' ')
        x = ''
        for i in kalimat_split:
            x += i
        print('*' + x.upper() + '*')


fungsi_kalimat()
print()
