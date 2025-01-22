from generate_and_test import generate_and_test  
from hill_climbing import hill_climbing  
  
class Scheduler:  
    def __init__(self, tasks):  
     self.tasks = tasks  
  
    def schedule(self, algorithm="generate_and_test"):  
     if algorithm == "generate_and_test":  
        return generate_and_test(self.tasks)  
     elif algorithm == "hill_climbing":  
        return hill_climbing(self.tasks)  
     else:  
        raise ValueError("Invalid algorithm")
