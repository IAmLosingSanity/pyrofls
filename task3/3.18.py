with open("devices01.txt", "r") as file:
    lines = file.readlines()

# Split the lines
def select_tablets(lines, K, M, R):
    # Split the lines
    for i in range(len(lines)):
        lines[i] = lines[i].split()

    # Sort by price
    lines.sort(key=lambda x: int(x[3]))

    # Select tablets that meet the requirements
    selected_devices = []
    for device in lines:
        if int(device[1]) >= M and int(device[2]) >= R:
            selected_devices.append(device)
            if len(selected_devices) == 1:
                break

    # Return selected devices as a string
    return '\n'.join([' '.join(device) for device in selected_devices]) + '\n' + f'Price for {K} tablets is ' + str(int(device[3]) * K)

print(select_tablets(lines, int(input("Enter quantity: ")), int(input("Enter memory at least: ")), int(input("Enter rating: "))))