def smaller_addition(lista):
    if len(lista) == 0:
        raise ValueError("La lista esta vacia")

    if len(lista) == 1:
        return lista[0]

    processed = []
    max_element = lista[0]
    smaller_sum = None
    for num in lista:
        partial_sum = 0
        if num in processed:
            continue

        for other in lista:
            if other != num:
                partial_sum += other

        if smaller_sum == None:
            smaller_sum = partial_sum
            continue
        if partial_sum <= smaller_sum:
            if (num > max_element):
                max_element = num
            smaller_sum = partial_sum

        processed.append(num)
    return (max_element, smaller_sum)
