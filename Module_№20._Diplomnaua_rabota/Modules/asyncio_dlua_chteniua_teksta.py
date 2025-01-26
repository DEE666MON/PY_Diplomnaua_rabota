import asyncio
from .ASYNC_chtenie_i_zapis_teksta import ChtenieIZapis

if __name__ == '__main__':
    spisok_faulov_dlua_chteniua = [f'../FDC/faul_dlua_chteniua{number}.txt' for number in range(1, 6)]
else:
    spisok_faulov_dlua_chteniua = [f'FDC/faul_dlua_chteniua{number}.txt' for number in range(1, 6)]


async def zapysk_asyncio_dlua_chteniua_teksta():
    raschet1 = asyncio.create_task(ChtenieIZapis.chtenie_teksta(spisok_faulov_dlua_chteniua[0]))
    raschet2 = asyncio.create_task(ChtenieIZapis.chtenie_teksta(spisok_faulov_dlua_chteniua[1]))
    raschet3 = asyncio.create_task(ChtenieIZapis.chtenie_teksta(spisok_faulov_dlua_chteniua[2]))
    raschet4 = asyncio.create_task(ChtenieIZapis.chtenie_teksta(spisok_faulov_dlua_chteniua[3]))
    raschet5 = asyncio.create_task(ChtenieIZapis.chtenie_teksta(spisok_faulov_dlua_chteniua[4]))
    await raschet1
    await raschet2
    await raschet3
    await raschet4
    await raschet5
    print(f"\nСумма задержки запросов: {ChtenieIZapis.summa_ojidaniua} секунд(а, ы).")
    ChtenieIZapis.summa_ojidaniua = 0.0


if __name__ == '__main__':
    asyncio.run(zapysk_asyncio_dlua_chteniua_teksta())
