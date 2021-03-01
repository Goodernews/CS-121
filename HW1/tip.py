dollar = int(input("Price dollars? "))
cent = int(input("Price cents? "))
tip = int(input("Tip percentage [0-100]? "))
print(str((dollar+(cent*0.01))*(tip*0.01)))
