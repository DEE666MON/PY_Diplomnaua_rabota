import multiprocessing
from .TandM_rascheti_int_i_float import Rascheti

uadro = multiprocessing.Process


def zapysk_uader_dlua_raschetov():
    uadro_pervoe = uadro(target=Rascheti.rascheti_int, args=("расчёт №1", 1000))
    uadro_vtoroe = uadro(target=Rascheti.rascheti_int, args=("расчёт №2", 250))
    uadro_tretie = uadro(target=Rascheti.rascheti_int, args=("расчёт №3", 500))
    uadro_chetvertoe = uadro(target=Rascheti.rascheti_float, args=("расчёт №4", 1000))
    uadro_puatoe = uadro(target=Rascheti.rascheti_float, args=("расчёт №5", 250))
    uadro_shestoe = uadro(target=Rascheti.rascheti_float, args=("расчёт №6", 500))
    uadro_pervoe.start()
    uadro_vtoroe.start()
    uadro_tretie.start()
    uadro_chetvertoe.start()
    uadro_puatoe.start()
    uadro_shestoe.start()
    uadro_pervoe.join()
    uadro_vtoroe.join()
    uadro_tretie.join()
    uadro_chetvertoe.join()
    uadro_puatoe.join()
    uadro_shestoe.join()
    print(f"\nСумма задержки ядер: {Rascheti.summa_ojidaniua} секунд(а, ы).")
    Rascheti.summa_ojidaniua = 0.0


if __name__ == '__main__':
    zapysk_uader_dlua_raschetov()
