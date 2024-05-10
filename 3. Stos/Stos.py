stack_of_numbers = []

data_sets = input("Podaj liczbę zestawów danych: ")
data_sets = int(data_sets)

for data_set in range(0, data_sets):
    sign = input("Podaj znak: ")
    if sign == "+" and len(stack_of_numbers) <= 10:
        number = input("Podaj liczbę: ")
        stack_of_numbers.append(number)
        print(":)")
    elif sign == "-":
        if stack_of_numbers:
            print(stack_of_numbers[-1])
            del stack_of_numbers[-1]
        else:
            print(":(")
    else:
        print(":(")
