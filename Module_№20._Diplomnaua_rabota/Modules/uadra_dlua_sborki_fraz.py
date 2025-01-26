import multiprocessing
from .TandM_sborka_frazi import SborkaFrazi

uadro = multiprocessing.Process


def zapysk_uader_dlua_sborki_fraz():
    uadro_pervoe = uadro(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №1", 200, 15000))
    uadro_vtoroe = uadro(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №2", 100, 15000))
    uadro_tretie = uadro(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №3", 50, 15000))
    uadro_chetvertoe = uadro(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №4", 200, 30000))
    uadro_puatoe = uadro(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №5", 100, 30000))
    uadro_shestoe = uadro(target=SborkaFrazi.sborka_frazi, args=("\nЗавершилась сборка фразы №6", 50, 30000))
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
    print(f"\nСумма задержки ядер: {SborkaFrazi.summa_ojidaniua} секунд(а, ы).")
    SborkaFrazi.summa_ojidaniua = 0.0


if __name__ == '__main__':
    zapysk_uader_dlua_sborki_fraz()
