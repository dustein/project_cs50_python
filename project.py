import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

EXERCISES = {
    "caminhada": 2.0,
    "caminhada rápida" : 5.0,
    "caminhada em trilha": 6.0,
    "corrida": 8.3,
    "corrida rápida": 11.5,
    "ciclismo": 4.0,
    "ciclismo moderado": 6.8,
    "ginástica": 2.5,
    "calistenia": 3.5,
    "musculação": 6.0,
    "circuito de treino": 8.0,
    "natação": 5.8,
    "pular corda": 8.0,
    "subida e descida de escadas": 4.0,
}

def main():
    exercises_names = list(EXERCISES.keys())
    console = Console()
    
    while True:
        # PARTE GRAFICA INICIO ---------------
        clear_screen()
        console.print(Panel.fit("MET Calculator", style="bold black on cyan"))
        table = Table(title="Exercise List")
        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Title", style="green")        
        for i, exercise in enumerate(EXERCISES.keys(), start=1):        
            table.add_row(str(i), exercise)
        console.print(table)
        # PARTE GRAFICA FIM ---------------

        
        try:
            user_response = input('Exercise number (or "x" to exit): ')
            if user_response.lower() == "x":
                break

            user_exercise = int(user_response)

            met_value = verify_met(user_exercise, exercises_names)

            if met_value is None:
                print("\nThis number is invalid !")
                input("Press ENTER to try again.")
                continue

            user_weight = float(input("Your actual weight (kg): "))
            exercise_duration = int(input("Exercise duration (minutes): "))


            calories_burned = calculate_calories(met_value, user_weight, exercise_duration)
            
            save_log(exercises_names[user_exercise -1], calories_burned)

            print(f'Aproximately {calories_burned:.2f} calories burned during {exercise_duration} minutes of {exercises_names[user_exercise -1]}.\n')
            another_exercise = input("Calculate another exercise? ( y / n ): ")
            if another_exercise.lower() != "y":
                break
    
        except ValueError:
            print("\nInvalid exercise number !")
            input("Press ENTER to try again...")


def verify_met(number, exercises_names):

    exercise_index = number - 1

    if 0 <= exercise_index < len(exercises_names):
        exercise = exercises_names[exercise_index]
        return EXERCISES[exercise]
    
    return None


def clear_screen():
    os.system('cls' if os.name == "nt" else "clear")


def calculate_calories(met_value, user_weight, exercise_duration):
    return met_value * user_weight * exercise_duration / 60

def save_log(exercise, calories):
    try:
        date_to_save = datetime.now().strftime("%d/%m/%Y - %H:%M")
        log_to_save = f'{date_to_save} - {exercise}: {calories:.2f} calories\n'

        with open("log.txt", "a") as file:
            file.write(log_to_save)

        return log_to_save.strip()

    except Exception:
        return "Error saving log..."



if __name__ == "__main__":
    main()