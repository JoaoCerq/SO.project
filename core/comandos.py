import os
from core.cores import Cores

stdInput = 0
stdOutput = 1

def cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except OSError as e: 
        erro = os.strerror(e.errno) 
        prompt = f"{Cores.VERMELHO}cd: falha ao entrar em '{path}': {erro}{Cores.RESET}\n"
        os.write(stdOutput, prompt.encode())


def executar_pipe(command_input):

    backup_std_in = os.dup(0)
    backup_std_out = os.dup(1)
            
    fdin = os.dup(backup_std_in)

    lista_comandos = command_input.split("|")
    num_comandos = len(lista_comandos)

    try:
        for i, cmd in enumerate(lista_comandos): #iterando sobre os comandos recebidos
            args = cmd.strip().split()
            if not args: continue
            os.dup2(fdin, 0) #configura a entrada do processo
            os.close(fdin)

            if i == num_comandos - 1: #se é o último comando, ele tem que usar a saída padrão
                fdout = os.dup(backup_std_out)
            else:
                fdin, fdout = os.pipe() #criao pipe: saída do atual = entrada do próximo

            os.dup2(fdout, 1)
            os.close(fdout)


            try:
                pid = os.fork()
            
                if pid == 0:
                    try:
                        os.execvp(args[0], args)
                    except OSError as e:
                        msg_erro = os.strerror(e.errno)
                        prompt = f"{Cores.VERMELHO}vish error ao executar '{args[0]}': {msg_erro} -> '{args[0]}'{Cores.RESET}\n"
                        os.write(stdOutput, prompt.encode())
                        if e.errno == 2: #ENOENT (Erro NO ENTity)
                            prompt = f"Verifique se digitou o nome certo.\n"
                            os.write(stdOutput, prompt.encode())
                            os._exit(1)
                    except Exception as e:
                        prompt = f"Erro ao executar: {e}"
                        os.write(stdOutput, prompt.encode())
                        os._exit(1)
                
                elif pid > 0:
                    _, status = os.wait() #os.wait() retorna (pid, status), pegamos só o status se quiser verificar erro   
                    os.write(stdOutput, b"\n")
                    if os.WEXITSTATUS(status) != 0:
                        pass  
                else:
                    print("Erro ao criar processo (fork falhou)")
                    
            except OSError as e:
                os.write(2, f"Erro no fork: {e}\n".encode())
    finally:
        #recupera o teclado e a tela originais para o Shell voltar ao normal
        os.dup2(backup_std_in, 0)
        os.dup2(backup_std_out, 1)
        os.close(backup_std_in)
        os.close(backup_std_out)

def executar_comando(command_input):
    if "|" in command_input: # Checagem de Pipe
        executar_pipe(command_input)
        return 
    
    args = command_input.strip().split() #Spara comando e args
    
    if not args:
        return #volta sem fazer nada

    
    pid = os.fork() #cria processo filho

    if pid == 0:

        # PROCESSO FILHO
        try:
            os.execvp(args[0], args) #substitui a imagem do processo pelo comando


        except OSError as e:
            msg_erro = os.strerror(e.errno)
            prompt = f"{Cores.VERMELHO}vish error ao executar '{args[0]}': {msg_erro} -> '{args[0]}'{Cores.RESET}\n"
            os.write(stdOutput, prompt.encode())
            if e.errno == 2: #ENOENT (Erro NO ENTity)
                prompt = f"Verifique se digitou o nome certo.\n"
                os.write(stdOutput, prompt.encode())
            os._exit(1)

        except Exception as e:
            prompt = f"Erro ao executar: {e}"
            os.write(stdOutput, prompt.encode())
            os._exit(1)


    elif pid > 0: #processo PAI "O processo pai deve aguardar o término do filho usando wait( ) ou os.wait ( )"
        # o pai tem q esperar o filho terminar
        _, status = os.wait() #os.wait() retorna (pid, status), pegamos só o status se quiser verificar erro   
        os.write(stdOutput, b"\n")
        if os.WEXITSTATUS(status) != 0:
             pass       
    else:
        print("Erro ao criar processo (fork falhou)")