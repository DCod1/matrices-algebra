from generador import construir_matriz, gauss_determinante, obtener_inversa
from tipos import describir_metodo
from pylatex import Document, Section, Subsection, Math, Matrix, NewLine
import os


def crear_directorio_salida():
    os.makedirs('salida/pdf', exist_ok=True)
    os.makedirs('salida/tex', exist_ok=True)


def interfaz_usuario():
    opciones = [
        "cuadrada", "rectangular", "diagonal", "triangular_superior",
        "triangular_inferior", "identidad", "nula", "fila", "columna"
    ]
    for idx, tipo in enumerate(opciones, start=1):
        print(f"{idx}. {tipo.replace('_', ' ').title()}")
    try:
        sel = int(input("Elige el tipo de matriz (1-9): "))
        if not 1 <= sel <= 9:
            raise ValueError
    except ValueError:
        print("Entrada no válida.")
        return None, None, None

    tipo = opciones[sel - 1]
    dims = input("Tamaño de la matriz (formato filas*columnas): ")
    try:
        f, c = map(int, dims.strip().split('*'))
    except:
        print("Formato inválido.")
        return None, None, None
    return tipo, f, c


def exportar_documento_latex(matriz, det, inversa, tipo):
    doc = Document()
    
    with doc.create(Section("Análisis de matriz")):
        doc.append(f"Tipo de matriz: {tipo.replace('_', ' ').title()}")
        doc.append(NewLine())

        doc.append("Matriz generada:")
        with doc.create(Math()) as math:
            math.append(Matrix(matriz))
        doc.append(NewLine())

        pasos = describir_metodo(tipo)
        if pasos:
            with doc.create(Subsection("Pasos del método")):
                for paso in pasos:
                    doc.append(f"{paso}\n")

        if det is not None:
            with doc.create(Subsection("Determinante")):
                doc.append(f"Determinante: {det:.2f}")

        if inversa is not None:
            with doc.create(Subsection("Matriz inversa")):
                with doc.create(Math()) as math:
                    math.append(Matrix(inversa))


    doc.generate_tex('salida/tex/resultado')
    doc.generate_pdf('salida/pdf/resultado', clean_tex=False, compiler='pdflatex')



if __name__ == "__main__":
    crear_directorio_salida()
    
    tipo, filas, columnas = interfaz_usuario()
    if tipo is None:
        exit()

    matriz = construir_matriz(tipo, filas, columnas)

    # Determinante e inversa si es cuadrada
    if filas == columnas:
        determinante = gauss_determinante(matriz)
        inversa = obtener_inversa(matriz)
    else:
        determinante = None
        inversa = None

    exportar_documento_latex(matriz, determinante, inversa, tipo)

    print("Cálculo finalizado.")
    print("Documento LaTeX exportado a carpeta salida.")
