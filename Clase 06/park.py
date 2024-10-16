# park.py
# ingresar personas hasta que el usuario ingrese la palabra no
# contar la cantidad de personas
# sumar la recaudación

mensaje = ''
print("Bienvenidos al parque")


while mensaje.lower() != 'no':

    age = input("Ingrese edad: ")

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
        
    mensaje = input("Desea ingresar más datos? si/no")
