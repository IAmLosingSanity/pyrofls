with open("devices.txt", "r") as file:
    lines = file.readlines()

# Split the lines
for i in range(len(lines)):
    lines[i] = lines[i].split()

# Sort by price
lines.sort(key=lambda x: int(x[3]))

# Input K, M, and R
K = int(input("How many tablets do you want to buy? "))
M = int(input("Enter the minimum memory requirement: "))
R = int(input("Enter the minimum rating requirement: "))

# Select tablets that meet the requirements
selected_devices = []
total_cost = 0
for device in lines:
    if int(device[1]) >= M and int(device[2]) >= R:
        selected_devices.append(device)
        total_cost += int(device[3])
        K -= 1
        if K == 0:
            break

# Print selected tablets and total cost
for device in selected_devices:
    print(f"{device[0]} {device[1]} {device[2]} {device[3]}")
print(f"Total cost: {total_cost}$")