## [Sistema](./README.md#Sistema)

### O arquivo `Sistema.py` é responsável por controlar e acessar as informações do sistema do robô

### A classe `Sistema` contém alguns métodos, dentre eles estão: 

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALSystem`

* #### O método `reiniciar` é responsável por realizar o processo de reinicialização do robô

* #### O método `desligar` possui a função de executar o desligamento do robô

* #### O método `robotName` permite a alteração do nome do robô

* #### O método `comando` requer que seja informado um comando (sh ou bash) para ser executado no sistema do robô

* #### O método `reiniciarNAO` reinicializa somente a API do NAOqi, essa função é muito util no caso de travamentos. Pois permite restaurar o acesso as funcionalidades do robô de modo mais rápido, sem precisar reiniciar todo o sistema operacional do robô

* #### O método `rede` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALConnectionManager`

* #### O método `redeWifi` alterna o modo de funcionamento da antena wireless do robô, podendo ser utilizada como `wifi station host` (robô conectado a uma rede wireless) ou `wifi access point` (o robô vira um roteador). A função possui dois parâmetros, o primeiro indica o `ssid` (nome) e o segundo `password` (a senha) da rede no modo access point. Por padrão o `ssid` da rede é o nome do robô e a `password` é `0123456789`

### [Voltar para página anterior](./README.md#Sistema)
