## [Memoria](./README.md#Memoria)

### O arquivo `Memoria.py` é responsável por acessar a memória e as informações dos sensores do robô

### A classe `Memoria` contém alguns métodos, dentre eles estão: 

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALMemory`

* #### O método `ler` retorna o valor de um sensor ou algo gravado na memória, é necessário informar a chave (índice)

* #### O método `escrever` grava uma informação na memória, é necessario informar uma chave (índice) e um valor

* #### O método `apagar` apaga um valor na memória, é necessário informar a chave (índice)

* #### O método `inscreverEvento` permite incluir um evento na memória, quando tem alguma alteração no valor da chave informada o evento é chamado

### [Voltar para página anterior](./README.md#Memoria)
