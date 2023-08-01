def first_fit_allocation(blocos_de_memoria, tamanho_necessario):
    """
    Simula o algoritmo de alocação de memória First-Fit.

    Parâmetros:
        blocos_de_memoria (lista): Lista contendo o tamanho dos blocos de memória disponíveis.
        tamanho_necessario (int): Tamanho necessário para alocar.

    Retorna:
        int: O índice do bloco alocado ou -1 se nenhum bloco adequado for encontrado.
    """
    for indice, tamanho_bloco in enumerate(blocos_de_memoria):
        if tamanho_bloco >= tamanho_necessario:
            blocos_de_memoria[indice] -= tamanho_necessario
            return indice

    return -1


# Exemplo de uso da função

blocos_de_memoria_lista = [100, 50, 200, 80, 150]
tamanho_bloco_necessario = 120

indice_alocacao = first_fit_allocation(blocos_de_memoria_lista, tamanho_bloco_necessario)
if indice_alocacao != -1:
    print(f"Bloco alocado no índice: {indice_alocacao}")
else:
    print("Nenhum bloco adequado encontrado para alocação.")
