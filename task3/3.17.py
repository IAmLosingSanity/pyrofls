with open("devices.txt", "r") as file:
    lines = file.readlines()
    
for i in range(len(lines)):
    lines[i] = lines[i].split()

suitable = []

money = int(input("How much do you have? (We have devices starting from 150$ to 500$) "))

for i in range(len(lines)):
    #pick a device for user price with max memory
    if lines[i][1] == str(max(int(lines[i][1]) for i in range(len(lines)))) and int(lines[i][3]) <= money:
        suitable.append(lines[i])

indices_to_remove = []
for j in range(len(suitable)):
    if suitable[j][2] != str(max(int(suitable[j][2]) for j in range(len(suitable)))):
        indices_to_remove.append(j)

for idx in reversed(indices_to_remove):
    suitable.pop(idx)

for i in range(len(suitable)):
    print(f"{suitable[i][0]} {suitable[i][1]} {suitable[i][2]} {suitable[i][3]}")


# with open("devices.txt", "r") as file:
#     suitable = []
#     money = int(input("How much do you have? (We have devices starting from 150$ to 500$) "))
#     for line in file:
#         device = line.split()
#         if not suitable or int(device[1]) > int(suitable[0][1]):
#             suitable = [device]  # replace the list with a single suitable device
#         elif int(device[1]) == int(suitable[0][1]) and int(device[3]) <= money:
#             suitable.append(device)
    
#     max_rating = max(int(device[2]) for device in suitable)
#     suitable = [device for device in suitable if int(device[2]) == max_rating]
    
#     for device in suitable:
#         print(f"{device[0]} {device[1]} {device[2]} {device[3]}")