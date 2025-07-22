from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class Horario:
    dia: str
    turno: str

@dataclass(frozen=True)
class Sala:
    nome: str

@dataclass(frozen=True)
class Professor:
    id: int
    nome: str

@dataclass(frozen=True)
class Disciplina:
    nome: str
    prof_id: int

@dataclass
class Aula:
    disciplina: Disciplina
    professor: Professor
    sala: Sala
    horario: Horario

class Cronograma:
    def __init__(self, aulas: List[Aula], alunos_matriculas: Dict[str, List[Disciplina]]):
        self.aulas = aulas
        self._alunos_matriculas = alunos_matriculas
        self._fitness = None

    @property
    def fitness(self) -> int:
        if self._fitness is None:
            self._fitness = self._calcular_fitness()
        return self._fitness

    def _calcular_fitness(self) -> int:
        penalidades = self._calcular_conflitos_recursos() + self._calcular_conflitos_alunos()
        return -penalidades

    def _calcular_conflitos_recursos(self) -> int:
        penalidades = 0
        horarios_ocupados = {}
        for aula in self.aulas:
            chave_prof = ("PROF", aula.professor.id, aula.horario)
            if chave_prof in horarios_ocupados: penalidades += 1000
            else: horarios_ocupados[chave_prof] = True
            chave_sala = ("SALA", aula.sala.nome, aula.horario)
            if chave_sala in horarios_ocupados: penalidades += 1000
            else: horarios_ocupados[chave_sala] = True
        return penalidades

    def _calcular_conflitos_alunos(self) -> int:
        penalidades = 0
        horarios_alunos = {}
        for aluno_nome, disciplinas_aluno in self._alunos_matriculas.items():
            disciplinas_aluno_nomes = [d.nome for d in disciplinas_aluno]
            for aula in self.aulas:
                if aula.disciplina.nome in disciplinas_aluno_nomes:
                    chave_aluno = (aluno_nome, aula.horario)
                    if chave_aluno in horarios_alunos: penalidades += 1000
                    else: horarios_alunos[chave_aluno] = True
        return penalidades
    
    def __repr__(self):
        return f"Cronograma(fitness={self.fitness})"