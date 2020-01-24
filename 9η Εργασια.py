num3 = 10
while num3 >= 9:
    try:
        num1 = input("Πληκτρολογίστε έναν αριθμό: ")
        num1 = int(num1)
    except ValueError:
        print("Προσπαθήστε ξανά")
        break
    if num1 < 0:
        num1 = num1*(-1)
    num1 = 3*num1 + 1
    num2 = 0
    for digit in str(num1):
        num2 += int(digit)
    num3 = num2
print(num3)