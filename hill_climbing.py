import random  
  
def hill_climbing(tasks, max_iterations=1000):  
    """  
    Hill Climbing algorithm to schedule tasks.  
  
    Args:  
        tasks (list): A list of tasks to schedule.  
        max_iterations (int, optional): Maximum number of iterations to perform. Defaults to 1000.  
  
    Returns:  
        schedule (list): A list of tasks in the order they should be scheduled, or None if no schedule is found.  
    """  
    current_schedule = generate_initial_schedule(tasks)  
    current_score = evaluate_schedule(current_schedule, tasks)  
  
    for _ in range(max_iterations):  
        neighbor = generate_neighbor(current_schedule)  
        neighbor_score = evaluate_schedule(neighbor, tasks)  
  
        if neighbor_score < current_score:  
            current_schedule = neighbor  
            current_score = neighbor_score  
  
    return current_schedule  
  
def generate_initial_schedule(tasks):  
    """  
    Generate an initial schedule for the tasks.  
  
    Args:  
        tasks (list): A list of tasks to schedule.  
  
    Returns:  
        schedule (list): A list of tasks in a random order.  
    """  
    random.shuffle(tasks)  
    return tasks  
  
def generate_neighbor(schedule):  
    """  
    Generate a neighbor of the current schedule.  
  
    Args:  
        schedule (list): A list of tasks in the order they should be scheduled.  
  
    Returns:  
        neighbor (list): A list of tasks in a new order.  
    """  
    i, j = random.sample(range(len(schedule)), 2)  
    schedule[i], schedule[j] = schedule[j], schedule[i]  
    return schedule  
  
def evaluate_schedule(schedule, tasks):  
    """  
    Evaluate the quality of a schedule.  
  
    Args:  
        schedule (list): A list of tasks in the order they should be scheduled.  
        tasks (list): A list of tasks to schedule.  
  
    Returns:  
        score (int): The total processing time of the schedule.  
    """  
    current_time = 0  
    score = 0  
    for task in schedule:  
        if current_time + task.processing_time > task.deadline:  
            score += 1000  # penalty for missing deadline  
        current_time += task.processing_time  
        score += task.processing_time  
    return score
