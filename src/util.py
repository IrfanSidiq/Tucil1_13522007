from protocol import BreachProtocol
import math
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def input_from_file():
    default_load_path = "../test/input/"
    input_file_valid = False
    while not input_file_valid:
        path_valid = False
        while not path_valid:
            filename = input("\nMasukkan nama file yang ingin dimuat: ")
            if os.path.exists(default_load_path + filename):
                path_valid = True
            else:
                print(f"File {filename} tidak ditemukan!\nPastikan file yang anda masukkan sudah ada di folder Tucil1_13522007/test/input")
                print("Note: Nama file beserta ekstensinya, contoh: 'percobaan1.txt'\n")
        if not validate_file(filename):
            print("Isi file txt tidak valid!\n")
        else:
            input_file_valid = True
    
    return BreachProtocol.load_file(filename)

def validate_file(path: str):
    default_load_path = "../test/input/"
    file = open(default_load_path + path, "r")
    f = file.readlines()

    input = []
    for line in f:
        input.append(line.strip())
    
    current_index = 0
    buffer_size = int(input[current_index])
    if buffer_size < 0:
        print("Ukuran buffer tidak boleh negatif!")
        return False
    
    matrix_width, matrix_height = map(int, input[current_index + 1].split())
    if matrix_width < 0 or matrix_height < 0:
        print("Ukuran matriks tidak boleh negatif!")
        return False

    current_index += matrix_height + 2

    number_of_sequences = int(input[current_index])
    if number_of_sequences < 0:
        print("Jumlah sekuens tidak boleh negatif!")
        return False
        
    file.close()
    return True

def input_from_keyboard():
    # Validation for each input
    is_number_of_token_valid = False
    while not is_number_of_token_valid:
        number_of_tokens = int(input("\nMasukkan jumlah token unik: "))
        if number_of_tokens >= 2:
            is_number_of_token_valid = True
        else:
            print("Jumlah tidak valid! Pastikan jumlah token unik >= 2\n")
    
    is_token_valid = False
    while not is_token_valid:    
        token = input("Masukkan token: ").split()
        if len(token) > number_of_tokens:
            print("Jumlah token terlalu banyak!\n")
        elif len(token) < number_of_tokens:
            print("Jumlah token terlalu sedikit!\n")
        else:
            is_token_unique = True
            for i in range(len(token)):
                for j in range(i+1, len(token)):
                    if token[i] == token[j]:
                        print("Terdapat token yang sama! Semua token harus unik\n")
                        is_token_unique = False
                        
            if is_token_unique:
                is_token_valid = True          
    
    is_buffer_size_valid = False
    while not is_buffer_size_valid:
        buffer_size = int(input("Masukkan ukuran buffer: "))
        if buffer_size >= 0:
            is_buffer_size_valid = True
        else:
            print("Ukuran buffer tidak boleh negatif!\n")
    
    is_matrix_size_valid = False
    while not is_matrix_size_valid:
        matrix_width, matrix_height = map(int, input("Masukkan ukuran matriks (Contoh: '6 6'): ").split())
        if matrix_width > 0 and matrix_height > 0:
            is_matrix_size_valid = True
        else:
            print("Ukuran matriks harus positif!\n")
    
    is_number_of_sequence_valid = False
    while not is_number_of_sequence_valid:
        number_of_sequence = int(input("Masukkan jumlah sekuens: "))
        if number_of_sequence >= 0:
            is_number_of_sequence_valid = True
        else:
            print("Jumlah sekuens tidak boleh negatif!\n")
    
    min_sequence_length = find_min_sequence_length(number_of_tokens, number_of_sequence)
    sequence_size_valid = False
    while not sequence_size_valid:
        max_sequence_length = int(input(f"Masukkan panjang maksimal sekuens (minimal ≥ {min_sequence_length}): "))
        if max_sequence_length >= min_sequence_length:
            sequence_size_valid = True
        else:
            print("Panjang tidak valid!\n")
    
    return BreachProtocol.random_generate(token, buffer_size, matrix_width, matrix_height, number_of_sequence, max_sequence_length)

# Finds minimum n satisfying a^2 + a^3 + ... + a^n >= s
def find_min_sequence_length(a: int, s: int):
    return math.ceil(math.log((s+a)*(a-1)/a + 1, a))