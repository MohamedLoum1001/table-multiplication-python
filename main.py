def table_multiplication(n,  min=1, max=10):
    if min > max:
        print("Erreur : le min est supérieur au max")
        return
    for i in range(min, max+1):
        print(i, "x", n, "=", i*n)
    print("---Fin de la table de multiplication---")
table_multiplication(3 )