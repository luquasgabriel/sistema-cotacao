# Requisitos do sistema

## Requisitos funcionais

### Usuarios e perfis

- O sistema deve manter usuarios autenticaveis.
- O sistema deve diferenciar pelo menos administradores, professores e alunos.
- O cadastro de professor deve permitir associar um cartao RFID com o
  codigo/UID unico lido pelo leitor.
- O cadastro de aluno deve permitir identificar matricula, nome, turma ou curso.

### Salas

- O sistema deve catalogar salas.
- Cada sala deve possuir um identificador unico.
- Cada sala deve possuir um QR Code usado para registro de entrada e saida dos
  alunos.
- Cada sala pode estar livre, liberada para aula, bloqueada ou em manutencao.

### Aulas e horarios

- O sistema deve registrar aulas planejadas com professor, sala, turma, horario
  de inicio e horario de termino.
- O sistema deve considerar tolerancias configuraveis para abertura antecipada,
  atraso e encerramento.
- O sistema deve registrar a duracao real da aula com base nos eventos de
  abertura e fechamento.

### Liberacao por RFID

- O sistema deve validar o codigo/UID do cartao RFID do professor.
- O sistema deve liberar a sala somente quando a regra de horario permitir.
- O sistema deve criar uma sessao de aula quando a sala for aberta.
- O sistema deve encerrar a sessao quando o professor usar o RFID para fechar a
  sala.
- O sistema deve registrar tentativas negadas com motivo.

### Presenca por QR Code

- O aluno deve registrar entrada escaneando o QR Code da sala durante uma sessao
  de aula aberta.
- O aluno deve registrar saida escaneando o QR Code da sala antes ou no momento
  de encerramento.
- O sistema deve impedir presenca em sala sem sessao de aula ativa.
- O sistema deve evitar registros duplicados indevidos.
- O sistema deve guardar horario de entrada, horario de saida e status da
  presenca.

### Auditoria

- O sistema deve registrar eventos relevantes de acesso.
- Eventos de RFID e QR Code devem manter data e hora.
- Eventos negados devem preservar o motivo para auditoria.

## Requisitos nao funcionais

- O backend deve ser desenvolvido em Django.
- O banco atual configurado e PostgreSQL.
- O codigo deve ser escrito em ingles.
- A documentacao deve ser escrita em portugues.
- O sistema deve usar timezone configurado para o contexto local do IFAL.
- Validacoes de acesso devem ocorrer no servidor.
- Segredos e configuracoes devem ficar em variaveis de ambiente.

## Fora do escopo imediato

- Implementacao fisica do leitor RFID.
- Firmware ou software embarcado dos dispositivos de porta.
- Catracas ou controle de acesso externo ao fluxo de salas.
