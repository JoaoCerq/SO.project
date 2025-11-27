================================================================================

------> Como compilar e rodar   


Não é necessário compilar — o shell foi programado em Python.

Requisitos

Python

Sistema operacional Unix-like (Linux, macOS ou WSL)

Para rodar

Dentro do diretório do projeto (shell/):

python shell.py


ou, se estiver na pasta acima:

python -m shell.shell


O prompt será exibido no formato:

nome_da_pasta > 


================================================================================

------> Quais chamadas ao sistema foram utilizadas


hamada	                    Função	                               
os.read()	leitura de entrada padrão                
os.write()	escrita em saída padrão          
os.fork()	criação de processo filho	                       
os.execvp()	substitui a imagem do processo	                 
os.wait()	espera o término do processo filho             
os.pipe()	cria um canal de comunicação               
os.dup()	duplica descritores de arquivo	                  
os.dup2()	redireciona descritores	     
os.close()	fecha descritores redundantes	                    
os.chdir()	muda o diretório atual


================================================================================

------> Exemplos de comandos testados e suas saídas ( em ordem de execução)

Comando                                                     Saída esperada:

echo Olá mundo!                                         Olá mundo!

ls                                                      core  readme.txt  shell.py  teste

cd teste                                                teste > (terminal)

ls                                                      Lorem_ipsum.txt  testes.txt

cd ..                                                   shell > (terminal)

ls teste                                                Lorem_ipsum.txt  testes.txt

cat teste/Lorem_ipsum.txt                               Lorem ipsum 

cat teste/Lorem_ipsum.txt | grep -w in                  Duis aute irure dolor in reprehenderit in voluptate 
                                                        velit esse cillum dolore eu fugiat nulla pariatur. 
                                                        Excepteur sint occaecat cupidatat non proident, sunt 
                                                        in culpa qui officia deserunt mollit anim id est laborum.

cat teste/Lorem_ipsum.txt | grep -w in | wc -l          3

comando_inexistente                                     vish error ao executar 'comando_inexistente': No such file or directory -> 'comando_inexistente'
                                                        Verifique se digitou o nome certo.

ctrl + D                                                Saindo do shell...

================================================================================

------> Limitações conhecidas da implementação.

Sem histórico de comandos	                Não há persistência de histórico ou setas para navegação.

Sem tratamento avançado de sinais	        Apenas Ctrl+C (KeyboardInterrupt) e Ctrl+D (EOF) são tratados







