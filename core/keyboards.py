from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

to_main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="В главное меню 🏠")]],
                                   resize_keyboard=True)

main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Задания 📋"),
                                           KeyboardButton(text="Отослать решение ✏️")],
                                          [KeyboardButton(text="Результаты 🏆"),
                                           KeyboardButton(text="Изменить имя 🔄")]],
                                resize_keyboard=True)

tasks_choice = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Задания I тура")],
                                             [KeyboardButton(text="Задания II тура")],
                                             [KeyboardButton(text="В главное меню 🏠")]],
                                   resize_keyboard=True)

solutions_choice = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отослать решение задания I тура")],
                                                 [KeyboardButton(text="Отослать решение задания II тура")],
                                                 [KeyboardButton(text="В главное меню 🏠")]],
                                       resize_keyboard=True)

results_choice = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Результаты I тура")],
                                               [KeyboardButton(text="Результаты II тура")],
                                               [KeyboardButton(text="Результаты олимпиады")],
                                               [KeyboardButton(text="В главное меню 🏠")]],
                                     resize_keyboard=True)

solutions_day1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="1️⃣"),
                                                KeyboardButton(text="2️⃣"),
                                                KeyboardButton(text="3️⃣")],
                                               [KeyboardButton(text="4️⃣"),
                                                KeyboardButton(text="5️⃣")],
                                               [KeyboardButton(text="В главное меню 🏠")]],
                                     resize_keyboard=True)

solutions_day2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="6️⃣"),
                                                KeyboardButton(text="7️⃣"),
                                                KeyboardButton(text="8️⃣")],
                                               [KeyboardButton(text="9️⃣"),
                                                KeyboardButton(text="🔟")],
                                               [KeyboardButton(text="В главное меню 🏠")]],
                                     resize_keyboard=True)
