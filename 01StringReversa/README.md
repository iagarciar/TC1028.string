![Tec de Monterrey](../../images/logotecmty.png)
# String en reversa

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

#### Descripción
Escribir un programa en Python que lea un string y muestre como salida el string recibido escrito en reversa. La salida deberá comenzar con el último carácter y terminando con el primer carácter del string original, y ademas deberá transformar el texto a mayúsculas.

#### Entrada
Un string

#### Salida
El string de entrada escrito en reversa y en mayúsculas.

***Ejemplo 1:***

Entrada:
```
globo
```

Salida:
```
OBOLG
```

***Ejemplo 2:***

Entrada:
```
teNgO 7 AñOs
```

Salida:
```
SOÑA 7 OGNET
```

***Ejemplo 3:***

Entrada:
```
AMOR A ROMA
```

Salida:
```
AMOR A ROMA
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