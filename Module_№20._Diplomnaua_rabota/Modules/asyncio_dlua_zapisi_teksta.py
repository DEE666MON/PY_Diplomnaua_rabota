import asyncio
from .ASYNC_chtenie_i_zapis_teksta import ChtenieIZapis


async def zapysk_asyncio_dlua_zapisi_teksta():
    if __name__ == '__main__':
        raschet1 = asyncio.create_task(ChtenieIZapis.zapis_teksta("../FDZ/asyncio_faul_dlua_zapisi1.txt", 1000000))
        raschet2 = asyncio.create_task(ChtenieIZapis.zapis_teksta("../FDZ/asyncio_faul_dlua_zapisi2.txt", 100000))
        raschet3 = asyncio.create_task(ChtenieIZapis.zapis_teksta("../FDZ/asyncio_faul_dlua_zapisi3.txt", 750000))
        raschet4 = asyncio.create_task(ChtenieIZapis.zapis_teksta("../FDZ/asyncio_faul_dlua_zapisi4.txt", 250000))
        raschet5 = asyncio.create_task(ChtenieIZapis.zapis_teksta("../FDZ/asyncio_faul_dlua_zapisi5.txt", 500000))
        await raschet1
        await raschet2
        await raschet3
        await raschet4
        await raschet5
    else:
        raschet1 = asyncio.create_task(ChtenieIZapis.zapis_teksta("FDZ/asyncio_faul_dlua_zapisi1.txt", 1000000))
        raschet2 = asyncio.create_task(ChtenieIZapis.zapis_teksta("FDZ/asyncio_faul_dlua_zapisi2.txt", 100000))
        raschet3 = asyncio.create_task(ChtenieIZapis.zapis_teksta("FDZ/asyncio_faul_dlua_zapisi3.txt", 750000))
        raschet4 = asyncio.create_task(ChtenieIZapis.zapis_teksta("FDZ/asyncio_faul_dlua_zapisi4.txt", 250000))
        raschet5 = asyncio.create_task(ChtenieIZapis.zapis_teksta("FDZ/asyncio_faul_dlua_zapisi5.txt", 500000))
        await raschet1
        await raschet2
        await raschet3
        await raschet4
        await raschet5
    print(f"\nСумма задержки запросов: {ChtenieIZapis.summa_ojidaniua} секунд(а, ы).")
    ChtenieIZapis.summa_ojidaniua = 0.0


if __name__ == '__main__':
    asyncio.run(zapysk_asyncio_dlua_zapisi_teksta())
