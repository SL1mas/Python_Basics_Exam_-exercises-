# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.
array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
    11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# 1 [1, 2, 3, 4, 5]
# 2 [6, 7, 8, 9, 10]        1*2=rezultatas 1
# 3 [11, 12, 13, 14, 15]    rezultatas 1*3=rezultatas 2
# 4 [16, 17, 18, 19, 20]    rezultatas 2*4=rezultatas 3
# 5 [21, 22, 23, 24, 25]    rezultatas 3*5=rezultatas 4


def array_multiplication(array):
    times = 0
    for rows in range(0, len(array)-1):
        print(f"**********{times+1}**********")
        if rows == 0:
            first_row_to_multiply = array[0]
        else:
            first_row_to_multiply = temporary_array
        second_row_to_multiply = array[times+1]
        print("Row 1", first_row_to_multiply)
        print("Row 2", second_row_to_multiply)
        times += 1
        temporary_array = []
        for columns in range(0, len(array[times])):
            multiplication = first_row_to_multiply[columns] * \
                second_row_to_multiply[columns]
            print("Daugyba", multiplication)
            temporary_array.append(multiplication)
    return temporary_array


temporary_array = array_multiplication(array)
print(temporary_array)
