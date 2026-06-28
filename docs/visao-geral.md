# Visao geral do projeto

## Objetivo

O Acesso IFAL tem como objetivo automatizar o controle de uso das salas e
registrar a presenca de professores e alunos com base em eventos verificaveis:
RFID para professores e QR Code para alunos.

## Contexto operacional

1. O professor chega no horario da aula.
2. O professor escaneia o cartao RFID no leitor da sala.
3. O sistema valida se existe aula prevista para aquele professor, sala e
   horario.
4. A sala e liberada e uma sessao de aula e iniciada.
5. Os alunos escaneiam o QR Code da sala para registrar entrada.
6. Ao final, os alunos escaneiam novamente o QR Code para registrar saida.
7. O professor escaneia o cartao RFID para trancar a sala.
8. O sistema encerra a sessao de aula e consolida os registros.

## Integracao com RFID

A integracao fisica com o leitor RFID esta fora deste repositorio por enquanto.
Ela ja existe externamente usando sockets. Este sistema deve expor ou consumir
uma interface clara para receber eventos como:

- codigo/UID do cartao RFID;
- identificador da sala ou dispositivo;
- tipo de evento detectado;
- data e hora do evento;
- metadados tecnicos do leitor, quando existirem.

## Escopo inicial

O sistema deve catalogar e relacionar:

- alunos;
- professores;
- salas;
- cartoes RFID de professores;
- QR Codes de salas;
- horarios e duracao das aulas;
- sessoes de liberacao de sala;
- registros de presenca do professor;
- registros de entrada e saida dos alunos.
