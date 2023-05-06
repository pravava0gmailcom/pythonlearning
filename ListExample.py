A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(type(A))
a = int(input("Enter a Number to search in List: "))
#print(a)
check = False

def checklist(x):
    for num in A:
        if num == x:
            return True
            break

check = checklist(a)

if check == True:
    print(f"Number {a} exists in the List")
else:
    print(f"Number {a} do not exist in the List")
