from asyncio import run
import logging

from aiogram import *
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings


from registration.get_name import get_name_router

from main_menu.transition import main_menu_transition_router
from main_menu.main_menu import main_menu_router

from results.results_choice import results_choice_router

from solutions.solutions_choice import solutions_choice_router
from solutions.solution_choice import solution_choice_router
from solutions.send_solution import send_solution_router

from tasks.tasks_choice import tasks_choice_router

from change_name.change_name import change_name_router

main_router = Router()


@main_router.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    cur.execute(f"SELECT * FROM users WHERE chat_id = {message.chat.id}")

    user = cur.fetchall()

    if user:
        user = user[0]

        if user[1]:
            await bot.send_message(chat_id=message.chat.id,
                                   text=strings.main_menu,
                                   reply_markup=keyboards.main_menu)

            await state.set_state(MainSG.main_menu)

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text=strings.ask_name)

            await state.set_state(MainSG.get_name)

    else:
        cur.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (message.chat.id, '', -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

        cur.execute(f"CREATE TABLE user_{message.chat.id} ("
                    f"task1 TEXT, "
                    f"task2 TEXT, "
                    f"task3 TEXT, "
                    f"task4 TEXT, "
                    f"task5 TEXT, "
                    f"task6 TEXT, "
                    f"task7 TEXT, "
                    f"task8 TEXT, "
                    f"task9 TEXT, "
                    f"task10 TEXT"
                    f")")
        db.commit()

        cur.execute(f"INSERT INTO user_{message.chat.id} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    ('', '', '', '', '', '', '', '', '', ''))
        db.commit()

        await bot.send_message(chat_id=message.chat.id,
                               text="Здравствуйте! Этот бот предназначен для проведения Сигма Олимпиады 2024 года.\n" +
                                    strings.ask_name)

        await state.set_state(MainSG.get_name)


dp.include_routers(main_router, get_name_router, main_menu_transition_router, main_menu_router, results_choice_router,
                   solutions_choice_router, tasks_choice_router, solution_choice_router, send_solution_router,
                   change_name_router)


async def main():
    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
