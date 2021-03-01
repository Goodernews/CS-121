
entrees, prices, name = [], [], input("Restaurant name? ")
for num in ["First", "Second", "Third"]:
    entrees.append(input(num +" entree? "))
    prices.append(input(num +" entree price? "))
print("\n" + str(name) + " Entrees\n" + (len(name)+8)*"-")
for dish in list(map(lambda x, y: x + str((max(map(len, entrees))-len(x)+2)*"."+"$" + (3-len(y))*" " + str(y)), entrees, prices)):
    print(dish)