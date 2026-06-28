# Fluxos principais

## Abertura da sala pelo professor

1. O leitor RFID detecta o cartao do professor.
2. O integrador externo envia o evento ao sistema.
3. O sistema localiza o cartao RFID ativo pelo `rfid_uid`.
4. O sistema identifica o professor associado.
5. O sistema verifica se existe aula prevista para o professor na sala e no
   horario permitido.
6. Se a regra for valida, o sistema cria uma `AccessSession` aberta.
7. A sala passa para o estado `in_use`.
8. O evento e registrado como aceito.

Caso a regra falhe, o sistema deve registrar o evento como negado com o motivo.

## Registro de entrada do aluno

1. O aluno escaneia o QR Code da sala.
2. O sistema identifica a sala pelo token do QR Code.
3. O sistema verifica se existe uma `AccessSession` aberta para a sala.
4. O sistema autentica ou identifica o aluno.
5. O sistema cria ou atualiza o `AttendanceRecord` com `checked_in_at`.

## Registro de saida do aluno

1. O aluno escaneia o QR Code da sala novamente.
2. O sistema identifica a sessao aberta.
3. O sistema encontra o registro de presenca do aluno.
4. O sistema grava `checked_out_at`.
5. O sistema recalcula o status da presenca, se necessario.

## Fechamento da sala pelo professor

1. O professor escaneia o cartao RFID.
2. O sistema identifica a `AccessSession` aberta para a sala.
3. O sistema valida se o professor e responsavel pela sessao.
4. O sistema grava `closed_at`.
5. A sala deixa o estado `in_use`.
6. O sistema registra o evento de fechamento.
7. Presencas sem saida podem ser marcadas conforme regra definida pelo projeto.

## Tentativas negadas

Tentativas negadas devem gerar `AccessEvent` para auditoria. Exemplos:

- cartao RFID desconhecido;
- professor sem aula naquele horario;
- sala diferente da aula planejada;
- QR Code usado sem sessao aberta;
- aluno tentando registrar presenca duplicada indevida.
