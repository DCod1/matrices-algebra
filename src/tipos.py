def describir_metodo(modo):
    pasos = {
        "cuadrada": [
            "1. Se aplica el método de eliminación de Gauss para llevar la matriz a forma triangular superior.",
            "2. El determinante se calcula como el producto de los elementos en la diagonal principal.",
            "3. Se obtiene la matriz de cofactores.",
            "4. Se halla la inversa aplicando $A^{-1} = \\frac{\\operatorname{adj}(A)}{\\det(A)}$."
        ],
        "rectangular": [
            "No es posible obtener el determinante de una matriz no cuadrada."
        ],
        "diagonal": [
            "1. Se confirma que la matriz es cuadrada.",
            "2. El determinante se obtiene multiplicando los valores de la diagonal."
        ],
        "triangular_superior": [
            "1. Se verifica que la matriz sea cuadrada.",
            "2. El determinante es el producto de la diagonal principal."
        ],
        "triangular_inferior": [
            "1. Se verifica que la matriz sea cuadrada.",
            "2. El determinante es el producto de la diagonal principal."
        ],
        "identidad": [
            "El determinante de una matriz identidad siempre es $1$."
        ],
        "nula": [
            "El determinante de una matriz nula es $0$."
        ],
        "fila": [
            "No se puede calcular el determinante para una matriz fila."
        ],
        "columna": [
            "No se puede calcular el determinante para una matriz columna."
        ]
    }
    return pasos.get(modo, [])
