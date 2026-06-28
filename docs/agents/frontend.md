# Agente Frontend

## Responsabilidade

Construir telas administrativas e operacionais para usuarios do Acesso IFAL.

## Diretrizes

- Textos da interface em **portugues**.
- Identificadores, nomes de blocos e arquivos de template em **ingles**.
- Seguir a paleta de cores do projeto: verde `#67C180`, verde claro `#D7F5E1`,
  cinza escuro `#232323`, cinza medio `#71717A`, cinza claro `#969696`.
- Usar daisyUI v5 com Tailwind CSS v4 para componentes de interface.
- Nao criar telas de CRUD: dados sao inseridos via Django Admin.
- Templates de listagem sao somente leitura, sem botoes de criar/editar/excluir.
- Usar heranca de templates: `base.html` para autenticacao,
  `dashboard/base.html` para telas internas com sidebar + header.
- Componentes reutilizaveis em `templates/includes/`.
- Responsividade: usar classes responsivas (`sm:`, `md:`, `lg:`) e
  `overflow-x-auto` em tabelas.

## Telas esperadas

| Template | Tipo | Descricao |
|----------|------|-----------|
| `registration/login.html` | Autenticacao | Login com split-screen |
| `registration/logged_out.html` | Autenticacao | Confirmacao de logout |
| `registration/password_reset_form.html` | Autenticacao | Solicitar redefinicao |
| `registration/password_reset_done.html` | Autenticacao | Email enviado |
| `registration/password_reset_confirm.html` | Autenticacao | Nova senha |
| `registration/password_reset_complete.html` | Autenticacao | Senha alterada |
| `dashboard/home.html` | Dashboard | Pagina inicial com turmas e acesso rapido |
| `dashboard/my_classes.html` | Dashboard | Detalhamento de turmas do professor |
| `dashboard/history.html` | Dashboard | Historico de sessoes de acesso |
| `attendance/record_list.html` | Presenca | Lista de registros de presenca |
| `attendance/report.html` | Presenca | Relatorio consolidado |
| `attendance/qr_checkin.html` | Presenca | Registro via QR Code |
| `rooms/list.html` | Salas | Lista de salas (leitura) |
| `rooms/status.html` | Salas | Status em tempo real |
| `people/student_list.html` | Pessoas | Lista de alunos (leitura) |
| `people/teacher_list.html` | Pessoas | Lista de professores (leitura) |
| `schedules/list.html` | Horarios | Lista de horarios (leitura) |
| `access/rfid_list.html` | Acesso | Cartoes RFID (leitura) |
| `access/event_list.html` | Acesso | Log de auditoria |
| `access/open_room_modal.html` | Acesso | Modais abrir/fechar sala |
| `profile/view.html` | Perfil | Visualizar perfil |
| `profile/edit.html` | Perfil | Editar perfil |
| `settings/view.html` | Config | Configuracoes do sistema |
| `includes/header.html` | Include | Cabecalho com busca e perfil |
| `includes/sidebar.html` | Include | Menu lateral com modo escuro |
| `includes/calendar_week.html` | Include | Calendario semanal |
| `includes/pagination.html` | Include | Paginacao reutilizavel |
| `includes/messages.html` | Include | Toast de mensagens |

## Contexto obrigatorio

Antes de implementar, consultar:

- `docs/visao-geral.md`
- `docs/requisitos.md`
- `docs/fluxos.md`
