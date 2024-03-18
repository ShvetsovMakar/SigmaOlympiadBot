from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings


async def get_results_day2():
    cur.execute(f"SELECT name, task6, task7, task8, task9, task10 FROM users")
    results = cur.fetchall()

    results.sort(key=lambda x: sum(x[1:]), reverse=True)

    return results
