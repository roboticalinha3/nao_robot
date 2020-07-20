## [Led](./README.md#Led)

### O arquivo `Led.py` é responsável por manusear a iluminação led existente no robô

### A classe `Led` contém alguns métodos, dentre eles estão: 

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALLeds`

* #### O método `hexParaRGB` retorna uma tupla contendo o resultado da conversão de hexadecimal para RGB

* #### O método `mudar` permite mudar as cores de um grupo de Leds, usando o modo RGB ou hexadecimal

* #### O método `mudar` permite ligar ou desligar um grupo de Leds

* #### O método `botoesCabeca` possibilita ativar os três segmentos (Frente, Meio e Trás) de iluminação dos botões da cabeça, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `botoesCabecaFrente` possibilita ativar o primeiro segmento (Frente) de iluminação dos botões da cabeça, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `botoesCabecaMeio` possibilita ativar o segundo segmento (Meio) de iluminação dos botões da cabeça, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `botoesCabecaTras` possibilita ativar o terceiro segmento (Trás) de iluminação dos botões da cabeça, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `orelhas` possibilita ativar a iluminação da orelha esquerda e direita, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `orelhaEsquerda` possibilita ativar a iluminação da orelha esquerda, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `orelhaDireita` possibilita ativar a iluminação da orelha direita, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `olhos` possibilita definir as cores da iluminação dos olhos, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `olhoEsquerdo` possibilita definir as cores da iluminação do olho esquerdo, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `olhoDireito` possibilita definir as cores da iluminação do olho direito, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `botaoPeito` possibilita definir as cores da iluminação do botão do peito, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `pes` possibilita definir as cores da iluminação dos pés, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `peEsquerdo` possibilita definir as cores da iluminação do pé esquerdo, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `peDireito` possibilita definir as cores da iluminação do pé direito, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `corpo` possibilita definir as cores da iluminação do corpo, é necessário informar um valor de intencidade do vermelho, verde e azul ou o código hexadecimal, o valor deve está no intervalo de 0 até 255, por padrão o valor das três cores é 0 que representa desligado

* #### O método `corpoVermelho` possibilita ativar a iluminação da corpo vermelho, é necessário informar um valor de intencidade do vermelho, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `corpoVerde` possibilita ativar a iluminação da corpo verde, é necessário informar um valor de intencidade do verde, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `corpoAzul` possibilita ativar a iluminação da corpo azul, é necessário informar um valor de intencidade do azul, o valor deve está no intervalo de 0 até 255, por padrão o valor é 0 que representa desligado

* #### O método `corpoRGB` alterna entre as cores do RGB, por padrão o valor informado é `True` que faz com que todo o processo de mudança das cores ocorra de modo assíncrono

### [Voltar para página anterior](./README.md#Led)
