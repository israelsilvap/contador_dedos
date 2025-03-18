import cv2
import mediapipe as mp

# Inicializa a captura de vídeo
video = cv2.VideoCapture(1)

# Inicializa o módulo de solução de mãos do MediaPipe
hands = mp.solutions.hands
# Configura para detectar até 2 mãos
Hands = hands.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = video.read()
    # Aplica espelhamento horizontal para corrigir orientação
    # img = cv2.flip(img, 1)
    
    # Converte a imagem para RGB
    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape

    # Inicializa o contador global de dedos levantados
    total_dedos_levantados = 0

    if handPoints and results.multi_handedness:
        for idx, handLms in enumerate(handPoints):
            # Desenha as conexões de mãos na imagem
            mpDraw.draw_landmarks(img, handLms, hands.HAND_CONNECTIONS)

            pontos = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                pontos.append((cx, cy))

            dedos = [8, 12, 16, 20]
            contador_dedos_mao = 0

            # Checa qual é a mão (direita ou esquerda)
            handLabel = results.multi_handedness[idx].classification[0].label

            # Verifica se os outros dedos estão levantados
            if pontos:
                # Lógica para polegar baseado na mão
                if handLabel == 'Right':
                    # Para mão esquerda, polegar está para a direita (cx menor)
                    if pontos[4][0] < pontos[3][0]:
                        contador_dedos_mao += 1
                else:  # Para mão direita
                    # Para mão direita, polegar está para a esquerda (cx maior)
                    if pontos[4][0] > pontos[3][0]:
                        contador_dedos_mao += 1

                # Verifica se os outros dedos estão levantados (indicador, médio, anelar e mínimo)
                for x in dedos:
                    if pontos[x][1] < pontos[x-2][1]:
                        contador_dedos_mao += 1

            # Adiciona o contador de dedos da mão atual ao contador global
            total_dedos_levantados += contador_dedos_mao

    # Desenha um retângulo e coloca o texto mostrando a contagem total de dedos levantados
    cv2.rectangle(img, (80, 10), (200, 110), (255, 0, 0), -1)
    cv2.putText(img, str(total_dedos_levantados), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)
    print(f"Total de Dedos Levantados: {total_dedos_levantados}")

    # Mostra a imagem com as marcações
    cv2.imshow('Imagem', img)
    cv2.waitKey(1)