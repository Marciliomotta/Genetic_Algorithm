import random
from typing import Tuple, List 
from domain.models import Cronograma
from .factory import CronogramaFactory

class AlgoritmoGenetico:
    def __init__(self, factory: CronogramaFactory, pop_size: int, generations: int, 
                 mutation_rate: float, elitism_rate: float):
        self.factory = factory
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate
        self.population = []
        self.fitness_history = [] 

    def _inicializar_populacao(self):
        self.population = [self.factory.criar_aleatorio() for _ in range(self.pop_size)]

    def _selecionar_pais(self) -> Tuple[Cronograma, Cronograma]:
        torneio = random.sample(self.population, k=5)
        pai1 = max(torneio, key=lambda ind: ind.fitness)
        torneio = random.sample(self.population, k=5)
        pai2 = max(torneio, key=lambda ind: ind.fitness)
        return pai1, pai2

    def _crossover(self, pai1: Cronograma, pai2: Cronograma) -> Cronograma:
        ponto_corte = random.randint(1, len(pai1.aulas) - 1)
        aulas_filho = pai1.aulas[:ponto_corte] + pai2.aulas[ponto_corte:]
        return Cronograma(aulas_filho, self.factory.alunos_matriculas)

    def _mutacao(self, individuo: Cronograma) -> Cronograma:
        aulas_mutadas = []
        for aula in individuo.aulas:
            if random.random() < self.mutation_rate:
                nova_aula = individuo.aulas[0].__class__(
                    disciplina=aula.disciplina, professor=aula.professor,
                    sala=random.choice(self.factory.salas),
                    horario=random.choice(self.factory.horarios)
                )
                aulas_mutadas.append(nova_aula)
            else:
                aulas_mutadas.append(aula)
        return Cronograma(aulas_mutadas, self.factory.alunos_matriculas)

    def run(self) -> Tuple[Cronograma, List[int]]:
        self._inicializar_populacao()

        for geracao in range(self.generations):
            self.population.sort(key=lambda ind: ind.fitness, reverse=True)
            
            melhor_fitness = self.population[0].fitness
            self.fitness_history.append(melhor_fitness) 
            print(f"Geração {geracao + 1}/{self.generations} | Melhor Fitness: {melhor_fitness}")

            if melhor_fitness == 0:
                print("\nSolução ótima encontrada!")
                break
            
            nova_populacao = []
            num_elite = int(self.pop_size * self.elitism_rate)
            nova_populacao.extend(self.population[:num_elite])
            
            while len(nova_populacao) < self.pop_size:
                pai1, pai2 = self._selecionar_pais()
                filho = self._crossover(pai1, pai2)
                filho_mutado = self._mutacao(filho)
                nova_populacao.append(filho_mutado)
            
            self.population = nova_populacao
        
        return self.population[0], self.fitness_history