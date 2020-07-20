## [Ouvinte](./README.md#Ouvinte)

### O arquivo `Ouvinte.py` é responsável por controlar os microfones do robô

### A classe `Ouvinte` contém alguns métodos, dentre eles estão: 

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALSpeechRecognition`

* #### O método `idioma` que define o idioma que deve ser utilizado para o reconhecimento de voz. O valor padrão do parâmetro `linguagem` é `Brazilian`

* #### O método `vocabulario` define uma lista de palavras que devem ser reconhecidas, podem especificar o grau de precisão de reconhecimento e também é possével informar se a palavra deve ou não ser ignorada

* #### O método `parametro` determina a configurção de parâmetros para a instância de conexão com a API de reconhecimento de voz. Por padrão foi definido com a configuração do nível de sensibilidade como sensitivo e hipóteses com o valor de 0.2. Recomendo deixar no modo padrão, bastando somente chamar a função sem especificar os valores dos parâmetros

* #### O método `iniciar` é responsável por iniciar a escuta dos microfones e realizar a análise (comparação) do que foi escutado com a lista de palavras que foi definida previamente. Essa função recebe dois parâmetros, o primeiro indica um callback que será chamado sempre que for reconhecida uma palavra, o segundo parâmetro informa por padrão que essa tarefa deve ser realizada de forma assíncrona, ou seja, sem bloquear o fluxo de execução do código Python

* #### O método `pausar` é usado quando necessitamos que o robô pare de escutar por um determinado momento. Se a função for chamada sem especificar o valor do parâmetro, ela se auto responsábiliza por pausar ou não o reconhecimento de voz. Caso deseje informar o seu modo de funcionamento, coloque `True` para pausar e `False` para remover a pausa

* #### O método `parar` tem a função de encerrar o reconhecimento de voz, podendo ser utilizado de duas formas. Na primeira forma, se não for especificado o valor do parâmetro `timer` ele encerra de imediato a reconhecimento de voz, já no segundo modo, o parâmetro `timer` recebe um tempo em segundos, onde esse tempo será utilizado como um contador (agendador de tarefa), quando o tempo acabar o reconhecimento de voz é finalizado

### [Voltar para página anterior](./README.md#Ouvinte)
