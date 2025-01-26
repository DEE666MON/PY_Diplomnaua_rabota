import asyncio
from .ASYNC_rascheti_int_i_float import Rascheti


async def zapysk_asyncio_dlua_raschetov():
    raschet1 = asyncio.create_task(Rascheti.rascheti_int("расчёт №1", 1000))
    raschet2 = asyncio.create_task(Rascheti.rascheti_int("расчёт №2", 250))
    raschet3 = asyncio.create_task(Rascheti.rascheti_int("расчёт №3", 500))
    raschet4 = asyncio.create_task(Rascheti.rascheti_float("расчёт №4", 1000))
    raschet5 = asyncio.create_task(Rascheti.rascheti_float("расчёт №5", 250))
    raschet6 = asyncio.create_task(Rascheti.rascheti_float("расчёт №6", 500))
    await raschet1
    await raschet2
    await raschet3
    await raschet4
    await raschet5
    await raschet6
    print(f"\nСумма задержки запросов: {Rascheti.summa_ojidaniua} секунд(а, ы).")
    Rascheti.summa_ojidaniua = 0.0


if __name__ == '__main__':
    asyncio.run(zapysk_asyncio_dlua_raschetov())
