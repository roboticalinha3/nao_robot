## [AsyncThread](./README.md#AsyncThread)

### O arquivo `AsyncThread.py` é responsável por criar um fluxo de execução de código paralelo, através da utilização de Threads

### A classe `AsyncThread` contém alguns métodos, dentre eles estão:

* #### O método `start` permite inicializar a execução da tarefa inserida no escopo da `AsyncThread`

* #### O método `stop` permite finalizar a execução da tarefa inserida no escopo da `AsyncThread`

* #### O método `join` faz com que o fluxo de execução que chamou (inicializou) a `Thread` aguarde a finalização da tarefa inserida no escopo da `AsyncThread`

* #### O método `running` retorna o status de execução da tarefa assíncrona, se em execução retorna `True`, no contrário retorna o valor `False`

* #### O método `timer` agenda um tempo limite para que a `Thread` seja finalizada, é necessário informar um valor em segundos, exemplo:

* >  ### `AsyncThread.timer(segundos)`

### [Voltar para página anterior](./README.md#AsyncThread)
