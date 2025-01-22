import random  
  
def generate_and_test(tasks, max_attempts=1000):  
    """  
    Generate-And-Test algorithm to schedule tasks.  
  
    Args:  
        tasks (list): A list of tasks to schedule.  
        max_attempts (int, optional): Maximum number of attempts to generate a schedule. Defaults to 1000.  
  
    Returns:  
        schedule (list): A list of tasks in the order they should be scheduled, or None if no schedule is found.  
    """  
    for _ in range(max_attempts):  
        schedule = generate_schedule(tasks)  
        if is_valid_schedule(schedule, tasks):  
            return schedule  
    return None  
  
def generate_schedule(tasks):  
    """  
    Generate a random schedule for the tasks.  
  
    Args:  
        tasks (list): A list of tasks to schedule.  
  
    Returns:  
        schedule (list): A list of tasks in a random order.  
    """  
    random.shuffle(tasks)  
    return tasks  
  
def is_valid_schedule(schedule, tasks):  
    """  
    Check if a schedule is valid.  
  
    Args:  
        schedule (list): A list of tasks in the order they should be scheduled.  
        tasks (list): A list of tasks to schedule.  
  
    Returns:  
        bool: True if the schedule is valid, False otherwise.  
    """  
    current_time = 0  
    for task in schedule:  
        if current_time + task.processing_time > task.deadline:  
            return False  
        current_time += task.processing_time  
    return True
