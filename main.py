from scheduler import Scheduler  
from tasks import tasks  
  
def simulate_manufacturing_plant(tasks):  
    scheduler = Scheduler(tasks)  
    schedule = scheduler.schedule(algorithm="generate_and_test")  
    if schedule:  
     print("Schedule:", schedule)  
     print("Total processing time:", sum(task.processing_time for task in schedule))  
    else:  
     print("No schedule found")  
  
simulate_manufacturing_plant(tasks)