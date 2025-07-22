import random
from typing import List, Dict
from domain.models import Cronograma, Aula, Disciplina, Professor, Sala, Horario

class CronogramaFactory:
    def __init__(self, disciplinas: List[Disciplina], professores: List[Professor],
                 salas: List[Sala], horarios: List[Horario],
                 alunos_matriculas: Dict[str, List[Disciplina]]):
        self.disciplinas = disciplinas
        self.professores = professores
        self.salas = salas
        self.horarios = horarios
        self.alunos_matriculas = alunos_matriculas
        self._prof_map = {p.id: p for p in professores}

    def criar_aleatorio(self) -> Cronograma:
        aulas = []
        for disciplina in self.disciplinas:
            professor = self._prof_map[disciplina.prof_id]
            sala = random.choice(self.salas)
            horario = random.choice(self.horarios)
            aulas.append(Aula(disciplina, professor, sala, horario))
        
        return Cronograma(aulas, self.alunos_matriculas)