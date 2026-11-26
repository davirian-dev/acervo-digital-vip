# Acervo Digital VIP — Arquitetura & Documentação

> Documento em Markdown (compatível com Obsidian e agentes de IA).

## 1. Visão Geral
- **Nome:** Acervo Digital VIP (`acervo-digital-vip`)
- **Stack:** Landing page & Painel estáticos (HTML/CSS/JS na Vercel) + Bot autônomo de vendas no Telegram em Python puro (`bot_telegram/bot_vendas.py`) + scripts Python de geração/otimização de capas em `assets/`.

## 2. Estrutura do Projeto
- `index.html` e `painel/index.html`: Página de vendas, tópicos do acervo e painel.
- `bot_telegram/bot_vendas.py` e `bot_telegram/config.py`: Bot em Python usando apenas biblioteca padrão (`urllib`/`json`) para atendimento, Pix, recebimento de comprovante e aprovação VIP em 1 toque (`README.md` na pasta).
- `ESTRATEGIA_CANAL_GRATIS_ISCA.md`: Documentação da estratégia de aquisição/funil.
- Scripts Python na raiz (`generate_*.py`, `process_real_photos.py`, `audit_*.py`): Ferramentas locais para capas e auditoria de mídia.
- `assets/capas_reais/`, `assets/ia_geradas/`, `assets/videos/`.

## 3. Regras para IA
1. **Zero Dependências no Bot:** Manter `bot_telegram/bot_vendas.py` compatível com Python padrão (sem exigir pacotes pesados desnecessários).
2. **Segurança de Tokens:** Nunca commitar `BOT_TOKEN` real em `config.py` ou arquivos públicos.
3. **Verificação:** Validar sintaxe Python (`python -m py_compile bot_telegram/bot_vendas.py`) ao editar o bot.
