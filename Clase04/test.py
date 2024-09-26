# Precedence of or & and
meal = "fruit"

money = 0

#prioridad en operaciones logicas
#no
#and
#or

if meal == "fruit" or meal == "sandwich" and money >= 2:  
        print("Lunch being delivered")
else:
    print("Can't deliver lunch")
        #V or F and F
        #V and F
        #V
#debería ser
#if (meal == "fruit" or meal == "sandwich") and money >= 2:  
