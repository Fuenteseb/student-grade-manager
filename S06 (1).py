nan = float("nan")

ARCHIVO = "Violencia_Intrafamiliar_Limpieza_Lógica_Computacional.xlsx"

GRUPOS_EDAD = ["Menor 1 año", "De 1 - 5 años", "De 6 - 13 años", "De 14 - 17 años", "De 18 - 26 años",
               "De 27 - 44 años", "De 45 - 59 años", "De 60 - 69 años", "De 70 - 79 años",
               "De 80 - 99 años", "De 100 - 105 años"]

def esta_en_rango(valor, minimo, maximo):
    if valor != valor:          
        return False
    if valor >= minimo and valor <= maximo:
        return True
    return False

def es_categoria_valida(categoria, categorias_permitidas):
    if categoria in categorias_permitidas:
        return True
    return False

def clasificar_aseguramiento(tipo):
    if tipo == "Contributivo":
        return "Contributivo"
    elif tipo == "Subsidiado":
        return "Subsidiado"
    else:
        return "Otro"      

def resumir(tipos, estratos, grupos):
    total = 0
    contador_contributivo = 0
    contador_subsidiado = 0
    contador_otro = 0
    suma_estrato = 0
    con_estrato = 0
    sin_estrato = 0
    contador_condicion = 0
    existe_condicion = False    

    # 2. Ciclo
    for i in range(len(tipos)):
        total += 1

        categoria = clasificar_aseguramiento(tipos[i])
        if categoria == "Contributivo":
            contador_contributivo += 1
        elif categoria == "Subsidiado":
            contador_subsidiado += 1
        else:
            contador_otro += 1

        if esta_en_rango(estratos[i], 1, 6):
            suma_estrato += estratos[i]
            con_estrato += 1
        else:
            sin_estrato += 1

        if es_categoria_valida(grupos[i], GRUPOS_EDAD) == False:
            contador_condicion += 1
            existe_condicion = True

    return (total, contador_contributivo, contador_subsidiado, contador_otro,
            suma_estrato, con_estrato, sin_estrato, contador_condicion, existe_condicion)


def mostrar_resumen(r):
    print("===== RESUMEN =====")
    print("Total de registros:", r[0])
    print("Contributivo:", r[1])
    print("Subsidiado:", r[2])
    print("Otro:", r[3])
    print("Suma de estrato:", r[4])
    print("Registros con estrato válido:", r[5])
    print("Registros sin estrato válido:", r[6])
    print("Grupos de edad inválidos:", r[7])
    print("¿Existe algún registro que cumpla la condición?:", r[8])

tipos_a = ["Contributivo", "Subsidiado", "Contributivo", "Contributivo", "Contributivo", "Subsidiado",
           "Vinculado", "Contributivo", "Subsidiado", "Subsidiado", "Vinculado", "Contributivo"]
estratos_a = [nan, nan, nan, 2, nan, 1, nan, 2, nan, 2, nan, nan]
grupos_a = ["De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años",
            "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años",
            "De 1 - 5 años", "De 1 - 5 años"]

tipos_b = ["Subsidiado", "Contributivo", "Subsidiado", "Subsidiado", "Contributivo", "Contributivo",
           "Contributivo", "Subsidiado", "Excepción", "Subsidiado", "Contributivo", "Contributivo"]
estratos_b = [1, nan, 1, nan, 1, 2, 1, 2, 2, 2, 2, nan]
grupos_b = ["Menor 1 año", "Menor 1 año", "Menor 1 año", "Menor 1 año", "Menor 1 año", "14 - 17 años",
            "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años"]

tipos_c = ["Contributivo", "Subsidiado", "Vinculado", nan, "Contributivo", "Contributivo",
           "Contributivo", "Contributivo", "Subsidiado", "Subsidiado"]
estratos_c = [2, 1, nan, nan, 2, 4, nan, nan, 2, 1]
grupos_c = ["De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "De 1 - 5 años", "14 - 17 años",
            "De 30 - 34 años", "De 30 - 34 años", "De 6 - 13 años", "De 18 - 26 años", "Menor 1 año"]

print("=== RETO 1: contador de registros ===")
valores = [22.5, 55.1, 72.3, 38.7, 61.4]
contador = 0
for valor in valores:
    contador += 1
print("Registros procesados:", contador)

print("--- Con el dataset (columna estrato, muestra A) ---")
contador = 0
for estrato in estratos_a:
    contador += 1
print("Registros procesados:", contador)

print("=== RETO 2: contador por categoría (tipo de aseguramiento) ===")
contador_a = 0   # Contributivo
contador_b = 0   # Subsidiado
contador_c = 0   # Otro
total = 0
for tipo in tipos_a:
    total += 1
    if tipo == "Contributivo":
        contador_a += 1
    elif tipo == "Subsidiado":
        contador_b += 1
    else:
        contador_c += 1
print("Categoría A (Contributivo):", contador_a)
print("Categoría B (Subsidiado):", contador_b)
print("Categoría C (Otro):", contador_c)
print("Total:", total)
print("¿A + B + C = TOTAL?", contador_a + contador_b + contador_c == total)

print("=== RETO 3: acumulador de valores ===")
valores = [10, 20, 30, 40, 50]
suma_valores = 0
for valor in valores:
    suma_valores += valor
print("Suma de valores:", suma_valores)

print("--- Con el dataset (columna estrato, muestra A) ---")
suma_estrato = 0
for estrato in estratos_a:
    if esta_en_rango(estrato, 1, 6):     
        suma_estrato += estrato
print("Suma de estrato:", suma_estrato)

print("=== RETO 4: bandera de existencia ===")
print("Condición 1: ¿hay algún registro con estrato 2? (muestra A)")
existe_condicion = False
for estrato in estratos_a:
    if estrato == 2:
        existe_condicion = True
print("¿Existe algún registro que cumpla la condición?:", existe_condicion)

print("Condición 2: ¿hay algún registro con estrato 6? (muestra A)")
existe_condicion = False
for estrato in estratos_a:
    if estrato == 6:
        existe_condicion = True
print("¿Existe algún registro que cumpla la condición?:", existe_condicion)

print("=== RETO 5: procesamiento y resumen ===")
print("--- Versión 1: datos de práctica ---")
valores = [22.5, 55.1, 72.3, 38.7, 61.4]
total = 0
categoria_a = 0   
categoria_b = 0   
categoria_c = 0   
suma_valores = 0
existe_condicion = False   
for valor in valores:
    total += 1
    suma_valores += valor
    if valor < 40:
        categoria_a += 1
    elif valor < 70:
        categoria_b += 1
    else:
        categoria_c += 1
    if valor > 70:
        existe_condicion = True
print("===== RESUMEN =====")
print("Total de registros:", total)
print("Categoría A:", categoria_a)
print("Categoría B:", categoria_b)
print("Categoría C:", categoria_c)
print("Suma de valores:", round(suma_valores, 1))
print("¿Existe algún registro que cumpla la condición?:", existe_condicion)

print("--- Versión 2: columnas reales del dataset (muestra A) ---")
resultado = resumir(tipos_a, estratos_a, grupos_a)
mostrar_resumen(resultado)

print("=== RETO 6: ningún registro cumple la condición ===")
print("Condición: grupo de edad inválido. Muestra A (las 12 filas tienen grupo válido).")
contador_condicion = 0
bandera = False
for grupo in grupos_a:
    if es_categoria_valida(grupo, GRUPOS_EDAD) == False:
        contador_condicion += 1
        bandera = True
print("contador_condicion =", contador_condicion)
print("bandera =", bandera)
print("Explicación: la bandera empieza en False y solo cambia a True dentro del if. Como ningún")
print("grupo de edad fue inválido, el if nunca se cumplió y la bandera se quedó en False.")

print("=== RETO 7: un solo registro cumple la condición ===")
print("Condición: grupo de edad inválido. Muestra B (solo el registro 6 es '14 - 17 años').")
contador_condicion = 0
bandera = False
iteracion = 0
for grupo in grupos_b:
    iteracion += 1
    if es_categoria_valida(grupo, GRUPOS_EDAD) == False:
        contador_condicion += 1
        bandera = True
        print("  -> La bandera cambió a True en la iteración", iteracion, "con el dato:", grupo)
print("contador =", contador_condicion)
print("bandera =", bandera)
print("Explicación: la bandera cambió en la iteración 6, que es donde aparece '14 - 17 años'")
print("(le falta la palabra 'De'). En las demás iteraciones el if no se cumplió.")

print("=== RETO 8: datos mixtos ===")
print("Muestra C: 10 registros con diferentes categorías y condiciones.")
print("Cálculo MANUAL (hecho a mano antes de ejecutar):")
manual_total = 10
manual_contributivo = 5
manual_subsidiado = 3
manual_otro = 2          
manual_suma = 12         
manual_condicion = True  
print("  Total:", manual_total, "| Contributivo:", manual_contributivo, "| Subsidiado:", manual_subsidiado,
      "| Otro:", manual_otro, "| Suma estrato:", manual_suma, "| Condición:", manual_condicion)

print("Resultado del PROGRAMA:")
resultado = resumir(tipos_c, estratos_c, grupos_c)
mostrar_resumen(resultado)

coincide = (resultado[0] == manual_total and resultado[1] == manual_contributivo
            and resultado[2] == manual_subsidiado and resultado[3] == manual_otro
            and resultado[4] == manual_suma and resultado[8] == manual_condicion)
print("¿El programa coincide con el cálculo manual?:", coincide)


print("=== RETO 9: error de inicialización ===")
print("Código con error (contador = 0 dentro del ciclo), condición: estrato igual a 2, muestra A:")
for estrato in estratos_a:
    contador = 0                  
    if estrato == 2:
        contador += 1
contador_con_error = contador
print("Contador con el error:", contador_con_error)

print("Código corregido (contador = 0 antes del ciclo):")
contador = 0
for estrato in estratos_a:
    if estrato == 2:
        contador += 1
print("Contador corregido:", contador)

print("\n1. ¿Qué problema existe? El contador se pone en 0 dentro del ciclo, en cada vuelta.")
print("2. ¿Por qué no conserva la información? Porque cada vez que empieza una vuelta el valor anterior")
print("   se borra. Al final solo queda lo que pasó en el último registro (aquí el último es nan, por eso da 0).")
print("3. ¿Dónde debe inicializarse? Antes del ciclo for, una sola vez.")
print("4. Corrección: poner contador = 0 arriba del for (ya está hecho en el código corregido).")
print("5. Diferencia: la versión con error da", contador_con_error, "y la corregida da 3, que es la cantidad real de estratos 2.")


print("\n=== CARGA DEL DATASET COMPLETO (puede tardar un poco) ===")
df = pd.read_excel(ARCHIVO, sheet_name="osb_saludmental_limpio")
tipos_df = df["tipoaseguramiento"].tolist()
estratos_df = df["estrato"].tolist()
grupos_df = df["grupoedad"].tolist()
print("Filas cargadas:", len(tipos_df))


print("\n=== RETO 10: integración con el dataset de trabajo ===")
print("Se reutilizan: esta_en_rango() y es_categoria_valida() de la S05, y clasificar_aseguramiento().")
resultado = resumir(tipos_df, estratos_df, grupos_df)
mostrar_resumen(resultado)
if resultado[5] > 0:
    print("Promedio de estrato (solo registros con estrato válido):", round(resultado[4] / resultado[5], 2))
print("¿Contributivo + Subsidiado + Otro = Total?",
      resultado[1] + resultado[2] + resultado[3] == resultado[0])
print("=== RETO FINAL: resumen del dataset ===")
print("===== RESUMEN DEL DATASET =====")
print("Total de registros:", resultado[0])
print("Categoría 1 (Contributivo):", resultado[1])
print("Categoría 2 (Subsidiado):", resultado[2])
print("Categoría 3 (Otro):", resultado[3])
print("Suma de valores (estrato):", resultado[4])
print("¿Se encontró la condición (grupo de edad inválido)?:", resultado[8])


print("=== CASOS DE PRUEBA ===")
casos = [
    ["1. Todos en una categoría",
     ["Contributivo", "Contributivo", "Contributivo", "Contributivo", "Contributivo"],
     [1, 2, 3, 4, 5],
     ["De 6 - 13 años", "De 6 - 13 años", "De 6 - 13 años", "De 6 - 13 años", "De 6 - 13 años"],
     (5, 5, 0, 0, 15, 5, 0, 0, False),
     "Contributivo = total"],
    ["2. Un registro cumple la condición",
     ["Contributivo", "Subsidiado", "Vinculado"],
     [1, 2, 3],
     ["De 1 - 5 años", "14 - 17 años", "De 6 - 13 años"],
     (3, 1, 1, 1, 6, 3, 0, 1, True),
     "Contador = 1 y bandera = True"],
    ["3. Varios cumplen la condición",
     ["Contributivo", "Contributivo", "Subsidiado", "Excepción"],
     [2, nan, 3, 1],
     ["De 30 - 34 años", "De 1 - 5 años", "14 - 17 años", "De 30 - 34 años"],
     (4, 2, 1, 1, 6, 3, 1, 3, True),
     "Condición cumplida 3 veces"],
    ["4. Ninguno cumple la condición",
     ["Subsidiado", "Subsidiado"],
     [1, 2],
     ["De 1 - 5 años", "De 6 - 13 años"],
     (2, 0, 2, 0, 3, 2, 0, 0, False),
     "Contador = 0 y bandera = False"],
    ["5. Datos mixtos (muestra C)",
     tipos_c, estratos_c, grupos_c,
     (10, 5, 3, 2, 12, 6, 4, 3, True),
     "Incluye vacíos (nan) y 3 grupos inválidos"],
    ["6. Datos conocidos para la suma",
     ["Contributivo", "Contributivo", "Contributivo", "Contributivo", "Contributivo", "Contributivo"],
     [1, 2, 3, 4, 5, 6],
     ["Menor 1 año", "De 1 - 5 años", "De 6 - 13 años", "De 14 - 17 años", "De 18 - 26 años", "De 27 - 44 años"],
     (6, 6, 0, 0, 21, 6, 0, 0, False),
     "1+2+3+4+5+6 = 21"],
]

pruebas_exitosas = 0
for caso in casos:
    obtenido = resumir(caso[1], caso[2], caso[3])
    esperado = caso[4]
    exitosa = (obtenido == esperado)
    if exitosa:
        pruebas_exitosas += 1
    print("  Caso", caso[0])
    print("  Datos (tipo):", caso[1])
    print("  Datos (estrato):", caso[2])
    print("  Datos (grupo de edad):", caso[3])
    print("  Resultado esperado:", esperado)
    print("  Resultado obtenido:", obtenido)
    print("  ¿Prueba exitosa?:", exitosa)
    print("  Observaciones:", caso[5])
print("Pruebas exitosas:", pruebas_exitosas, "de", len(casos))


print("=== PREGUNTAS DE REFLEXIÓN ===")
print("1. ¿Diferencia entre contador y acumulador?")
print("   El contador suma 1 cada vez (cuenta cuántos hay). El acumulador suma el valor del dato (por ejemplo el estrato).")
print("2. ¿Por qué inicializar antes del ciclo?")
print("   Porque si no existe, Python da error al sumarle; y si se pone dentro del ciclo se borra en cada vuelta.")
print("3. ¿Qué problema resuelve una bandera?")
print("   Guarda si algo pasó al menos una vez mientras se recorren los datos, sin tener que contar cuántas veces.")
print("4. ¿Qué pasa si un contador se reinicia dentro del ciclo?")
print("   Pierde lo acumulado y al final solo refleja el último registro (ver Reto 9).")
print("5. ¿Cómo verifiqué que el resumen es correcto?")
print("   Calculé a mano una muestra pequeña (Reto 8), la comparé con el programa, hice 6 casos de prueba y revisé que")
print("   Contributivo + Subsidiado + Otro = Total en el dataset completo.")
print("6. ¿Relación entre categorías y total si son exhaustivas y excluyentes?")
print("   La suma de todas las categorías debe ser igual al total.")
print("7. ¿Por qué reutilizar funciones existentes?")
print("   Porque la regla queda escrita una sola vez, ya está probada y si cambia se corrige en un solo lugar.")
print("8. ¿Qué variables del dataset sirvieron para contadores?")
print("   tipoaseguramiento (Contributivo/Subsidiado/Otro) y también sexo, ciclo_vital o grupoedad.")
print("9. ¿Qué variable usé como acumulador y por qué?")
print("   estrato, porque es numérica (1 a 6). Se suman solo los estratos válidos y se ignoran los vacíos.")
print("10. ¿Qué condición usé para la bandera y por qué es útil?")
print("   Que exista un grupo de edad inválido (fuera de la lista GRUPOS_EDAD). Sirve para saber si el dataset")
print("   todavía tiene errores de escritura que hay que limpiar.")

print("=== PSEUDOCÓDIGO ===")
print("INICIO")
print("  Leer el dataset")
print("  total = 0, contributivo = 0, subsidiado = 0, otro = 0")
print("  suma_estrato = 0, contador_condicion = 0, bandera = False")
print("  PARA cada registro")
print("    total = total + 1")
print("    SI estrato es válido ENTONCES suma_estrato = suma_estrato + estrato")
print("    categoria = clasificar_aseguramiento(tipo)")
print("    SI categoria es Contributivo ENTONCES contributivo = contributivo + 1")
print("    SINO SI categoria es Subsidiado ENTONCES subsidiado = subsidiado + 1")
print("    SINO otro = otro + 1")
print("    SI grupo de edad NO es válido ENTONCES")
print("      contador_condicion = contador_condicion + 1")
print("      bandera = True")
print("  FIN PARA")
print("  Mostrar resumen")
print("FIN")
