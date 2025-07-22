import itertools 
import random

POP_SIZE = 150
GENERATIONS = 500
MUTATION_RATE = 0.05
ELITISM_RATE = 0.1

PROFESSORES_DATA = [
    {"id": 1, "nome": "Prof. Alan Turing"},
    {"id": 2, "nome": "Prof. Marie Curie"},
    {"id": 3, "nome": "Prof. Isaac Newton"},
    {"id": 4, "nome": "Prof. Ada Lovelace"},
    {"id": 5, "nome": "Prof. Galileu Galilei"},
    {"id": 6, "nome": "Prof. Rosalind Franklin"},
    {"id": 7, "nome": "Prof. Stephen Hawking"},
    {"id": 8, "nome": "Prof. Simone de Beauvoir"},
    {"id": 9, "nome": "Prof. Carl Sagan"},
    {"id": 10, "nome": "Prof. Grace Hopper"}
]

DISCIPLINAS_DATA = [
    {"nome": "Algoritmos Avançados", "prof_id": 1},
    {"nome": "Inteligência Artificial", "prof_id": 1},
    {"nome": "Arquitetura de Computadores", "prof_id": 4},
    {"nome": "Sistemas Operacionais", "prof_id": 4},
    {"nome": "Compiladores", "prof_id": 10},
    {"nome": "Redes de Computadores", "prof_id": 10},
    {"nome": "Mecânica Quântica", "prof_id": 2},
    {"nome": "Física Clássica", "prof_id": 3},
    {"nome": "Termodinâmica", "prof_id": 5},
    {"nome": "Astrofísica", "prof_id": 7},
    {"nome": "Cosmologia", "prof_id": 7},
    {"nome": "Genética", "prof_id": 6},
    {"nome": "Radioatividade", "prof_id": 2},
    {"nome": "Filosofia Existencialista", "prof_id": 8},
    {"nome": "Lógica Filosófica", "prof_id": 8},
    {"nome": "Introdução à Astronomia", "prof_id": 9},
    {"nome": "Astrobiologia", "prof_id": 9},
    {"nome": "Cálculo Vetorial", "prof_id": 3},
    {"nome": "Álgebra Linear", "prof_id": 5},
    {"nome": "Equações Diferenciais", "prof_id": 3},
]

SALAS_DATA = [
    {"nome": f"Sala {i}"} for i in range(1, 9)
]

DIAS_SEMANA = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
TURNOS = ["Manhã", "Tarde", "Noite"]

HORARIOS_DATA = [
    {"dia": dia, "turno": turno}
    for dia, turno in itertools.product(DIAS_SEMANA, TURNOS)
]

ALUNOS_MATRICULAS_DATA = {
    f"Aluno_{i+1:02d}": random.sample([d['nome'] for d in DISCIPLINAS_DATA], k=random.randint(3, 5))
    for i in range(30)
}