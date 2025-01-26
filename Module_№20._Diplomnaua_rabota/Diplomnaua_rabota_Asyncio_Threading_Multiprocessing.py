'''
Дипломная работа по теме:
"Сравнение различных подходов к реализации асинхронного программирования:
asyncio, threading и multiprocessing"
'''

from datetime import datetime
import asyncio

time_start_programmi = 0
time_end_programmi = 0
time_start = 0
time_end = 0


def ramki(flag=True):
    if flag:
        for i in range(100):
            print("*", end="")
    else:
        for i in range(50):
            print("-", end="")
    print()


def vremua_izmeritel(flag=False):
    global time_start, time_end
    if not flag:
        time_start = datetime.now()
        return None
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res, "- (часы:минуты:секунды.миллиСекунды)")


#####################################################################################

##### ASYNCIO #####
from Modules.asyncio_dlua_raschetov import zapysk_asyncio_dlua_raschetov
from Modules.asyncio_dlua_chteniua_teksta import zapysk_asyncio_dlua_chteniua_teksta
from Modules.asyncio_dlua_zapisi_teksta import zapysk_asyncio_dlua_zapisi_teksta
from Modules.asyncio_dlua_sborki_fraz import zapysk_asyncio_dlua_sborki_fraz

if __name__ == '__main__':
    ramki()
    print("Asyncio:")
    time_start_programmi = datetime.now()

    # РАСЧЁТЫ #
    ramki(False)
    print("РАСЧЁТЫ:", end="")
    vremua_izmeritel()

    asyncio.run(zapysk_asyncio_dlua_raschetov())

    print("'РАСЧЁТЫ' выполнилось за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'РАСЧЁТЫ'.")
    ramki(False)
    # РАСЧЁТЫ #

    # ЧТЕНИЕ ФАЙЛОВ #
    ramki(False)
    print("ЧТЕНИЕ ФАЙЛОВ:", end="")
    vremua_izmeritel()

    asyncio.run(zapysk_asyncio_dlua_chteniua_teksta())

    print("'ЧТЕНИЕ ФАЙЛОВ' выполнилось за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'ЧТЕНИЕ ФАЙЛОВ'.")
    ramki(False)
    # ЧТЕНИЕ ФАЙЛОВ #

    # ЗАПИСЬ ФАЙЛОВ #
    ramki(False)
    print("ЗАПИСЬ ФАЙЛОВ:", end="")
    vremua_izmeritel()

    asyncio.run(zapysk_asyncio_dlua_zapisi_teksta())

    print("'ЗАПИСЬ ФАЙЛОВ' выполнилась за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'ЗАПИСЬ ФАЙЛОВ'.")
    ramki(False)
    # ЗАПИСЬ ФАЙЛОВ #

    # СБОРКА ФРАЗЫ #
    ramki(False)
    print("СБОРКА ФРАЗЫ:", end="")
    vremua_izmeritel()

    asyncio.run(zapysk_asyncio_dlua_sborki_fraz())

    print("'СБОРКА ФРАЗЫ' выполнилась за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'СБОРКА ФРАЗЫ'.")
    ramki(False)
    # СБОРКА ФРАЗЫ #

    time_end_programmi = datetime.now()
    print(f"Asyncio закончился за {time_end_programmi - time_start_programmi}.")
    ramki()
##### ASYNCIO #####

#####################################################################################

##### THREADING #####
from Modules.potoki_dlua_raschetov import zapysk_potokov_dlua_raschetov
from Modules.potoki_dlua_chteniua_teksta import zapysk_potokov_dlua_chteniua_teksta
from Modules.potoki_dlua_zapisi_teksta import zapysk_potokov_dlua_zapisi_teksta
from Modules.potoki_dlua_sborki_fraz import zapysk_potokov_dlua_sborki_fraz

if __name__ == '__main__':
    ramki()
    print("Threading:")
    time_start_programmi = datetime.now()

    # РАСЧЁТЫ #
    ramki(False)
    print("РАСЧЁТЫ:", end="")
    vremua_izmeritel()

    zapysk_potokov_dlua_raschetov()

    print("'РАСЧЁТЫ' выполнилось за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'РАСЧЁТЫ'.")
    ramki(False)
    # РАСЧЁТЫ #

    # ЧТЕНИЕ ФАЙЛОВ #
    ramki(False)
    print("ЧТЕНИЕ ФАЙЛОВ:", end="")
    vremua_izmeritel()

    zapysk_potokov_dlua_chteniua_teksta()

    print("'ЧТЕНИЕ ФАЙЛОВ' выполнилось за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'ЧТЕНИЕ ФАЙЛОВ'.")
    ramki(False)
    # ЧТЕНИЕ ФАЙЛОВ #

    # ЗАПИСЬ ФАЙЛОВ #
    ramki(False)
    print("ЗАПИСЬ ФАЙЛОВ:", end="")
    vremua_izmeritel()

    zapysk_potokov_dlua_zapisi_teksta()

    print("'ЗАПИСЬ ФАЙЛОВ' выполнилась за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'ЗАПИСЬ ФАЙЛОВ'.")
    ramki(False)
    # ЗАПИСЬ ФАЙЛОВ #

    # СБОРКА ФРАЗЫ #
    ramki(False)
    print("СБОРКА ФРАЗЫ:", end="")
    vremua_izmeritel()

    zapysk_potokov_dlua_sborki_fraz()

    print("'СБОРКА ФРАЗЫ' выполнилась за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'СБОРКА ФРАЗЫ'.")
    ramki(False)
    # СБОРКА ФРАЗЫ #

    time_end_programmi = datetime.now()
    print(f"Threading закончился за {time_end_programmi - time_start_programmi}.")
    ramki()
##### THREADING #####

#####################################################################################

##### MULTIPROCESSING #####
from Modules.uadra_dlua_raschetov import zapysk_uader_dlua_raschetov
from Modules.uadra_dlua_chteniua_teksta import zapysk_uader_dlua_chteniua_teksta
from Modules.uadra_dlua_zapisi_teksta import zapysk_uader_dlua_zapisi_teksta
from Modules.uadra_dlua_sborki_fraz import zapysk_uader_dlua_sborki_fraz

if __name__ == '__main__':
    ramki()
    print("Multiprocessing:")
    time_start_programmi = datetime.now()

    # РАСЧЁТЫ #
    ramki(False)
    print("РАСЧЁТЫ:", end="")
    vremua_izmeritel()

    zapysk_uader_dlua_raschetov()

    print("'РАСЧЁТЫ' выполнилось за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'РАСЧЁТЫ'.")
    ramki(False)
    # РАСЧЁТЫ #

    # ЧТЕНИЕ ФАЙЛОВ #
    ramki(False)
    print("ЧТЕНИЕ ФАЙЛОВ:", end="")
    vremua_izmeritel()

    zapysk_uader_dlua_chteniua_teksta()

    print("'ЧТЕНИЕ ФАЙЛОВ' выполнилось за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'ЧТЕНИЕ ФАЙЛОВ'.")
    ramki(False)
    # ЧТЕНИЕ ФАЙЛОВ #

    # ЗАПИСЬ ФАЙЛОВ #
    ramki(False)
    print("ЗАПИСЬ ФАЙЛОВ:", end="")
    vremua_izmeritel()

    zapysk_uader_dlua_zapisi_teksta()

    print("'ЗАПИСЬ ФАЙЛОВ' выполнилась за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'ЗАПИСЬ ФАЙЛОВ'.")
    ramki(False)
    # ЗАПИСЬ ФАЙЛОВ #

    # СБОРКА ФРАЗЫ #
    ramki(False)
    print("СБОРКА ФРАЗЫ:", end="")
    vremua_izmeritel()

    zapysk_uader_dlua_sborki_fraz()

    print("'СБОРКА ФРАЗЫ' выполнилась за время: ", end="")
    vremua_izmeritel(True)
    print("Конец 'СБОРКА ФРАЗЫ'.")
    ramki(False)
    # СБОРКА ФРАЗЫ #

    time_end_programmi = datetime.now()
    print(f"Multiprocessing закончился за {time_end_programmi - time_start_programmi}.")
    ramki()
##### MULTIPROCESSING #####

#####################################################################################
