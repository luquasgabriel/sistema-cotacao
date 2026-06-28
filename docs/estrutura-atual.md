# Analise da estrutura atual

## Estado atual do repositorio

O projeto esta em uma base Django com a seguinte estrutura principal:

- `config/`: configuracoes Django, rotas, ASGI e WSGI;
- `accounts/`: app de usuarios;
- `theme/`: app de tema com Tailwind e DaisyUI;
- `manage.py`: entrada de comandos Django;
- `requirements.txt`: dependencias Python;
- `README.md`: resumo do projeto.

## Pontos adequados aos requisitos

- O projeto ja usa Django, uma escolha adequada para CRUD administrativo,
  autenticacao, permissoes e dashboards.
- O app `accounts` ja define `AUTH_USER_MODEL` customizado, o que facilita
  evoluir perfis de professor e aluno sem depender diretamente do usuario
  padrao do Django.
- O banco configurado e PostgreSQL, adequado para registrar eventos,
  relacionamentos e auditoria.
- O timezone e idioma estao configurados para contexto brasileiro:
  `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Maceio'`.
- O app `theme` ja prepara uma base visual com Tailwind.

## Lacunas em relacao aos requisitos

- Ainda nao existem apps de dominio para salas, aulas, presenca, RFID ou QR
  Code.
- O modelo `User` ainda nao diferencia professor, aluno e administrador.
- Ainda nao existem entidades para `Student`, `Teacher`, `Room`,
  `ClassSchedule`, `AccessSession`, `AttendanceRecord` e `AccessEvent`.
- Ainda nao existem endpoints ou servicos para receber eventos da integracao
  externa via sockets/RFID.
- Ainda nao existem telas para cadastro de alunos, professores, salas e horarios.
- Ainda nao existe regra de negocio para abrir, fechar ou validar sessoes de
  aula.
- O template base ainda esta com textos padrao de exemplo do Django Tailwind.
- O arquivo `requirements.txt` aparenta estar codificado com bytes nulos
  possivelmente por UTF-16/UTF-16LE. Isso pode atrapalhar instalacoes com
  `pip install -r requirements.txt` se nao for normalizado para UTF-8.

## Estrutura recomendada para evolucao

Sugestao de apps Django:

- `accounts`: autenticacao, usuarios e papeis gerais;
- `people`: dados academicos de alunos e professores;
- `rooms`: cadastro de salas e QR Codes;
- `schedules`: aulas planejadas e regras de horario;
- `access`: sessoes de abertura/fechamento, eventos RFID e auditoria;
- `attendance`: registros de entrada, saida e status de presenca.

Essa divisao mantem o app `accounts` focado em autenticacao e evita misturar
regras academicas com usuarios de login.

## Proxima etapa tecnica recomendada

1. Definir os modelos de dominio em ingles.
2. Criar migrations para as entidades principais.
3. Registrar os modelos no Django Admin.
4. Implementar servicos de negocio para validar abertura, fechamento e presenca.
5. Criar endpoints para eventos RFID e QR Code.
6. Substituir o template base de exemplo por uma interface inicial do sistema.
