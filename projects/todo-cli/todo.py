# uv init folder name jo create krna hai!
# uv add click to create virtual environment
# activating scripts .venv\Scripts\activate

import click # to create CLI
import os # to check if file exists
import json # to read and write json file

TODO_FILE = "todo.json"

def load_task():
    if os.path.exists(TODO_FILE):
        return[]
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    

def save_tasks (tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@click.group()
def cli():
    """Simple CLI for managing your todo tasks"""
    pass

@click.command()
@click.argument("task")
def add (task):
    """add new task to the list"""
    tasks = load_task()
    tasks.append({"task":task, "done":False})
    save_tasks(tasks)
    click.echo(f"task added successfuly {task}")



@click.command()
def list():
    """list all the tasks"""
    tasks = load_task()
    if not tasks:
        click.echo("No tasks found!")
        return
    for index, task in enumerate(tasks, 1):
        status = "✔" if task ["done"] else "❌"
        click.echo (f"{index}, {task["task"]}, [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete (task_number):
    """mark the task as completed"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1 ]["done"] = True
        save_tasks(tasks)
        click.echo(f"task {task_number} marked as completed!")
    else:
        click.echo(f"invalid {task_number}!")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """remove the task from the list"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"removed task {removed_task['task']}")
    else:
        click.echo("invalid task number")



cli.add_command(add)
cli.add_command(list)
cli.command(complete)
cli.command(remove)

if __name__== "__main__":
    cli()
