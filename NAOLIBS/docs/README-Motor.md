## [Motor](./README.md#Motor)

### O arquivo `Motor.py` é responsável por controlar os motores do robô

### A classe `Motor` contém alguns métodos, dentre eles estão: 

* #### O método `movimento` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALMotion`

* #### O método `angulo` serve para definir o angulor em um determinado motor, requer que seja informado três parâmetros, sendo o primeiro o `nome` do motor, o segundo `tempo` em que deve levar para realizar a mudança de ângulo, o terceiro chama-se `angulo` que corresponde propriamente ao ângulo

* ## Eu (Matheus Johann Araújo), menciono desde já, que os métodos de controle dos braços (**`bracoEsquerdo(params...)` e `bracoDireito(params...)`**) do robô foram desenvolvidos por: Laura Gabrielle de Lira Silva e Wesley Oliveira de Souza

* #### O método `bracos` permite controlar o ângulo dos braços esquerdo e direito, e possui os parâmetros `nome`, `angulo`, `tempo`, `rigidez` e `async`. O único parâmetro obrigatório é o `nome` dos motores, que são:

>> * ### `antebraco` intervalo de ângulo `-120` até `120`
>> * ### `mao` intervalo de ângulo `-105` até `105`
>> * ### `cotovelo` intervalo de ângulo `-90` até `0`
>> * ### `ombro` intervalo de ângulo `-18` até `80`

* #### O método `bracoEsquerdo` permite controlar o ângulo do braço esquerdo, e possui os parâmetros `nome`, `angulo`, `tempo`, `rigidez` e `async`

* #### O método `bracoDireito` permite controlar o ângulo do braço direito, e possui os parâmetros `nome`, `angulo`, `tempo`, `rigidez` e `async`

* #### O método `cabecaDireita` permite movimentar a cabeça do robô para o lado direito, sendo necessário informar nos parâmetros o ângulo que o motor deve realizar e o tempo para conclusão do movimento

* #### O método `cabecaEsquerda` permite movimentar a cabeça do robô para o lado esquerdo, sendo necessário informar nos parâmetros o ângulo que o motor deve realizar e o tempo para conclusão do movimento

* #### O método `cabecaBaixo` permite movimentar a cabeça do robô para baixo, sendo necessário informar nos parâmetros o ângulo que o motor deve realizar e o tempo para conclusão do movimento

* #### O método `cabecaCima` permite movimentar a cabeça do robô para cima, sendo necessário informar nos parâmetros o ângulo que o motor deve realizar e o tempo para conclusão do movimento

* #### O método `cabecaCentro` movimenta a cabeça do robô para a posição central (inicial)

* #### O método `rigidez` possibilita definir a intencidade da rigidez do motor ou de um grupo de motores. Sendo necessário informar nos parâmetros o nome do motor, o valor da rigidez (0 até 100) e o tempo de duração

* #### O método `rigidezCabeca` define a porcentagem da rigidez do motor da cabeça do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezBracoEsquerdo` define a porcentagem da rigidez dos motores do braço esquerdo do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezBracoDireito` define a porcentagem da rigidez dos motores do braço direito do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezBracos` define a porcentagem da rigidez dos motores do braço esquerdo e direito do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezPernaEsquerda` define a porcentagem da rigidez dos motores da perna esquerda do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezPernaDireita` define a porcentagem da rigidez dos motores da perna direita do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezPernas` define a porcentagem da rigidez dos motores da perna esquerda e direita do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `rigidezCorpo` define a rigidez dos motores de todo o corpo do robô, o valor a ser informado no parâmetro deve ser de `0` até `100`

* #### O método `maoEsquerda` permite realizar o fechamento ou abertura da mão esquerda do robô. Se o valor do parâmetro `abrir` for `True` a mão é aberta, no caso de ser `False` a mão será fechada

* #### O método `maoDireita` permite realizar o fechamento ou abertura da mão direita do robô. Se o valor do parâmetro `abrir` for `True` a mão é aberta, no caso de ser `False` a mão será fechada

* #### O método `maos` permite realizar o fechamento ou abertura de ambas as mãos do robô de modo simultâneo. Se o valor do parâmetro `abrir` for `True` a mão é aberta, no caso de ser `False` a mão será fechada

* #### O método `moverPernas` tem a função de movimentar as pernas do robô para fazê-lo andar. Possui quatro parâmetros, sendo o último opcional, o primeiro indica a direção de locomoção através do eixo X do plano cartesiano, o valor a ser informado deve sem um numeral em metros, o segundo indica a direção de locomoção através do eixo Y e o valor a ser informado deve um número em metros, o terceiro parâmetro informa a rotação do robô em torno de seu próprio eixo a medida deve ser dada em graus

* #### O método `pararAndar` realiza o ato de cancelar o movimento das pernas do robô

* #### O método `andarFrente` faz com que o robô se mova para frente. A função recebe dois parâmetros, ambos opcionais, o primeiro indica a distância em metros que deve se deslocar no eixo X, o valor padrão atribuído é `0.025`, já o segundo parâmetro é um multiplicador da distância, seu valor padrão é `1`

* #### O método `andarTras` faz com que o robô se mova para trás. A função recebe dois parâmetros, ambos opcionais, o primeiro indica a distância em metros que deve se deslocar no eixo X, o valor padrão atribuído é `0.025`, já o segundo parâmetro é um multiplicador da distância, seu valor padrão é `1`

* #### O método `andarEsquerda` faz com que o robô se mova para esquerda. A função recebe dois parâmetros, ambos opcionais, o primeiro indica a distância em metros que deve se deslocar no eixo Y, o valor padrão atribuído é `0.025`, já o segundo parâmetro é um multiplicador da distância, seu valor padrão é `1`

* #### O método `andarDireita` faz com que o robô se mova para direita. A função recebe dois parâmetros, ambos opcionais, o primeiro indica a distância em metros que deve se deslocar no eixo Y, o valor padrão atribuído é `0.025`, já o segundo parâmetro é um multiplicador da distância, seu valor padrão é `1`

* #### O método `andarGirandoHorario` faz o movimento de giro no sentido horário em torno do próprio eixo do robô. A função recebe como parâmetro um valor em graus

* #### O método `andarGirandoAntiHorario` faz o movimento de giro no sentido anti-horário em torno do próprio eixo do robô. A função recebe como parâmetro um valor em graus

* #### O método `postura` permite alterar as posturas existentes no robô. As posturas são `Stand`, `StandInit`, `StandZero`, `Crouch`, `Sit` e outras. A função postura recebe como parâmetros o nome da postura e a velocidade em que deve ocorre a alterar entre a postura atual para a postura informada. A velocidade é um valor entre `0` (0%) até `1` (100%), o valor padrão da velocidade é `0.5` (50%)

* #### O método `posturaStand` permite alterar a postura atual do robô para a postura `Stand`. O parâmetro `vel` (velocidade) é opcional, seu valor padrão é `0.5` (50%)

* #### O método `posturaStandInit` permite alterar a postura atual do robô para a postura `StandInit`. O parâmetro `vel` (velocidade) é opcional, seu valor padrão é `0.5` (50%)

* #### O método `posturaStandZero` permite alterar a postura atual do robô para a postura `StandZero`. O parâmetro `vel` (velocidade) é opcional, seu valor padrão é `0.5` (50%)

* #### O método `posturaCrouch` permite alterar a postura atual do robô para a postura `Crouch`. O parâmetro `vel` (velocidade) é opcional, seu valor padrão é `0.5` (50%) e após ser realizada a mudança da postura é reduzida a rigidez dos motores para `20%`

* #### O método `posturaSit` permite alterar a postura atual do robô para a postura `Sit`. O parâmetro `vel` (velocidade) é opcional, seu valor padrão é `0.5` (50%) e após ser realizada a mudança da postura é reduzida a rigidez dos motores para `20%`

### [Voltar para página anterior](./README.md#Motor)
