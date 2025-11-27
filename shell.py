import os
from core.io_utils import ler_comando, print_help
from core.comandos import executar_comando, cd
from core.cores import Cores
stdInput = 0
stdOutput = 1




def main():
    while True:
        try:
            entrada = ler_comando()
            if entrada == "exit":
                break
            elif entrada[:3] == "cd ":
                cd(entrada[3:])
            elif entrada == "help":
                print_help()
            else:
                executar_comando(entrada)
        except KeyboardInterrupt:
            os.write(stdOutput, b"\n")
            continue
        except EOFError:
            prompt = f"{Cores.AMARELO}\nSaindo do shell...\n{Cores.RESET}"
            os.write(stdOutput, prompt.encode())
            break


if '__main__' == __name__:
    main()