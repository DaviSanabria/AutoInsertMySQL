# This is a sample Python script.
import os
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def creaClientes(numCli):
    #Lista generos
    genList = ["No binario", "Femenino", "Masculino"]
    #Lista de municipios
    muniList = ["Bogota","Medellin","Cali","Barranquilla","Cartagena"]
    #Creación del archivo
    file = open ('cliente.txt','w')
    file.write("/*cliente*/" + os.linesep)
    #Loop
    i = 1;
    while (i<=numCli):
        #Aleatorio municipio
        munRand = random.randint(0,4)
        #Aleatorio genero
        gen = random.randint(0,2)
        #Aleatorio edad
        edad = random.randint(18,80)
        file.write("INSERT INTO cliente VALUES("+str(i)+", '"+str(muniList[munRand])+"', '"+str(genList[gen])+"', "+str(edad)+");"+ os.linesep)
        i=i+1;
    file.close()

#Automatización ventas
def creaVentas(numCli, numVen):
    #Lista temporadas
    tempList = ["Black Friday", "San Valentin", "Navidad", "Halloween", "Sin IVA", "Año nuevo", "Escolar"]
    #Creación del archivo
    file = open ('venta.txt','w')
    file.write("/*venta*/" + os.linesep)
    #Loop
    i = 1;
    while (i<=numVen):
        #Aleatorio temporada
        tempRand = random.randint(0,6)
        #Aleatorio cliente
        cliRand = random.randint(1,numCli)
        file.write("INSERT INTO venta VALUES("+str(i)+", '"+str(tempList[tempRand])+"', "+str(cliRand)+");"+ os.linesep)
        i=i+1;
    file.close()

#Automatización productos_ventas
def creaProdyVenta(numVen, numProd):
    # Creación del archivo
    file = open('producto_venta.txt', 'w')
    file.write("/*producto_venta*/" + os.linesep)
    #loop venta
    i=1
    while (i <= numVen):
        #loop productos
        x = 1
        while (x<=5):
            #aleatorio de producto
            prodRand = random.randint(1, numProd)
            file.write("INSERT INTO producto_venta VALUES(" + str(i) +", "+ str(prodRand)+");" + os.linesep)
            x = x + 1;
        i= i + 1;
    file.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numClientes = 150
    numVentas = 800
    numProductos = 18
    creaClientes(numClientes)
    creaVentas(numClientes, numVentas)
    creaProdyVenta(numVentas,numProductos)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
