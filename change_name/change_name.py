from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

change_name_router = Router()


@change_name_router.message(MainSG.change_name)
async def change_name(message: types.Message, state: FSMContext):
    if message.text == "В главное меню 🏠":
        await bot.send_message(chat_id=message.chat.id,
                               text=strings.main_menu,
                               reply_markup=keyboards.main_menu)

        await state.set_state(MainSG.main_menu)

    else:
        name = message.text.replace('"', "\'\'")

        if len(name) > 20:
            await bot.send_message(chat_id=message.chat.id,
                                   text="Это имя слишком длинное!\n"
                                        "Введите имя, длина которого не более 20 символов",
                                   reply_markup=keyboards.to_main_menu)

        else:
            cur.execute(f"UPDATE users SET name = \"{name}\" WHERE chat_id = {message.chat.id}")
            db.commit()

            await bot.send_message(chat_id=message.chat.id,
                                   text=f"Ваше новое имя - {name}!\n",
                                   reply_markup=keyboards.to_main_menu)

            await state.set_state(MainSG.to_main_menu)
