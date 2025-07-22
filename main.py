import config
import csv
from typing import List 
import matplotlib.pyplot as plt 

from domain.models import Professor, Disciplina, Sala, Horario, Cronograma
from genetic_algorithm.factory import CronogramaFactory
from genetic_algorithm.engine import AlgoritmoGenetico

def plot_convergence(fitness_history: List[int]):
    plt.figure(figsize=(12, 6))
    plt.plot(fitness_history, label='Melhor Fitness por Geração')
    plt.title('Convergência do Algoritmo Genético')
    plt.xlabel('Geração')
    plt.ylabel('Fitness')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    filename = "convergencia_fitness.png"
    plt.savefig(filename)
    print(f"Gráfico de convergência salvo como '{filename}'")

def export_to_csv(cronograma: Cronograma, filename: str = "cronograma.csv"):
    headers = ["Disciplina", "Professor", "Sala", "Dia", "Turno"]
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for aula in sorted(cronograma.aulas, key=lambda a: (config.DIAS_SEMANA.index(a.horario.dia), config.TURNOS.index(a.horario.turno))):
            writer.writerow([
                aula.disciplina.nome,
                aula.professor.nome,
                aula.sala.nome,
                aula.horario.dia,
                aula.horario.turno
            ])
    print(f"Cronograma exportado para '{filename}'")

def export_to_html(cronograma: Cronograma, all_horarios: List[Horario], filename: str = "cronograma.html"):
    html_head = """<html><head><title>Cronograma de Aulas</title><style>
    body { font-family: sans-serif; } table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ddd; text-align: left; padding: 8px; vertical-align: top; }
    th { background-color: #f2f2f2; } .aula { background-color: #e0f7fa; padding: 5px; margin-bottom: 5px; border-radius: 4px; font-size: 12px;}
    </style></head><body><h1>Cronograma de Aulas Otimizado</h1><table><tr><th>Horário</th>"""
    dias = config.DIAS_SEMANA
    turnos = config.TURNOS
    for dia in dias:
        html_head += f"<th>{dia}</th>"
    html_head += "</tr>"
    
    html_body = ""
    for turno in turnos:
        html_body += f"<tr><th>{turno}</th>"
        for dia in dias:
            html_body += "<td>"
            aulas_no_slot = [a for a in cronograma.aulas if a.horario.dia == dia and a.horario.turno == turno]
            for aula in aulas_no_slot:
                html_body += f"<div class='aula'><b>{aula.disciplina.nome}</b><br>{aula.professor.nome}<br><i>{aula.sala.nome}</i></div>"
            html_body += "</td>"
        html_body += "</tr>"

    html_foot = "</table></body></html>"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_head + html_body + html_foot)
    print(f"Cronograma exportado para '{filename}'")

def setup_domain_objects():
    professores = [Professor(**data) for data in config.PROFESSORES_DATA]
    disciplinas = [Disciplina(**data) for data in config.DISCIPLINAS_DATA]
    salas = [Sala(**data) for data in config.SALAS_DATA]
    horarios = [Horario(**data) for data in config.HORARIOS_DATA]
    disc_map = {d.nome: d for d in disciplinas}
    alunos_matriculas = {
        aluno: [disc_map[disc_nome] for disc_nome in disc_list]
        for aluno, disc_list in config.ALUNOS_MATRICULAS_DATA.items()
    }
    return professores, disciplinas, salas, horarios, alunos_matriculas

def main():
    print("1. Configurando o ambiente a partir do arquivo de configuração...")
    professores, disciplinas, salas, horarios, alunos_matriculas = setup_domain_objects()

    print("2. Inicializando a fábrica de cronogramas...")
    factory = CronogramaFactory(disciplinas, professores, salas, horarios, alunos_matriculas)

    print("3. Inicializando o motor do algoritmo genético...")
    ag = AlgoritmoGenetico(
        factory=factory,
        pop_size=config.POP_SIZE,
        generations=config.GENERATIONS,
        mutation_rate=config.MUTATION_RATE,
        elitism_rate=config.ELITISM_RATE
    )

    print("\n4. Iniciando a evolução...\n")
    melhor_solucao, fitness_history = ag.run()

    print("\n--- PÓS-PROCESSAMENTO ---")
    print("5. Gerando artefatos de saída...")
    plot_convergence(fitness_history)
    export_to_csv(melhor_solucao)
    export_to_html(melhor_solucao, horarios)

    print("\n--- MELHOR CRONOGRAMA ENCONTRADO (resumo no console) ---")
    aulas_ordenadas = sorted(melhor_solucao.aulas, key=lambda a: (config.DIAS_SEMANA.index(a.horario.dia), config.TURNOS.index(a.horario.turno)))
    for aula in aulas_ordenadas:
        print(f"  - {aula.disciplina.nome:<20} | {aula.professor.nome:<15} | "
              f"{aula.sala.nome:<10} | {aula.horario.dia}, {aula.horario.turno}")

if __name__ == "__main__":
    main()