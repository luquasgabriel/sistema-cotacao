# Mapeamento de Pinos - ESP32

Este documento detalha as conexões físicas utilizadas no código do cliente, com o mapeamento e a descrição funcional de cada pino.

---

## Esquema feito no Fritzing

![Esquema](https://lh3.googleusercontent.com/d/1OdcU7BMJvIeZnYeSkOe968MppkN1R-nf)

---

## Componentes do Sistema

| Componente | Funcionalidade Principal |
| :--- | :--- |
| **ESP32** | Gerencia Wi-Fi, conexão com o servidor, lógica RFID e periféricos. |
| **Módulo Leitor de RFID (MFRC522)** | Identificação de usuários via tags/cartões. |
| **Servo Motor** | Mecanismo físico que simula a tranca para abertura da porta. |
| **Display LCD I2C** | Interface visual para as mensagens de status do sistema. |
| **DFPlayer Mini** | Módulo de áudio para feedback sonoro. |
| **LED RGB** | Sinalização luminosa do estado do sistema. |
| **Botão (Push-button)** | Acionamento manual da fechadura pelo lado interno. |

---

## Tabela de Conexões

| Componente | Pino ESP32 | Descrição da Função |
| :--- | :--- | :--- |
| **MFRC522 (SDA/SS)** | 5 | Pino de Habilitação do Módulo |
| **MFRC522 (RST)** | 2 | Pino de Reset de Hardware do Módulo |
| **MFRC522 (SCK)** | 18 | Pino de Clock do Barramento SPI |
| **MFRC522 (MOSI)** | 23 | Pino de Dados de Saída do Mestre (SPI) |
| **MFRC522 (MISO)** | 19 | Pino de Dados de Entrada do Mestre (SPI) |
| **LED Vermelho** | 14 | Pino de Controle de Sinalização para "Acesso Negado" |
| **LED Verde** | 12 | Pino de Controle de Sinalização para "Acesso Permitido" |
| **LED Azul** | 13 | Pino de Controle de Sinalização de Processamento RFID |
| **Servo Motor** | 32 | Pino de Controle de Posicionamento do Servo (PWM) |
| **Botão** | 25 | Pino de Entrada do botão para Acionamento Manual da Fechadura |
| **LCD I2C (SDA)** | 21 | Pino de Dados Serial para Comunicação I2C |
| **LCD I2C (SCL)** | 22 | Pino de Clock Serial para Comunicação I2C |
| **DFPlayer Mini (TX)** | 16 | Pino de Transmissão de Comandos (Serial para Player) |
| **DFPlayer Mini (RX)** | 17 | Pino de Recepção de Dados (Serial do Player) |