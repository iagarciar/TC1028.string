![Tec de Monterrey](../../images/logotecmty.png)

# Suma de rango

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

#### Descripción
En este ejercicio deberás leer varios numeros enteros, uno en cada linea hasta encontrar la palabra fin.

La estructura del programa es la siguiente:

El primer número es el limite inferior. [li] 
Los siguientes números (al menos un número) son limites superiores (cada uno de ellos es un limite superior) [ls_x] 
fin

El objetivo es sumar todos los números [enteros] entre el limite inferior y cada uno de los limites superiores. 

<b>Ejemplo de la estructura de la entrada y cada uno de los resultados:</b>
-2 [limite inferior]
4  [limite superior] [desde -2 hasta 4] = -2+-1+0+1+2+3+4 -> <b>7</b>
6 [limite superior] [desde -2 hasta 6 ] = -2+-1+0+1+2+3+4+5+6 -> <b>18</b>
1 [limite superior] [desde -2 hasta 1] = -2+-1+0+1 -> <b>-2</b>
fin
<b>En este caso la salida sería:</b>
[7, 18, -2]

#### Entrada
Un limite inferior (número entero)
Al menos un limite superior (número entero)
la palabra **fin** (string)

#### Salida
La salidas es una lista que contiene cada uno de los resultados. Cada resultado es la suma entre el limite inferior y cada uno de los limites superiores. 

***Ejemplo 1:***

Entrada:
```
-2
4
6
1
fin
```

Salida:
```
[7, 18, -2]
```

***Ejemplo 2:***

Entrada:
```
3
5
7
9
10
4
fin
```

Salida:
```
[12, 25, 42, 52, 7]
```

***Ejemplo 3:***

Entrada:
```
1
1
fin
```

Salida:
```
[1]
```

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

La salida del programa debe de ser exactamente de la siguiente forma:

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`pytest [nombre de la carpeta] -vv`, subela a tu repositorio en GitHub,
con el proceso de commit + push.