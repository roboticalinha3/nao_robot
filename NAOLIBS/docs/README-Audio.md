## [Audio](./README.md#Audio)

### O arquivo `Audio.py` é responsável por criar controlar os auto-falantes do robô

### A classe `Audio` contém alguns métodos, dentre eles estão:

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), é necessário informar um número (1 até 4) que indica qual API do robô o NAOLIBS deve se conectar, e tem como retorna da função a conexão com a API

> * ### O de número 1 acessa o `ALAudioDevice`
> * ### O de número 2 acessa o `ALAudioPlayer`
> * ### O de número 3 acessa o `ALTextToSpeech`
> * ### O de número 4 acessa o `ALAnimatedSpeech`

* #### O método `volume` permite altera e obter o volume do global robô, essa função sempre retorna o valor do volume atual, quando recebe algum valor no parâmetro `vol` de 0 até 100 o volume é alterado:

> * ### `Audio.volume(75)` o volume foi alterado e retorna o volume atual 75%
> * ### `Audio.volume()` retorna o volume atual

* #### O método `iniciarMusica` permite executar (tocar) um arquivo de áudio que está dentro do robô, é necessário informa no parâmetro o nome ou caminho da localização do arquivo de som. E a função tem como retorno um `id` (identificador) de onde está executando o arquivo de áudio.

> * #### O parâmetro `name` indica o nome do arquivo de som
> * #### O parâmetro `begin` indica o ínicio de onde deve ser tocado o arquivo de som, valor padrão é 0
> * #### O parâmetro `volume` indica o nível de volume que o arquivo de áudio de tocar, o valor de ser de 0 até 100, o valor padrão é 100
> * #### O parâmetro `balance` indica o nível de volume em cada lado (direita e esquerda) dos auto-falantes, o valor padrão é 0 que indica que ambos os lados teram o mesmo volume
> * #### O parâmetro `path` indica o caminho de onde o arquivo de som se encontra
> * ### É obrigatório informar o parâmetro `name` ou `path`, exemplos:
>> * ### `Audio.iniciarMusica(name = "DancaDoPSY.mp3", begin = 0, volume = 100, balance = 0)`
>> * ### `Audio.iniciarMusica(path = "/home/nao/DancaDoPSY.mp3", begin = 0, volume = 100, balance = 0)`

* #### O método `pararMusica` prove uma forma de encerrar o tocar de um arquivo de áudio, sendo necessário indicar na chamada da função o `id` de execução da música. Exemplo:

>> * ### `Audio.pararMusica(id)`

* #### O método `pararMusicas` permite encerrar todos os arquivos de áudio em execução. Exemplo:

>> * ### `Audio.pararMusicas()`

* #### O método `falar` possibilita transcrever uma frase ou texto em um fala, é possível personalizar o modo em que o texto será dito, como velocidade da fala, intonação, fala animada com gestos e tipo de movimentação dos gestos. Exemplo:

> * #### `Audio.falar(texto, animado = False, speed = 80, voice_shaping = 100, configuracao = { "speakingMovementMode": "contextual", "bodyLanguageMode": "contextual" }, async = False)`
> * #### O parâmetro `texto` indica o conteúdo do texto que deve ser transcrito em fala
> * #### O parâmetro `animado` indica se durante a fala do texto o robô deve realizar gestos, os valores aceitos são `True` e `False`, o valor padrão é `False`. Observação: Para que funcione corretamente, é necessário que o robô esteja com alguma postura que o deixe em pé, como `Stand`, `StandInit`, `StandZero`, dê preferência pela postura `Stand` e mantenha o robô em pé sem que haja outro código em execução que utiliza os motores, no contrário, pode haver conflitos ao tentar acessar um dos motores que já esteja em uso, resultando em movimentos inesperados e que podem ocasionar danos ao robô
> * #### O parâmetro `speed` define a velocidade em que deve ser dito texto, o valor padrão é 80
> * #### O parâmetro `voice_shaping` configura a intonação da voz do robô, o valor padrão é 100
> * #### O parâmetro `configuracao` deve conter um JSON que informe o modo de operação do gestos, caso esteja com o modo de animação habilitado, o valor padrão é `{"speakingMovementMode": "contextual", "bodyLanguageMode": "contextual"}`

### [Voltar para página anterior](./README.md#Audio)
