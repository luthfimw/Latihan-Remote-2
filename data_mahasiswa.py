'''
file ini berisikan kode untuk menginputkan data mahasiswa
'''

data = []
#memasukkan data
nama = input("Masukkan nama \t: ").upper()
alamat = input('Masukkan alamat :').upper()
nim = input('Masukan nim \t: ').upper()
while True:
    try:
        telp = int(input('masukan nomor telepon : '))
        if len(str(telp)) != 12 and len(str(telp)) != 13:
            print('Mohon masukkan nomor anda dengan benar')
        else:
            pass
    except ValueError:
        print('Mohon masukkan angka saja')
    break
sementara = [nama,alamat,nim,telp]
data.append(sementara)
print(f'data yang anda masukkan : \n{data}')
