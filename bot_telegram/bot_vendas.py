#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot Oficial de Atendimento e Vendas — ACERVO DIGITAL VIP
Opera 100% autônomo, sem dependências externas pesadas (Telegram Bot API nativa).
"""

import os
import sys
import time
import json
import urllib.request
import urllib.parse
from config import (
    BOT_TOKEN,
    ADMIN_CHAT_ID,
    VALOR_PROMO,
    VALOR_ORIGINAL,
    CHAVE_PIX,
    TIPO_CHAVE,
    CANAL_VIP_INVITE_LINK,
    SITE_OFICIAL
)

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def api_request(method, data=None):
    """Executa chamadas HTTP para a Telegram Bot API com tratamento de erros."""
    url = f"{API_URL}/{method}"
    try:
        if data:
            json_data = json.dumps(data).encode("utf-8")
            req = urllib.request.Request(
                url, 
                data=json_data, 
                headers={"Content-Type": "application/json"}
            )
        else:
            req = urllib.request.Request(url)
            
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERRO API] {method}: {e}", file=sys.stderr)
        return None

def send_message(chat_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return api_request("sendMessage", payload)

def send_photo(chat_id, photo_file_id, caption="", reply_markup=None):
    payload = {
        "chat_id": chat_id,
        "photo": photo_file_id,
        "caption": caption,
        "parse_mode": "HTML"
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return api_request("sendPhoto", payload)

def answer_callback_query(callback_query_id, text=None):
    payload = {"callback_query_id": callback_query_id}
    if text:
        payload["text"] = text
    return api_request("answerCallbackQuery", payload)

def menu_principal():
    return {
        "inline_keyboard": [
            [
                {"text": f"⚡ Comprar Acesso Vitalício ({VALOR_PROMO})", "callback_data": "comprar_pix"}
            ],
            [
                {"text": "📋 Ver Chave Pix Copia & Cola", "callback_data": "ver_pix"},
                {"text": "📸 Enviar Comprovante", "callback_data": "enviar_comprovante"}
            ],
            [
                {"text": "📂 Categorias & Cursos Disponíveis", "callback_data": "ver_catalogo"},
                {"text": "🌐 Visitar Vitrine Web", "url": SITE_OFICIAL}
            ],
            [
                {"text": "❓ Como Funciona o Acesso", "callback_data": "duvidas_frequentes"}
            ]
        ]
    }

def handle_start(chat_id, user_first_name):
    msg = (
        f"👋 Olá, <b>{user_first_name}</b>! Bem-vindo(a) ao <b>Acervo Digital VIP</b>! ⚡\n\n"
        f"Aqui você garante acesso vitalício a mais de <b>1.000 cursos, ferramentas e automações</b> "
        f"organizados por tópicos direto no Telegram.\n\n"
        f"🏷️ <b>OFERTA RELÂMPAGO:</b>\n"
        f"De <s>{VALOR_ORIGINAL}</s> por apenas <b>{VALOR_PROMO}</b> (pagamento único, sem mensalidades).\n\n"
        f"Escolha uma das opções abaixo para liberar seu acesso imediatamente:"
    )
    send_message(chat_id, msg, menu_principal())

def handle_comprar_pix(chat_id):
    msg = (
        f"💳 <b>PAGAMENTO VIA PIX — ACERVO DIGITAL VIP</b>\n\n"
        f"📌 <b>Valor Promocional:</b> <code>{VALOR_PROMO}</code> (Único / Vitalício)\n"
        f"🔑 <b>Tipo de Chave:</b> {TIPO_CHAVE}\n"
        f"🔑 <b>Chave Pix:</b>\n<code>{CHAVE_PIX}</code>\n\n"
        f"<i>(Toque na chave acima para copiar automaticamente)</i>\n\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"<b>COMO LIBERAR SEU ACESSO:</b>\n"
        f"1. Abra o app do seu banco e faça o Pix de <b>{VALOR_PROMO}</b>.\n"
        f"2. Tire um print ou salve o comprovante.\n"
        f"3. Envie a foto do comprovante diretamente aqui nesta conversa.\n"
        f"4. Nosso sistema validará e enviará seu link exclusivo de entrada aos tópicos VIP!"
    )
    markup = {
        "inline_keyboard": [
            [{"text": "📸 Enviar Comprovante Agora", "callback_data": "enviar_comprovante"}],
            [{"text": "⬅️ Voltar ao Menu", "callback_data": "menu_inicio"}]
        ]
    }
    send_message(chat_id, msg, markup)

def handle_catalogo(chat_id):
    msg = (
        f"📚 <b>CONTEÚDOS ORGANIZADOS POR TÓPICOS NO TELEGRAM:</b>\n\n"
        f"🤖 <b>1. Inteligência Artificial & Agentes:</b> ChatGPT Avançado, Claude 3.5, Lovable, Midjourney, Whisper, N8N.\n"
        f"📈 <b>2. Tráfego Pago & Performance:</b> Meta Ads, TikTok Ads, Google Ads, Escala e Contingência.\n"
        f"💻 <b>3. Programação & DevOps:</b> Python do Zero ao Avançado, Linux Pro, APIs REST, Docker, SQL.\n"
        f"🎬 <b>4. Edição de Vídeo & Criadores:</b> Premiere, After Effects, CapCut, Sound Design e Canais Dark.\n"
        f"🛒 <b>5. E-commerce & Dropshipping:</b> Shopee, Mercado Livre, Lojas Virtuais, Mineração de Produtos.\n"
        f"💰 <b>6. Finanças & Investimentos:</b> Milhas Aéreas, Mercado Financeiro, Criptoativos e Macroeconomia.\n"
        f"🌍 <b>7. Idiomas & Soft Skills:</b> Inglês Completo, Oratória, Produtividade (Notion / Segundo Cérebro).\n\n"
        f"Tudo com download direto e sem limites, vitalício por <b>{VALOR_PROMO}</b>!"
    )
    markup = {
        "inline_keyboard": [
            [{"text": f"⚡ Quero Liberar Tudo por {VALOR_PROMO}", "callback_data": "comprar_pix"}],
            [{"text": "⬅️ Voltar ao Menu", "callback_data": "menu_inicio"}]
        ]
    }
    send_message(chat_id, msg, markup)

def handle_duvidas(chat_id):
    msg = (
        f"❓ <b>PERGUNTAS FREQUENTES:</b>\n\n"
        f"<b>1. O acesso é vitalício mesmo?</b>\n"
        f"Sim! Você paga uma única vez <b>{VALOR_PROMO}</b> e tem acesso ilimitado sem mensalidades.\n\n"
        f"<b>2. Como recebo os cursos?</b>\n"
        f"Você recebe um link de convite exclusivo para os canais e tópicos organizados no próprio Telegram.\n\n"
        f"<b>3. Tem suporte?</b>\n"
        f"Sim, suporte técnico oficial direto pelo Telegram.\n\n"
        f"<b>4. Posso baixar os arquivos?</b>\n"
        f"Sim, todos os vídeos, PDFs, modelos e códigos estão disponíveis para download imediato."
    )
    markup = {
        "inline_keyboard": [
            [{"text": f"⚡ Garantir Acesso Vitalício ({VALOR_PROMO})", "callback_data": "comprar_pix"}],
            [{"text": "⬅️ Voltar ao Menu", "callback_data": "menu_inicio"}]
        ]
    }
    send_message(chat_id, msg, markup)

def process_callback_query(cb):
    cb_id = cb.get("id")
    data = cb.get("data")
    message = cb.get("message", {})
    chat_id = message.get("chat", {}).get("id")

    if data == "menu_inicio":
        answer_callback_query(cb_id)
        send_message(chat_id, "Menu Principal:", menu_principal())
    elif data == "comprar_pix" or data == "ver_pix":
        answer_callback_query(cb_id)
        handle_comprar_pix(chat_id)
    elif data == "ver_catalogo":
        answer_callback_query(cb_id)
        handle_catalogo(chat_id)
    elif data == "duvidas_frequentes":
        answer_callback_query(cb_id)
        handle_duvidas(chat_id)
    elif data == "enviar_comprovante":
        answer_callback_query(cb_id)
        send_message(
            chat_id, 
            "📸 <b>Envie a foto ou PDF do comprovante</b> diretamente aqui nesta conversa para conferência."
        )
    elif data.startswith("aprovar_"):
        # Ação do Admin
        target_chat_id = data.split("_")[1]
        answer_callback_query(cb_id, "Acesso aprovado com sucesso!")
        
        # Enviar link VIP ao comprador
        msg_sucesso = (
            f"🎉 <b>PAGAMENTO CONFIRMADO COM SUCESSO!</b>\n\n"
            f"Seu acesso vitalício ao <b>Acervo Digital VIP</b> foi liberado.\n\n"
            f"👇 <b>Clique no link abaixo para entrar agora:</b>\n"
            f"🚀 {CANAL_VIP_INVITE_LINK}\n\n"
            f"Seja muito bem-vindo(a) e bons estudos!"
        )
        send_message(target_chat_id, msg_sucesso)
        send_message(chat_id, f"✅ O usuário <code>{target_chat_id}</code> recebeu o link VIP!")

def process_message(msg):
    chat_id = msg.get("chat", {}).get("id")
    text = msg.get("text", "")
    from_user = msg.get("from", {})
    first_name = from_user.get("first_name", "Amigo(a)")
    username = from_user.get("username", "sem_username")

    # Recebimento de Comprovante (Foto ou Documento)
    if "photo" in msg or "document" in msg:
        resp_user = (
            "✅ <b>Comprovante recebido com sucesso!</b>\n\n"
            "Nossa equipe ou robô de conferência está checando seu Pix.\n"
            "Em poucos instantes você receberá seu link exclusivo de acesso aqui mesmo! ⏳"
        )
        send_message(chat_id, resp_user)

        # Se houver admin configurado, notificar com botão de aprovação
        if ADMIN_CHAT_ID:
            legenda_admin = (
                f"🚨 <b>NOVO COMPROVANTE RECEBIDO!</b>\n\n"
                f"👤 <b>Cliente:</b> {first_name} (@{username})\n"
                f"🆔 <b>Chat ID:</b> <code>{chat_id}</code>\n"
                f"💰 <b>Valor Esperado:</b> {VALOR_PROMO}\n"
            )
            markup_admin = {
                "inline_keyboard": [
                    [
                        {"text": "✅ Liberar Acesso VIP", "callback_data": f"aprovar_{chat_id}"}
                    ]
                ]
            }
            if "photo" in msg:
                photo_id = msg["photo"][-1]["file_id"]
                send_photo(ADMIN_CHAT_ID, photo_id, legenda_admin, markup_admin)
            else:
                send_message(ADMIN_CHAT_ID, legenda_admin, markup_admin)
        return

    # Comandos de Texto
    if text.startswith("/start"):
        handle_start(chat_id, first_name)
    elif text.lower() in ["pix", "chave pix", "pagar", "comprar"]:
        handle_comprar_pix(chat_id)
    elif text.lower() in ["cursos", "catalogo", "grade"]:
        handle_catalogo(chat_id)
    else:
        # Fallback inteligente
        send_message(
            chat_id,
            f"Olá {first_name}! Como posso te ajudar hoje?",
            menu_principal()
        )

def main():
    if BOT_TOKEN == "SEU_BOT_TOKEN_AQUI":
        print("="*60)
        print("⚠️ ATENÇÃO: Defina TELEGRAM_BOT_TOKEN no arquivo config.py ou no .env!")
        print("Obtenha seu token gratuitamente conversando com o @BotFather no Telegram.")
        print("="*60)
        return

    print("🚀 Bot do Telegram Acervo Digital VIP iniciado com sucesso!")
    print("Aguardando novas mensagens e comprovantes...")
    
    offset = None
    while True:
        try:
            params = {"timeout": 30}
            if offset:
                params["offset"] = offset
            
            updates = api_request("getUpdates", params)
            if updates and updates.get("ok"):
                for item in updates.get("result", []):
                    offset = item["update_id"] + 1
                    if "message" in item:
                        process_message(item["message"])
                    elif "callback_query" in item:
                        process_callback_query(item["callback_query"])
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nBot finalizado pelo operador.")
            break
        except Exception as e:
            print(f"[Loop Exception] {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
