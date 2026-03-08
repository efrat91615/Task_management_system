
tasks = []

def get_tasks():
    """
    Returns the list of all current tasks.
    """
    return tasks
def add_task(title: str, description: str, task_type: str, start_date: str, end_date: str, status: str):
    """Adds a new task to the system."""
    new_id = len(tasks) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "type": task_type,
        "start_date": start_date,
        "end_date": end_date,
        "status": status
    }
    tasks.append(new_task)
    return f"Success: Task '{title}' added."

def update_task_status(task_id: int, status: str):
    """Updates the status of a task."""
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            return f"Task {task_id} status updated to '{status}'."
    return "Task not found."

def delete_task(task_id: int):
    """Deletes a task by ID."""
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            return f"Task {task_id} deleted."
    return "Task not found."
