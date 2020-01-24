def totalcost(list, tax, items):
    cost = 0
    count = 1
    for item in list:
        cost += items.get(item)
        count += 1
    cost = cost + cost*(int(tax)*0.01)
    return cost


items = {
    "Μπανάνες": 2,
    "Φράουλες": 1,
    "Μήλα": 2.5,
    "Πορτοκάλια": 2,
    "Καρπούζια": 5,
    "Κεράσια": 1.5,
    "Πεπόνια": 3,
    "Αχλάδια": 2,
    "Μανταρίνια": 1.5
}
try:
    cart = input("Αγορές: ")
    tax = input("Ποσοστό Φόρου: ")
    list = cart.split(" ")
    print(totalcost(list,tax,items))
except TypeError:
    print("Πληκτρολογίστε ξανά")