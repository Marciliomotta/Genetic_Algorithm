from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import csv
from config import DIAS_SEMANA, TURNOS
from domain.models import Cronograma 

def plot_convergence(fitness_history: List[int]):
    plt.figure(figsize=(12, 6))
    plt.plot(fitness_history, label='Melhor Fitness por Geração')
    plt.title('Convergência do Algoritmo Genético')
    plt.xlabel('Geração')
    plt.ylabel('Fitness')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show() 

def export_to_csv(cronograma: Cronograma, filename: str = "cronograma.csv"):
    headers = ["Disciplina", "Professor", "Sala", "Dia", "Turno"]
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for aula in sorted(cronograma.aulas, key=lambda a: (DIAS_SEMANA.index(a.horario.dia), TURNOS.index(a.horario.turno))):
            writer.writerow([aula.disciplina.nome, aula.professor.nome, aula.sala.nome, aula.horario.dia, aula.horario.turno])
    print(f"Cronograma exportado para '{filename}'")