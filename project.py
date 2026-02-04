import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

EXERCISES = {
    "caminhada": 2.0,
    "caminhada rapida" : 5.0,
    "caminhada em trilha": 6.0,
    "corrida": 8.3,
    "corrida rapida": 11.5,
    "ciclismo": 4.0,
    "ciclismo moderado": 6.8,
    "ginastica": 2.5,
    "calistenia": 3.5,
    "musculacao": 6.0,
    "circuito": 8.0,
    "natacao": 5.8,
    "corda": 8.0,
    "escadas": 4.0,
}

def main():
    clear_screen()
    console = Console()

    console.print(Panel.fit("MET Calculator", style="bold black on cyan"))
    table = Table(title="Exercise List")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="green")        
    for i, exercise in enumerate(EXERCISES.keys(), start=1):        
        table.add_row(str(i), exercise)
    console.print(table)

    codes_exercises = list(EXERCISES.keys())
    user_exercise = int(input("Exerice number: "))
    met_value = verify_met(user_exercise)

    print(met_value)


def verify_met(number):
    exercise_index = number - 1

    if 0 <= exercise_index < len(EXERCISES):
        ...

    print(exercise)
    return exercise_name


def clear_screen():
    os.system('cls' if os.name == "nt" else "clear")


def function_n():
    ...


if __name__ == "__main__":
    main()