## [Sensor](./README.md#Sensor)

### O arquivo `Sensor.py` é responsável por acessar as informações que são fornecidas através dos sensores do robô

### A classe `Sensor` contém alguns métodos, dentre eles estão: 

* #### O método `adicionar` recebe dois parâmetos, no primeiro deve ser informado o nome do sensor, já no segundo é necessário passar uma função de callback (lambda ou nome da função)

* #### O método `eventos` retorna a lista sensores que estam cadastrados na váriavel `listaEventos`, todos os sensores armazenados possuem um evento (callback) associado

* #### O método `monitor` é utilizado para monitorar o estado dos sensores, sempre que houver uma alteração no estado do sensor ou em seu valor é chamada a função `callback` associada a este sensor, sendo passado como valor de parâmetro do `callback` o valor do estado atual do sensor

* #### O método `cabecaFrente` é responsável por acompanhar o estado do primeiro botão (sensor) da cabeça do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão da cabeça resulta-rá em uma chamada da função de `callback`

* #### O método `cabecaMeio` é responsável por acompanhar o estado do segundo botão (sensor) da cabeça do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão da cabeça resulta-rá em uma chamada da função de `callback`

* #### O método `cabecaTras` é responsável por acompanhar o estado do terceiro botão (sensor) da cabeça do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão da cabeça resulta-rá em uma chamada da função de `callback`

* #### O método `maoDireita` é responsável por acompanhar o estado do botão (sensor) da mão direita do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão da mão resulta-rá em uma chamada da função de `callback`

* #### O método `maoEsquerda` é responsável por acompanhar o estado do botão (sensor) da mão esquerda do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão da mão resulta-rá em uma chamada da função de `callback`

* #### O método `peDireito` é responsável por acompanhar o estado do botão (sensor) do pé direito do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão do pé resulta-rá em uma chamada da função de `callback`

* #### O método `peEsquerdo` é responsável por acompanhar o estado do botão (sensor) do pé esquerdo do robô. Se não for informado um `callback` como parâmetro dessa função, é retornado o estado atual do sensor, no contrário, todo toque no botão do pé resulta-rá em uma chamada da função de `callback`

### [Voltar para página anterior](./README.md#Sensor)
