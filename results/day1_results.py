from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings


async def get_results_day1():
    cur.execute(f"SELECT name, task1, task2, task3, task4, task5 FROM users")
    results = cur.fetchall()

    results.sort(key=lambda x: sum(x[1:]), reverse=True)

    return results
