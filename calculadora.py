
#Calculadora de eventos 
import time

tarifa = input("Ingresa un monto: $")
porcentaje = tarifa * input("Ingresa un porcentaje:")

#----DESGLOSE----
print("--------------")
print("DESGLOSE:")

print ("La comision es de: $\n"), porcentaje 

ivaporcentaje =porcentaje *1.16
print ("La comision con IVA es de: $\n"),ivaporcentaje


porcentaje2 = tarifa + porcentaje
print ("EL costo del boleto con cargos es de: $\n"), porcentaje2


tarifaconiva = (tarifa+ivaporcentaje)
print ("El costo del boleto con cargos e IVA es de: $\n"),tarifaconiva

comision1 = .035
comision2 = 2.50

comisiones = (tarifaconiva*comision1+comision2)*1.16
print ("La Comision cobro pago con tarjeta IVA incluido es de: $\n"),comisiones

costototal = tarifaconiva + comisiones
print ("Precio al publico: $\n"),costototal

time.sleep(4)
#Utilidades
print("---------------")
print ("ASISTENCIA Y UTILIDADES")
numeroasistentes = input("Ingresa la cantidad de asistentes:")
utilidades = numeroasistentes*porcentaje
print ("Si asisten al evento"),numeroasistentes,("personas")
print ("Tus utilidades son de: $"),float(utilidades)
time.sleep(4)
#Impacto ambiental
print ("-----------------")
print("IMPACTO AMBIENTAL")
impacto = numeroasistentes * float(1.7)
print("El impacto aproximado anual producido por la cantidad de asistentes es de:"),impacto


if impacto > 600:
		print ("Toneladas capturadas de Co2:")

else: 
	    print ("Kilos capturados de Co2:")


time.sleep(5)
#gastos
print ("----------------")
print ("GASTOS")
gastos = input("Ingresa tus gastos $")
gastos1 = utilidades- gastos
print "Gastaste $", gastos 
print "Te quedan $", gastos1

time.sleep(5)
#particiones
print("----------------")
print("GANANCIAS POR SOCIO:")

socio1 = "Carlos = $", utilidades *.45
socio2 = "Chary = $" , utilidades *.35
socio3 = "Marco = $" , utilidades *.10
socio4 = "Rosy = $" , utilidades *.10

print socio1
print socio2
print socio3
print socio4



