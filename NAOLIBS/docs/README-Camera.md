## [Camera](./README.md#Camera)

### O arquivo `Camera.py` é responsável por manusear as opções da câmera

### A classe `Camera` contém alguns métodos, dentre eles estão:

* #### O método `conn` serve para acessar o núcleo de interação do hardware do robô (NAOqi API), o retorno da função é uma conexão com a API `ALVideoDevice`

* #### O método `cima` ativa a câmera de cima e desativa a de baixo

* #### O método `baixo` ativa a câmera de baixo e desativa a de cima

* #### O método `iniciarCaptura` inicializa a execução da câmera para captura de imagem

* #### O método `obterCaptura` obtem uma captura de imagem, um único frame

* #### O método `pararCaptura` encerra a execução da câmera para captura de frames

* #### O método `pararCapturas` encerra todas as execuções da câmera que capturam frames de imagem

* #### O método `imagemSalvar` permite salvar uma imagem capturada em disco

* #### O método `imagemRGB` retorna uma captura de imagem já convertida de BGR para o padrão RGB

* #### O método `imagemCinza` retorna a conversão de uma imagem para escala de cinza (preto e branco)

* #### O método `imagemMASK` aplica uma transformação nas cores da imagem, inserindo uma especie de máscara de cor que destaca os elementos na imagem, e retorna o resultado da operação

* #### O método `imagemSaida` obtem uma captura de imagem em RGB, converte para Cinza, aplica a máscara, sobrepõe a imagem Cinza com a máscara e salva o resultado de cada transformação no disco do robô

### [Voltar para página anterior](./README.md#Camera)
