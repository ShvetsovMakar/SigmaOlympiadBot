from aiogram.fsm.state import StatesGroup, State

class MainSG(StatesGroup):
    get_name = State()

    to_main_menu = State()
    main_menu = State()

    tasks_choice = State()
    solutions_choice = State()
    results_choice = State()

    solution_choice = State()
    send_solution = State()

    change_name = State()
