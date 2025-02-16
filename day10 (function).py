#def nama_fungsi

# def menu():
#     print('Pilih bangun datar :')
#     print('1. Persegi')
#     print('2. Persegi Panjang')
#     print('3. Segitiga')
#     print('4. Jajar Genjang')
#     print('5. Lingkaran')
#     print('6. Trapesium')
#     print('7. Belah ketupat')
#     print('8. Layang-layang')

# def sapa_orang(nama, umur):
#     print(f'Hi {nama}!')
#     print(f'serius lu umur {umur}?')


# sapa_orang('Rizal', 21) #klo mau call 
# sapa_orang('Asep', 22)
# sapa_orang('Loki', 23)



# def nanya_nama():
#       nama = input('Nama lu siapa? ')
#       print(f'Halo {nama}')

# nanya_nama()




#praktik
# PI = 3.14
# r = int(input('Masukkan jari-jari ='))

# def volume_bola(r):
#     volume = (4/3) * PI * (r ** 3)
#     # print(f"Volume bola dengan jari-jari {r} = {volume:.2f}")

# volume_bola(5)



# def volume_bola_luas_ling(r):
#     volume = ((4/3)*PI*r**3)
#     luasling = PI*r**2
#     return volume, luasling

# volbola, luasling = volume_bola_luas_ling(5)
# print(volume_bola_luas_ling(5))
# print(volbola)
# print(luasling)


#praktik

def Tampilmenu():
    return '''Pilih bangun datar :
1. Persegi
2. Persegi Panjang
3. Segitiga
4. Jajar Genjang
5. Lingkaran
6. Trapesium
7. Belah Ketupat
8. Layang-layang'''

def luas_persegi(sisi):       # SHORTCUT     def luas_persegi(sisi):
    luas = sisi *sisi                        #return sisi*sisi
    return luas

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def luas_segitiga(alas, tinggi):
   luas = 0.5 * alas * tinggi
   return luas

def luas_jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    return luas

def luas_lingkaran(Pi, r):
    luas = Pi * r **2
    return luas

def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    luas = 0.5 *(sisi_atas + sisi_bawah) * tinggi
    return luas

def luas_belah_ketupat(diagonal1, diagonal2):
    luas = 0.5 * diagonal1 * diagonal2
    return luas

def luas_layang_layang(diagonal1, diagonal2):
    luas = 0.5 * diagonal1 * diagonal2
    return luas

def volume_kubus(sisi):
    volume = sisi **3
    return volume

def volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

print('Kalkulator Bangun Datar dan Bangun Ruang')
print('''Pilih Kategori :
1. Bangun Datar
2. Bangun Ruang''')

kategori = input('Masukkan pilihan: ')

if kategori == '1':
    print(Tampilmenu())
    pilihan = input('Masukkan pilihan: ')

    if pilihan == '1':
        sisi = float(input('Masukkan panjang sisi persegi: '))
        print(f'Luas persegi = {luas_persegi(sisi):.2f}')

    elif pilihan == '2':
        panjang = float(input('Masukkan panjang :'))
        lebar = float(input('Masukkan lebar :'))
        print(f'Luas persegi panjang = {luas_persegi_panjang(panjang, lebar):.2f}')
        
    elif pilihan == '3':
        alas = float(input('Masukkan alas :'))
        tinggi = float(input('Masukkan tinggi :'))
        print(f'Luas segitiga = {luas_segitiga(alas, tinggi):.2f}')

    elif pilihan == '4':
        alas = float(input('Masukkan alas :'))
        tinggi = float(input('Masukkan tinggi :'))
        print(f'Luas jajar genjang = {luas_jajar_genjang(alas, tinggi):.2f}')

    elif pilihan == '5':
        r = float(input('Masukkan jari-jari :'))
        Pi = 3.14
        print(f'Luas lingkaran = {luas_lingkaran(r, Pi):.2f}')

    elif pilihan == '6':
        sisi_atas = float(input('Masukkan  sisi atas :'))
        sisi_bawah = float(input('Masukkan sisi bawah :'))
        print(f'Luas trapesium = {luas_trapesium(sisi_bawah, sisi_atas):.2f}')

    elif pilihan == '7':
        d1= float(input('Masukkan diagonal pertama :'))
        d2 = float(input('Masukkan diagonal kedua :'))
        print(f'Luas belah ketupat = {luas_belah_ketupat(d1, d2):.2f}')

    elif pilihan == '8':
        d1= float(input('Masukkan diagonal pertama :'))
        d2 = float(input('Masukkan diagonal kedua :'))
        print(f'Luas layang-layang = {luas_layang_layang(d1, d2):.2f}')

    else:
        print('Itu yang lu pilih kaga ada di list!')

elif kategori == '2':
    print('Operasi Bangun Ruang:')
    print('1. Volume Kubus')
    print('2. Volume Balok')
    operasi = input('Pilih bangun ruangnya bang: ')

    if operasi == '1':
        sisi = float(input('Masukkan sisi : '))
        print(f'Volume kubus = {volume_kubus(sisi):.2f}')

    elif operasi == '2':
        panjang = float(input('Masukkan panjang : '))
        lebar = float(input('Masukkan lebar : '))
        tinggi = float(input('Masukkan tinggi :'))
        print(f'Volume balok = {volume_balok(panjang, lebar, tinggi):.2f}')

    else:
        print('Yang lu pilih gada di list itu!')
else:
    print('Yang lu pilih kaga ada di list kocak')






 





