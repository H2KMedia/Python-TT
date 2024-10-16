prompt = "\n Dime algo y lo repito"
prompt += "\n Ingrese la palabra para finalizar  "

message = ""

while message != "salir":
    message = input(prompt)
    print()
    print(10*"*")
    print(message)
    