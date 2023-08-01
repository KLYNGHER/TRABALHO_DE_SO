

# função que receberá como parâmetros bloco_memoria e taamanho_necessario

def best_fit_allocation(blocos_memoria, tamanho_necessario):
    indice_alocado = -1
    
#1. O código percorre a lista de blocos de memória disponíveis (`blocos_memoria`) usando um loop `for`.
#2. Para cada bloco de memória na lista, o código verifica se o tamanho do bloco é maior ou igual ao tamanho necessário (`tamanho_necessario`) pelo processo que precisa ser alocado

    for i, tamanho_bloco in enumerate(blocos_memoria):
        if tamanho_bloco >= tamanho_necessario:
            if indice_alocado == -1 or tamanho_bloco < blocos_memoria[indice_alocado]:
                indice_alocado = i
    
#4. Após percorrer todos os blocos, o código verifica se foi encontrado um bloco adequado para alocação (`indice_alocado != -1`). Se sim, subtrai o tamanho do bloco necessário do bloco selecionado (`blocos_memoria[indice_alocado] -= tamanho_necessario`), efetivamente alocando a memória para o processo. 
    if indice_alocado != -1:
        blocos_memoria[indice_alocado] -= tamanho_necessario
        return indice_alocado
    else:
        return -1

# 5. Se não for encontrado nenhum bloco adequado para alocação, a função retorna `-1`, indicando que não foi possível alocar o processo com o tamanho necessário.
if __name__ == "__main__":
    # Lista de blocos de memória disponíveis (tamanhos em bytes)
    blocos_memoria = [100, 50, 200, 80, 150]
    
    # Tamanho do bloco necessário (em bytes)
    tamanho_necessario = 70
    
#6. O exemplo de uso do código fornece uma lista de blocos de memória (`blocos_memoria`) e um tamanho necessário (`tamanho_necessario`). A função `best_fit_allocation` é chamada com esses valores, e o índice do bloco selecionado é armazenado na variável `indice_alocado`. Se o índice não for igual a `-1`, a alocação foi bem-sucedida, e é impressa uma mensagem informando qual bloco foi alocado. Caso contrário, é impressa uma mensagem informando que nenhum bloco adequado foi encontrado para alocar a memória.
    indice_alocado = best_fit_allocation(blocos_memoria, tamanho_necessario)
    
    if indice_alocado != -1:
        print(f"Bloco {indice_alocado} alocado para a memória.")
    else:
        print("Nenhum bloco adequado encontrado para alocar a memória.")
