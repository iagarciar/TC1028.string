# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["paracaidas","3"],
    ["","","par-aca-ida-s"],
    ["Revisa los guiones entre letras y que al final de la palabra no agregue guiones"]
    ),
    # Test case 2
    (
    ["elefante","4"],
    ["","","elef-ante"],
    ["Revisa los guiones entre letras y que al final de la palabra no agregue guiones"]
    ),
    # Test case 3
    (
    ["elefante","3"],
    ["","","ele-fan-te"],
    ["Revisa los guiones entre letras y que al final de la palabra no agregue guiones"]
    ),
    # Test case 4
    (
    ["mar","1"],
    ["","","m-a-r"],
    ["Revisa los guiones entre letras y que al final de la palabra no agregue guiones"]
    ),
    # Test case 5
    (
    ["elefante","-3"],
    ["","","ERROR!"],
    ["Revisa si el número es entero positivo"]
    )
]
