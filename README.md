# 🦠 Parásito: El Lenguaje de Programación Esteganográfico

> *"El código que ves hace una cosa; los comentarios que ignoras hacen otra, y el ruido blanco esconde un grito de auxilio."*

**Parásito** es un lenguaje de programación esotérico (esolang) conceptual que carece de sintaxis convencional. Vive como un parásito dentro del código fuente de un programa anfitrión (como Python). 

Mientras que el compilador del lenguaje anfitrión ignora los comentarios para ejecutar el código principal, **el intérprete de Parásito ignora el código principal y compila exclusivamente los comentarios.**

---

## 🧠 ¿Cómo funciona? La Regla de la Imparidad

Parásito se basa en la **esteganografía algorítmica**. El motor procesa los comentarios aplicando una regla de lectura estricta: **solo evalúa las palabras ubicadas en posiciones impares** (1ª, 3ª, 5ª...). 

Las palabras en posiciones pares se descartan computacionalmente. Su única función es actuar como "pegamento gramatical" para que el texto parezca una nota técnica corporativa.

### 🛠️ Sintaxis Completa (Turing Completo)
El lenguaje lee el texto palabra por palabra. Cualquier signo de puntuación (`, . : ! ?`) pegado a una palabra se limpia automáticamente para que puedas redactar sin romper el código.

* **Memoria:** 
  * `limpiar`: Resetea toda la memoria y la consola.
  * `guardar [X]`: Guarda el valor `X` en el acumulador.
  * `archivar [var]`: Guarda el acumulador en la variable `var`.
  * `recordar [var]`: Carga la variable `var` en el acumulador.
* **Aritmética y Texto:** 
  * `sumar [X]`: Suma matemáticamente `X` (o una variable) al acumulador.
  * `restar [X]`: Resta `X` al acumulador.
  * `unir [X]`: Concatena cadenas de texto.
* **Control de Flujo:** 
  * `destino [etiqueta]`: Crea un punto de anclaje invisible en el código.
  * `saltar [etiqueta]`: Salto incondicional al punto indicado.
  * `revisar [etiqueta]`: Salto condicional. **Solo salta** si el acumulador es mayor a `0`.
* **I/O:** 
  * `mostrar`: Imprime el acumulador.
  * `espacio`: Imprime un espacio `" "`.
  * `salto`: Imprime un salto de línea `\n`.

---

## 👻 Esteganografía Multinivel: "El Fantasma"

Dado que Parásito descarta por completo las palabras en posiciones pares, el lenguaje incorpora una tercera capa secreta para humanos.

A través del **Acróstico Par**, el programador puede usar la primera letra de cada palabra par descartada para enviar un mensaje directo, evadiendo la lógica computacional del lenguaje anfitrión y del propio Parásito.

### 🧩 Diseccionando un Bloque de Código
Imaginemos este comentario inocente: 
> *"Limpiar El guardar sistema 10 tiene sumar errores."*

Opera en tres dimensiones simultáneas:
1. **Capa Anfitrión:** Python ve un `#` e ignora todo.
2. **Capa Parásito:** Lee los impares -> `Limpiar` -> `guardar` -> `10` -> `sumar`. (El motor suma 10 al acumulador).
3. **Capa Fantasma:** Lee los pares -> **E**l, **s**istema, **t**iene, **e**rrores. (Mensaje: **ESTE**).

---

## 🎯 Conclusión

El mayor reto de **Parásito** no es la complejidad matemática, sino la **restricción lingüística humana**. Programar aquí requiere resolver un algoritmo de máquina mientras mantienes una cohesión gramatical impecable para el ojo humano. 

Es el único lenguaje donde una coma mal puesta o una falta de ortografía en un comentario puede causar un fallo crítico en el bucle lógico del sistema.