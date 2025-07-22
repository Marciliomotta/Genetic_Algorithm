import config
import matplotlib.pyplot as plt 

from domain.models import Professor, Disciplina, Sala, Horario, Cronograma
from genetic_algorithm.factory import CronogramaFactory
from genetic_algorithm.engine import AlgoritmoGenetico
from graphic import export_to_csv, plot_convergence

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
    print("\n--- INICIALIZAÇÃO ---")
    professores, disciplinas, salas, horarios, alunos_matriculas = setup_domain_objects()
    factory = CronogramaFactory(disciplinas, professores, salas, horarios, alunos_matriculas)
    ag = AlgoritmoGenetico(
        factory=factory,
        pop_size=config.POP_SIZE,
        generations=config.GENERATIONS,
        mutation_rate=config.MUTATION_RATE,
        elitism_rate=config.ELITISM_RATE
    )
    print("\n--- EXECUÇÃO DO ALGORITMO GENÉTICO ---")
    melhor_solucao, fitness_history = ag.run()

    print("\n--- PÓS-PROCESSAMENTO ---")
    plot_convergence(fitness_history) 
    export_to_csv(melhor_solucao)

    print("\n--- MELHOR CRONOGRAMA ENCONTRADO ---")
    for aula in sorted(melhor_solucao.aulas, key=lambda a: (config.DIAS_SEMANA.index(a.horario.dia), config.TURNOS.index(a.horario.turno))):
        print(f"  - {aula.disciplina.nome:<25} | {aula.professor.nome:<25} | "
              f"{aula.sala.nome:<15} | {aula.horario.dia}, {aula.horario.turno}")

if __name__ == "__main__":
    main()