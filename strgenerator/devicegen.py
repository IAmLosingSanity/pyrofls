import random

# List of device names
device_names = ["Apple", "Samsung", "Asus", "Xiaomi", "Huawei"]

# Function to generate memory in TB
def generate_memory():
    return 2 ** random.randint(1, 9)

# Function to generate a random rating from 1 to 5
def generate_rating():
    return random.randint(1, 5)

# List of device prices
device_prices = [150, 200, 250, 300, 350, 400, 450, 500]

# Input for the number of lines in the final file
num_lines = int(input("Enter the number of devices: "))

# Generate devices list
devices = []
for _ in range(num_lines):
    name = random.choice(device_names)
    memory = generate_memory()
    rating = generate_rating()
    price = random.choice(device_prices)
    devices.append(f"{name} {memory} {rating} {price}")

# Save the devices list to a .txt file
with open("devices.txt", "w") as file:
    for device in devices:
        file.write(device + "\n")

print("Devices list has been saved to devices.txt")