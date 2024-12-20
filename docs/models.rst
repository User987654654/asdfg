Модели системы
=============

Классы и перечисления
--------------------

TaskPriority
~~~~~~~~~~~
.. autoclass:: models.TaskPriority
   :members:
   :undoc-members:
   :show-inheritance:

TaskStatus
~~~~~~~~~
.. autoclass:: models.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

Task
~~~~
.. autoclass:: models.Task
   :members:
   :undoc-members:
   :show-inheritance:

Диаграмма классов
----------------
Система состоит из следующих основных компонентов:

* Класс ``Task`` - центральный класс для работы с задачами
* Перечисление ``TaskPriority`` - определяет приоритеты задач
* Перечисление ``TaskStatus`` - определяет возможные статусы задач