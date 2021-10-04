![Tec de Monterrey](../../images/logotecmty.png)
# Separa con Guiones

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

#### Descripción
Escribe un programa que reciba un string y un número entero positivo, el programa crea una nueva cadena con la cadena original pero dividida con guiones en cada intervalo del número recibido y la imprime a pantalla. Si recibe un número negativo o 0, deberá imprimir el mensaje: "ERROR!".

#### Entrada
Primera linea: un string
Segunda linea: un número entero

#### Salida
Un string con los guiones marcados

***Ejemplo 1:***

Entrada:
```
Paracaidas
3
```

Salida:
```
Par-aca-ida-s
```

***Ejemplo 2:***

Entrada:
```
elefante
4
```

Salida:
```
elef-ante
```

***Ejemplo 3:***

Entrada:
```
cosa
4
```

Salida:
```
cosa
```

***Ejemplo 4:***

Entrada:
```
azul
1
```

Salida:
```
a-z-u-l
```

***Ejemplo 5:***

Entrada:
```
elote
-2
```

Salida:
```
ERROR!
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