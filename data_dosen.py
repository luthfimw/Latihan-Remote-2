import os
os.system('cls')

'''
saya ingin mengumpulkan data nama, alamat, kota asal
'''

list_semua = []
nomor_data = []
print(f'{"="*20} SELAMAT DATANG  {"="*20}')
while True:
    nama = input("Masukkan nama dosen lengkap  \t: ")
    nama = nama.upper()

    alamat = input('Masukkan alamat dosen  \t: ')
    alamat = alamat.upper()

    kota_asal = input('Masukkan kota asal dosen : ')
    kota_asal = kota_asal.upper()

    data_kumpul = [nama,alamat,kota_asal]
    list_semua.append(data_kumpul)
    no_sekarang = [len(list_semua)]
    nomor_data.extend(no_sekarang)
    
    while True:
        pilihan = input('Apakah anda ingin memasukkan data dosen yang lainnya? ktik "iya" jika lanjut, ketik "tidak" jika sudah selesai input data : ').lower()
        print(f'Anda memiliki nomor kartu data diri yang telah anda inputkan : {len(list_semua)}')
        if pilihan == 'tidak':
            print('Nomor kartu yang anda miliki :', end='')
            for i in nomor_data:
                print(i,end=', ')
            print()
            print(f'{"="*20} TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI {"="*20}')
            break
        if pilihan == 'iya':
            
            break
        else:
            print('Mohon masukkan "iya" atau "tidak"')
    if pilihan == 'iya':
        continue
    if pilihan == 'tidak':
        break
    

#mencetak data 
for i in list_semua:
    print(f'{"="*10} Berikut ini adalah tampilan data kalian {"="*10}')
    print(f'Nama \t : {i[0]}')
    print(f'Alamat \t : {i[1]}')
    print(f'Kota Asal: {i[2]}')
    print(f'{"="*30}')
    
#menghapus data tertentu

    