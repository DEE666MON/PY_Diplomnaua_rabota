import multiprocessing
from .TandM_chtenie_i_zapis_teksta import ChtenieIZapis

uadro = multiprocessing.Process

if __name__ == '__main__':
    spisok_faulov_dlua_chteniua = [f'../FDC/faul_dlua_chteniua{number}.txt' for number in range(1, 6)]
else:
    spisok_faulov_dlua_chteniua = [f'FDC/faul_dlua_chteniua{number}.txt' for number in range(1, 6)]


def zapysk_uader_dlua_chteniua_teksta():
    uadro_pervoe = uadro(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[0],))
    uadro_vtoroe = uadro(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[1],))
    uadro_tretie = uadro(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[2],))
    uadro_chetvertoe = uadro(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[3],))
    uadro_puatoe = uadro(target=ChtenieIZapis.chtenie_teksta, args=(spisok_faulov_dlua_chteniua[4],))
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
    zapysk_uader_dlua_chteniua_teksta()
