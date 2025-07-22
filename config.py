import itertools 

POP_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.05
ELITISM_RATE = 0.1

PROFESSORES_DATA = [
    {"id": 1, "nome": "Prof. João"},
    {"id": 2, "nome": "Prof. Maria"},
    {"id": 3, "nome": "Prof. Pedro"}
]

DISCIPLINAS_DATA = [
    {"nome": "Cálculo", "prof_id": 1},
    {"nome": "IA", "prof_id": 2},
    {"nome": "Estrutura de Dados", "prof_id": 3},
    {"nome": "Programação", "prof_id": 3}
]

SALAS_DATA = [
    {"nome": "Sala 101"},
    {"nome": "Sala 102"}
]

DIAS_SEMANA = ["Seg", "Ter", "Qua", "Qui", "Sex"]
TURNOS = ["Manhã", "Tarde", "Noite"]

HORARIOS_DATA = [
    {"dia": dia, "turno": turno}
    for dia, turno in itertools.product(DIAS_SEMANA, TURNOS)
]

ALUNOS_MATRICULAS_DATA = {
    "Ana": ["Cálculo", "IA"],
    "Beto": ["IA", "Programação"],
    "Carla": ["Cálculo", "Estrutura de Dados"],
    "Daniel": ["Estrutura de Dados", "Programação"]
}