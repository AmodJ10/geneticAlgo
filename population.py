import DNA
import random

population = []
totalPopulation = 100
mutationRate = 0

def setup(population,totalPopulation):
      
    mutationRate = 0.01
    
    for i in range(totalPopulation):
        population.append(DNA.DNA())

def draw():
    
    offsprings = []
    for i in range(totalPopulation):
            mother = population.getParent()
            father = population.getParent()

            while(mother == father):
                father = self.getParent()
            offspring1, offspring2 = self.getCrossover(mother,father)
            offsprings.append(offspring1)
            offsprings.append(offspring2)
        offsprings += self.individuals
        offsprings.sort(key = lambda x : x.getFitness(),reverse=False)
    
    for i in range(totalPopulation):
    
        a = random.randint(0,len(matingPool)-1)
        b = random.randint(0,len(matingPool)-1)    

        while b!=a:
            b = random.randint(0,len(matingPool)-1)    

        parentA = matingPool[a]
        parentB = matingPool[b]

        
        child = parentA.crossOver(parentB)
        child.mutate(mutationRate)
        
        population.append(child)
        
def getParent(self):
    if random.random() > 0.5:
        # Tournament Selection
        return population.tournamentSelection()
    else : 
        # Biased Random Selection
        return population.biasedRandomSelection()
    
def tournamentSelection(self):
        candidate1 = self.individuals[random.randint(0,self.population-1)]
        candidate2 = self.individuals[random.randint(0,self.population-1)]

        while(candidate1 == candidate2):
            candidate2 = self.individuals[random.randint(0,self.population-1)]
        
        if candidate1.getFitness() < candidate2.getFitness():
            return candidate1
        else:
            return candidate2
    
def biasedRandomSelection(self):
    fitnessSum = 0
    for i in self.individuals:
        fitnessSum += i.getFitness()
    proportions = [fitnessSum/i.getFitness() for i in self.individuals]
    proportionsSum = sum(proportions)
    normalizedProportions = [p/proportionsSum for p in proportions]

    cumulativeProportions = []
    cumulativeTotal = 0
    for np in normalizedProportions:
        cumulativeTotal += np
        cumulativeProportions.append(cumulativeTotal)

    selectedValue = random.random()

    for i in range(self.population):
        if selectedValue <= cumulativeProportions[i]:
            return self.individuals[i]
    return self.individuals[random.randint(0,self.population - 1)] # Redundan

        
setup(population,totalPopulation)

while True:
    fitness_array = [i.fitness for i in population]
    if max(fitness_array) >= 44:
        break
    else:
        print(population[fitness_array.index(max(fitness_array))])



