from protocol import BreachProtocol
import os

def input_from_file():
    default_load_path = "input/"
    path_valid = False
    while not path_valid:
        filename = input("\nMasukkan nama file yang ingin dimuat: ")
        if os.path.exists(default_load_path + filename):
            path_valid = True
        else:
            print(f"File {filename} tidak ditemukan!\n")
    
    return BreachProtocol.load_file(filename)

def input_from_keyboard():
    number_of_tokens = int(input("\nMasukkan jumlah token unik: "))
    token = input("Masukkan token: ").split()
    buffer_size = int(input("Masukkan ukuran buffer: "))
    matrix_width, matrix_height = map(int, input("Masukkan ukuran matriks (Contoh: '6 6'): ").split())
    number_of_sequence = int(input("Masukkan jumlah sekuens: "))
    max_sequence_size = int(input("Masukkan ukuran maksimal sekuens: "))
    
    return BreachProtocol.random_generate(token, buffer_size, matrix_width, matrix_height, number_of_sequence, max_sequence_size)


print("\nSelamat datang di Cyberpunk 2077 Breach Protocol Solver!")

input_valid = False
while not input_valid:
    input_choice = input("Pilih metode input yang diinginkan (f: file, k: keyboard): ")
    if input_choice == "f" or input_choice == "F":
        game = input_from_file()
        input_valid = True
    elif input_choice == "k" or input_choice == "K":
        game = input_from_keyboard()
        input_valid = True
    else:
        print("Mohon masukkan input yang valid (f/k).\n")

if input_choice == "f" or input_choice == "F":
    print("\nGame berhasil dimuat!")
else:
    print("\nGame berhasil dihasilkan secara random!")
    game.display_generated_game()
    
print("\nMohon tunggu...\n")
game.solve()

confirm_save = input("\nApakah ingin menyimpan solusi? (y/n): ")
if (confirm_save == "y" or confirm_save == "Y"):
    game.export_file()
    print("File berhasil disimpan!")

print("\nTerima kasih telah menggunakan program ini!\n")