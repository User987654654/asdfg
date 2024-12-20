Руководство пользователя
====================

Создание задачи
--------------
Для создания новой задачи необходимо указать следующие параметры:

* Название задачи
* Описание задачи
* Приоритет (LOW, MEDIUM, HIGH, URGENT)
* Срок выполнения

Пример создания задачи::

    from models import Task, TaskPriority
    from datetime import datetime

    task = Task(
        title="Разработка новой функции",
        description="Реализовать функцию экспорта данных",
        priority=TaskPriority.HIGH,
        deadline=datetime(2024, 12, 31)
    )

Управление статусом
------------------
Задача может находиться в одном из следующих статусов:

* NEW - новая задача
* IN_PROGRESS - задача в работе
* ON_REVIEW - задача на проверке
* DONE - задача выполнена

Для изменения статуса используйте метод ``change_status``::

    from models import TaskStatus
    task.change_status(TaskStatus.IN_PROGRESS)

Назначение исполнителя
---------------------
Для назначения исполнителя задачи используйте метод ``assign_to``::

    task.assign_to(user)