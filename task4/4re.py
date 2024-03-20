import re

def replacei(text):
    pattern = r'(\b\w+\b)\s*=\s*\1\s*\+\s*1'
    replacement = r'\1++'
    return re.sub(pattern, replacement, text)

with open('input.txt', 'r') as file:
    csharp_code = file.read()
    updated_code = replacei(csharp_code)

with open('input.txt', 'w') as file:
    file.write(updated_code)