import threading
from .TandM_chtenie_i_zapis_teksta import ChtenieIZapis

potok = threading.Thread

if __name__ == '__main__':
    spisok_faulov_dlua_chteniua = [f'../FDC/faul_dlua_chteniua{number}.txt' for number in range(1, 6)]
else:
    spisok_faulov_dlua_chteniua = [f'FDC/faul_dlua_chteniua{number}.txt' for number in range(1, 6)]


def zapysk_potokov_dlua_chteniua_teksta():
    potok_perviu = potok(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[0],))
    potok_vtorou = potok(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[1],))
    potok_tretiu = potok(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[2],))
    potok_chetvertiu = potok(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[3],))
    potok_puatiu = potok(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[4],))
    potok_perviu.start()
    potok_vtorou.start()
    potok_tretiu.start()
    potok_chetvertiu.start()
    potok_puatiu.start()
    potok_perviu.join()
    potok_vtorou.join()
    potok_tretiu.join()
    potok_chetvertiu.join()
    potok_puatiu.join()
    print(f"\nСумма задержки потоков: {ChtenieIZapis.summa_ojidaniua} секунд(а, ы).")
    ChtenieIZapis.summa_ojidaniua = 0.0


if __name__ == '__main__':
    zapysk_potokov_dlua_chteniua_teksta()
