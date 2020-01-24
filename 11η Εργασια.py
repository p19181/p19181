numbers_to_be_checked = ['2745', '2934', '1827', '3726', '1032', '4871', '8473',
                         '1029', '1947', '1029', '9403', '4324', '7480', '9461'
                         '9485', '0473', '9384', '2716', '6583', '5462', '9843']
correct_input = False
while not correct_input:
    numbers = input("Πληκτρολογίστε 6 αριθμούς: ")
    if len(numbers) == 6:
        correct_input = True
exists = False
for group in numbers_to_be_checked:
    if group in numbers:
        exists = True
print(exists)