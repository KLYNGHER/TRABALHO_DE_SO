import threading

# Variáveis para armazenar o tamanho de cada processo e o resultado de cálculos
tamanho_processo1 = 0
tamanho_processo2 = 0
tamanho_processo3 = 0
calc = 0

# Função que representa o processo 1
def processo1():
    global tamanho_processo1
    global calc

    while True:
        tamanho_processo1 += 1
        calc = 2 * 2
        if tamanho_processo1 == 100000:
            break

# Função que representa o processo 2
def processo2():
    global tamanho_processo2
    global calc

    while True:
        tamanho_processo2 += 1
        calc = 2 * 2
        if tamanho_processo2 == 100000:
            break

# Função que representa o processo 3
def processo3():
    global tamanho_processo3
    global calc

    while True:
        tamanho_processo3 += 1
        calc = 2 * 2
        if tamanho_processo3 == 100000:
            break

# Função que implementa o escalonamento Round Robin
def round_robin_scheduler(processos, quantum):
    threads = []
    for processo in processos:
        thread = threading.Thread(target=processo, args=())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Cálculo do tempo total de execução e tempo médio de espera
    tempo_total_execucao = max(tamanho_processo1, tamanho_processo2, tamanho_processo3) * quantum
    tempo_medio_espera = (tempo_total_execucao - len(processos) * quantum) / len(processos)
    
    return tempo_total_execucao, tempo_medio_espera

if __name__ == "__main__":
    processos = [processo1, processo2, processo3]
    quantum = 0.001  # Você pode escolher qualquer valor para o quantum
    
    # Chamada da função de escalonamento e exibição dos resultados
    tempo_total, tempo_medio_espera = round_robin_scheduler(processos, quantum)
    print("Tempo total de execução:", round(tempo_total, 2))      
    print("Tempo médio de espera:", round(tempo_medio_espera, 2)) 
