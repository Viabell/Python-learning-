#for loop untuk jumlah looping yang udah fix
#for [elemen] in [iterable]

# angka = [1, 2, 3, 4, 5, 6]

# for a in angka:
#     print(a)

#range(start, stop, step)

# for i in range(6):
#     print(angka[i])

# for i in range(2, 12):
#   print(i)

# for i in range(0, 9, 2):
#   print(i)

# for i in range(6, 1, -1): #buat mundur
#    print(i)


#function len() #length
# angka = [1, 2, 3, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 2]
# print(len(angka))

# for i in range (len(angka)):
#  print(angka[i])

#praktik
# n = 5
# hasil = 1
# for i in range(n, 0, -1):
#     hasil *= i #hasil = hasil * 1
#     print(f'Nilai i = {i}')
#     print(f'Hasil sekarang = {hasil}')


#while [kondisi benar]:

# n = -1
# while (n < 0):
#     n = int(input('Masukkan bilangan positif: '))

# print(n)


# break & continue
# for i in range(1, 11):
#     if i == 5:
#         break
#     else:
#         print(i)

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i)
