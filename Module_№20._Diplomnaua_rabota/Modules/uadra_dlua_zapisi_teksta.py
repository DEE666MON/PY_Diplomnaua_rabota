import multiprocessing
from .TandM_chtenie_i_zapis_teksta import ChtenieIZapis

uadro = multiprocessing.Process


def zapysk_uader_dlua_zapisi_teksta():
    if __name__ == '__main__':
        uadro_pervoe = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/multiprocessing_faul_dlua_zapisi1.txt", 1000000))
        uadro_vtoroe = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/multiprocessing_faul_dlua_zapisi2.txt", 100000))
        uadro_tretie = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/multiprocessing_faul_dlua_zapisi3.txt", 750000))
        uadro_chetvertoe = uadro(target=ChtenieIZapis.zapis_teksta,
                                 args=("../FDZ/multiprocessing_faul_dlua_zapisi4.txt", 250000))
        uadro_puatoe = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("../FDZ/multiprocessing_faul_dlua_zapisi5.txt", 500000))
    else:
        uadro_pervoe = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/multiprocessing_faul_dlua_zapisi1.txt", 1000000))
        uadro_vtoroe = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/multiprocessing_faul_dlua_zapisi2.txt", 100000))
        uadro_tretie = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/multiprocessing_faul_dlua_zapisi3.txt", 750000))
        uadro_chetvertoe = uadro(target=ChtenieIZapis.zapis_teksta,
                                 args=("FDZ/multiprocessing_faul_dlua_zapisi4.txt", 250000))
        uadro_puatoe = uadro(target=ChtenieIZapis.zapis_teksta,
                             args=("FDZ/multiprocessing_faul_dlua_zapisi5.txt", 500000))
    uadro_pervoe.start()
    uadro_vtoroe.start()
    uadro_tretie.start()
    uadro_chetvertoe.start()
    uadro_puatoe.start()
    uadro_pervoe.join()
    uadro_vtoroe.join()
    uadro_tretie.join()
    uadro_chetvertoe.join()
    uadro_puatoe.join()
    print(f"\nСумма задержки ядер: {ChtenieIZapis.summa_ojidaniua} секунд(а, ы).")
    ChtenieIZapis.summa_ojidaniua = 0.0


if __name__ == '__main__':
    zapysk_uader_dlua_zapisi_teksta()
