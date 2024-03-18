from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

from results.day1_results import get_results_day1
from results.day2_results import get_results_day2
from results.olymp_results import get_results_olymp

results_choice_router = Router()


async def send_results(results, message, type):
    for i in range(len(results)):
        results[i] = list(results[i])
    max_len = max(len("Участник"), len(max(results, key=lambda x: len(x[0]))[0]))

    types_dict = {
        1: "ТАБЛИЦА РЕЗУЛЬТАТОВ 1 ТУРА\n"
           "Для каждого участника указан балл за 1, 2, 3, 4 и 5 задачу,\n",
        2: "ТАБЛИЦА РЕЗУЛЬТАТОВ 2 ТУРА\n"
           "Для каждого участника указан балл за 6, 7, 8, 9 и 10 задачу\n",
        3: "ТАБЛИЦА РЕЗУЛЬТАТОВ ОЛИМПИАДЫ\n"
           "Для каждого участника указана сумма баллов за I и II туры\n"
    }

    text = types_dict[type]

    for i in range(len(results)):
        text += f'\n{i + 1}. ' + results[i][0] + ' |' + '|'.join([str(j) for j in results[i][1:]]) + '|'

    await bot.send_message(chat_id=message.chat.id,
                           text=text,
                           reply_markup=keyboards.results_choice)


@results_choice_router.message(MainSG.results_choice)
async def choice(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    elif message.text == "Результаты II тура":
        if handling["results1"]:
            results = await get_results_day1()
            await send_results(results, message, type=1)

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Результаты первого тура ещё недоступны",
                                   reply_markup=keyboards.results_choice)

    elif message.text == "Результаты I тура":
        if handling["results2"]:
            results = await get_results_day2()
            await send_results(results, message, type=2)

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Результаты второго тура ещё недоступны",
                                   reply_markup=keyboards.results_choice)

    elif message.text == "Результаты олимпиады":
        if handling["results2"]:
            results = await get_results_olymp()
            await send_results(results, message, type=3)

        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Результаты олимпиады ещё недоступны",
                                   reply_markup=keyboards.results_choice)

    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.error,
                               reply_markup=keyboards.results_choice)
