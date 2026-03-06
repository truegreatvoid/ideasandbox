def o_jogo() -> None:
    """
    Jogo do 100

    > ./v1.py > Rascunho

    > ./v2.py > Melhorias

    Melhorias:
    - Melhorar o código utilizando classes
    - Número de jogadores
    - Número de tentativas para jogar novamente
    - Número de limite de tentativas por jogador
    - Personalização do Limite (soma máxima)
    - Jogar com o computador
    """
    pass


class Jogasso:
    def __init__(
        self,
        player_count: int = 2,
        player_1: bool = True,
        value_soma: int = 0,
        value_limit: int = 100,
    ):
        self.player_count = player_count
        self.value_soma = value_soma
        self.value_limit = value_limit
        self.value_input = int(0)


if __name__ == "__main__":
    print("Bem vindo ao jogo do 100!")
