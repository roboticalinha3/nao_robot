## [Comportamento](./README.md#Comportamento)

### O arquivo `Comportamento.py` é responsável por manusear as opções de comportamentos existentes na memória do robô

### A classe `Comportamento` contém alguns métodos, dentre eles estão:

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALBehaviorManager`

* #### O método `listar` retorna uma lista com o nome de todos os comportamentos existentes na memória do robô

* #### O método `iniciar` inicia a execução de um comportamento, é necessário informar o nome do comportamento que deve ser chamado

* #### O método `parar` para a execução de um comportamento, é necessário informar o nome do comportamento que deve ser parado, e aplica por padrão a postura `Crouch`

* #### O método `pararTodos` para a execução de todos os comportamentos, e aplica por padrão a postura `Crouch`

### [Voltar para página anterior](./README.md#Comportamento)
