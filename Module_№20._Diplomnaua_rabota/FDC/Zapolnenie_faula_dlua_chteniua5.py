with open("faul_dlua_chteniua5.txt", "w", encoding='utf-8') as file:
    desuat_Millionov = 10000000
    odna_Sotnua = 100
    check_I = 100000
    for i in range(1, 1000001):
        file.write(f"{desuat_Millionov + i * odna_Sotnua}\n")
        if i == check_I:
            desuat_Millionov *= 10
            odna_Sotnua *= 10
            check_I += 100000