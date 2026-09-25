# 🦠 Parásito: El Lenguaje de Programación Esteganográfico

> *"El código que ves hace una cosa; los comentarios que ignoras hacen otra."*

**Parásito** es un lenguaje de programación esotérico (esolang) que carece de archivos ejecutables, entorno aislado o símbolos especiales. En su lugar, vive como un parásito oculto dentro del código fuente de un programa anfitrión (como Python, C++ o JavaScript).

El paradigma de este lenguaje invierte las reglas de la informática tradicional: mientras que el compilador del lenguaje anfitrión ignora los comentarios para ejecutar el código principal, **el intérprete de Parásito ignora el código principal y compila exclusivamente los comentarios.**

---

## 🧠 ¿Cómo funciona? La Regla de la Imparidad

Parásito se basa en la **esteganografía algorítmica**. Para que el programa funcione sin ser detectado en una revisión de código corporativa, el creador debe escribir comentarios que parezcan lenguaje natural y que aparentemente documenten el código anfitrión.

El motor de Parásito procesa los comentarios aplicando una única regla de lectura estricta: **solo evalúa las palabras ubicadas en posiciones impares** (1ª, 3ª, 5ª, etc.). Las palabras en posiciones pares se consideran "ruido blanco" y se ignoran; su única función es gramatical, sirviendo de pegamento para que la oración tenga sentido semántico para un lector humano.

---

## 🛠️ Sintaxis y Funcionalidades

Parásito es un lenguaje completo con memoria persistente, operaciones aritméticas y control de flujo, capaz de ejecutar bucles y saltos condicionales.

Todas las instrucciones requieren que la palabra clave caiga en una posición impar. El argumento de la instrucción será siempre la *siguiente* palabra impar.

### 1. Memoria y Variables
*   `guardar [dato]`: Sobrescribe la memoria volátil (el Acumulador) con el `[dato]` exacto.
*   `archivar [nombre]`: Guarda el valor actual del Acumulador en una variable persistente llamada `[nombre]`.
*   `recordar [nombre]`: Carga el valor de la variable `[nombre]` en el Acumulador.

### 2. Aritmética y Texto
*   `sumar [valor]`: Suma matemáticamente el `[valor]` (o el contenido de una variable) al Acumulador.
*   `restar [valor]`: Resta el `[valor]` al Acumulador.
*   `unir [valor]`: Concatena texto. (Ej: "Hola" + `unir Mundo` = "HolaMundo").

### 3. Control de Flujo (Saltos y Bucles)
*   `destino [etiqueta]`: Crea un punto de anclaje invisible en el código.
*   `saltar [etiqueta]`: Salto incondicional. El programa retrocede o avanza hasta el `destino` indicado.
*   `revisar [etiqueta]`: Salto condicional. **Solo** salta al destino si el valor numérico del Acumulador es **mayor que 0**.

### 4. Entrada y Salida (I/O)
*   `mostrar`: Imprime el contenido del Acumulador en consola.
*   `espacio`: Imprime un espacio en blanco.
*   `salto`: Imprime un salto de línea (`\n`).
*   `limpiar`: Borra el historial de la consola.

---

## 🎭 Estética: El Camuflaje Corporativo

Mientras otros lenguajes esotéricos buscan la belleza en formas visuales geométricas o en notas musicales, la estética de Parásito es puramente **literaria y psicológica**. 

El código más "bello" en Parásito es aquel que logra ejecutar un algoritmo complejo mientras el texto resultante parece un comentario técnico extremadamente aburrido que cualquier jefe o revisor de código aprobaría sin sospechar.

---

## 🚀 Ejemplo de Uso: Bucle de Cuenta Atrás

El flujo de trabajo se divide en dos capas. A continuación, vemos un script de red anfitrión (capa 1) cuyos comentarios esconden un bucle de cuenta atrás en Parásito (capa 2).

**Archivo: `conexion_red.py`**
```python
import parasito

def conectar_servidor():
    # Es necesario guardar el 3 inicial, para luego archivar el contador temporal.
    # El destino del bucle requiere siempre recordar el contador actual, 
    # para así mostrar datos. 
    # Añadir un espacio sirve para restar un 1 seguro.
    # Al archivar el contador modificado, podemos revisar el bucle nuevamente.
    # Al terminar, guardar el "Despegue" permite siempre mostrar progreso.
    
    print("Iniciando conexión HTTP al servidor...")
    # ... código real de conexión anfitrión ...

# La ejecución anfitriona fluye con normalidad
conectar_servidor()

# 🦠 Al final, el archivo despierta al parásito que lee sus propios comentarios
parasito.despertar(__file__)
