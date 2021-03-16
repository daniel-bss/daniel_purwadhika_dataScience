def telepon():
    nomor = input('Masukkan Nomor HP : ')
    x = list()
    x.extend(nomor)

    if len(nomor) > 13:
        print('Nomor HP hanya maksimal 13 Angka')

    elif x[0:2] != ['0','8']:
        print('Nomor HP harus dimulai dengan "08"')

    else:
        print('Nomor HP Saya Adalah',nomor)

telepon()