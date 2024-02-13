import util

util.clear_screen()

print("""
888888b.                                     888           8888888b.                  888                             888 
888  "88b                                    888           888   Y88b                 888                             888 
888  .88P                                    888           888    888                 888                             888 
8888888K.  888d888 .d88b.   8888b.   .d8888b 88888b.       888   d88P 888d888 .d88b.  888888 .d88b.   .d8888b .d88b.  888 
888  "Y88b 888P"  d8P  Y8b     "88b d88P"    888 "88b      8888888P"  888P"  d88""88b 888   d88""88b d88P"   d88""88b 888 
888    888 888    88888888 .d888888 888      888  888      888        888    888  888 888   888  888 888     888  888 888 
888   d88P 888    Y8b.     888  888 Y88b.    888  888      888        888    Y88..88P Y88b. Y88..88P Y88b.   Y88..88P 888 
8888888P"  888     "Y8888  "Y888888  "Y8888P 888  888      888        888     "Y88P"   "Y888 "Y88P"   "Y8888P "Y88P"  888 
                                                                                                                          
=========================================================================================================================
""")

# Input data
input_valid = False
while not input_valid:
    input_choice = input("Pilih metode input yang diinginkan (f: file, k: keyboard): ")
    if input_choice == "f" or input_choice == "F":
        game = util.input_from_file()
        input_valid = True
    elif input_choice == "k" or input_choice == "K":
        game = util.input_from_keyboard()
        input_valid = True
    else:
        print("Mohon masukkan input yang valid (f/k).\n")

if input_choice == "f" or input_choice == "F":
    print("\nGame berhasil dimuat!")
else:
    print("\nGame berhasil dihasilkan secara random!")
    game.display_generated_game()

# Solve from given data
print("\nMohon tunggu...\n")
game.solve()
game.display_solution()

# Save result if prompted
confirm_save = input("\nApakah ingin menyimpan solusi? (y/n): ")
if (confirm_save == "y" or confirm_save == "Y"):
    game.export_file()
    print("File berhasil disimpan!")

print("\nTerima kasih telah menggunakan program ini!\n")
