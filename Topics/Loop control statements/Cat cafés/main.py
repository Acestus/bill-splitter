max_number = 0

while True:
    my_input = input()
    cafe = my_input.split()
    if cafe[0] == "MEOW":
        break
    my_name = cafe[0]
    my_number = int(cafe[1])
    if my_number > max_number:
        max_number = my_number
        max_name = my_name

print(max_name)
