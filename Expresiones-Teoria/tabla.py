import re
expresion = r'([0-9])'
resultado = re.compile(expresion)
prueba =  raw_input("Entrada: ")

busqueda = re.search(resultado,prueba)
x=1
if busqueda:

    rango= range(1,11)
    while x<=10:
        print int(prueba[0])*x
        x+=1
else:
    print "qr"

        
    

       
    
