from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards

get_name_router = Router()


@get_name_router.message(MainSG.get_name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text.replace('"', "\'\'")

    if len(name) > 20:
        await bot.send_message(chat_id=message.chat.id,
                               text="Это имя слишком длинное!\n"
                                    "Введите имя, длина которого не более 20 символов")
    else:

        cur.execute(f"UPDATE users SET name = \"{name}\" WHERE chat_id = {message.chat.id}")
        db.commit()

        await bot.send_message(chat_id=message.chat.id,
                               text=f"Ваше имя - {name}!",
                               reply_markup=keyboards.to_main_menu)

        await state.set_state(MainSG.to_main_menu)
