# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        ["-2","2","4","6","fin"],
        ["","","","","", "[0, 7, 18]"],
        "Error en una de las 2 listas o en los números dentro de ellas"
    ),
    # Test case 2
    (
    ["5","10","15","20","fin"],
    ["","","","","","[45, 110, 200]"],
    ["Si son 3 limites superiores, debe tener 3 resultados. ¿Estan correctos los resultados?"]
    ),
    # Test case 3
    (
    ["-10","10","20","fin"],
    ["","","","","[0, 155]"],
    ["Si son 2 limites superiores, debe tener 2 resultados. ¿Estan correctos los resultados?"]
    ),
    # Test case 4
    (
    ["-101","1","fin"],
    ["","","","[-5150]"],
    ["Si es 1 limites superior, debe tener 1 resultado. ¿Esta correcto el resultado?"]
    ),
    # Test case 5
    (
    ["-5","-5","-5","fin"],
    ["","","","","[-5, -5]"],
    ["Si el limite superior e inferior son el mismo número, ¿tu resultado es correcto?"]
    )
]
