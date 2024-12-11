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
    task_name: str, task_description: str, task_priority: int, task_status: int
) -> str:
    task_priority_to_str = TASKS_PRIORITY[task_priority]
    task_status_to_str = TASKS_STATUS[task_status]
    with open("id.txt", "r", encoding="utf-8") as id_file_read:
        id = int(id_file_read.read())
    current_id = id + 1
    with open("id.txt", "w", encoding="utf-8") as id_file_write:
        id_file_write.write(str(current_id))
    return f"{current_id}, {task_name}, {task_description}, {task_priority_to_str}, {task_status_to_str}\n"


def read_all_tasks(sort_by: str = None) -> None:
    tasks_list = []
    with open("tasks.txt", "r", encoding="utf-8") as file_to_read:
        tasks_list = [line.strip().split(", ") for line in file_to_read]

    if sort_by == "priority":

        def priority_key(task):
            return list(TASKS_PRIORITY.values()).index(task[3].lower())

        tasks_list.sort(key=priority_key)
    elif sort_by == "status":

        def status_key(task):
            return list(TASKS_STATUS.values()).index(task[4].lower())

        tasks_list.sort(key=status_key)

    for task in tasks_list:
        print(", ".join(task))


def read_chosen_task(by: int, value: str) -> None:
    with open("tasks.txt", "r", encoding="utf-8") as file_to_read:
        for line in file_to_read:
            current_task = line.strip().split(", ")
            if by == 1 and current_task[0] == value:
                print(", ".join(current_task))
            elif by in (2, 3) and current_task[by - 1].lower() == value.lower().strip():
                print(", ".join(current_task))


def delete_chosen_task(id: int) -> None:
    tasks_list = []
    with open("tasks.txt", "r", encoding="utf-8") as file_to_read:
        tasks_list = [line.strip().split(", ") for line in file_to_read]
    task_found = False
    for task in tasks_list:
        if int(task[0]) == id:
            tasks_list.remove(task)
            task_found = True
            break
    if task_found:
        with open("tasks.txt", "w", encoding="utf-8") as file_to_write:
            test_str = "\n".join([", ".join(task) for task in tasks_list])
            file_to_write.write(test_str)
        print("Задача удалена.")
    else:
        print("Задача с таким ID нету.")


def modify_chosen_task(id: int, field: int, new_value: str) -> None:
    tasks_list = []
    with open("tasks.txt", "r", encoding="utf-8") as file_to_read:
        tasks_list = [line.strip().split(", ") for line in file_to_read]
    task_found = False
    for task in tasks_list:
        if int(task[0]) == id:
            task_found = True
            if field == 1:
                task[1] = new_value
            elif field == 2:
                task[2] = new_value
            elif field == 3:
                task[3] = TASKS_PRIORITY[int(new_value)]
            elif field == 4:
                task[4] = TASKS_STATUS[int(new_value)]
            else:
                print("Неверное поле для изменения.")
                return
            with open("tasks.txt", "w", encoding="utf-8") as file_to_write:
                test_str = "\n".join([", ".join(task) for task in tasks_list])
                test_str += "\n"
                file_to_write.write(test_str)
            print("Задача обновлена.")
            break

    if not task_found:
        print("Задача не найдена.")


def hard_reset():
    user_agree = input("Вы уверены? 1 - Да, 0 - Нет: ")
    if int(user_agree):
        with open("tasks.txt", "w", encoding="utf-8") as file_to_write:
            file_to_write.write("")
        with open("id.txt", "w", encoding="utf-8") as file_to_write:
            file_to_write.write("0")
    else:
        print("Удаление отменено")


while True:
    print("Выберите действие:")
    print("1 - Создать новую задачу")
    print("2 - Просмотреть задачи")
    print("3 - Обновить задачу")
    print("4 - Удалить задачу")
    print("5 - Hard reset")
    print("0 - Выйти из программы")

    user_answer = input("Что вы хотите сделать: ")

    try:
        user_answer = int(user_answer)

        if user_answer == 1:
            task_name = input("Введите название: ")
            task_description = input("Введите описание: ")
            print("Выберите приоритет: 1 - Low, 2 - Medium, 3 - High")
            task_priority = int(input("Приоритет: "))
            print("Выберите статус: 1 - New, 2 - WIP, 3 - Done")
            task_status = int(input("Статус: "))
            with open("tasks.txt", "a", encoding="utf-8") as file:
                file.write(
                    add_new_task(
                        task_name, task_description, task_priority, task_status
                    )
                )
            print("Задача добавлена.")

        elif user_answer == 2:
            print("Выберите сортировку (priority, status или ничего не пишите): ")
            sort_by = input("Сортировать по: ").strip()
            if sort_by not in ["", "priority", "status"]:
                print("Неверный параметр")
                continue
            read_all_tasks(sort_by)

        elif user_answer == 3:
            id = int(input("Введите ID задачи для обновления: "))
            print(
                "Что хотите обновить? 1 - название, 2 - описание, 3 - приоритет, 4 - статус"
            )
            field = int(input("Введите номер поля для обновления: "))
            new_value = input("Введите новое значение: ")
            modify_chosen_task(id, field, new_value)
            print("Задача обновлена.")

        elif user_answer == 4:
            id = int(input("Введите ID задачи для удаления: "))
            delete_chosen_task(id)

        elif user_answer == 5:
            hard_reset()

        elif user_answer == 0:
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

    except ValueError:
        print("Введите корректное число.")
