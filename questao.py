
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a == 0:
    print("O coeficiente 'a' não pode ser igual a zero em uma equação do 2º grau.")
else:
    delta = b**2 - 4 * a * c

    print(f"\nDelta = {delta:.2f}")

    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais:")
        print(f"X1 = {raiz1:.2f}")
        print(f"X2 = {raiz2:.2f}")

    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma única raiz real (raízes iguais):")
        print(f"X = {raiz:.2f}")

    else:
        print("A equação não possui raízes reais (Delta negativo).")