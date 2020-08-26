def number_of_bottles():
    for i in range(100, 0, -1):
        if i != 1:
            print("{i} bottles of milk on the wall, {i} bottles of milk.' /n' Take one down and pass it around, {i} bottles of milk on the wall.")
        elif i ==1:
            print("es uno")

        
number_of_bottles()     