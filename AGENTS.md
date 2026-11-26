# Regras do Projeto — Acervo Digital VIP

- **Documentação:** Leia `docs/ARQUITETURA.md` e `docs/WORKFLOW-IA.md` antes de editar o projeto.
- **Módulos:**
  - Site & Painel: `index.html`, `painel/index.html`
  - Bot Telegram de vendas: `bot_telegram/bot_vendas.py` e `bot_telegram/config.py` (manter compatível com Python padrão, sem segredos hardcoded)
  - Scripts utilitários de imagem: `*.py` na raiz
- **Verificação:** Ao alterar `bot_telegram/*.py`, executar `python -m py_compile bot_telegram/bot_vendas.py`.

## Padrões de Qualidade & Engenharia (Antigravity Suite)
- **Rigor Técnico & Invariantes (Gravitas)**:
  - Grounding pré-mutação obrigatório (ler o módulo, os chamadores e configurações antes de editar).
  - Nunca fechar tarefa sem validação real (executar python -m py_compile, pytest ou teste funcional do bot/serviço).
- **Ciclo de Features & Bugs (Superpowers)**:
  - Usar systematic-debugging (reproduzir -> isolar causa raiz -> corrigir pontualmente -> testar regressão).
  - Mudanças de arquitetura devem ser precedidas por plano estruturado (writing-plans).
- **Arquitetura (Graphify)**: Grafo de dependências gerado em graphify-out/. Para rastrear rotas, imports e fluxos, consulte o grafo ou execute graphify query.
