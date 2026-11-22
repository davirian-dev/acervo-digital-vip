import os

# Configurações do Bot de Vendas - ACERVO DIGITAL VIP
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "SEU_BOT_TOKEN_AQUI")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "") # ID do Telegram do dono para receber comprovantes

# Dados de Pagamento
VALOR_PROMO = "R$ 9,90"
VALOR_ORIGINAL = "R$ 19,90"
CHAVE_PIX = "71981223348"
TIPO_CHAVE = "Telefone"
BENEFICIARIO = "Acervo Digital VIP"

# Link do Canal / Grupo de Tópicos dos Cursos do Telegram
CANAL_VIP_INVITE_LINK = "https://t.me/+-gV1v2gZzGozZDFh"
SITE_OFICIAL = "https://acervo-digital-vip.vercel.app"
