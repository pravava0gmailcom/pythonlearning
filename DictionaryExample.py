A = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five'}
#print(type(A))

Key_Value = input("Do you want search 'Key' or 'Value' in the Dict?\n"
                  "Enter either Key or Value : ")

check = False

def checkKey(x):
    for value in A.keys():
        if value == x:
            return True
            break

def checkValue(x):
    for value in A.values():
        if value == x:
            return True
            break

if Key_Value == 'Key' or Key_Value == 'key' or Key_Value == 'KEY':
    key = int(input("Enter a Key to search in the Dict: "))
    check = checkKey(key)
    if check == True:
        print(f"Key {key} exists in the Dict")
    else:
        print(f"Key {key} do not exist in the Dict")

elif Key_Value == 'Value' or Key_Value == 'value' or Key_Value == 'VALUE':
    value = input("Enter a Value to search in the Dict: ")
    check = checkValue(value)
    if check == True:
        print(f"Value {value} exists in the Dict")
    else:
        print(f"Value {value} do not exist in the Dict")

else:
    print(f"{Key_Value} is an invalid response. Good Bye.")
