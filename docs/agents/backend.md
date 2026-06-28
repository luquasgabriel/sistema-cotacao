# Agente Backend

## Responsabilidade

Evoluir a aplicacao Django, modelos, servicos, endpoints, admin e integracoes do
Acesso IFAL.

## Diretrizes

- Escrever codigo em ingles.
- Usar modelos Django para persistencia relacional.
- Manter regras de negocio em servicos ou funcoes de dominio testaveis.
- Persistir eventos de RFID e QR Code para auditoria.
- Evitar colocar regra critica apenas no frontend.
- Criar migrations sempre que modelos forem alterados.

## Contexto obrigatorio

Antes de implementar, consultar:

- `docs/requisitos.md`
- `docs/modelo-dominio.md`
- `docs/fluxos.md`
- `docs/estrutura-atual.md`

## Prioridades tecnicas

1. Separar autenticacao de informacoes academicas.
2. Criar entidades de salas, aulas, sessoes e presencas.
3. Implementar validacoes de abertura e fechamento.
4. Criar endpoints para eventos externos.
5. Cobrir regras principais com testes.
