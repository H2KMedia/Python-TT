#admission < 4 age is free
#admission between 4 and 18 if $500
#admission > 18 is $1000
#admission > 60 is $750

'''
#forma 1
age = int(input("Ingrese cu edad: "))
if age < 4:
    print("Tue entrada cuesta $0.")
elif age >= 4 and age < 18:
    print("Tue entrada cuesta $500.")
elif age >= 18 and age < 60:
    print("Tu entrada cuesta $750.)")
else:
    print("Tue entrada cuesta $1000.")

    
print("")
print(50*"*")
'''

#forma 2
age = input("Ingrese edad: ")

if age.isdigit() and age > "0":
    age = int(age)
    if age < 4:
        price = 0
    elif age >= 4 and age < 18:
        price = 500
    elif age >= 18 and age < 60:
        price = 1000
    elif age >= 60:
        price = 750
    # else:
    #     price = 750
    
    print(f"Tu entrada cuesta ${price}")
else:
    print("Error!")
    
    
'''
if [condición]:
    [instrucciones por verdadero]
else
    [condiciones por falso]
'''
