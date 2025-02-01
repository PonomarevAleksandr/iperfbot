from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from src.utils.func import run_iperf_test
from src.utils.keyboards import get_format_keyboard
from src.utils.fsm_state import IperfTest

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! 👋 Я помогу проверить скорость сети через Iperf3.\n\n"
                         "Используй команду /play, чтобы начать тест.")


@router.message(Command("play"))
async def play_handler(message: types.Message, state: FSMContext):
    await message.answer("Выберите формат вывода результатов:", reply_markup=get_format_keyboard())
    await state.set_state(IperfTest.format_choice)


@router.message(IperfTest.format_choice)
async def format_choice_handler(message: types.Message, state: FSMContext):
    format_type = 1 if "График" in message.text else 2
    await state.update_data(format=format_type)

    await message.answer("Введите время проверки (в секундах):")
    await state.set_state(IperfTest.duration)


@router.message(IperfTest.duration, F.text.regexp(r"^\d+$"))
async def duration_handler(message: types.Message, state: FSMContext):
    await state.update_data(duration=int(message.text))
    await message.answer("Введите IP-адрес сервера для теста:")
    await state.set_state(IperfTest.ip_address)


@router.message(IperfTest.ip_address)
async def ip_address_handler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    ip = message.text
    duration = user_data["duration"]
    format_type = user_data["format"]

    await message.answer(f"Запускаю тест на {duration} секунд... ⏳")

    result = await run_iperf_test(ip, duration, format_type)

    if isinstance(result, str):
        await message.answer(result, parse_mode="Markdown")
    else:
        await message.answer_photo(result)

    await state.clear()
