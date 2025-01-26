import threading
from .TandM_sborka_frazi import SborkaFrazi

potok = threading.Thread


def zapysk_potokov_dlua_sborki_fraz():
    potok_perviu = potok(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №1", 200, 15000))
    potok_vtorou = potok(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №2", 100, 15000))
    potok_tretiu = potok(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №3", 50, 15000))
    potok_chetvertiu = potok(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №4", 200, 30000))
    potok_puatiu = potok(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №5", 100, 30000))
    potok_shestou = potok(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №6", 50, 30000))
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
    print(f"\nСумма задержки потоков: {SborkaFrazi.summa_ojidaniua} секунд(а, ы).")
    SborkaFrazi.summa_ojidaniua = 0.0


if __name__ == '__main__':
    zapysk_potokov_dlua_sborki_fraz()
