from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings

main_menu_transition_router = Router()


@main_menu_transition_router.message(MainSG.to_main_menu)
async def transition(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=strings.main_menu,
                           reply_markup=keyboards.main_menu)

    await state.set_state(MainSG.main_menu)
