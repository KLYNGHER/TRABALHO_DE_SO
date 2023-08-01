class Processo:
    def __init__(self, pid, tempo_execucao, prioridade):
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade

def escalonamento_por_prioridade(processos):
    tempo_total_execucao = 0
    tempo_espera_total = 0
    n = len(processos)

    # Ordenar os processos pela prioridade, sendo 0 a mais alta prioridade
    processos.sort(key=lambda x: x.prioridade)

    for i, processo in enumerate(processos):
        tempo_total_execucao += processo.tempo_execucao
        tempo_espera_total += (tempo_total_execucao - processo.tempo_execucao)

    tempo_medio_espera = tempo_espera_total / n

    return tempo_total_execucao, tempo_medio_espera

if __name__ == "__main__":
    # Criação dos processos (ID do Processo, Tempo de Execução, Prioridade)
    processos = [
        Processo(1, 10, 2),
        Processo(2, 6, 1),
        Processo(3, 8, 3),
        Processo(4, 3, 4),
    ]

    tempo_total_execucao, tempo_medio_espera = escalonamento_por_prioridade(processos)

    print(f"Tempo total de execução: {tempo_total_execucao}")
    print(f"Tempo médio de espera: {tempo_medio_espera}")
