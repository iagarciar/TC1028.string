![Tec de Monterrey](../../images/logotecmty.png)
# Palíndromo

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

#### Descripción
Desarrolla un programa en Python que contenga una función que identifique si una palabra es un palíndromo o no.
"Un palíndromo (del griego palin dromein, volver a ir atrás), es una palabra, o frase que se lee igual adelante que atrás." (https://es.wikipedia.org/wiki/Pal%C3%ADndromo).
Los palíndromos en este ejercicios podrán contener, mayusculas, minusculas y espacios.


#### Entrada
Un string.

#### Salida
Un string, si es o no es palíndromo. 

***Ejemplo 1:***

Entrada:
```
anitalavalatina
```

Salida:
```
es un palíndromo
```

***Ejemplo 2:***

Entrada:
```
Anita lava la tina
```

Salida:
```
es un palíndromo
```

***Ejemplo 3:***

Entrada:
```
cosa
```

Salida:
```
no es un palíndromo
```

***Ejemplo 4:***

Entrada:
```
Amor a Roma
```

Salida:
```
es un palíndromo
```

***Ejemplo 5:***

Entrada:
```
filosofo filoso
```

Salida:
```
no es un palíndromo
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