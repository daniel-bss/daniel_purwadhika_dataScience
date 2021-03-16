def hitung_karakter():    
    kalimat = input('Masukkan Kalimat : ').split(' ')
    a = None
    for i in kalimat:
        if a is None or a < len(i):
            a = len(i)

    print('Jumlah Karakter Terbanyak Adalah Sebesar %d Karakter' %a)

    for i in kalimat:
        if len(i) == a:
            print('Karakter Yang Berjumlah %d Adalah: %s' %(a,i))

        
hitung_karakter()
