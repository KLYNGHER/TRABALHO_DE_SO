
# 1. É definida uma classe Processo que representa cada tarefa com suas propriedades, como id, tempo_execucao e prioridade.
class Processo:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
# 2. A função escalona_prioridade_preemptiva é definida para receber uma lista de processos e simular o escalonamento por Prioridade Preemptiva. A função retorna o tempo_total_execucao e o tempo_medio_espera.
def escalona_prioridade_preemptiva(processos):
    tempo_total_execucao = 0
    tempo_espera_total = 0
    numero_processos = len(processos)
    processos_restantes = processos.copy()
# 3. A função inicia a execução em um loop enquanto existirem processos a serem executados (processos_restantes).
    while processos_restantes:
        proximo_processo = None

# 4. Em cada iteração do loop, é feito um loop pelos processos_restantes para encontrar o próximo processo a ser executado, com base na prioridade. O processo com menor prioridade (maior número) é escolhido como próximo a ser executado (proximo_processo).
        for processo in processos_restantes:
            if proximo_processo is None or processo.prioridade < proximo_processo.prioridade:
                proximo_processo = processo

# 5. O processo selecionado é removido da lista de processos restantes (processos_restantes) para evitar que ele seja escolhido novamente na mesma iteração.
        processos_restantes.remove(proximo_processo)

# 6. O processo selecionado é executado por 1 unidade de tempo (tempo_total_execucao += 1) e seu tempo de execução é decrementado em 1 (proximo_processo.tempo_execucao -= 1).
        tempo_total_execucao += 1
        proximo_processo.tempo_execucao -= 1

# 7. Em seguida, verifica-se se o processo ainda possui tempo de execução restante. Se possuir, ele é colocado de volta na lista de processos restantes (processos_restantes.append(proximo_processo)), para que possa ser reavaliado em futuras iterações.
        if proximo_processo.tempo_execucao > 0:
            # Caso possua, coloca o processo de volta na lista de processos restantes
            processos_restantes.append(proximo_processo)
        else:
# 8. Se o processo não tiver mais tempo de execução restante, significa que ele terminou a execução, então seu tempo de espera é calculado (tempo_espera_processo = tempo_total_execucao - proximo_processo.prioridade) e o valor é acumulado no tempo_espera_total
            tempo_espera_processo = tempo_total_execucao - proximo_processo.prioridade
            tempo_espera_total += tempo_espera_processo
# 9. O loop continua até que todos os processos tenham sido executados.
# 10. Finalmente, é calculado o tempo_medio_espera dividindo o tempo_espera_total pelo número de processos.
    tempo_medio_espera = tempo_espera_total / numero_processos
    return tempo_total_execucao, tempo_medio_espera


# Teste com outros processos
if __name__ == "__main__":
    # Lista de processos no formato (id, tempo_execucao, prioridade)
    processos = [
        Processo(1, 4, 2),
        Processo(2, 7, 1),
        Processo(3, 5, 2),
        Processo(4, 3, 3),
    ]

    # Chamada da função de escalonamento
    tempo_total, tempo_medio_espera = escalona_prioridade_preemptiva(processos)
    
# 10. Os resultados são impressos na tela, mostrando o tempo_total_execucao e o tempo_medio_espera após a simulação do escalonamento por Prioridade Preemptiva.
    print(f"\nTempo total de execução: {tempo_total}")
    print(f"Tempo médio de espera: {tempo_medio_espera:.2f} unidades de tempo")
