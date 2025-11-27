import os
from core.cores import Cores

stdInput = 0
stdOutput = 1

def ler_comando():
    dir_absoluto = os.getcwd()
    dir_atual = dir_absoluto.split('/')[-1]

    prompt = f"{Cores.VERDE}{dir_atual}{Cores.RESET} > "
    os.write(stdOutput, prompt.encode())

    entrada_bytes = os.read(stdInput, 1024) #Os.write trabalha em bytes
    
    if not entrada_bytes: #tratar Ctrl+D
        raise EOFError
    entrada_limpa = entrada_bytes.decode().strip()


    return entrada_limpa

def print_help():
    prompt = f"vish: Implementação de um shell básico em PYTHON.\n"
    os.write(stdOutput, prompt.encode())