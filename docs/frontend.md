# Front-end

Este documento descreve a estrutura de templates do Acesso IFAL, a organizacao
das telas e as convencoes de interface.

## Stack

- **Tailwind CSS v4** via PostCSS
- **daisyUI v5** para componentes de interface
- **Django Templates** com heranca e includes

## Tema

Dois temas definidos no CSS:

| Tema | Classe | Descricao |
|------|--------|-----------|
| `acesso-ifal` | default | Tema claro com cores do IFAL |
| `acesso-ifal-dark` | `prefersdark: true` | Tema escuro |

O tema e aplicado via `data-theme` no `<html>` e persistido no `localStorage`.

## Paleta de cores

| Cor | Hex | Uso |
|-----|-----|-----|
| Verde primario | `#67C180` | Botoes principais, links, destaques |
| Verde claro | `#D7F5E1` | Background do header, sidebar, botoes secundarios |
| Verde hover | `#E8F8ED` | Background de botoes, avatar |
| Verde escuro | `#6DAE43` | Indicador de status online |
| Texto principal | `#232323` | Textos principais |
| Texto secundario | `#71717A` | Textos auxiliares |
| Texto muted | `#969696` | Placeholders, textos informativos |
| Alerta vermelho | `#FF676A` | Confirmacoes de acoes criticas |
| Alerta laranja | `#F8AF67` | Acoes de fechamento |
| Background input | `#F2F4F8` | Campos de busca |
| Borda input | `#E7E8E9` | Bordas de campos |

## Estrutura de templates

Os templates estao organizados dentro de `templates/`, na raiz do projeto:

```
templates/
├── base.html                    # Template base global (blocos de heranca)
├── dashboard/
│   ├── base.html                # Layout compartilhado (sidebar + header)
│   ├── home.html                # Dashboard principal
│   ├── my_classes.html          # Minhas turmas
│   └── history.html             # Historico de acessos
├── attendance/
│   ├── record_list.html         # Lista de presencas
│   ├── report.html              # Relatorios
│   └── qr_checkin.html          # Registro de presenca via QR Code
├── rooms/
│   ├── list.html                # Lista de salas (somente leitura)
│   └── status.html              # Status em tempo real das salas
├── people/
│   ├── student_list.html        # Lista de alunos (somente leitura)
│   └── teacher_list.html        # Lista de professores (somente leitura)
├── schedules/
│   └── list.html                # Lista de horarios (somente leitura)
├── access/
│   ├── rfid_list.html           # Lista de cartoes RFID (somente leitura)
│   ├── event_list.html          # Log de auditoria
│   └── open_room_modal.html     # Modais de abrir/fechar sala
├── profile/
│   ├── view.html                # Visualizar perfil
│   └── edit.html                # Editar perfil
├── settings/
│   └── view.html                # Configuracoes do sistema
├── registration/
│   ├── login.html               # Tela de login
│   ├── logged_out.html          # Sessao encerrada
│   ├── password_reset_form.html # Solicitar redefinicao de senha
│   ├── password_reset_done.html # Email enviado
│   ├── password_reset_confirm.html # Definir nova senha
│   └── password_reset_complete.html # Senha redefinida
└── includes/
    ├── header.html              # Header compartilhado
    ├── sidebar.html             # Sidebar de navegacao
    ├── navbar.html              # Navbar (nao utilizada atualmente)
    ├── messages.html            # Toast de mensagens
    ├── pagination.html          # Paginacao
    └── calendar_week.html       # Calendario semanal
```

## Heranca de templates

### Template base global (`base.html`)

Define a estrutura HTML basica com carregamento do Tailwind CSS e script de tema
claro/escuro. Blocos disponiveis: `title`, `extra_head`, `body`, `navbar`,
`content`, `footer`, `extra_js`.

### Layout do dashboard (`dashboard/base.html`)

Estende `base.html` e inclui sidebar e header. Bloco principal: `dashboard_content`.
Bloco para modais: `modals`.

```django
{% extends "dashboard/base.html" %}

{% block title %}Nome da Pagina - Acesso IFAL{% endblock %}

{% block dashboard_content %}
<!-- conteudo da pagina -->
{% endblock %}

{% block modals %}
{% include "access/open_room_modal.html" %}
{% endblock %}
```

### Telas de autenticacao

Estendem `base.html` diretamente com layout split-screen: formulario a esquerda
(fundo branco) e branding a direita (fundo verde `#D7F5E1` com logo e nome do
sistema). O lado direito fica oculto em mobile (`hidden lg:flex`).

## Navegacao

### Sidebar

A sidebar (`includes/sidebar.html`) contem links para as rotas implementadas:

| Item | URL | Icone |
|------|-----|-------|
| Dashboard | `dashboard:home` | Casa |
| Presencas | `dashboard:attendance` | Prancheta |
| Historico | `dashboard:history` | Relogio |

Inclui toggle de modo escuro no rodape.

### Header

O header (`includes/header.html`) contem:
- Botao hamburger para abrir sidebar no mobile
- Botao de notificacoes
- Avatar com dropdown do perfil (Meu Perfil, Administracao, Sair)

## Cadastro de dados

Nesta fase inicial, o cadastro de dados e feito exclusivamente pelo Django
Admin. Os templates de listagem sao somente leitura (sem botoes de criar/editar/
excluir).

## Variaveis de contexto esperadas

### Dashboard (`home.html`)
- `classes`: lista de turmas do professor logado

### Presencas (`record_list.html`)
- `records`: lista de `AttendanceRecord`
- `classes`: lista de turmas para filtro
- `stats`: dicionario com `total`, `present`, `absent`

### Historico (`history.html`)
- `sessions`: lista de `AccessSession`
- `rooms`: lista de salas para filtro

### Relatorios (`report.html`)
- `report_rows`: dados agregados por turma
- `stats`: dicionario com `sessions_count`, `avg_attendance`, `rooms_in_use`
- `classes`, `rooms`: para filtros

### Salas (`rooms/list.html`)
- `rooms`: lista de `Room`

### Alunos (`people/student_list.html`)
- `students`: lista de `Student`
- `courses`: lista de cursos distintos

### Professores (`people/teacher_list.html`)
- `teachers`: lista de `Teacher`

### Horarios (`schedules/list.html`)
- `schedules`: lista de `ClassSchedule`
- `teachers`, `rooms`: para filtros

### RFID (`access/rfid_list.html`)
- `cards`: lista de `RfidCard`

### Auditoria (`access/event_list.html`)
- `events`: lista de `AccessEvent`
- `rooms`: para filtro

## Rotas implementadas

| URL | View | Template |
|-----|------|----------|
| `/` | redirect `dashboard:home` | -- |
| `/dashboard/` | `home` | `dashboard/home.html` |
| `/dashboard/presencas/` | `attendance` | `attendance/record_list.html` |
| `/dashboard/historico/` | `history` | `dashboard/history.html` |
| `/dashboard/perfil/` | `profile` | `profile/view.html` |
| `/accounts/login/` | LoginView | `registration/login.html` |
| `/accounts/logout/` | LogoutView | `registration/logged_out.html` |
| `/accounts/password-reset/` | PasswordResetView | `registration/password_reset_form.html` |
| `/admin/` | Django Admin | Admin nativo |

## Status de teste das telas

### Testaveis

| Tela | Observacao |
|------|------------|
| Login | View e URL existem |
| Logout | View e URL existem |
| Reset de senha (4 telas) | Views e URLs existem |
| Dashboard home | View existe, dados vazios sem models |
| Sidebar/navegacao | Layout funcional |
| Modo escuro | JavaScript independente |
| Perfil (visualizar) | View existe |
| Minhas turmas | View existe, dados vazios |
| Presencas | View existe, dados vazios |
| Historico | View existe, dados vazios |
| Modais abrir/fechar sala | HTML/JS funcional |
| Django Admin | Nativo do Django |

### Nao testaveis (dependem de views/URLs nao implementadas)

| Tela | Motivo |
|------|--------|
| Perfil (editar) | View `profile_edit` nao existe |
| Relatorios | URL nao implementada |
| Lista de salas | URL nao implementada |
| Status das salas | URL nao implementada |
| Lista de alunos | URL nao implementada |
| Lista de professores | URL nao implementada |
| Lista de horarios | URL nao implementada |
| Cartoes RFID | URL nao implementada |
| Auditoria | URL nao implementada |
| Configuracoes | URL nao implementada |
| QR Check-in | URL nao implementada |

## Design de referencia

O design de referencia esta no Figma:
- **Arquivo**: Testes-LSOR
- **File Key**: `B9uvIQZTx4iBs2ZQoFV58U`
- **Acesso**: via MCP `figma-developer-mcp` ou API REST

Componentes do Figma mapeados:
- `Header/08` → `includes/header.html`
- `Menu` → `includes/sidebar.html`
- `Button` → botoes daisyUI customizados
- `Text Field` → inputs daisyUI
- `Avatar` → avatar do header
- `Dropdown Menu` → dropdown do perfil
- `Event` → cards de eventos
