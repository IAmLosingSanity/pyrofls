import random
import string

def generate_string(n, flags):
    result = ''
    if 'n' in flags:
        result += ''.join(random.choice(string.digits) for _ in range(n))
    if 'l' in flags:
        result += ''.join(random.choice(string.ascii_letters) for _ in range(n))
    if 'nl' in flags:
        result += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    return result

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    flags = input("Enter flags (e.g. n, l, nl): ")
    n = int(input("Enter the number of characters: "))
    generated_string = generate_string(n, flags)
    filename = input("Enter the filename to save the generated string: ")
    save_to_file(filename, generated_string)
    print(f"Generated string saved to {filename}")

if __name__ == "__main__":
    main()