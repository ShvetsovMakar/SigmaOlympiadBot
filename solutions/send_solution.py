from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

send_solution_router = Router()


@send_solution_router.message(MainSG.send_solution)
async def get_solution(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    else:
        solution = message.text.replace('"', "\'\'")

        cur.execute(f"SELECT cur_task FROM users WHERE chat_id = {message.chat.id}")
        cur_task = cur.fetchall()[0][0]

        cur.execute(f"UPDATE user_{message.chat.id} SET task{cur_task} = \"{solution}\"")
        db.commit()

        await bot.send_message(chat_id=message.chat.id,
                               text=f"Вы успешно отправили решение задачи #{cur_task}",
                               reply_markup=keyboards.to_main_menu)

        await state.set_state(MainSG.to_main_menu)
