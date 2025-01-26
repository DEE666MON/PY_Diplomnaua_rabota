import asyncio
from .ASYNC_sborka_frazi import SborkaFrazi


async def zapysk_asyncio_dlua_sborki_fraz():
    raschet1 = asyncio.create_task(SborkaFrazi.sborka_frazi("\nЗавершилась сборка фразы №1", 200, 15000))
    raschet2 = asyncio.create_task(SborkaFrazi.sborka_frazi("\nЗавершилась сборка фразы №2", 100, 15000))
    raschet3 = asyncio.create_task(SborkaFrazi.sborka_frazi("\nЗавершилась сборка фразы №3", 50, 15000))
    raschet4 = asyncio.create_task(SborkaFrazi.sborka_frazi("\nЗавершилась сборка фразы №4", 200, 30000))
    raschet5 = asyncio.create_task(SborkaFrazi.sborka_frazi("\nЗавершилась сборка фразы №5", 100, 30000))
    raschet6 = asyncio.create_task(SborkaFrazi.sborka_frazi("\nЗавершилась сборка фразы №6", 50, 30000))
    await raschet1
    await raschet2
    await raschet3
    await raschet4
    await raschet5
    await raschet6
    print(f"\nСумма задержки запросов: {SborkaFrazi.summa_ojidaniua} секунд(а, ы).")
    SborkaFrazi.summa_ojidaniua = 0.0


if __name__ == '__main__':
    asyncio.run(zapysk_asyncio_dlua_sborki_fraz())
