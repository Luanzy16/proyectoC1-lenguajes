# Analizador Léxico en Python

### Integrantes 

- Luis Sánchez
- David Bermudez
- Santiago Ospina

Este proyecto implementa un analizador léxico para el lenguaje Python sin utilizar librerías externas. El programa lee un archivo de código fuente `.py`, analiza los tokens y genera un archivo de salida `.txt` con la lista de tokens detectados. En caso de encontrar un error léxico, se aborta el análisis y se muestra un mensaje de error en la terminal.

## Requisitos
Este analizador está escrito en Python puro y no requiere ninguna biblioteca adicional.

## Cómo ejecutar el analizador

1. Guarda el código fuente del analizador en un archivo llamado `prueba.py`.
2. Coloca el archivo de código Python que deseas analizar en la misma carpeta que `prueba.py`.
3. Ejecuta el siguiente comando en la terminal:
   ```sh
   python3 prueba.py ejemplo.py
   ```
   Donde `ejemplo.py` es el código fuente a analizar.
4. Si el análisis es exitoso, se generará un archivo `nombre_tokens.txt` con la lista de tokens detectados.
5. Si se detecta un error léxico, el programa imprimirá un mensaje de error y finalizará la ejecución.

## Formato de salida

El programa genera un archivo `nombre_tokens.txt` con la siguiente estructura para cada token detectado:
```
<tipo_de_token,lexema,fila,columna>
```
- Para palabras reservadas: `<tipo_de_token,fila,columna>` (sin el lexema, ya que es igual al token).
- Para identificadores: `<id,lexema,fila,columna>`.
- Para cadenas: `<tk_cadena,lexema,fila,columna>`.
- Para números enteros: `<tk_entero,lexema,fila,columna>`.

Ejemplo de salida:
```
<id,x,1,1>
<tk_asignacion,1,3>
<tk_entero,10,1,5>
<id,y,2,1>
<tk_asignacion,2,3>
<tk_entero,20,2,5>
```

## Explicación del código

1. **Lectura del archivo de entrada**: El programa abre el archivo especificado y lee su contenido línea por línea.
2. **Procesamiento de caracteres**: Se recorren los caracteres para identificar tokens válidos.
3. **Clasificación de tokens**:
   - Identificadores y palabras reservadas.
   - Números enteros (con o sin signo).
   - Cadenas de texto delimitadas por comillas.
   - Operadores y símbolos especiales.
4. **Manejo de errores léxicos**:
   - Si se encuentra un carácter o secuencia no reconocida, se imprime el error y se detiene el análisis.
5. **Generación del archivo de salida**: Si no hay errores, se escribe la lista de tokens en `tokens.txt`.

## Ejemplo de error léxico

Entrada (`archivo.py`):
```python
x = 10
y = 20
z = x &@ y 
print(z)
```

Salida en la terminal:
```
>>> Error léxico(linea:3,posicion:7)
```

El programa detecta `&@` como un error léxico, lo reporta y finaliza la ejecución inmediatamente.

