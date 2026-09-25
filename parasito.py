import tokenize

def despertar(ruta_archivo):
    comentarios = []
    
    # 1. Extraer los comentarios
    with open(ruta_archivo, 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        for tok in tokens:
            if tok.type == tokenize.COMMENT:
                comentarios.append(tok.string.lstrip('#').strip())
                
    texto_unido = " ".join(comentarios)
    palabras = texto_unido.split()
    
    # REGLA PARÁSITO: Posiciones impares (0, 2, 4...)
    impares = palabras[::2] 
    
    # FIX: Ahora limpiamos absolutamente toda la puntuación
    def limpiar(palabra):
        return palabra.lower().strip(' ,.!?:;"\'()[]{}')

    # --- FASE 1: REGISTRO DE ETIQUETAS (DESTINOS) ---
    etiquetas = {}
    for i in range(len(impares)):
        if limpiar(impares[i]) == "destino":
            if i + 1 < len(impares):
                etiquetas[limpiar(impares[i+1])] = i + 2 

    memoria = {}
    acumulador = ""
    resultado = ""
    i = 0
    
    def obtener_valor(idx):
        if idx >= len(impares): return ""
        raw_val = impares[idx].strip(' ,.!?:;"\'()[]{}')
        clave = limpiar(impares[idx])
        return memoria.get(clave, raw_val) 
    
    # --- FASE 2: EJECUCIÓN (TURING COMPLETO) ---
    while i < len(impares):
        cmd = limpiar(impares[i])
        
        if cmd == "guardar":
            i += 1
            if i < len(impares): acumulador = impares[i].strip(' ,.!?:;"\'()[]{}')
        elif cmd == "archivar":
            i += 1
            if i < len(impares): memoria[limpiar(impares[i])] = acumulador
        elif cmd == "recordar":
            i += 1
            if i < len(impares): acumulador = memoria.get(limpiar(impares[i]), "")
        elif cmd == "sumar" or cmd == "restar":
            i += 1
            if i < len(impares):
                val = obtener_valor(i)
                try:
                    base = float(acumulador) if acumulador != "" else 0.0
                    num = float(val)
                    nuevo_val = base + num if cmd == "sumar" else base - num
                    acumulador = str(int(nuevo_val)) if nuevo_val.is_integer() else str(nuevo_val)
                except ValueError: pass
        elif cmd == "unir":
            i += 1
            if i < len(impares): acumulador = str(acumulador) + str(obtener_valor(i))
        elif cmd == "saltar":
            i += 1
            if i < len(impares):
                dest = limpiar(impares[i])
                if dest in etiquetas: i = etiquetas[dest] - 1 
        elif cmd == "revisar":
            i += 1
            if i < len(impares):
                try:
                    if float(acumulador) > 0:
                        dest = limpiar(impares[i])
                        if dest in etiquetas: i = etiquetas[dest] - 1
                except ValueError: pass
        elif cmd == "mostrar": resultado += str(acumulador)
        elif cmd == "espacio": resultado += " "
        elif cmd == "salto":   resultado += "\n"
        elif cmd == "limpiar":
            resultado = ""
            acumulador = ""
            memoria = {}
        elif cmd == "destino": 
            i += 1 # Ignoramos el nombre de la etiqueta al pasar sobre ella
            
        i += 1 
        
    print("\n[🦠 EJECUCIÓN DEL PARÁSITO]")
    print(resultado if resultado else "(El parásito guardó silencio)")
    print("[--------------------------]")

    # --- FASE 3: ESTEGANOGRAFÍA FANTASMA ---
    # Extraemos palabras pares (índices 1, 3, 5...)
    pares = palabras[1::2]
    acrostico = ""
    for p in pares:
        letra = p.strip(' ,.!?:;"\'()[]{}')
        if letra:
            acrostico += letra[0].upper()
            
    print("\n[👻 ESCÁNER DE FANTASMAS (Acróstico Par)]")
    print(f"Mensaje oculto: {acrostico}")
    print("[---------------------------------------]\n")