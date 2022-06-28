import datetime
from tkinter import N
from turtle import clear

import colorama
now = datetime.datetime.now()
print("Date / Time : ",now.strftime("%Y-%m-%d %H:%M:%S"))
print()

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

jumharga = 0

print('*********** HOMEMADE PASTA J&A *************')
print('**** With Pasta, Everthing is Possible *****')
print(Back.RED + Fore.BLUE + 'PROMOTION : Get RM5 instant cash voucher with RM80 purchases') 

print('1.SPAGHETTI')
print('2.ANGEL HAIR')
print('3.PENNE')
print('4.RAVIOLI')
print('5.FARFALLE')
print('********************************************')

beli = str(input('Wanna buy my pasta? (Y/N) : '))
print()

while (beli != "N"): 

    print(Back.BLUE + Fore.RED +'Which pasta are you interested?')
    print(' 1. SPAGHETTI - RM6.90/pack')
    print(' 2. ANGEL HAIR - RM6.90/pack')
    print(' 3. PENNE - RM7.90/pack')
    print(' 4. RAVIOLI - RM5.90/kg')
    print(' 5. FARFALLE - RM6.90/pack')
    pilih = int(input('Please key in the number : '))

    if pilih ==1:
     bilpack = int(input('How many packs? : '))
     jenis = 'SPAGHETTI' 
     ppp = 6.90
     harga = bilpack * ppp
     
    elif pilih ==2:
     bilpack = int(input('How many packs? : '))
     jenis = 'ANGEL HAIR'
     ppp = 6.90
     harga = bilpack * ppp

    elif pilih ==3:
     bilpack = int(input('How many packs? : '))
     jenis = 'PENNE'
     ppp = 7.90
     harga = bilpack * ppp

    elif pilih ==4:
     bilpack = int(input('How many kg? : '))
     jenis = 'RAVIOLI'
     ppp = 5.90
     harga = bilpack * ppp

    else:
     bilpack = int(input('How many packs? : '))
     jenis = 'FARFALLE'
     ppp = 6.90
     harga = bilpack * ppp

  
    print(jenis, '----', bilpack, ' X ', ppp, ' = RM ', format(harga,'.2f'))     
    print()
  
    jumharga = jumharga + harga

    beli = str(input('Still want to buy? (Y/N) : '))

print() 
print(Fore.CYAN + 'TOTAL : RM', format(jumharga,'.2f'))

print('***************************************')


if jumharga > 80:
   print("Wow, you get instant cash voucher RM5.00")
   hargalepasdiskaun = jumharga - 5
   print(Fore.LIGHTCYAN_EX + "Discounted Price = RM ", format(hargalepasdiskaun,'.2f'))
   print()
   
else:
   diskaun = 0
   print()

print(Fore.LIGHTGREEN_EX + 'THANK YOU FOR BUYING OUR HOMEMADE PASTA')
print(Fore.LIGHTGREEN_EX + 'PLEASE COME AGAIN')