print('Kalkulator Bangun Datar dan Bangun Ruang')
print('''Pilih Kategori:
1. Bangun datar
2. Bangun ruang''')

pilihan = input('Masukkan pilihan: ')


if pilihan == '1':
        print('Pilih bangun datar:')
        print('1. Persegi')
        print('2. Persegi Panjang')
        print('3. Segitiga')
        print('4. Jajar Genjang')
        print('5. Lingkaran')
        print('6. Trapesium')
        print('7. Belah Ketupat')
        print('8. Layang-layang')
        try:
            operasi = input('Pilih bangun datarnya: ')
        except ValueError:
             print('cuman bisa masulkin int doang bang')
        if operasi == '1':
            sisi = float(input('Masukkan panjang sisi persegi: '))
            try:
                hasil = sisi ** 2
            except ArithmeticError:
                 print('kalkulasi salah')
            print(f'Luas persegi = {hasil}')

        elif operasi == '2':
            panjang = float(input('Masukkan panjang: '))
            lebar = float(input('Masukkan lebar: '))
            hasil = panjang * lebar
            print(f'Luas persegi panjang = {hasil}')
            
        elif operasi == '3':
            alas = float(input('Masukkan alas: '))
            tinggi = float(input('Masukkan tinggi: '))
            hasil = 0.5 * alas * tinggi
            print(f'Luas segitiga = {hasil}')

        elif operasi == '4':
            alas = float(input('Masukkan alas: '))
            tinggi = float(input('Masukkan tinggi: '))
            hasil = alas * tinggi
            print(f'Luas jajar genjang = {hasil}')

        elif operasi == '5':
            r = float(input('Masukkan jari-jari: '))
            Pi = 3.14
            hasil = Pi * r ** 2
            print(f'Luas lingkaran = {hasil}')

        elif operasi == '6':
            sisi_atas = float(input('Masukkan sisi atas: '))
            sisi_bawah = float(input('Masukkan sisi bawah: '))
            tinggi = float(input('Masukkan tinggi: '))
            hasil = 0.5 * (sisi_atas + sisi_bawah) * tinggi
            print(f'Luas trapesium = {hasil}')

        elif operasi == '7':
            d1 = float(input('Masukkan diagonal pertama: '))
            d2 = float(input('Masukkan diagonal kedua: '))
            hasil = 0.5 * d1 * d2
            print(f'Luas belah ketupat = {hasil}')

        elif operasi == '8':
            d1 = float(input('Masukkan diagonal pertama: '))
            d2 = float(input('Masukkan diagonal kedua: '))
            hasil = 0.5 * d1 * d2
            print(f'Luas layang-layang = {hasil}')

        else:
            print('Pilihan gada di list!')

elif pilihan == '2':
        print('Operasi Bangun Ruang:')
        print('1. Volume Kubus')
        print('2. Volume Balok')
        operasi = input('Pilih bangun ruangnya: ')

        if operasi == '1':
            sisi = float(input('Masukkan sisi: '))
            hasil = sisi ** 3
            print(f'Volume kubus = {hasil}')
        elif operasi == '2':
            panjang = float(input('Masukkan panjang: '))
            lebar = float(input('Masukkan lebar: '))
            tinggi = float(input('Masukkan tinggi: '))
            hasil = panjang * lebar * tinggi
            print(f'Volume balok = {hasil}')
        else:
            print('Pilihan tidak ada di daftar!')
else:
        print('Pilihan tidak ada di daftar kategori!')

# except ValueError:
    # print('Input yang dimasukkan harus berupa angka. Silakan coba lagi.')
