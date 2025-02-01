from aiogram.fsm.state import StatesGroup, State

class IperfTest(StatesGroup):
    """Состояния для iperf3 теста"""
    format_choice = State()
    duration = State()
    ip_address = State()
