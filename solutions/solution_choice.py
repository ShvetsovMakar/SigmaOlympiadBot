from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

solution_choice_router = Router()


@solution_choice_router.message(MainSG.solution_choice)
async def choice(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    elif message.text in choices_int.keys():
        choice_int = choices_int[message.text]

        cur.execute(f"UPDATE users SET cur_task = {choice_int} WHERE chat_id = {message.chat.id}")
        db.commit()

        cur.execute(f"SELECT task{choice_int} FROM user_{message.chat.id}")
        solution = cur.fetchall()[0][0]

        if solution:
            text = f"Ваше прошлое решение этой задачи: {solution}\n\n" \
                   f"Пришлите новое решение для задачи под номером {choice_int}\n" \
                   f"Решение нужно отправить текстом, фотографии не проверяются"
        else:
            text = f"Пришлите решение для задачи под номером {choice_int}\n" \
                   f"Решение нужно отправить текстом, фотографии не проверяются"

        await bot.send_message(chat_id=message.chat.id,
                               text=text,
                               reply_markup=keyboards.to_main_menu)

        await state.set_state(MainSG.send_solution)

    else:
        cur.execute(f"SELECT cur_task FROM users WHERE chat_id = {message.chat.id}")
        cur_tasks = cur.fetchall()[0][0]

        if cur_tasks == 1:
            keyboard = keyboards.solutions_day1

        else:
            keyboard = keyboards.solutions_day2

        await bot.send_message(chat_id=message.chat.id,
                               text=strings.error,
                               reply_markup=keyboard)
