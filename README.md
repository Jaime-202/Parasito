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

## 🧪 Demostraciones Prácticas (Ejemplos)

El proyecto incluye 3 archivos de prueba completos que demuestran todas las capacidades de Parásito:

### 📄 [`prueba1.py`](./prueba1.py) — Infiltración en Código Anfitrión Inocente
* **Qué hace**: Simula un script Python normal de autenticación de usuarios. En los comentarios del módulo se oculta un programa en Parásito que concatena datos corporativos, genera un archivo secreto infiltrado (`.parasito_secret.txt`) y transmite la palabra acróstica `SECRET` en las posiciones pares.

### 📄 [`prueba2.py`](./prueba2.py) — Infección Automática de Repositorios
* **Qué hace**: Crea una estructura de repositorio (`mi_repositorio_objetivo`) con múltiples módulos Python (`modulo_pago.py`, `servicio_email.py`). Utiliza `parasito.infectar_repositorio()` para escanear e inyectar de forma imperceptible los comentarios esteganográficos en todos los scripts `.py`. Al ejecutar cualquiera de los scripts del repositorio, la lógica original de Python funciona normalmente mientras el Parásito se activa en segundo plano.

### 📄 [`prueba3.py`](./prueba3.py) — Bucle Condicional Turing-Completo y Sinónimos Técnicos
* **Qué hace**: Demuestra la potencia lógica del lenguaje realizando un **bucle de cuenta regresiva (`3, 2, 1`)** utilizando control de flujo condicional (`nodo`, `evaluar`, `sustraer`, `recordar`, `expresar`) y el diccionario extendido de sinónimos técnicos en español.

---

## 🚀 Cómo Ejecutar los Ejemplos

Puedes ejecutar cualquiera de las pruebas desde la terminal:

```bash
python prueba1.py
python prueba2.py
python prueba3.py
```

---

## 🎯 Conclusión

El mayor reto de **Parásito** no es la complejidad matemática, sino la **restricción lingüística humana**. Programar aquí requiere resolver un algoritmo de máquina mientras mantienes una cohesión gramatical impecable para el ojo humano.