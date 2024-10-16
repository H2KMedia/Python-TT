# park.py
# ingresar personas hasta que el usuario ingrese la palabra no
# contar la cantidad de personas
# sumar la recaudación


print("Bienvenidos al parque")

flag = True #variable bandera - booleana

while flag: #flag == True

    age = input("Ingrese edad: (-1 para salir) ")
    if age != '-1':
    
        if age.isdigit():
            age = int(age)
            if age > 0: 
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
                print("Valor no permitido!")
        else:
            print("Valor no permitido!")
    else:
        flag = False

#informar cantidad de personas y recaudación