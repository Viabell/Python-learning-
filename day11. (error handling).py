#try (untuk nyoba suatu program)
# except ExceptionType:
#else :
#pass untuk nandaiin sesuatu yang belum kelar


try:
        num =int(input('Masukkan nilai :'))
        hasil = 10/num
except ZeroDivisionError:
        print('benerin konversinya')
except ValueError:
     print('Jangan masukin string')                  
else: 
     print(f"Hasilnya adalah {hasil}")
finally:
        print('Tabrak aja lah')


# try:
#     num =int(input('Masukkan nilai :'))
#     hasil = 10/num
# except Exception as e:
#     print(f'Terjadi error : {e}')

# data = [10, 5, 0, 'a', None]

# for item in data:
#     try:
#         result = 10/item
#     except Exception as e:
#         print(f'Error : {e}')