import threading
from .TandM_rascheti_int_i_float import Rascheti

potok = threading.Thread


def zapysk_potokov_dlua_raschetov():
    potok_perviu = potok(target=Rascheti.rascheti_int, args=("расчёт №1", 1000))
    potok_vtorou = potok(target=Rascheti.rascheti_int, args=("расчёт №2", 250))
    potok_tretiu = potok(target=Rascheti.rascheti_int, args=("расчёт №3", 500))
    potok_chetvertiu = potok(target=Rascheti.rascheti_float, args=("расчёт №4", 1000))
    potok_puatiu = potok(target=Rascheti.rascheti_float, args=("расчёт №5", 250))
    potok_shestou = potok(target=Rascheti.rascheti_float, args=("расчёт №6", 500))
    potok_perviu.start()
    potok_vtorou.start()
    potok_tretiu.start()
    potok_chetvertiu.start()
    potok_puatiu.start()
    potok_shestou.start()
    potok_perviu.join()
    potok_vtorou.join()
    potok_tretiu.join()
    potok_chetvertiu.join()
    potok_puatiu.join()
    potok_shestou.join()
    print(f"\nСумма задержки потоков: {Rascheti.summa_ojidaniua} секунд(а, ы).")
    Rascheti.summa_ojidaniua = 0.0


if __name__ == '__main__':
    zapysk_potokov_dlua_raschetov()
