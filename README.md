# 🦠 Parásito: El Lenguaje de Programación Esteganográfico

> *"El código que ves hace una cosa; los comentarios que ignoras hacen otra."*

**Parásito** es un lenguaje de programación esotérico (esolang) conceptual que carece de sintaxis convencional, archivos ejecutables propios o un entorno aislado. En su lugar, vive como un parásito oculto dentro del código fuente de un programa anfitrión (como Python, C++ o JavaScript).

El paradigma de este lenguaje invierte las reglas tradicionales de la programación: mientras que el compilador del lenguaje anfitrión ignora los comentarios para ejecutar el código principal, **el intérprete de Parásito ignora el código principal y compila exclusivamente los comentarios.**

---

## 🧠 ¿Qué es y cómo funciona?

Parásito se basa en la **esteganografía algorítmica** (el arte de ocultar información dentro de otra información). Su objetivo principal no es la eficiencia, sino el camuflaje. 

Para que el programa parásito funcione sin ser detectado en una revisión de código (Code Review) o por otros programadores, el creador debe escribir comentarios que parezcan lenguaje natural y que aparentemente expliquen el código anfitrión.

El "secreto" del intérprete de Parásito radica en una regla de lectura estricta: **solo procesa las palabras ubicadas en posiciones impares** dentro de un bloque de comentarios. El resto de las palabras (las ubicadas en posiciones pares) se consideran "ruido blanco" y el intérprete las descarta por completo.

---

## 🛠️ Instrucciones Básicas

El lenguaje procesa el texto palabra por palabra. Si una palabra en posición impar coincide con una instrucción válida, la ejecuta. Si no coincide, simplemente la ignora. 

Las instrucciones fundamentales del lenguaje son:

*   `guardar`: Toma la *siguiente* palabra impar del comentario y la almacena en el registro de memoria.
*   `mostrar`: Imprime en la pantalla el contenido actual del registro de memoria.
*   `espacio`: Imprime un espacio en blanco (muy útil para formatear frases).

### Ejemplo conceptual de una inyección:

Imagina que un programador escribe este comentario inocente en su código:
> *"Al iniciar, guardar el Hola suele mostrar un mensaje, dejando espacio libre. Tras esto, guardar el Mundo nos permite luego mostrar datos."*

Si el intérprete de Parásito lee ese texto, extraerá solo las posiciones impares (1ª, 3ª, 5ª, etc.), revelando el verdadero programa oculto:

1. Al *(ignorado)*
3. **guardar** *(comando)*
5. **"Hola"** *(dato almacenado)*
7. **mostrar** *(comando)*
9. mensaje *(ignorado)*
11. **espacio** *(comando)*
13. Tras *(ignorado)*
15. **guardar** *(comando)*
17. **"Mundo"** *(dato almacenado)*
19. permite *(ignorado)*
21. **mostrar** *(comando)*

El resultado final en la consola será la frase **"Hola Mundo"**, generada a partir de un comentario aparentemente normal.

---

## 🚀 ¿Cómo se utiliza?

Para utilizar Parásito, el flujo de trabajo se divide en dos capas:

1. **La Capa del Anfitrión (El disfraz):** El programador escribe un script normal y corriente en Python (por ejemplo, una calculadora de impuestos o un algoritmo de ordenación). Este programa debe ser 100% funcional.
2. **La Capa del Parásito (La inyección):** El programador redacta los comentarios de su script midiendo cuidadosamente las palabras. Debe asegurarse de que las instrucciones de Parásito caigan exactamente en los saltos impares, usando las palabras pares para dar sentido gramatical a la oración.

Para ejecutarlo, hemos desarrollado una pequeña librería en Python. Esta librería utiliza herramientas de análisis léxico para "leerse a sí misma", extraer todos los comentarios del archivo que se está ejecutando, aplicar el filtro de palabras impares y ejecutar la lógica oculta, todo en tiempo real. 

El usuario solo tiene que ejecutar su programa anfitrión con normalidad y, al finalizar, la librería despertará al parásito para revelar su resultado en la consola.

---

## 🎯 El Desafío y Reflexión Final

El mayor reto al diseñar y programar en **Parásito** no es la complejidad computacional o matemática, sino la **restricción lingüística humana**. 

Escribir en Parásito requiere una dualidad mental profunda: debes resolver un problema lógico en el lenguaje anfitrión y, al mismo tiempo, resolver un problema literario y gramatical en los comentarios. El objetivo es que la oración tenga un sentido semántico perfecto para el ojo humano, pero oculte un algoritmo perfecto para la máquina.

Es un lenguaje donde el error de sintaxis no te lo da el compilador; te lo da tu compañero de trabajo cuando te pregunta: *"¿Por qué este comentario está redactado de forma tan extraña?"*.