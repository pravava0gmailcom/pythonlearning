A = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#print(type(A))
a = int(input("Enter a Number to search in Tuple: "))
#print(a)
check = False

def checktuple(x):
    for num in A:
        if num == x:
            return True
            break

check = checktuple(a)

if check == True:
    print(f"Number {a} exists in the Tuple")
else:
    print(f"Number {a} do not exist in the Tuple")
