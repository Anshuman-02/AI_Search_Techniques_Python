class Task:  
    def __init__(self, processing_time, deadline):  
        self.processing_time = processing_time  
        self.deadline = deadline  
  
    def __repr__(self):  
        return f"Task(processing_time={self.processing_time}, deadline={self.deadline})"  
  
# Define some example tasks  
tasks = [  
    Task(10, 20),  
    Task(5, 15),  
    Task(8, 18),  
    Task(12, 22),  
    Task(15, 25),  
    Task(20, 30),  
]