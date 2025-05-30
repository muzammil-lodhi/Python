import click #to create a cli
import json #to save and load tasks from a file
import os #to check if the file exeist or not



TODO_FILE = "todo.json"  # Define the filename where tasks are stored


# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE):  # Check if file exists
        return []  # If not, return an empty list
    with open(TODO_FILE, "r") as file:  # Open the file in read mode
        return json.load(file)  # Load and return the JSON data as a Python list


# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:  # Open the file in write mode
        json.dump(tasks, file, indent=4)  # Save tasks as formatted JSON


@click.group()  # Define a Click command group (main CLI)
def cli():
      """Simple Todo List Manage"""  # Docstring for the CLI
      pass  # No action, acts as a container for commands


@click.command()  # Define a command called 'add'
@click.argument("task")  # Accepts a required argument (task name)
def add(task):
    """"Add a new task to the list"""
    tasks = load_tasks()  # Load existing tasks
    tasks.append({"task":task, "done":False})  # Append a new task (default: not done)
    save_tasks(tasks) # Save the updated tasks
    click.echo(f"task added successfully: (task)") # Print a success message
    
    
@click.command()  # Define a command called 'list'
def list():
    """List all the tasks"""
    tasks = load_tasks() # Load existing tasks
    if not tasks:   # If there are no tasks
        click.echo("no tasks found!")   # Print message
        return   # Stop execution
    for index,task in enumerate(tasks, 1):  # Loop through tasks with numbering
        status="✓" if task["done"] else "✗"  # Show '✓' for completed, '✗' for not
        click.echo(f"{index}. {task["task"]} [{status}]")  # Print task with status

        
@click.command() # Define a command called 'complete'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()  # Load existing tasks
    if 0 < task_number <= len(tasks): # Ensure task number is valid
        tasks[task_number - 1]["done"] = True  # Mark as done
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as complete") # Print success message
    else:
        click.echo(f"Invalid task number: {task_number}")  # Handle invalid numbers

@click.command()
@click.argument("task_number", type = int)
def  remove(task_number):
    """"Remove a task from the list"""
    tasks= load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task= tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task:{removed_task["task"]}")
    else:
        click.echo(f"Invalid task number")
 


         

        
        
        
    
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)
if __name__ == "__main__" :
    cli()
