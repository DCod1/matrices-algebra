import numpy as np

def construir_matriz(clase, f, c):
    if clase == 'cuadrada':
        return np.random.randint(1, 10, size=(f, f))
    elif clase == 'rectangular':
        return np.random.randint(1, 10, size=(f, c))
    elif clase == 'diagonal':
        return np.diag(np.random.randint(1, 10, size=f))
    elif clase == 'triangular_superior':
        return np.triu(np.random.randint(1, 10, size=(f, c)))
    elif clase == 'triangular_inferior':
        return np.tril(np.random.randint(1, 10, size=(f, c)))
    elif clase == 'identidad':
        return np.eye(f)
    elif clase == 'nula':
        return np.zeros((f, c))
    elif clase == 'fila':
        return np.random.randint(1, 10, size=(1, c))
    elif clase == 'columna':
        return np.random.randint(1, 10, size=(f, 1))
    raise ValueError("Tipo de matriz inválido.")

def gauss_determinante(M):
    M = M.astype(float)
    n = len(M)
    for i in range(n):
        if M[i][i] == 0:
            return 0
        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n):
                M[j][k] -= factor * M[i][k]
    return np.prod(np.diag(M))

def obtener_inversa(M):
    n = len(M)
    A = M.astype(float)
    adjunta = np.zeros_like(A)
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            cofactor = gauss_determinante(minor)
            adjunta[j][i] = ((-1)**(i + j)) * cofactor
    det = gauss_determinante(A)
    if det == 0:
        return None
    return adjunta / det
