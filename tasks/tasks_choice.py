from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

tasks_choice_router = Router()


@tasks_choice_router.message(MainSG.tasks_choice)
async def choice(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    elif message.text == "Задания первого тура":
        if handling["day1"]:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Ссылка на задания первого тура",
                                   reply_markup=keyboards.tasks_choice)

        else:
            if handling["results1"]:
                text = "Первый тур окончен"

            else:
                text = "Первый тур ещё не начался"

            await bot.send_message(chat_id=message.chat.id,
                                   text=text,
                                   reply_markup=keyboards.tasks_choice)

    elif message.text == "Задания второго тура":
        if handling["day2"]:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Ссылка на задания второго тура",
                                   reply_markup=keyboards.tasks_choice)
        else:
            if handling["results2"]:
                text = "Второй тур окончен"

            else:
                text = "Второй тур ещё не начался"

            await bot.send_message(chat_id=message.chat.id,
                                   text=text,
                                   reply_markup=keyboards.tasks_choice)

    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.error,
                               reply_markup=keyboards.tasks_choice)
