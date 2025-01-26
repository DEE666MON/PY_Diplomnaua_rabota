import threading
from .TandM_chtenie_i_zapis_teksta import ChtenieIZapis

potok = threading.Thread


def zapysk_potokov_dlua_zapisi_teksta():
    if __name__ == '__main__':
        potok_perviu = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/threading_faul_dlua_zapisi1.txt", 1000000))
        potok_vtorou = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/threading_faul_dlua_zapisi2.txt", 100000))
        potok_tretiu = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/threading_faul_dlua_zapisi3.txt", 750000))
        potok_chetvertiu = potok(target=ChtenieIZapis.zapis_teksta,
                                 args=("../FDZ/threading_faul_dlua_zapisi4.txt", 250000))
        potok_puatiu = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/threading_faul_dlua_zapisi5.txt", 500000))
    else:
        potok_perviu = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/threading_faul_dlua_zapisi1.txt", 1000000))
        potok_vtorou = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/threading_faul_dlua_zapisi2.txt", 100000))
        potok_tretiu = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/threading_faul_dlua_zapisi3.txt", 750000))
        potok_chetvertiu = potok(target=ChtenieIZapis.zapis_teksta,
                                 args=("FDZ/threading_faul_dlua_zapisi4.txt", 250000))
        potok_puatiu = potok(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/threading_faul_dlua_zapisi5.txt", 500000))
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
    zapysk_potokov_dlua_zapisi_teksta()
