#looping di dalam looping

# for i in range(1, 11):#outer loop
#     for j in range(1, 11):#inner loop
#         for k in range(1, 11):
#             print(f'nilai i = {i}, j = {j}, k = {k}')
#     print('')
# print('')

#praktik
# for i in range(1, 11):
#     for j in range(1, 11):
#         hasil = i * j
#         print(f' {i} * {j} = {hasil}')
#     print('')


A =     [[1, 2], #i = [1, 2]
        [3, 4]]

B = [[4, 3],
    [2, 1]]

hasil = [[0, 0],
        [0, 0]]

# print(A)

# for baris in range(len(A)): # = 2 -> range(2) -> 0, 1 ->
#     for kolom in range(len(B[0])):
#         hasil[baris][kolom] = A[baris][kolom] - B[baris][kolom]
#         print(hasil[baris][kolom], end = ' ')
#     print('')



# 3 loop
for i in range(len(A[0])): #i == 0
      for j in range(len(B)):
           for k in range(len(B[0])):#0, 1
                hasil[i][j] += A[i][k] * B[k][j]
      print(hasil)



#unpacking

# data = (1, 2, 3, 4, 5)
# a, b, *c = data
# print(a, b, c)


# data = [[1,2] , [3, 4] , [5, 6]]

# for a, b in data:
#      print(a, b)

kamus = {'nama' : 'asep', 'umur' : 14, 'Negara' : 'Indonesia'} 

#menggunakan items() 'cuman bisa di dictionary'
# for key, value in kamus.items():
#     print(f'{key} : {value}')



# .enumerate() 'dipake di list

data_nama_mahasiswa = ['Asep', 'Jamal', 'Raul']

for idx, value in enumerate(data_nama_mahasiswa):
    print(f'indeks [{idx}], Valuenya : {value}')