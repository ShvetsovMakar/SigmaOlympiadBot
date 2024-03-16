from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

main_menu_router = Router()


@main_menu_router.message(MainSG.main_menu)
async def main_menu(message: types.Message, state: FSMContext):
    if message.text == "Задания 📋":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.tasks_choice,
                               reply_markup=keyboards.tasks_choice)

        await state.set_state(MainSG.tasks_choice)

    elif message.text == "Отослать решение ✏️":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.solutions_choice,
                               reply_markup=keyboards.solutions_choice)

        await state.set_state(MainSG.solutions_choice)

    elif message.text == "Результаты 🏆":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.results_choice,
                               reply_markup=keyboards.results_choice)

        await state.set_state(MainSG.results_choice)

    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.error,
                               reply_markup=keyboards.main_menu)
