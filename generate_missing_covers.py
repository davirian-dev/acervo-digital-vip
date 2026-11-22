import os
from PIL import Image, ImageDraw, ImageFont

CAPAS_DIR = '/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais'
os.makedirs(CAPAS_DIR, exist_ok=True)

# Lista de capas a criar com identidade visual espetacular
COVERS = [
    {
        'filename': 'Bilinguismo-Montessori.webp',
        'badge': 'MÉTODO MONTESSORI',
        'badge_color': (245, 158, 11),  # Âmbar
        'title': 'Bilinguismo Infantil &\nMétodo Montessori',
        'subtitle': 'Educação Cognitiva e Prática 2026',
        'theme_color': (245, 158, 11),
        'bg_top': (20, 15, 30),
        'bg_bottom': (8, 6, 12),
        'icon': '🎓'
    },
    {
        'filename': 'canal_historia_bw.webp',
        'badge': 'ARQUIVO HISTÓRICO',
        'badge_color': (148, 163, 184), # Slate
        'title': 'História em\nPreto e Branco',
        'subtitle': 'Documentários, Guerras e Fatos Raros',
        'theme_color': (226, 232, 240),
        'bg_top': (25, 28, 36),
        'bg_bottom': (10, 11, 15),
        'icon': '🏛️'
    },
    {
        'filename': 'seo_sem_segredos.webp',
        'badge': 'SEO TÉCNICO',
        'badge_color': (16, 185, 129),  # Emerald
        'title': 'SEO Sem Segredos:\nDo Zero ao Topo 1',
        'subtitle': 'Indexação, Core Web Vitals e RankBrain',
        'theme_color': (16, 185, 129),
        'bg_top': (6, 30, 22),
        'bg_bottom': (3, 15, 11),
        'icon': '🔍'
    },
    {
        'filename': 'formacao_seo_discover.webp',
        'badge': 'ALTO TRÁFEGO',
        'badge_color': (6, 182, 212),   # Cyan
        'title': 'Formação SEO Master\n& Google Discover',
        'subtitle': 'Milhões de Visitas Orgânicas sem Anúncios',
        'theme_color': (6, 182, 212),
        'bg_top': (6, 28, 36),
        'bg_bottom': (3, 14, 18),
        'icon': '🚀'
    },
    {
        'filename': 'youtube_seo_extremo.webp',
        'badge': 'ALGORITMO YOUTUBE',
        'badge_color': (239, 68, 68),   # Red
        'title': 'YouTube SEO &\nRetenção Extrema',
        'subtitle': 'CTR Elevado, Thumbnails e Ganchos Virais',
        'theme_color': (239, 68, 68),
        'bg_top': (38, 8, 8),
        'bg_bottom': (18, 4, 4),
        'icon': '🎬'
    },
    {
        'filename': 'copywriting_retencao_vsl.webp',
        'badge': 'CONVERSÃO MÁXIMA',
        'badge_color': (168, 85, 247),  # Purple
        'title': 'Copywriting &\nRetenção de Audiência',
        'subtitle': 'VSLs Magnéticas, Storytelling e Ofertas',
        'theme_color': (168, 85, 247),
        'bg_top': (30, 10, 42),
        'bg_bottom': (15, 5, 21),
        'icon': '✍️'
    },
    {
        'filename': 'google_meu_negocio_local.webp',
        'badge': 'DOMINÂNCIA LOCAL',
        'badge_color': (59, 130, 246),  # Blue
        'title': 'Google Meu Negócio\n& SEO Local Pro',
        'subtitle': 'Coloque Empresas Locais no Topo 1 do Maps',
        'theme_color': (59, 130, 246),
        'bg_top': (10, 24, 46),
        'bg_bottom': (5, 12, 23),
        'icon': '📍'
    },
    {
        'filename': 'funis_retencao_ltv.webp',
        'badge': 'CRESCIMENTO LTV',
        'badge_color': (234, 179, 8),   # Yellow
        'title': 'Funis de Retenção\n& LTV Infinito',
        'subtitle': 'Monetização Recorrente e E-mail Automático',
        'theme_color': (234, 179, 8),
        'bg_top': (35, 28, 5),
        'bg_bottom': (18, 14, 2),
        'icon': '🔄'
    }
]

WIDTH, HEIGHT = 640, 360

# Tenta carregar fontes do sistema linux
font_paths = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
]
font_main = None
font_sub = None
font_badge = None

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_main = ImageFont.truetype(fp, 32)
            font_sub = ImageFont.truetype(fp, 16)
            font_badge = ImageFont.truetype(fp, 12)
            break
        except Exception:
            pass

if not font_main:
    font_main = ImageFont.load_default()
    font_sub = font_main
    font_badge = font_main

for item in COVERS:
    # 1. Gradiente de fundo escuro premium
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 10, 15))
    draw = ImageDraw.Draw(img)
    
    top_c = item['bg_top']
    bot_c = item['bg_bottom']
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(top_c[0] * (1 - ratio) + bot_c[0] * ratio)
        g = int(top_c[1] * (1 - ratio) + bot_c[1] * ratio)
        b = int(top_c[2] * (1 - ratio) + bot_c[2] * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # 2. Glow radial sutil no canto superior direito
    tc = item['theme_color']
    for r in range(160, 0, -4):
        alpha = int(18 * (r / 160))
        glow_color = (
            min(255, int(tc[0] * 0.4)),
            min(255, int(tc[1] * 0.4)),
            min(255, int(tc[2] * 0.4))
        )
        draw.ellipse([WIDTH - 120 - r, -40 - r, WIDTH - 120 + r, -40 + r], fill=glow_color)
    
    # 3. Grid tech decorativo sutil
    for x in range(0, WIDTH, 40):
        draw.line([(x, 0), (x, HEIGHT)], fill=(255, 255, 255, 12), width=1)
    for y in range(0, HEIGHT, 40):
        draw.line([(0, y), (WIDTH, y)], fill=(255, 255, 255, 12), width=1)

    # 4. Moldura interna com glassmorphism
    draw.rectangle([12, 12, WIDTH - 13, HEIGHT - 13], outline=(255, 255, 255, 40), width=1)
    
    # 5. Badge pill no canto superior esquerdo
    badge_text = item['badge']
    b_color = item['badge_color']
    # pill bg
    draw.rounded_rectangle([32, 28, 32 + len(badge_text)*10 + 16, 56], radius=6, fill=(15, 23, 42), outline=b_color, width=1)
    draw.text((40, 36), badge_text, font=font_badge, fill=b_color)

    # 6. Selo VIP no canto superior direito
    draw.rounded_rectangle([WIDTH - 125, 28, WIDTH - 32, 56], radius=6, fill=(16, 185, 129, 30), outline=(16, 185, 129), width=1)
    draw.text((WIDTH - 117, 36), "ACERVO VIP", font=font_badge, fill=(52, 211, 153))

    # 7. Título principal
    lines = item['title'].split('\n')
    y_pos = 130
    for line in lines:
        draw.text((32, y_pos), line, font=font_main, fill=(255, 255, 255))
        y_pos += 40
    
    # 8. Subtítulo / autor
    draw.text((32, y_pos + 12), item['subtitle'], font=font_sub, fill=(156, 163, 175))

    # 9. Barra inferior temática com gradiente de progresso
    draw.rectangle([32, HEIGHT - 38, WIDTH - 32, HEIGHT - 34], fill=(30, 41, 59))
    draw.rectangle([32, HEIGHT - 38, int(WIDTH * 0.75), HEIGHT - 34], fill=b_color)
    draw.text((32, HEIGHT - 28), "ACESSO VITALÍCIO • TELEGRAM VIP • 100% LIBERADO", font=font_badge, fill=(100, 116, 139))
    
    out_path = os.path.join(CAPAS_DIR, item['filename'])
    img.save(out_path, 'WEBP', quality=85)
    print(f"Salvo: {item['filename']} ({os.path.getsize(out_path)} bytes)")

# Compatibilidade para consoles com nomes alternativos
aliases = [
    ('console_pc_steam.webp', 'console_pc_games.webp'),
    ('console_psp_psvita.webp', 'console_psp_vita.webp'),
    ('console_ps1_retro.webp', 'console_retro_emuladores.webp')
]
for src, target in aliases:
    src_path = os.path.join(CAPAS_DIR, src)
    tgt_path = os.path.join(CAPAS_DIR, target)
    if os.path.exists(tgt_path) and not os.path.exists(src_path):
        with open(tgt_path, 'rb') as f_in, open(src_path, 'wb') as f_out:
            f_out.write(f_in.read())
        print(f"Criado alias: {src} -> {target}")

print("Todas as capas faltantes geradas com sucesso!")
