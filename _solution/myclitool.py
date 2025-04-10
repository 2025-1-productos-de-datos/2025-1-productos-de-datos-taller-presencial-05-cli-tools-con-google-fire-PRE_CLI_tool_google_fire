"""Command line interface (CLI) tool"""

#
# Estructura:
#
# mycli +--- command_1
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#       |
#       +--- command_2
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#


import fire


class Command1:
    """Comandos relacionados con COMMAND1"""

    @staticmethod
    def run(a: str):
        """Ejecuta un subcomando 1-1"""
        print(f"\n---> Ejecutando command 1 subcommand 1: a = {a}\n")

    @staticmethod
    def stop(b: str):
        """Ejecuta un subcomando 1-2"""
        print(f"\n---> Ejecutando command 1 subcommand 2: b = {b}\n")


class Command2:
    """Comandos relacionados con COMMAND2"""

    @staticmethod
    def jump(c: str):
        """Ejecuta un subcomando 2-1"""
        print(f"\n---> Ejecutando command 2 subcommand 1: c = {c}\n")

    @staticmethod
    def cry(d: str):
        """Ejecuta un subcomando 2-2"""
        print(f"\n---> Ejecutando command 2 subcommand 2: d = {d}\n")


class MyCLI:
    """Herramienta de linea de comandos"""

    command1 = Command1
    command2 = Command2


if __name__ == "__main__":
    fire.Fire(MyCLI)