from aiogram import *
from aiogram.fsm.context import FSMContext

from main_bot.config import *

from core.states import MainSG
from core import keyboards
from core import strings


async def get_results_olymp():
    cur.execute(f"SELECT name, task1, task2, task3, task4, task5, task6, task7, task8, task9, task10 FROM users")
    results = cur.fetchall()

    results.sort(key=lambda x: sum(x[1:]), reverse=True)

    for i in range(len(results)):
        results[i] = [results[i][0], sum(results[i][1:])]

    return results
