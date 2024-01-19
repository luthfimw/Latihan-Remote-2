import os
os.system('cls')

'''
saya ingin mengumpulkan data nama, alamat, kota asal
'''

list_semua = []

print(f'{"="*20} SELAMAT DATANG  {"="*20}')
while True:
    nama = input("Masukkan nama lengkap  \t: ")
    nama = nama.upper()

    alamat = input('Masukkan alamat anda  \t: ')
    alamat = alamat.upper()

    kota_asal = input('Masukkan kota asal anda : ')
    kota_asal = kota_asal.upper()

    data_kumpul = [nama,alamat,kota_asal]
    list_semua.append(data_kumpul)

    pilihan = input('Apakah anda ingin memasukkan data yang lainnya? ktik "iya" jika lanjut, ketik "tidak" jika sudah selesai input data : ')
    if pilihan == 'tidak':
        print(f'{"="*20} TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI {"="*20}')
        break
    
#mencetak data 
for i in list_semua:
    print(f'{"="*10} Berikut ini adalah tampilan data kalian {"="*10}')
    print(f'Nama \t : {i[0]}')
    print(f'Alamat \t : {i[1]}')
    print(f'Kota Asal: {i[2]}')
    print(f'{"="*30}')
    
