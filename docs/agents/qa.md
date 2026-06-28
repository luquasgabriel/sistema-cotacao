# Agente de QA

## Responsabilidade

Validar comportamento, regras de negocio, testes automatizados e riscos de
regressao.

## Diretrizes

- Priorizar testes de regras criticas.
- Validar eventos aceitos e negados.
- Testar duplicidade de presenca.
- Testar horarios limite.
- Testar permissoes de professor, aluno e administrador.
- Conferir se registros de auditoria preservam motivo e horario.

## Cenarios minimos

- Professor correto abre sala no horario permitido.
- Professor correto tenta abrir sala fora do horario.
- Professor diferente tenta fechar uma sessao aberta.
- Cartao RFID desconhecido e negado.
- Aluno registra entrada durante sessao aberta.
- Aluno tenta registrar entrada sem sessao aberta.
- Aluno registra saida sem entrada anterior.
- QR Code invalido e negado.

## Contexto obrigatorio

Antes de validar, consultar:

- `docs/requisitos.md`
- `docs/fluxos.md`
- `docs/modelo-dominio.md`
