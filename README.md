# Contador de Dedos

Este projeto utiliza a biblioteca OpenCV e o MediaPipe para detectar e contar o número de dedos levantados em uma imagem de vídeo em tempo real.

## Requisitos

- Python 3.x
- OpenCV
- MediaPipe

## Instalação

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd contador_dedos
    ```
3. Instale as dependências:
    ```sh
    pip install opencv-python mediapipe
    ```

## Uso

1. Execute o script `contador_de_dedos.py`:
    ```sh
    python contador_de_dedos.py
    ```
2. O script abrirá uma janela de vídeo que mostrará a contagem total de dedos levantados.

## Funcionamento

- O script captura o vídeo da câmera.
- Utiliza o MediaPipe para detectar as mãos e os pontos de referência.
- Conta o número de dedos levantados com base na posição dos pontos de referência.
- Exibe a contagem total de dedos levantados na tela.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.
