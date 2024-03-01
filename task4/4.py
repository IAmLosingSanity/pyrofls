def replace_increment(text):
    lines = text.split(';')
    for i, line in enumerate(lines):
        parts = line.split()
        if len(parts) == 5 and parts[1] == '=' and parts[2] == parts[0] and parts[3] == '+' and parts[4] == '1':
            lines[i] = '\n' + parts[0] + '++'
    return '; '.join(lines).strip()

with open('input.txt', 'r') as file:
    csharp_code = file.read()
    updated_code = replace_increment(csharp_code)

with open('input.txt', 'w') as file:
    file.write(updated_code)