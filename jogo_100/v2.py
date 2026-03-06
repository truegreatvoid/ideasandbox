CYAN = "\033[96m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
DARKCYAN = "\033[36m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


class Jogasso:
    def __init__(
        self,
        player_count: int = 2,
        value_soma: int = 0,
        value_limit: int = 100,
    ):
        self.player_count = player_count
        self.value_limit = value_limit

        self.player = [f"Player {i + 1}" for i in range(player_count)]
        self.current_player = 0

        self.value_input = int(0)
        self.value_soma = value_soma

        self.limit_attempts_per_player = 3
        self.limit_attempts = self.player_count * self.limit_attempts_per_player

        self.history = []


if __name__ == "__main__":
    print(f"{CYAN}=" * 60)
    print("Bem vindo ao jogo do 100!")
    print("=" * 60)
    print(f"{RESET} " * 20)

    try:
        print(f"{YELLOW}Antes de começar, vamos configurar o jogo!")
        print(" " * 20)
        count_players = int(input("Digite a quantidade de jogadores: "))
        value_limit = int(input("Digite o limite de soma: "))
        print(
            f"{BOLD}{BLUE}Note*: O jogo termina quando o limite de tentativas é atingido. O jogador mais próximo do valor alvo vence.{RESET}"
        )
        limit_attempts = int(input(f"{YELLOW}Digite o limite de tentativas total: "))
        limit_attempts_per_player = int(
            input("Digite o limite de tentativas por jogador: ")
        )

    except ValueError:
        print("Opção ou valor inválido! Favor tentar novamente.")
