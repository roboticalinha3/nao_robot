## <a href="https://matheusjohannaraujo.herokuapp.com">Matheus Johann Araújo</a>

> ##### Country: Brasil
> ##### State: Pernambuco
> ##### Date: 2021-03-22

# Documentação da biblioteca <a href="https://github.com/matheusjohannaraujo/nao_robot/tree/master/NAOLIBS/docs/">NAOLIBS</a>

## A biblioteca NAOLIBS foi criada com o propósito de facilitar o acesso ao controle das funcionalidades do robô humanoide NAO v6

### Requerimentos para funcionar no robô NAO v6

* Necessita ter o [`Python v2.7.14`](https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi) instalado
* Precisa instalar o [`Numpy`](https://pypi.org/project/numpy) e [`OpenCV (cv2)`](https://pypi.org/project/opencv-python)
* Para instalar a biblioteca e as dependencias, é necessário acessar o robô utilizando o protocolo SSH
* Utilizo o [`WinSCP v5.15.3`](https://winscp.net/download/WinSCP-5.15.3-Setup.exe) junto com o [`Putty v0.70`](https://the.earth.li/~sgtatham/putty/0.70/w32/putty-0.70-installer.msi), pois me permite acessar o shell do robô pelo prompt de comando do Putty e transferir os arquivos e pastas no computador para o robô e vice-versa através do WinSCP
* Ou utilize o [`Snowflake SSH GUI`](https://github.com/subhra74/snowflake) no lugar do `WinSCP` e `Putty`, é possível usá-lo em Windows, Linux e macOS

### Se conectando ao robô
* Para se conectar ao robô é necessário saber três coisas, o endereço IP do robô, o usuário e a senha. Em meu caso, o IP é `192.168.0.2`, o usuário se chama `nao` e a senha também é `nao`

* No WinSCP selecione o protocolo `SFTP`, preencha o campo host com o endereço `IP` do robo, e os demais campos, após preencher salve as configurações e marque a opção salvar senha, pois ajuda muito quando se está com pressa

* Feito o login, caso apareça uma mensagem de Sim ou Não sobre uma chave de autenticação, sempre clique em sim

* No WinSCP tem uma opção chamada Putty, ao clicar ele já abre o terminal do Putty, nesse momento será pedido a senha do robô, em meu caso a senha é `nao`

* Quando o computador se conectar ao robô por padrão é feito login no usuário padrão (sem privilégios adminstrativos), para mudar para administrador execute o comando **`su`**, a senha padrão é `root`

* A pasta padrão de login pelo terminal é `/home/nao/`

### Dicas para modificar as configurações do sistema operacional do NAO v6

* O sistema operacional do NAO v6 por padrão não permite a alteração das configurações do sistema do robô, mesmo sendo usuário `root`, para liberar essa trava é necessário executar o comando **`mount -w -o remount /`**, esse comando remonta a unidade `/` (raiz do sistema) com permissão de escrita, lembre-se, este comando só precisa ser executado quando for necessário mexer nas configurações do robô (sistema operacional, NAOqi, etc), se o robô reiniciar ou se hover desconexão do SSH o comando deixa de funcionar, sendo necessário ser executá-lo novamente na nova conexão

* Para instalar o `Numpy` e o `OpenCV` é necessário ter o `pip`, muita das vezes o que já vem instalado no robô pode não funcionar. Recomendo instalar manualmente, para isso, é necessário que o robô esteja em uma rede com acesso a internet. Para baixar o PIP rode o comando **`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`**, feito o download, execute o comando **`python get-pip.py`** para instalar o PIP

* Com o novo **`pip`** já instalado basta somente executar os comandos abaixo para baixar e instalar o Numpy e OpenCV

* > ### `pip install numpy`

* > ### `pip install opencv-python`

### Instalação do NAOLIBS como biblioteca Python no robô NAO v6

* É necessário ter seguido as instruções descritas acima em **`Dicas para modificar as configurações do sistema operacional do NAO v6`**

* Copie a pasta `NAOLIBS` do seu computador para dentro do robô no caminho `/home/nao/`, pelo terminal SSH rode o seguinte comando para executar o arquivo que se encontra em `/home/nao/NAOLIBS/install.sh`

* > ### `cd NAOLIBS; chmod +x install.sh; sed -i -e 's/\r$//' install.sh; ./install.sh; cd ..`

* A mensagem que deve aparecer no terminal é `NAOLIBS - Instalado com sucesso.`

### Usando a biblioteca NAOLIBS

* Pode ser utilizada por meio do interpretador do python (Shell interativo) ou através de um código python

* Entre no Shell Interativo do `Python`, e importe todas as funcinalidades do NAOLIBS com o comando **`from NAOLIBS import *`** ou através do comando **`import NAOLIBS as NL`**

* Fazendo o robô falar, **`Audio.texto("Olah, meu nome eh NAO")`**

* Caso tenha um `arquivo.py`, você pode incluir todas as classes manualmente através da instrução **`from NAOLIBS import os, time, sys, uuid, AsyncThread, Audio, Camera, Comportamento, Config, Led, Memoria, ModoAutonomo, Motor, Sensor, Sistema`** ou importar tudo através do comando **`from NAOLIBS import *`** 

## Arquivos que compõem o software

* [AsyncThread.py](./README.md#AsyncThread)
* [Audio.py](./README.md#Audio)
* [Bateria.py](./README.md#Bateria)
* [Camera.py](./README.md#Camera)
* [Comportamento.py](./README.md#Comportamento)
* [Config.py](./README.md#Config)
* [Led.py](./README.md#Led)
* [Main.py](./README.md#Main)
* [Memoria.py](./README.md#Memoria)
* [MotoAutonomo.py](./README.md#MotoAutonomo)
* [Motor.py](./README.md#Motor)
* [Ouvinte.py](./README.md#Ouvinte)
* [Print.py](./README.md#Print)
* [Sensor.py](./README.md#Sensor)
* [Sistema.py](./README.md#Sistema)

### Cada arquivo citado acima tem em seu contéudo uma classe com o mesmo nome do arquivo, exceto os arquivos `Main.py` e `Config.py`

<strike>
## Main

### O arquivo `Main.py` é utilizado para escrever um código que deve ser executado após a inicialização do NAOqi. Para funcionar é necessário configurar o carregamento do arquivo em ***`/etc/init.d/main-naolibs.sh`***, para isso, escreva `nohup sh /etc/init.d/main-naolibs.sh > /dev/null 2>&1` dentro do arquivo ***`/etc/init.d/naoqi`*** abaixo da linha onde é definida a função `start() {`

### Exemplo de configuração do arquivo ***`/etc/init.d/naoqi`***
```bash
start() {
  nohup sh /etc/init.d/main-naolibs.sh > /dev/null 2>&1 &
  # A linha com o NOHUP foi adicionada!!!
  echo 5 > /proc/sys/vm/swappiness
  local bin=$(basename "${BINARY}")
  .
  .
  .
}

stop() {
  pkill -f /usr/lib/python2.7/NAOLIBS/Main.py
  # A linha com o PKILL foi adicionada!!!
  ebegin "Stopping naoqi"
  local bin=$(basename "${BINARY}")
  .
  .
  .
}
```
</strike>

## Config

### O arquivo `Config.py` é responsável por conter as configurações do robô, por padrão possui uma varíavel chamada `ip_addr` que indica o IP do robô, e outra varíavel chamada `port_num` contendo o número da porta de acesso para conectar a API NAOqi

### O arquivo `Config.py` é responsável por conter as configurações do robô, por padrão possui uma varíavel chamada `ip_addr` que indica o IP do robô, e outra varíavel chamada `port_num` contendo o número da porta de acesso para conectar a API NAOqi

## AsyncThread

### O arquivo `AsyncThread.py` é responsável por criar um fluxo de execução de código paralelo, através da utilização de Threads

#### [Ler mais . . .](./README-AsyncThread.md#AsyncThread)

## Audio

### O arquivo `Audio.py` é responsável por criar controlar os auto-falantes do robô

#### [Ler mais . . .](./README-Audio.md#Audio)

## Bateria

### O arquivo `Bateria.py` é responsável por obter informações relacionadas a bateria do robô

#### [Ler mais . . .](./README-Bateria.md#Bateria)

## Camera

### O arquivo `Camera.py` é responsável por manusear as opções da câmera

#### [Ler mais . . .](./README-Camera.md#Camera)

## Comportamento

### O arquivo `Comportamento.py` é responsável por manusear as opções de comportamentos existentes na memória do robô

#### [Ler mais . . .](./README-Comportamento.md#Comportamento)

## Led

### O arquivo `Led.py` é responsável por manusear a iluminação led existente no robô

#### [Ler mais . . .](./README-Led.md#Led)

## Memoria

### O arquivo `Memoria.py` é responsável por acessar a memória e as informações dos sensores do robô

#### [Ler mais . . .](./README-Memoria.md#Memoria)

## ModoAutonomo

### O arquivo `ModoAutonomo.py` é responsável por manusear o modo autonomo do robô

#### [Ler mais . . .](./README-ModoAutonomo.md#ModoAutonomo)

## Motor

### O arquivo `Motor.py` é responsável por controlar os motores do robô

#### [Ler mais . . .](./README-Motor.md#Motor)

## Ouvinte

### O arquivo `Ouvinte.py` é responsável por controlar os microfones do robô

#### [Ler mais . . .](./README-Ouvinte.md#Ouvinte)

## Print

### O arquivo `Print.py` é responsável por exibir informações no console do robô

### A classe `Print` contém um único método, que é o `__init__` construtor da classe. Esse método recebe como parâmetro o valor que deve ser impresso no console. Exemplo:

* ```Print("Olá meu nome é Matheus")```

## Sensor

### O arquivo `Sensor.py` é responsável por acessar as informações que são fornecidas através dos sensores do robô

#### [Ler mais . . .](./README-Sensor.md#Sensor)

## Sistema

### O arquivo `Sistema.py` é responsável por controlar e acessar as informações do sistema do robô

#### [Ler mais . . .](./README-Sistema.md#Sistema)
