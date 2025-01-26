from time import sleep


class Rascheti:
    summa_ojidaniua = 0.0

    def rascheti_int(*args):
        proizvedenie = 1
        kolvo = 0
        time_sleep = 0.5
        Rascheti.summa_ojidaniua += time_sleep
        while kolvo < args[1]:
            proizvedenie *= 2 ** kolvo
            kolvo += 1
        sleep(time_sleep)
        print(f"\nЗавершился {args[0]}, задержка {time_sleep}. ", end="")

    def rascheti_float(*args):
        proizvedenie = 1.0
        kolvo = 0
        time_sleep = 0.5
        Rascheti.summa_ojidaniua += time_sleep
        while kolvo < args[1]:
            proizvedenie *= 1.3349 ** kolvo
            kolvo += 1
        sleep(time_sleep)
        print(f"\nЗавершился {args[0]}, задержка {time_sleep}. ", end="")
