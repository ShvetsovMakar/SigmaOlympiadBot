from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

results_choice_router = Router()


@results_choice_router.message(MainSG.results_choice)
async def choice(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    elif message.text == "Результаты первого тура":
        if handling["results1"]:
            pass

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Результаты первого тура ещё недоступны",
                                   reply_markup=keyboards.results_choice)

    elif message.text == "Результаты второго тура":
        if handling["results2"]:
            pass

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Результаты второго тура ещё недоступны",
                                   reply_markup=keyboards.results_choice)

    elif message.text == "Результаты олимпиады":
        if handling["results2"]:
            pass

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Результаты олимпиады ещё недоступны",
                                   reply_markup=keyboards.results_choice)

    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.error,
                               reply_markup=keyboards.results_choice)
