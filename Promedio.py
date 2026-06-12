#BASE DE DATOS DE ESTUDIANTES 
estudiantes = {}

cantidad_estudiantes = int(input("Cuántos estudiantes quieres ingresar: "))

contador_estudiantes = 0 

while contador_estudiantes < cantidad_estudiantes: 
    nombres_estudiante = input("Ingresa el nombre del estudiante {}: ".format(contador_estudiantes + 1)) 
    
    contador_estudiantes = contador_estudiantes + 1 
    
    contador_notas = 0 
    
    cantidad_notas = int(input("Cuántas notas quieres ingresar del estudiante {}: ".format(nombres_estudiante))) 
    
    notas_estudiante = [] 
    
    while contador_notas < cantidad_notas: 
        nota = float(input("Ingresa una nota del estudiante {}: ".format(nombres_estudiante))) 
        notas_estudiante.append(nota) 
        
        contador_notas = contador_notas + 1 
        
    estudiantes[nombres_estudiante] = {"notas": notas_estudiante}

def suma_notas(notas_estudiante):
        suma = 0
        for nota in notas_estudiante:
            suma = (suma+nota)
        return suma
def promedio_notas(notas_estudiante):
        promedio = suma_notas(notas_estudiante) / len (notas_estudiante)
        return promedio
resultado= promedio_notas(notas_estudiante)
def nota_mayor(notas_estudiante):
        mayor = 0
        for nota in notas_estudiante:
            if nota > mayor:
                mayor = nota
        return mayor
def nota_menor(notas_estudiante):
        menor = notas_estudiante[0]
        for nota in notas_estudiante:
            if nota < menor:
                menor = nota
        return menor
def aprobado(notas__estudiante):
        if promedio_notas(notas_estudiante) >= 3.0:
              return "Aprobado"
        else:            
             return "Reprobado"
            
for estudiante in estudiantes:
     notas_estudiante = estudiantes[estudiante]["notas"]
     print("Estudiante:", estudiante)
     print("Notas:", notas_estudiante)
     promedio = promedio_notas(notas_estudiante)
     estudiantes[estudiante]["promedio"] = promedio
     print("Promedio:", promedio)
     mayor = nota_mayor(notas_estudiante)
     estudiantes[estudiante]["mayor"] = mayor
     print("Mayor:", mayor)
     menor= nota_menor(notas_estudiante)
     estudiantes[estudiante]["menor"] = menor
     print("Menor:", menor)
     estado = aprobado(notas_estudiante)
     estudiantes[estudiante]["estado"] = estado
     print(estado)