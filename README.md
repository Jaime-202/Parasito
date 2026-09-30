# 🦠 Parásito: El Lenguaje de Programación Esteganográfico & Motor de Infección

> *"El código que ves hace una cosa; los comentarios que ignoras hacen otra, y el ruido blanco esconde un grito de auxilio."*

**Parásito** es un lenguaje de programación esotérico (esolang) conceptual que carece de sintaxis convencional. Vive como un parásito dentro del código fuente de un programa anfitrión (como Python). 

Mientras que el compilador del lenguaje anfitrión ignora los comentarios para ejecutar el código principal, **el intérprete de Parásito ignora el código principal y compila exclusivamente los comentarios.**

---

## 🧠 ¿Cómo funciona? La Regla de la Imparidad

Parásito se basa en la **esteganografía algorítmica**. El motor procesa los comentarios aplicando una regla de lectura estricta: **solo evalúa las palabras ubicadas en posiciones impares** (1ª, 3ª, 5ª...). 

Las palabras en posiciones pares se descartan computacionalmente. Su única función es actuar como "pegamento gramatical" para que el texto parezca una nota técnica corporativa.

---

## 🛠️ Sintaxis Completa y Diccionario Técnico Extendido

El lenguaje incluye un **diccionario de comandos extendido con sinónimos técnicos en español**, permitiendo redactar comentarios de aspecto profesional sin romper la lógica del código.

### 📚 Comandos y Sinónimos

| Categoría | Comando Principal | Sinónimos Válidos | Descripción |
| :--- | :--- | :--- | :--- |
| **Memoria** | `limpiar` | `resetear`, `borrar` | Resetea la memoria, variables y consola. |
| | `guardar` | `almacenar`, `setear`, `asignar` | Guarda el siguiente valor en el acumulador. |
| | `archivar` | `registrar`, `guardar_var` | Guarda el acumulador en la variable especificada. |
| | `recordar` | `cargar`, `recuperar` | Carga la variable indicada en el acumulador. |
| **Aritmética y Texto** | `sumar` | `adicionar`, `incrementar` | Suma un valor o variable al acumulador. |
| | `restar` | `sustraer`, `decrementar` | Resta un valor al acumulador. |
| | `multiplicar` | `escalar` | Multiplica el acumulador. |
| | `dividir` | `partir` | Divide el acumulador (evitando división por cero). |
| | `unir` | `concatenar`, `anexar` | Concatena texto/cadenas. |
| **Control de Flujo** | `destino` | `etiqueta`, `marca`, `nodo` | Crea una etiqueta de salto invisible. |
| | `saltar` | `ir`, `brincar` | Salto incondicional a la etiqueta. |
| | `revisar` | `evaluar`, `comprobar`, `validar` | Salto condicional (solo si acumulador > 0). |
| **I/O y Salida** | `mostrar` | `imprimir`, `expresar`, `revelar` | Imprime el acumulador en la consola del parásito. |
| | `espacio` | `blank` | Imprime un espacio en blanco `" "`. |
| | `salto` | `linea` | Imprime un salto de línea `\n`. |
| **Infiltración / Infección** | `secreto` | `ocultar` | Genera un archivo `.parasito_secret.txt` en el directorio. |
| | `infectar` | `propagar`, `infiltrar` | Inyecta código parásito en el objetivo especificado. |

---

## 👻 Esteganografía Multinivel: "El Fantasma" (Acróstico Par)

Dado que Parásito descarta por completo las palabras en posiciones pares, el lenguaje incorpora una tercera capa secreta para humanos.

A través del **Acróstico Par**, el programador usa la primera letra de cada palabra par descartada para enviar un mensaje directo (ej. `SECRET`, `HACKED`), evadiendo tanto al lenguaje anfitrión como a la interpretación directa de Parásito.

### 🧩 Diseccionando un Bloque de Código (3 Dimensiones)
Imaginemos este comentario: 
> *"Limpiar El guardar sistema 10 tiene sumar errores."*

1. **Capa Anfitrión:** Python ve `#` e ignora la línea.
2. **Capa Parásito (Impares):** `Limpiar` -> `guardar` -> `10` -> `sumar`. (Suma 10 al acumulador).
3. **Capa Fantasma (Pares):** **E**l, **s**istema, **t**iene, **e**rrores. (Mensaje acróstico: **ESTE**).

---

## 🧪 Demostraciones Prácticas — Las 4 Pruebas

El proyecto incluye **4 archivos de prueba** que demuestran, capa por capa, todas las capacidades de Parásito. Cada uno actúa como un programa Python completamente funcional mientras esconde en sus comentarios dos programas adicionales invisibles.

---

### 🔬 ¿Cómo leer cada prueba?

Cada archivo de prueba tiene **3 dimensiones simultáneas**:

| Capa | Quién la ejecuta | ¿Qué ve / hace? |
|---|---|---|
| **Capa 1 — Anfitrión** | Python | Código normal y funcional (autenticación, cálculo, etc.) |
| **Capa 2 — Parásito (impares)** | VM Parásito | Instrucciones del esolang en posiciones 1ª, 3ª, 5ª... de cada comentario |
| **Capa 3 — Fantasma (pares)** | El ojo humano | Primera letra de las palabras en posición 2ª, 4ª, 6ª... forma un acróstico secreto |

**Ejemplo diseccionado:**
```
# Asignar Servidor "ACCESO_" Enlace Anexar Conexion
  ───────────────────────────────────────────────
  Impar:  Asignar         "ACCESO_"      Anexar      → VM: guarda y concatena
  Par:            Servidor        Enlace       Conexion → Acróstico: S·E·C → "SEC..."
```

---

### 📄 [`prueba1.py`](./prueba1.py) — Autenticación Infiltrada

**Capa anfitrión:** Servicio de login corporativo (`admin / 1234`).

**Capa Parásito:** La VM concatena credenciales secretas paso a paso:
```
Asignar "ACCESO_"        → acumulador = "ACCESO_"
Anexar  "CONCEDIDO_"     → acumulador = "ACCESO_CONCEDIDO_"
Anexar  "NIVEL_ALPHA"    → acumulador = "ACCESO_CONCEDIDO_NIVEL_ALPHA"
Expresar                 → imprime el resultado
Ocultar "PAYLOAD_..."    → escribe .parasito_secret.txt
```

**Capa Fantasma:** Palabras pares `Servidor · Enlace · Conexion · Registro · Entrada · Transmision` → acróstico **`SECRET`**

---

### 💉 [`prueba2.py`](./prueba2.py) — Infección Automática de Repositorios

**Capa anfitrión:** Script Python que crea un repositorio de prueba (`mi_repositorio_objetivo/`) con módulos reales (`modulo_pago.py`, `servicio_email.py`).

**Capa Parásito:** Usa `parasito.infectar_repositorio()` para:
1. Escanear todos los `.py` del repositorio víctima.
2. Inyectar al final de cada archivo un bloque con `import parasito` + `parasito.despertar()`.
3. Ejecutar el módulo infectado con `subprocess` — el código original funciona, pero el Parásito se activa en silencio.

**Capa Fantasma:** Las palabras pares del comentario inyectado forman el acróstico **`HACKED`**.

> Esta prueba simula un **supply chain attack** esteganográfico: el repositorio víctima parece intacto para cualquier revisor humano.

---

### 🔁 [`prueba3.py`](./prueba3.py) — Bucle Turing-Completo

**Capa anfitrión:** Función `calcular_matriz_financiera()` que devuelve una matriz de ejemplo.

**Capa Parásito:** Demuestra que el esolang es Turing-completo ejecutando un bucle de cuenta atrás con variables, aritmética y saltos condicionales:
```
Almacenar 3 → Archivar cont
[etiqueta: bucle]
  Recordar msg → Expresar        → imprime mensaje
  Recordar cont → Expresar       → imprime 3, 2, 1...
  Sustraer 1 → Archivar cont
  Evaluar bucle                  → si cont > 0, salta
Almacenar "¡Bucle_Completado!" → Expresar
Ocultar "SISTEMA_TOTALMENTE_CONTROLADO"
```

**Salida de la VM:**
```
Bucle_Iniciado: 3
Bucle_Iniciado: 2
Bucle_Iniciado: 1
¡Bucle_Completado!
```

**Capa Fantasma:** Palabras pares forman el acróstico **`CICLO`**.

---

### 🧮 [`prueba4.py`](./prueba4.py) — Calculadora Interactiva con Menú

**Capa anfitrión:** Calculadora corporativa completamente funcional con menú interactivo que soporta suma, resta, multiplicación, división, potencia y módulo, además de un historial de operaciones.

**Capa Parásito:** Escondido en los comentarios de las funciones aritméticas, la VM construye y muestra un mensaje filosófico perturbador sobre los números:
```
"LOS_NUMEROS SON_SOLO ILUSIONES ___ Y_EL_PARASITO ES_REAL___
>>> CALCULA_TU_FUTURO <<<"
```
Y escribe en disco: `.parasito_secret.txt` → `LA_CALCULADORA_TE_VIGILA`

**Capa Fantasma:** Acróstico **`NUMBERS`** en las palabras pares de los comentarios.

```
╔══════════════════════════════════════╗
║   🧮  CALCULADORA CORPORATIVA v4.0   ║
╠══════════════════════════════════════╣
║  [1]  Suma              (a + b)      ║
║  [2]  Resta             (a - b)      ║
║  [3]  Multiplicación    (a × b)      ║
║  [4]  División          (a ÷ b)      ║
║  [5]  Potencia          (a ^ b)      ║
║  [6]  Módulo            (a mod b)    ║
║  [0]  Salir                          ║
╚══════════════════════════════════════╝
```

---

## 🗺️ Mapa de las 4 Pruebas

```
prueba1.py  →  CONCATENACIÓN + MENSAJE SECRETO en código de autenticación
prueba2.py  →  PROPAGACIÓN / INFECCIÓN automática de repositorios ajenos
prueba3.py  →  TURING-COMPLETITUD: bucles, variables y saltos condicionales
prueba4.py  →  CALCULADORA INTERACTIVA: el anfitrión más inocente oculta el grito más oscuro
```

---

## 🚀 Cómo Ejecutar los Ejemplos

```bash
python prueba1.py
python prueba2.py
python prueba3.py
python prueba4.py
```

---

## 🎯 Conclusión

El mayor reto de **Parásito** no es la complejidad matemática, sino la **restricción lingüística humana**. Programar aquí requiere resolver un algoritmo de máquina mientras mantienes una cohesión gramatical impecable para el ojo humano.

Cada prueba es, simultáneamente, un programa funcional, un programa esotérico y un mensaje secreto. **Tres realidades superpuestas en el mismo archivo de texto.**