#entradas
def resolver_ecuacion_segundo_grado(A, B, C):
#caja negra
    D = B**2 - 4*A*C
    if D > 0:
        X1 = (-B + math.sqrt(D)) / (2 * A)
        X2 = (-B - math.sqrt(D)) / (2 * A)
        return f"Dos soluciones reales: X1 = {X1}, X2 = {X2}"
    elif D == 0:
        X1 = -B / (2 * A)
        return f"Una solución real: X1 = X2 = {X1}"
    else:
        return "No tiene solución en los números reales"
