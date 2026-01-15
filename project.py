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
    print("Lista de Exercícios:")
    for i, exercise in enumerate(EXERCISES.keys(), 1):        
        print(f'{i} - {exercise}', end="\n")

    user_exercise = input("Digite o nome do exercício: ")
    met_value = verify_met(user_exercise)

    print(met_value)


def verify_met(exercise):
    exercise_name = exercise.lower().strip()
    print(exercise)
    return exercise_name


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()