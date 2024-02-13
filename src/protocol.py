from typing import List, Tuple
import random
import time
import datetime
import sys

class BreachProtocol:
    possible_solution_buffers = []
    possible_solution_coordinates = []
    
    def __init__(self, matrix: List[List[str]], sequences: List[str], sequence_rewards: List[int], buffer_size: int, path: str):
        self.matrix = matrix
        self.sequences = sequences
        self.sequence_rewards = sequence_rewards
        self.buffer_size = buffer_size
        self.visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    def load_file(path: str):
        default_load_path = "../test/input/"
        file = open(default_load_path + path, "r")
        f = file.readlines()

        input = []
        for line in f:
            input.append(line.strip())
        
        current_index = 0
        buffer_size = int(input[current_index])
        matrix_width, matrix_height = map(int, input[current_index + 1].split())
        matrix = [["" for _ in range(matrix_width)] for _ in range(matrix_height)]

        current_index += 2
        for i in range(matrix_height):
            row = input[i + current_index].split()
            for j in range(matrix_width):
                matrix[i][j] = row[j]

        current_index += matrix_height
        number_of_sequences = int(input[current_index])
        sequences = ["" for _ in range(number_of_sequences)]
        sequence_rewards = [0 for _ in range(number_of_sequences)]

        idx = current_index + 1
        for i in range(number_of_sequences):
            sequences[i] = input[idx]
            sequence_rewards[i] = int(input[idx + 1])
            idx += 2
            
        file.close()
        return BreachProtocol(matrix, sequences, sequence_rewards, buffer_size, path)
    
    def random_generate(tokens: List[str], buffer_size: int, matrix_width: int, matrix_height: int, number_of_sequences: int, max_sequence_size: int):
        matrix = [["" for _ in range(matrix_width)] for _ in range(matrix_height)]
        sequences = ["" for _ in range(number_of_sequences)]
        sequence_rewards = [0 for _ in range(number_of_sequences)]
        
        for i in range(matrix_height):
            for j in range(matrix_width):
                idx = random.randint(0, len(tokens) - 1)
                matrix[i][j] = tokens[idx]
        
        for i in range(number_of_sequences):
            sequence = ""
            sequence_length = random.randint(2, max_sequence_size)
            contains_duplicate_sequence = True
            
            while contains_duplicate_sequence:
                sequence = ""            
                for _ in range(sequence_length):
                    idx = random.randint(0, len(tokens) - 1)
                    sequence += tokens[idx] + " "
                
                contains_duplicate_sequence = False
                for j in range(i):
                    if sequence == sequences[j]:
                        contains_duplicate_sequence = True
                        break
            
            sequences[i] = sequence
            sequence_rewards[i] = random.randint(1, 5) * 2 * sequence_length
            
        return BreachProtocol(matrix, sequences, sequence_rewards, buffer_size, "")

    def display_generated_game(self):
        print("\nMatriks yang dihasilkan:")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j] + " ", end="")
            print()
        
        print("\nSekuens yang dihasilkan:")
        for i in range(len(self.sequences)):
            print(f"{i+1}.", self.sequences[i] + "dengan reward berbobot", self.sequence_rewards[i])

    def solve(self):
        start_time = time.time()
        
        self.generate_possible_solutions(0, 0, [], [], True)
        self.choose_best_solution()
        
        end_time = time.time()
        self.execution_time = end_time - start_time

    def generate_possible_solutions(self, row: int, col: int, current_buffer: List[str], current_coordinates: List[Tuple[int, int]], horizontal: bool):
        if len(current_buffer) == self.buffer_size:
            self.possible_solution_buffers.append(current_buffer)
            self.possible_solution_coordinates.append(current_coordinates)
            return
        
        continue_search = False
        if horizontal:
            for i in range(len(self.matrix[0])):
                if not self.visited[row][i]:
                    continue_search = True
                    self.visited[row][i] = True
                    self.generate_possible_solutions(
                        row, i,
                        current_buffer + [self.matrix[row][i]],
                        current_coordinates + [(i + 1, row + 1)],
                        False)
                    self.visited[row][i] = False
        else:
            for i in range(len(self.matrix)):
                if not self.visited[i][col]:
                    continue_search = True
                    self.visited[i][col] = True
                    self.generate_possible_solutions(
                        i, col,
                        current_buffer + [self.matrix[i][col]],
                        current_coordinates + [(col + 1, i + 1)],
                        True)
                    self.visited[i][col] = False
                    
        
        if not continue_search:
            self.possible_solution_buffers.append(current_buffer)
            self.possible_solution_coordinates.append(current_coordinates)
                            
    def choose_best_solution(self):
        best_solution_index = -999
        max_reward = 0
        
        for i in range(len(self.possible_solution_buffers)):
            total_reward = 0
            for j in range(len(self.sequences)):
                if self.contains_sequence(self.possible_solution_buffers[i], self.sequences[j].split()):               
                    total_reward += self.sequence_rewards[j]
                    
            if total_reward > max_reward:
                max_reward = total_reward
                best_solution_index = i
        
        self.best_solution_index = best_solution_index
        self.max_reward = max_reward
    
    def contains_sequence(self, buffer: List[str], sequence: List[str]):
        if len(sequence) > len(buffer):
            return False
        
        i = 0
        found = False
        
        while not found and i < len(buffer) - len(sequence) + 1:
            if buffer[i] == sequence[0]:
                j, idx = 1, i + 1
                match = True
                
                while match and j < len(sequence):
                    if buffer[idx] != sequence[j]:
                        match = False
                    j, idx = j + 1, idx + 1
                
                if match:
                    found = True
            i += 1
        
        return found
    
    def display_solution(self):
        print(f"Reward maksimal: {self.max_reward}")
        
        if self.best_solution_index != -999:     # Solution found
            print(f"Isi buffer:", end="")
            for cell in self.possible_solution_buffers[self.best_solution_index]:
                print(f" {cell}", end="")
            print(f"\nKoordinat tiap token:")
            for coordinate in self.possible_solution_coordinates[self.best_solution_index]:
                print(f"{coordinate[0]}, {coordinate[1]}")
        else:
            print("Tidak ada solusi")
        
        print(f"\nWaktu eksekusi: {round(self.execution_time * 1000)} ms")
        
    def export_file(self):
        default_save_path = "../test/output/"
        file_name = str(datetime.datetime.now().replace(microsecond=0)).replace(":", "-") + ".txt"
        
        with open(default_save_path + file_name, "w") as file:
            file.write(f"{self.max_reward}\n")
            
            if self.best_solution_index != -999:
                for cell in self.possible_solution_buffers[self.best_solution_index]:
                    file.write(f"{cell} ")
                file.write("\n")
                for coordinate in self.possible_solution_coordinates[self.best_solution_index]:
                    file.write(f"{coordinate[0]}, {coordinate[1]}\n")
            else:
                file.write("Tidak ada solusi\n")
                
            file.write(f"\n{round(self.execution_time * 1000)} ms")