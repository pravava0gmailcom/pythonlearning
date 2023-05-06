A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#print(type(A))
a = int(input("Enter a Number to search in Set: "))
#print(a)
check = False

def checkset(x):
    for num in A:
        if num == x:
            return True
            break

check = checkset(a)

if check == True:
    print(f"Number {a} exists in the Set")
else:
    print(f"Number {a} do not exist in the Set")
