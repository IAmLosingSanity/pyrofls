import random

def generate_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = random.randint(1, 10)
            row.append(element)
        matrix.append(row)

    file_name = input("Enter the name of the file to save the matrix: ")
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

    print(f"Matrix of size {n}x{n} with random integers has been generated and saved in {file_name}")

n = int(input("Enter the size N for the matrix: "))
generate_matrix(n)