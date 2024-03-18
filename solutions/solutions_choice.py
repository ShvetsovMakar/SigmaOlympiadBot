from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

solutions_choice_router = Router()


@solutions_choice_router.message(MainSG.solutions_choice)
async def choice(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    elif message.text == "Отослать решение задания I тура":
        if handling["day1"]:
            await bot.send_message(chat_id=message.chat.id,
                                   text=strings.solution_choice,
                                   reply_markup=keyboards.solutions_day1)

            cur.execute(f"UPDATE users SET cur_task = 1 WHERE chat_id = {message.chat.id}")
            db.commit()

            await state.set_state(MainSG.solution_choice)

        else:
            if handling["results1"]:
                text = "Первый тур окончен"

            else:
                text = "Первый тур ещё не начался"

            await bot.send_message(chat_id=message.chat.id,
                                   text=text,
                                   reply_markup=keyboards.solutions_choice)

    elif message.text == "Отослать решение задания II тура":
        if handling["day2"]:
            await bot.send_message(chat_id=message.chat.id,
                                   text=strings.solution_choice,
                                   reply_markup=keyboards.solutions_day2)

            cur.execute(f"UPDATE users SET cur_task = 2 WHERE chat_id = {message.chat.id}")
            db.commit()

            await state.set_state(MainSG.solution_choice)

        else:
            if handling["results2"]:
                text = "Второй тур окончен"

            else:
                text = "Второй тур ещё не начался"

            await bot.send_message(chat_id=message.chat.id,
                                   text=text,
                                   reply_markup=keyboards.solutions_choice)

    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.error,
                               reply_markup=keyboards.solutions_choice)
