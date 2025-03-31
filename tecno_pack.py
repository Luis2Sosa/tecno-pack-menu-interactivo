def consola_interactiva(opción):
    if opción == "envio": return envio
    elif opción == "soporte": return soporte
    elif opción == "horario": return horario
    elif opción == "contacto": return contacto
    else:
        return lambda: "Opción no válida\n"
        
        
def envio():
    return "\nTenemos envios en todo el país\n"   
def soporte():
    return "\nAsistencia las 24 horas\n"  
def horario():
    return "\nNuestro horario es de 8 AM a 5 PM 'Dias feriados no laborables'\n" 
def contacto():
    return "Nuestro número de contacto es '849-357-7777'"    

def consola(funcion):
    return funcion()
    
print("BIENVENIDOS A TECNO PACK")    
print("Productos tecnológicos para el hogar\n")  

while True:
    print("\nMenú\n")
    print("Envio")
    print("Soporte")
    print("Horario")
    print("Contacto")
    print("Salir\n")
    
    opción = input("\nQue desea saber?\n").lower()
    if opción == "salir":
        print("\nGracias por utilizar nuestros servicios.\n")
        break
    interactiva = consola_interactiva(opción)
    print(interactiva())