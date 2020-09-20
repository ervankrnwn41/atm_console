from customer import Customer

import random
from datetime import datetime
from os import system
from getpass import getpass

system("")

menu_utama = [
	"cek saldo", 
	"debet / withdraw", 
	"simpan / deposit", 
	"ganti pin", 
	"keluar"
]

atm = Customer(id)
date_now = datetime.now()

def msg_value_error():
	print("[INFO]")
	print(f"===> hanya dapat menerima inputtan angka!")
	print("=================================================")

while True:
	print("=" * 30)
	print("Selamat Datang di ATM Progate")
	print(f"Waktu : {date_now}")
	print("=" * 30)
	print()
	
	try: 
		id = int(getpass("Masukkan PIN Anda: "))
		trial = 3
		
		while id != atm.check_pin():

			print(f"Anda salah memasukkan PIN!")
			print("=" * 30)
			print(f"Kesempatan tersisa: [{trial}x]")
			print("=" * 30)

			if trial == 0:
				print("=============================")
				print(f"[LIMIT] Percobaan tersisa {trial}x")
				print("[INFO] Silahkan hubungi customer service di 0101010")
				print("=============================")
				exit()
				
			id = int(getpass("Masukkan PIN Anda: "))
			trial -= 1
					
		system("clear")
		while True:
			print("=============================")
			print("Selamat Datang di ATM Progate")
			print(f"Waktu : {date_now}")
			print("=============================")
			print("Menu Utama: ")
			
			for count, menu in enumerate(menu_utama, 1):
				print(f"{count}. {menu.title()}")
			
			try: 	
				select_menu = int(input("Silahkan pilih menu ~> "))
				
				if select_menu >= 1 and select_menu <= 5:
					
					if select_menu == 1:
						system("clear")
						print(f"MENU ~> '{menu_utama[select_menu-1]}'")
						print(f"Saldo anda saat ini: IDR. {atm.check_balance()}")
					
					elif select_menu == 2:
						system("clear")
						print(f"{'-' * 30}|")
						print(f"|     MENU       | '{menu_utama[select_menu-1]}'")
						print(f"{'-' * 30}|")
						print(f"| Saldo saat ini | {atm.check_balance()}")
						print(f"{'-' * 30}|")
						debet_saldo = int(input("Debet Saldo: "))
						'''
						if atm.check_balance <= 50000:
							print("[MESSAGE] - Maaf, minimal saldo yang tersisa setelah penarikan minimal IDR. {}")
						else:
							pass
						'''
						
						print(f"[MESSAGE]: Anda akan melakukan debet dengan nominal {debet_saldo}")
						verify_withdraw = input("KONFIRMASI [y/n]: ")
						
						if verify_withdraw == "y" or verify_withdraw == "Y":
							print(f"Saldo awal : IDR. {atm.check_balance()}")
							
							if debet_saldo < atm.check_balance():
								atm.withdraw_balance(debet_saldo)
								print(f"[SUCCESS] Transaksi debet berhasil!")
								print(f"Saldo tersisa: {atm.check_balance()}")
								
							else:
								print("[GAGAL] Maaf, saldo Anda tidak mencukupi untuk melakukan tarikan!")
								print("Silahkan melakukan penambahan saldo")
								
						elif verify_withdraw == "n" or verify_withdraw == "N":
							break
							
						else:
							print("pilihan tidak tersedia")
				
					elif select_menu == 3:
						system("clear")
						print(f"MENU ~> '{menu_utama[select_menu-1]}'")
						print(f"Saldo anda saat ini berjumlah {atm.check_balance()}")

						verify_deposit = input("[KONFIRMASI]: Anda akan melakukan deposit [y/n]?")
						
						
						if verify_deposit == "y":
							print(f"Saldo awal anda {atm.check_balance()}")				
							balance = float(input("Jumlah deposit: "))
							atm.deposit_balance(balance)
							print(f"Deposit sebesar {balance} telah berhasil ditambahkan")
							print(f"Saldo anda saat ini berjumlah {atm.check_balance()}")
								
						elif verify_withdraw == "n":
							break
						
					elif select_menu == 4:
						system("clear")
						print(f"MENU ~> '{menu_utama[select_menu-1]}'")
						verify_pin = int(input("Masukkan PIN lama Anda: "))
						
						while verify_pin != atm.check_pin():
							print(f"PIN anda salah!")
							verify_pin = int(input("Masukkan PIN lama Anda: "))
						
						updated_pin = int(input("[+] PIN Baru: "))
						verify_new_pin = int(input("[+] Konfirmasi PIN Baru Anda: "))
						
						if verify_new_pin == updated_pin:
							print("[SUCCESS] - PIN telah berhasil diganti!")
							atm.custPin = verify_new_pin
							
						else:
							print("[FAILED] - Maaf, pin Anda tidak sesuai!")
						
					elif select_menu == 5:
						system("clear")
						print(f"MENU ~> '{menu_utama[select_menu-1]}'")
						
						resi = random.randint(100000, 1000000)
						last_balance = atm.check_balance()
						
						print("======== INVOICE ========")
						print(f"[=] Saldo Akhir: {last_balance}")
						print(f"[=] Nomor Record: {resi}")
						print(f"[=] Waktu: {date_now}")
						print("=========  END  =========")
						exit()
						
				else:
					print("Maaf, menu belum tersedia!")
					print(f"Pilihan menu hanya tersedia dari 1 hingga {len(menu_utama)}")
				
			except ValueError:
				system("clear")
				msg_value_error()
				
	except ValueError:
		system("clear")
		msg_value_error()

