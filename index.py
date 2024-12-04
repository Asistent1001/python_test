# def add_new_task(task):
#     print(task)

# while True:
#     user_answer = input("Выберите действие: ")
#     try:
#         user_answer = int(user_answer)
#         print(user_answer)
#     except ValueError:
#         print("Введите число")


# Детали
# Из чего состоит?

#     Задача должна состоять из названия, описания, приоритета, статуса и уникального идентификатора.
#     Приоритет может иметь три варианта низкий, средний, высокий
#     Статус может иметь три варианта новая, в процессе, завершена
#
#       Уникальный идентификатор (id), это просто цифра, которая всегда на 1 больше чем самая большая
#     из уже существующих. Например, если у вас задач нет, то для первой этот параметр будет равен 1.
#     Если у вас уже есть задачи с номерами 1, 2, 3. То новая будет создана с номером 4.
#     Если пользователь удалил несколько задач, и у вас остались задачи 1, 3, 5, то следующая будет с номером 6.

#     if user_answer == 0:
#         break

TASKS_PRIORITY = {
    1: "low",
    2: "medium",
    3: "high",
}

TASKS_STATUS = {
    1: "new",
    2: "wip",
    3: "done",
}


def add_new_task(
    task_name: str,
    task_description: str,
    task_priority: int,
    task_status: int,
) -> str:
    task_priority_to_str = TASKS_PRIORITY[task_priority]
    task_status_to_str = TASKS_STATUS[task_status]
    with open("id.txt", "r", encoding="utf-8") as id_file_read:
        id = int(id_file_read.read())
    current_id = id + 1
    with open("id.txt", "w", encoding="utf-8") as id_file_write:
        id_file_write.write(str(current_id))
    return f"{current_id}, {task_name}, {task_description}, {task_priority_to_str}, {task_status_to_str}\n"


# with open("tasks.txt", "a", encoding="utf-8") as file:
#     file.write(
#         add_new_task("Учить питон", "Надо учить чтобы не прослыть дураком", 3, 2)
#     )


def read_all_tasks() -> None:
    with open("tasks.txt", "r", encoding="utf-8") as file_to_read:
        content = file_to_read.read()
        print(content)


# read_all_tasks()


def read_chosen_task_by_id(id: int) -> str:
    list_of_tasks = []
    with open("tasks.txt", "r", encoding="utf-8") as file_to_read:
        for line in file_to_read:
            current_task = line.strip().split(", ")
            list_of_tasks.append(current_task)
        print(list_of_tasks[id - 1])


read_chosen_task_by_id(1)
