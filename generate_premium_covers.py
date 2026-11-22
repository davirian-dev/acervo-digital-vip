#!/usr/bin/env python3
"""
Gera capas premium com Pillow para ferramentas, canais VIP e banners de tópicos.
Gradientes ricos + tipografia forte + ícones emoji + glow sutil.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

OUT = "assets/capas_reais"
os.makedirs(OUT, exist_ok=True)

W, H = 640, 360

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def draw_gradient(draw, w, h, c1, c2, direction='vertical'):
    for i in range(h if direction == 'vertical' else w):
        t = i / (h if direction == 'vertical' else w)
        c = lerp_color(hex_to_rgb(c1), hex_to_rgb(c2), t)
        if direction == 'vertical':
            draw.line([(0, i), (w, i)], fill=c)
        else:
            draw.line([(i, 0), (i, h)], fill=c)

def add_glow_circle(img, cx, cy, radius, color, alpha=60):
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    r, g, b = hex_to_rgb(color)
    for i in range(radius, 0, -2):
        a = int(alpha * (i / radius))
        od.ellipse([cx-i, cy-i, cx+i, cy+i], fill=(r, g, b, a))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=20))
    img.paste(Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB'))

def get_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def draw_text_centered(draw, text, y, font, fill=(255,255,255)):
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    # Shadow
    draw.text((x+2, y+2), text, font=font, fill=(0,0,0,180))
    draw.text((x, y), text, font=font, fill=fill)

def draw_text_wrapped(draw, text, y, font, max_w, fill=(255,255,255)):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = f"{current} {w}".strip()
        bbox = draw.textbbox((0,0), test, font=font)
        if bbox[2] - bbox[0] > max_w and current:
            lines.append(current)
            current = w
        else:
            current = test
    if current:
        lines.append(current)
    for line in lines:
        draw_text_centered(draw, line, y, font, fill)
        y += font.size + 6
    return y

def draw_badge(draw, text, y, font_size=14):
    f = get_font(font_size)
    bbox = draw.textbbox((0,0), text, font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    px, py = 16, 6
    bx = (W - tw - px*2) // 2
    draw.rounded_rectangle([bx, y, bx+tw+px*2, y+th+py*2], radius=12, fill=(16,185,129,200))
    draw.text((bx+px, y+py), text, font=f, fill=(255,255,255))
    return y + th + py*2 + 10

def create_cover(filename, title, subtitle, emoji_icon, grad_top, grad_bottom, glow_color, badge=None):
    img = Image.new('RGB', (W, H))
    draw = ImageDraw.Draw(img)
    draw_gradient(draw, W, H, grad_top, grad_bottom)
    add_glow_circle(img, W//2, H//2 - 30, 150, glow_color, alpha=40)
    draw = ImageDraw.Draw(img)
    
    # Emoji/icon grande no centro
    icon_font = get_font(72)
    draw_text_centered(draw, emoji_icon, 40, icon_font)
    
    # Título
    title_font = get_font(28)
    y = draw_text_wrapped(draw, title, 140, title_font, W - 60)
    
    # Subtítulo
    sub_font = get_font(16)
    y = draw_text_wrapped(draw, subtitle, y + 8, sub_font, W - 40, fill=(180, 220, 220))
    
    # Badge
    if badge:
        draw_badge(draw, badge, min(y + 10, H - 50))
    
    # Borda sutil
    draw.rounded_rectangle([2, 2, W-3, H-3], radius=12, outline=hex_to_rgb(glow_color) + (80,), width=1)
    
    path = os.path.join(OUT, filename)
    img.save(path, 'WEBP', quality=85)
    print(f"  ✓ {filename} ({os.path.getsize(path):,} bytes)")

# =====================================================
# FERRAMENTAS (8 covers)
# =====================================================
print("\n🔧 FERRAMENTAS:")
ferramentas = [
    ("ferramenta_typebot_bots.webp", "Typebot & Bots", "Chatbots prontos para WhatsApp e Telegram", "🤖", "#1a1040", "#0a0520", "#8b5cf6", "AUTOMAÇÃO"),
    ("ferramenta_canva_pro.webp", "Canva Pro", "Templates premium e design profissional", "🎨", "#1a0a30", "#0a0520", "#ec4899", "DESIGN"),
    ("ferramenta_videos_virais.webp", "Vídeos Virais", "Pack completo para criação de conteúdo viral", "🎬", "#0a1a30", "#050a20", "#3b82f6", "CONTEÚDO"),
    ("ferramenta_paginas_vendas.webp", "Páginas de Vendas", "Landing pages de alta conversão prontas", "📄", "#0a2020", "#051015", "#14b8a6", "VENDAS"),
    ("ferramenta_prompts_ia.webp", "Prompts de IA", "Mega pack de prompts para ChatGPT e Gemini", "🧠", "#1a1030", "#0a0820", "#a855f7", "INTELIGÊNCIA"),
    ("ferramenta_plrs_revenda.webp", "PLRs & Revenda", "Produtos digitais prontos para revender", "💰", "#1a1a0a", "#0a0a05", "#eab308", "RENDA EXTRA"),
    ("ferramenta_planilhas_gestao.webp", "Planilhas & Gestão", "Dashboards e controle financeiro profissional", "📊", "#0a1a20", "#050a15", "#06b6d4", "ORGANIZAÇÃO"),
    ("ferramenta_leads_prospeccao.webp", "Leads & Prospecção", "Ferramentas de captação e funil de vendas", "🎯", "#200a0a", "#100505", "#ef4444", "VENDAS"),
]
for f in ferramentas:
    create_cover(*f)

# =====================================================
# CANAIS VIP (16 covers)
# =====================================================
print("\n📺 CANAIS VIP:")
canais = [
    ("canal_nutritips_saude.webp", "NutriTips Saúde", "Dicas de nutrição e vida saudável", "🥗", "#0a200a", "#051005", "#22c55e", "SAÚDE"),
    ("canal_apk_premium.webp", "APK Premium", "Apps modificados e premium liberados", "📱", "#0a0a20", "#050520", "#6366f1", "APPS"),
    ("canal_fabrica_de_robos.webp", "Fábrica de Robôs", "Automações e bots prontos para usar", "⚙️", "#1a0a20", "#0a0510", "#a855f7", "BOTS"),
    ("canal_receitas_cozinha.webp", "Receitas & Cozinha", "Receitas fáceis e gourmet do dia a dia", "👨‍🍳", "#200a0a", "#100505", "#f97316", "CULINÁRIA"),
    ("canal_mente_vencedora.webp", "Mente Vencedora", "Mentalidade de sucesso e produtividade", "💎", "#0a1020", "#050810", "#3b82f6", "MINDSET"),
    ("canal_analise_cripto.webp", "Análise Cripto", "Sinais e análise de criptomoedas", "₿", "#1a1a00", "#0a0a00", "#f59e0b", "CRYPTO"),
    ("canal_wallpapers_hd.webp", "Wallpapers HD", "Papéis de parede 4K exclusivos", "🖼️", "#100a1a", "#080510", "#c084fc", "DESIGN"),
    ("canal_notas_medicas.webp", "Notas Médicas", "Material de estudo para área da saúde", "🏥", "#0a1a1a", "#050a0a", "#2dd4bf", "MEDICINA"),
    ("canal_audio_livros.webp", "Audiolivros", "Biblioteca de audiobooks completos", "🎧", "#1a0a10", "#0a0508", "#ec4899", "LEITURA"),
    ("canal_figurinhas_design.webp", "Figurinhas & Design", "Packs de stickers e recursos gráficos", "✨", "#1a1020", "#0a0810", "#8b5cf6", "CRIATIVO"),
    ("canal_biblioteca_gamer.webp", "Biblioteca Gamer", "Jogos, ROMs e emuladores organizados", "🎮", "#0a1020", "#050810", "#10b981", "GAMES"),
    ("canal_teologia_gospel.webp", "Teologia & Gospel", "Estudos bíblicos e materiais teológicos", "📖", "#1a1510", "#0a0a08", "#d97706", "FÉ"),
    ("canal_livros_medicina.webp", "Livros & Medicina", "Acervo de livros PDF e materiais médicos", "📚", "#0a1520", "#050a10", "#0ea5e9", "ESTUDO"),
    ("canal_gols_ao_vivo.webp", "Gols ao Vivo", "Melhores momentos e gols em tempo real", "⚽", "#0a200a", "#051005", "#22c55e", "FUTEBOL"),
    ("canal_softwares_2026.webp", "Softwares 2026", "Programas e licenças atualizados", "💻", "#101020", "#080810", "#6366f1", "TECH"),
    ("canal_achadinhos_promocoes.webp", "Achadinhos & Promoções", "Ofertas e cupons de desconto diários", "🏷️", "#200a10", "#100508", "#f43f5e", "ECONOMIA"),
    ("canal_historia_bw.webp", "História & Cultura", "Documentários e conteúdo histórico", "🏛️", "#151515", "#0a0a0a", "#94a3b8", "CULTURA"),
]
for c in canais:
    create_cover(*c)

# =====================================================
# BANNERS TÓPICOS (8 covers)
# =====================================================
print("\n🏷️ BANNERS TÓPICOS:")
banners = [
    ("banner_topicos_ia_automacao.webp", "IA & Automação", "ChatGPT, Gemini, N8N, Bots e Machine Learning", "🤖", "#1a0a30", "#0a0520", "#a855f7", "12 TÓPICOS"),
    ("banner_topicos_trafego_vendas.webp", "Tráfego & Vendas", "Google Ads, Facebook Ads, Funis e Copy", "📈", "#0a1a0a", "#050a05", "#22c55e", "10 TÓPICOS"),
    ("banner_topicos_drop_ecommerce.webp", "Drop & E-commerce", "Shopee, Shopify, Mercado Livre e Dropshipping", "🛒", "#1a1a0a", "#0a0a05", "#eab308", "8 TÓPICOS"),
    ("banner_topicos_dev_hacking.webp", "Dev & Hacking", "Programação, Pentest, Redes e Cibersegurança", "💻", "#0a1020", "#050810", "#3b82f6", "10 TÓPICOS"),
    ("banner_topicos_youtube_criadores.webp", "YouTube & Criadores", "Monetização, Edição, Thumbnails e Growth", "🎬", "#200a0a", "#100505", "#ef4444", "8 TÓPICOS"),
    ("banner_topicos_financas_cripto.webp", "Finanças & Cripto", "Day Trade, Bitcoin, Renda Fixa e Investimentos", "💰", "#1a1500", "#0a0a00", "#f59e0b", "6 TÓPICOS"),
    ("banner_topicos_mentalidade_performance.webp", "Mentalidade", "Produtividade, Foco, Liderança e Disciplina", "🧠", "#100a1a", "#080510", "#c084fc", "6 TÓPICOS"),
    ("banner_topicos_copy_lancamentos.webp", "Copy & Lançamentos", "VSL, Emails, Headlines e Estratégias de Launch", "✍️", "#0a1a1a", "#050a0a", "#14b8a6", "8 TÓPICOS"),
]
for b in banners:
    create_cover(*b)

# =====================================================
# SEO + EDUCAÇÃO (8 covers extras)
# =====================================================
print("\n🔍 SEO & EDUCAÇÃO:")
seo_edu = [
    ("seo_sem_segredos.webp", "SEO Sem Segredos", "Domine o Google e ranqueie em 1º lugar", "🔍", "#0a1a20", "#050a15", "#06b6d4", "SEO"),
    ("formacao_seo_discover.webp", "Formação SEO Discover", "Tráfego orgânico massivo via Google Discover", "🌐", "#0a200a", "#051005", "#22c55e", "TRÁFEGO"),
    ("youtube_seo_extremo.webp", "YouTube SEO Extremo", "Algoritmo, Tags, Títulos e Ranqueamento", "▶️", "#200a0a", "#100505", "#ef4444", "YOUTUBE"),
    ("copywriting_retencao_vsl.webp", "Copywriting & VSL", "Textos que vendem e retêm audiência", "✍️", "#1a0a20", "#0a0510", "#a855f7", "COPY"),
    ("google_meu_negocio_local.webp", "Google Meu Negócio", "Domine buscas locais e Google Maps", "📍", "#0a1a0a", "#050a05", "#22c55e", "LOCAL"),
    ("funis_retencao_ltv.webp", "Funis & Retenção LTV", "Maximize o valor vitalício do seu cliente", "🔄", "#0a0a20", "#050520", "#6366f1", "FUNIS"),
    ("Bilinguismo-Montessori.webp", "Bilinguismo Montessori", "Ensino bilíngue com método Montessori", "🌍", "#1a1510", "#0a0a08", "#d97706", "EDUCAÇÃO"),
]
for s in seo_edu:
    create_cover(*s)

print(f"\n✅ Total: {len(ferramentas) + len(canais) + len(banners) + len(seo_edu)} capas geradas!")
