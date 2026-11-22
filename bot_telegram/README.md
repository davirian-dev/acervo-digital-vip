# 🤖 Bot de Vendas & Atendimento — Acervo Digital VIP

Bot autônomo em Python para realizar o atendimento, enviar chave Pix, receber comprovantes e liberar o acesso aos canais de tópicos do Telegram.

## 🚀 Como Colocar no Ar:

1. **Obtenha o Token do Bot:**
   - No Telegram, abra a conversa com o [@BotFather](https://t.me/BotFather).
   - Digite `/newbot`, escolha o nome (ex: `Acervo Digital VIP Oficial`) e um username (ex: `AcervoDigitalVIP_bot`).
   - Copie o **Token de Acesso HTTP** fornecido.

2. **Configure o Bot:**
   - Abra o arquivo `config.py` e cole seu token em `BOT_TOKEN`.
   - Se quiser receber os comprovantes dos clientes no seu privado, coloque seu Chat ID em `ADMIN_CHAT_ID` (você descobre seu ID enviando uma mensagem para [@userinfobot](https://t.me/userinfobot)).

3. **Inicie o Bot:**
   ```bash
   python3 bot_vendas.py
   ```

## 🛠️ Recursos Automáticos:
- **Zero Dependências Pesadas:** Funciona diretamente com a biblioteca padrão do Python (`urllib`/`json`), sem quebras ou conflitos de pacotes.
- **Menu Interativo:** Botões inline com cópia da chave Pix, catálogo de cursos e dúvidas frequentes.
- **Recepção de Comprovantes:** Quando o cliente manda a foto do comprovante, o bot acolhe o cliente e notifica o administrador com um botão de **[Liberar Acesso VIP]**.
- **Aprovação em 1 Toque:** Ao clicar no botão, o bot envia o link exclusivo de entrada ao cliente instantaneamente.
