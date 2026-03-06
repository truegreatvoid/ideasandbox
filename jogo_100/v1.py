from time import sleep


def o_jogo():
    """
    Rascunho
    """
    pass


RANGE_INPUT = list(range(1, 9 + 1))
RANGE_RESET = list(range(1, 2 + 1))
OPTION_LIST = {"1": "(1) Jogar novamente", "2": "(2) Sair"}


def check_limit(x: int, y: int) -> bool:
    return True if x < y else False


def ckech_limit_range(x: int, y: int) -> bool:
    return True if x >= y + 1 else False


# def check_input(x: int) -> bool:
#     # return True (x > 0 or x < 9) else False
#     # return True x in range(1,9) else False
#     return x in range(1, 9)


def sum_value(value_input: int, value_soma: int):
    return value_soma + value_input


def player_switch(player_1: bool) -> bool:
    return not player_1


def player_label(player_1: bool) -> str:
    return "Player 1" if player_1 else "Player 2"


def gz(player_1: bool, value_soma: int) -> str:
    return f"Parabéns para o {player_label(player_1)}, você venceu! Soma final: {value_soma}."


def check_range(x: int, y: list) -> bool:
    return x in y


def option_list(x):
    return "\n".join(f"{key} - {value}" for key, value in x.items())


def rerun():
    is_over = True

    print(f"""
===============
Fim de jogo
Para continuar, digite:
Escolha:
{option_list(OPTION_LIST)}
===============
""")

    while is_over:
        try:
            value_reset = int(input("Digite sua escolha: "))
        except ValueError:
            print("Opção inválida!")
            continue

        match value_reset:
            case 1:
                print(f"""
===============
Opção escolhida: {value_reset}
===============
                """)
                sleep(2)
                return play()

            case 2:
                sleep(2)
                return exit_game()

            case _:
                print(
                    f"Opção inválida! Escolha as opções validas: {list(OPTION_LIST.keys())}"
                )
                continue


def exit_game():
    print("Saiu do jogo!")
    exit()


def play():
    player_1 = True

    value_soma = int(0)
    value_input = int(0)
    value_limit = 100

    result = check_limit(value_soma, value_limit)

    while result:
        print(f"Soma atual dos valores: {value_soma}")

        try:
            value_input = int(
                input(
                    f"Jogador {player_label(player_1)}, escolha um número entre 1 e 9? "
                )
            )
        except ValueError:
            print("Número inválido!")
            continue

        if not check_range(value_input, RANGE_INPUT):
            print("Número inválido! Escolha entre 1 e 9.")
            continue

        value_temp = sum_value(value_input, value_soma)

        if ckech_limit_range(value_temp, value_limit):
            print("Soma ultrapassou limite!")
            continue

        value_soma = value_temp

        if not check_limit(value_soma, value_limit):
            print(gz(player_1, value_soma))
            rerun()
            return

        player_1 = player_switch(player_1)


play()
