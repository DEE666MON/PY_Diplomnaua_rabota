import asyncio


class ChtenieIZapis:
    summa_ojidaniua = 0.0

    async def chtenie_teksta(*args):
        all_data = []
        time_sleep = 1.0
        ChtenieIZapis.summa_ojidaniua += time_sleep
        with open(args[0], "r", encoding='utf-8') as file:
            if file.readline() != '':
                all_data.append(file.read())
            await asyncio.sleep(time_sleep)
        print(f"\nЗавершилось чтение файла {args[0]}, задержка {time_sleep}. ", end="")

    async def zapis_teksta(*args):
        time_sleep = 1.0
        ChtenieIZapis.summa_ojidaniua += time_sleep
        with open(args[0], "w", encoding='utf-8') as file:
            for i in range(args[1]):
                file.write(f"Кто-то, где-то, делает какой-то заказ, № {i + 1} \n.")
        await asyncio.sleep(time_sleep)
        print(f"\nЗавершилась запись в файл {args[0]}, задержка {time_sleep}. ", end="")
