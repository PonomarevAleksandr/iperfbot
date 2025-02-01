import iperf3
import matplotlib.pyplot as plt
from aiogram.types import FSInputFile

async def run_iperf_test(ip: str, duration: int, format_type: int):
    """
    Запускает iperf3 тест и возвращает либо график, либо текстовые данные
    """
    client = iperf3.Client()
    client.duration = duration
    client.server_hostname = ip

    try:
        result = client.run()
        if result is None:
            return "Ошибка: сервер Iperf3 недоступен. Попробуйте другой IP."
    except Exception as e:
        return f"Ошибка при запуске теста: {e}"

    data = result.json
    byte_transfer = []
    time_intervals = []

    for interval in data["intervals"]:
        start = round(interval["streams"][0]["start"])
        transfer = round(interval["streams"][0]["bytes"] / 1e6, 2)  # В мегабайтах
        byte_transfer.append(transfer)
        time_intervals.append(start)

    if format_type == 1:
        return await generate_graph(time_intervals, byte_transfer)
    else:
        return generate_text_report(data)

async def generate_graph(time_intervals, byte_transfer):
    """
    Создаёт график скорости передачи
    """
    plt.figure(figsize=(8, 4))
    plt.plot(time_intervals, byte_transfer, marker="o", linestyle="-", color="b")
    plt.xlabel("Время (секунды)")
    plt.ylabel("Передано (MB)")
    plt.title("График скорости передачи")
    plt.grid()
    plt.savefig("speed_graph.png")
    plt.close()

    return FSInputFile("speed_graph.png")

def generate_text_report(data):
    """
    Генерирует текстовый отчёт по результатам iperf3 теста
    """
    text_results = ["📊 **Результаты теста:**"]
    for interval in data["intervals"]:
        start = round(interval["streams"][0]["start"])
        end = round(interval["streams"][0]["end"])
        transfer = round(interval["streams"][0]["bytes"] / 1e6, 2)
        bandwidth = round(interval["streams"][0]["bits_per_second"] / 8e6, 2)

        text_results.append(f"⏳ {start}-{end} с | 📦 {transfer} MB | 🚀 {bandwidth} MB/s")

    return "\n".join(text_results)
