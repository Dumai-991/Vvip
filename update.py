import os,sys


PERINTAH = """
cd $HOME
cd Vvip
mv .datame1 $HOME
mv Hasil $HOME
cd
rm -rf Vvip
git clone https://github.com/Dumai-991/Vvip
cd
mv Hasil Vvip
mv .datame1 Vvip
cd Vvip
"""

print(" |-->Tunggu Sebentar Sedang Update Script....")
os.system(PERINTAH)
print(' |')
print(' |')
print(' |-->Update Script Sudah Selesai...')
print(' |-->Silahkan Jalankan Perintah Ini : python update.py')
os.sys.exit()

