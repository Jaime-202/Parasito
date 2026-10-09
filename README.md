# 🦠 Parásito — El Lenguaje de Programación Esteganográfico

> *"El código que ves hace una cosa; los comentarios que ignoras hacen otra, y el ruido blanco esconde un grito de auxilio."*

**Parásito** es un lenguaje de programación esotérico (**esolang**) que no tiene sintaxis propia. Vive como un parásito dentro del código fuente de un programa anfitrión Python.

Mientras Python ejecuta el programa principal ignorando los comentarios, **el intérprete de Parásito ignora el código principal y compila exclusivamente los comentarios.**

---

## 🧠 Concepto: La Regla de la Imparidad

Los comentarios actúan como texto técnico de aspecto normal. Pero Parásito aplica una regla estricta de lectura:

- **Palabras en posición IMPAR** (1ª, 3ª, 5ª…) → son las instrucciones ejecutables del esolang
- **Palabras en posición PAR** (2ª, 4ª, 6ª…) → son "pegamento gramatical" invisible para la VM, pero su **primera letra** forma un acróstico secreto para el ojo humano

Esto da lugar a **3 capas simultáneas** dentro de un mismo archivo `.py`:

| Capa | Quién la ejecuta | Qué hace |
|---|---|---|
| **1 — Anfitrión** | Python | Programa funcional normal |
| **2 — Parásito** | VM Parásito | Instrucciones esolang en posiciones impares |
| **3 — Fantasma** | El ojo humano | Acróstico formado por la 1ª letra de las palabras pares |

### Ejemplo diseccionado

```
# Limpiar Nodo  Almacenar Usuario  "LOS_NUMEROS_" Modulo  Unir Buffer  "SON_SOLO_" Entrada
  ───────────────────────────────────────────────────────────────────────────────────────
  Impar:  Limpiar    Almacenar        "LOS_NUMEROS_"         Unir          "SON_SOLO_"
  Par:            Nodo        Usuario                Modulo       Buffer              Entrada
                  N           U                      M            B                   E  → NUMBE…
```

- **Python** → ignora toda la línea (es un comentario)
- **VM Parásito** → ejecuta: `limpiar`, `guardar "LOS_NUMEROS_"`, `unir "SON_SOLO_"`
- **Fantasma** → acróstico: **N·U·M·B·E·R·S**

---

## 🛠️ ISA — Tabla de Instrucciones Completa

| Categoría | Comando | Sinónimos válidos | Descripción |
|---|---|---|---|
| **MEM** | `limpiar` | `resetear`, `borrar` | Resetea acumulador, variables y salida |
| **MEM** | `guardar <val>` | `almacenar`, `setear`, `asignar` | Carga `<val>` en el acumulador |
| **MEM** | `archivar <var>` | `registrar`, `guardar_var` | Guarda el acumulador en la variable `<var>` |
| **MEM** | `recordar <var>` | `cargar`, `recuperar` | Carga `<var>` en el acumulador |
| **ARITH** | `sumar <val>` | `adicionar`, `incrementar` | Acumulador ← Acumulador + val |
| **ARITH** | `restar <val>` | `sustraer`, `decrementar` | Acumulador ← Acumulador − val |
| **ARITH** | `multiplicar <val>` | `escalar` | Acumulador ← Acumulador × val |
| **ARITH** | `dividir <val>` | `partir` | Acumulador ← Acumulador ÷ val (seguro contra ÷0) |
| **ARITH** | `unir <val>` | `concatenar`, `anexar` | Concatenación de cadenas |
| **FLOW** | `destino <id>` | `etiqueta`, `marca`, `nodo` | Define una etiqueta de salto |
| **FLOW** | `saltar <id>` | `ir`, `brincar` | Salto incondicional a `<id>` |
| **FLOW** | `revisar <id>` | `evaluar`, `comprobar`, `validar` | Salto condicional si Acumulador > 0 |
| **I/O** | `mostrar` | `imprimir`, `expresar`, `revelar` | Imprime el acumulador |
| **I/O** | `espacio` | `blank` | Añade un espacio en blanco |
| **I/O** | `salto` | `linea` | Añade un salto de línea `\n` |
| **INF** | `secreto <msg>` | `ocultar` | Escribe `.parasito_secret.txt` en el Escritorio |
| **INF** | `infectar <ruta>` | `propagar`, `infiltrar` | Inyecta código Parásito en un archivo objetivo |

---

## 🚀 Cómo ejecutar

**Requisito:** Python 3.10 o superior.

```bash
# Clona el repositorio
git clone https://github.com/TU_USUARIO/parasito.git
cd parasito

# Ejecuta cualquiera de las 4 demos
python prueba1.py
python prueba2.py
python prueba3.py
python prueba4.py
```

---

## 🧪 Las 4 Demos

### [`prueba1.py`](./prueba1.py) — Autenticación Infiltrada
**Anfitrión:** Servicio de login corporativo (`admin / 1234`).  
**Parásito:** Concatena `ACCESO_CONCEDIDO_NIVEL_ALPHA` y escribe el secreto en disco.  
**Fantasma:** Acróstico → **`SECRET`**

---

### [`prueba2.py`](./prueba2.py) — Infección de Repositorios
**Anfitrión:** Crea un repositorio Python de prueba con módulos reales.  
**Parásito:** Escanea e inyecta código parásito en cada `.py` del repositorio víctima.  
**Fantasma:** Acróstico → **`HACKED`**

> Simula un **supply chain attack** esteganográfico: el repositorio víctima parece intacto a simple vista.

---

### [`prueba3.py`](./prueba3.py) — Bucle Turing-Completo
**Anfitrión:** Función que calcula una matriz financiera de ejemplo.  
**Parásito:** Demuestra Turing-completitud con un bucle de cuenta atrás usando variables, aritmética y saltos condicionales.  
**Fantasma:** Acróstico → **`CICLO`**

```
Salida de la VM:
  Bucle_Iniciado: 3
  Bucle_Iniciado: 2
  Bucle_Iniciado: 1
  ¡Bucle_Completado!
```

---

### [`prueba4.py`](./prueba4.py) — Calculadora Interactiva *(Demo principal)*
**Anfitrión:** Calculadora corporativa con menú (suma, resta, multiplicación, división, potencia, módulo).  
**Parásito:** Construye el mensaje `LOS_NUMEROS_SON_SOLO_ILUSIONES... EL_PARASITO_SI_ES_REAL.` y escribe `.parasito_secret.txt` en el **Escritorio** del usuario.  
**Fantasma:** Acróstico → **`NUMBERS`**

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

## 💉 El Pendrive Infectado (Demo en Vivo)

Este repositorio incluye un **vector de demostración física** pensado para presentaciones:

1. Clona el repo en un pendrive con etiqueta **"USB CONTAGIADO / ACTIVO"**
2. Ejecuta `lanzar_demo.bat` en el ordenador del aula (doble clic)
3. Interactúa con la calculadora
4. Al salir, el Parásito se activa y crea `.parasito_secret.txt` en el **Escritorio** de esa máquina
5. Acompaña la demo con la ficha técnica imprimible: `cheatsheet_parasito.html`

---

## 📁 Estructura del repositorio

```
parasito/
├── parasito.py              # Motor del lenguaje: intérprete, VM, infección
├── prueba1.py               # Demo: autenticación infiltrada (acróstico SECRET)
├── prueba2.py               # Demo: infección de repositorios (acróstico HACKED)
├── prueba3.py               # Demo: bucle Turing-completo (acróstico CICLO)
├── prueba4.py               # Demo: calculadora interactiva (acróstico NUMBERS)
├── conexion_red.py          # Módulo auxiliar de ejemplo
├── lanzar_demo.bat          # Script de demo para Windows (pendrive)
└── cheatsheet_parasito.html # Ficha ISA imprimible (A4, lista para plastificar)
```

---

## 🗺️ Arquitectura del motor (`parasito.py`)

```
parasito.despertar(archivo)
    │
    ├── [1] Extrae comentarios con tokenize
    │
    ├── [2] Separa palabras IMPARES (instrucciones) y PARES (pegamento)
    │
    ├── [3] FASE 1 — Pre-scan: registra etiquetas de salto (destino)
    │
    ├── [4] FASE 2 — Ejecución de la VM: bucle principal
    │       ├── guardar / archivar / recordar  → gestión de memoria
    │       ├── sumar / restar / multiplicar / dividir / unir → aritmética y texto
    │       ├── destino / saltar / revisar → control de flujo
    │       ├── mostrar / espacio / salto → salida
    │       └── secreto / infectar → capacidades de infección
    │
    └── [5] FASE 3 — Acróstico Fantasma: primera letra de cada palabra par
```

---

## 🎯 Conclusión

El mayor reto de **Parásito** no es la complejidad matemática, sino la **restricción lingüística humana**: programar aquí exige resolver un algoritmo de máquina mientras mantienes una cohesión gramatical impecable para el ojo humano.

Cada archivo es, simultáneamente, **un programa funcional**, **un programa esotérico** y **un mensaje secreto**. Tres realidades superpuestas en el mismo archivo de texto.