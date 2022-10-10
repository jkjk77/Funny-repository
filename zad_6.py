def fun6(list1: list, list2: list) -> list:
    nowa_lista = list1 + list2
    nowa_lista = list(dict.fromkeys(nowa_lista))
    nowa_lista = [num**3 for num in nowa_lista]
    return nowa_lista
    
lista1 = [1, 2, 5, 6]
lista2 = [2, 5, 1]

print(fun6(lista1, lista2))