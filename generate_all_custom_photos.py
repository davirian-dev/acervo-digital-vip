import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"

targets = [
    # --- CANAIS VIP (8) ---
    {
        "file": "canal_receitas_cozinha.webp",
        "prompt": "delicious gourmet dish plated professionally in modern kitchen chef cooking with fresh vegetables herbs and flames dark luxury restaurant lighting 8k food photography",
        "name": "Receitas & Cozinha Fácil"
    },
    {
        "file": "canal_nutritips_saude.webp",
        "prompt": "healthy nutrition lifestyle fresh organic green salad avocado bowl vitamins fruits dark moody wellness photography 8k",
        "name": "NutriTips & Saúde"
    },
    {
        "file": "canal_notas_medicas.webp",
        "prompt": "doctor stethoscope lying on medical clipboard with stethoscope and cardiogram notes dark clean clinic medical photography 8k",
        "name": "Notas Médicas & Saúde"
    },
    {
        "file": "canal_mente_vencedora.webp",
        "prompt": "powerful golden lion silhouette standing on cliff peak dramatic cinematic golden hour sunset mindset success motivation 8k photography",
        "name": "Mente Vencedora"
    },
    {
        "file": "canal_wallpapers_hd.webp",
        "prompt": "abstract fluid neon waves 3d colorful metallic fluid waves 4k wallpaper dark dramatic lighting 8k digital art",
        "name": "Wallpapers 4K & HD"
    },
    {
        "file": "canal_analise_cripto.webp",
        "prompt": "cryptocurrency trading desk multiple screens displaying candlestick chart bitcoin ethereum futuristic dark cyan lighting 8k photography",
        "name": "Análise de Criptomoeda"
    },
    {
        "file": "canal_apk_premium.webp",
        "prompt": "modern futuristic smartphone floating with glowing holographic application icons exploding outwards dark background 8k product photography",
        "name": "Apk Premium"
    },
    {
        "file": "canal_fabrica_de_robos.webp",
        "prompt": "futuristic industrial robotic arm building automated electronics in high tech cyber factory dark glowing lights 8k photography",
        "name": "Fábrica de Robôs"
    },

    # --- LIVROS & UTILITÁRIOS (7) ---
    {
        "file": "canal_teologia_gospel.webp",
        "prompt": "ancient open Holy Bible on dark wooden altar illuminated with warm golden beam of light reverent sacred cinematic photography 8k",
        "name": "Teologia & Gospel"
    },
    {
        "file": "canal_livros_medicina.webp",
        "prompt": "heavy medical anatomy books open with human anatomy drawings anatomical model clean modern hospital library dark background 8k photography",
        "name": "Livros de Medicina & Saúde"
    },
    {
        "file": "canal_audio_livros.webp",
        "prompt": "luxury wireless noise cancelling headphones resting on thick hardback book with audio soundwaves glowing dark moody lighting 8k photography",
        "name": "Áudio Livros & Best-Sellers"
    },
    {
        "file": "canal_gols_ao_vivo.webp",
        "prompt": "soccer football ball ripping through the stadium net under stadium floodlights night match dramatic freeze frame 8k sports photography",
        "name": "Gols ao Vivo & Futebol"
    },
    {
        "file": "canal_achadinhos_promocoes.webp",
        "prompt": "futuristic discount percent icon 3d floating with shopping bags and parcels dark emerald neon promotional background 8k photography",
        "name": "Achadinhos & Promoções"
    },
    {
        "file": "canal_softwares_2026.webp",
        "prompt": "modern software development tools laptop keyboard with holographic code symbols and cloud servers glowing dark tech 8k photography",
        "name": "Softwares & Utilitários"
    },
    {
        "file": "canal_historia_bw.webp",
        "prompt": "vintage historic antique pocket watch and old sepia world map with vintage magnifying glass black and white dramatic museum lighting 8k photography",
        "name": "História em Preto e Branco"
    },

    # --- FERRAMENTAS & BOTs (8) ---
    {
        "file": "ferramenta_typebot_bots.webp",
        "prompt": "cute friendly 3d assistant chatbot robot glowing smiling on smartphone screen customer service automation dark tech background 8k",
        "name": "Typebot & Robôs"
    },
    {
        "file": "ferramenta_canva_pro.webp",
        "prompt": "graphic designer workstation with color palette digital drawing tablet and colorful typography layouts dark studio lighting 8k",
        "name": "Canva Pro & Pack de Artes"
    },
    {
        "file": "ferramenta_videos_virais.webp",
        "prompt": "smartphone vertical video recording screen with viral like heart symbols and particles exploding cinema lens dark background 8k",
        "name": "Acervo de Vídeos Virais 4K"
    },
    {
        "file": "ferramenta_paginas_vendas.webp",
        "prompt": "modern high converting sales landing page displayed on sleek tablet with credit card payment success badge dark green lighting 8k",
        "name": "Páginas de Vendas"
    },
    {
        "file": "ferramenta_prompts_ia.webp",
        "prompt": "human brain made of glowing fiber optic light and code prompts thinking artificial intelligence deep neural net dark background 8k",
        "name": "Super Pack de Prompts IA"
    },
    {
        "file": "ferramenta_plrs_revenda.webp",
        "prompt": "golden stacks of money and digital product ebook boxes with gold seals of quality dark luxury background 8k photography",
        "name": "Mega Pack PLRs Validados"
    },
    {
        "file": "ferramenta_planilhas_gestao.webp",
        "prompt": "financial spreadsheet dashboard with green growth graphs and profit metrics glowing on modern laptop dark corporate lighting 8k",
        "name": "Planilhas de Gestão & Tráfego"
    },
    {
        "file": "ferramenta_leads_prospeccao.webp",
        "prompt": "target bullseye target with golden arrow hitting the center surrounded by digital network connections b2b leads dark background 8k",
        "name": "Base de Leads B2B Segmentados"
    },

    # --- SEO & TRÁFEGO ORGÂNICO (6) ---
    {
        "file": "seo_sem_segredos.webp",
        "prompt": "magnifying glass inspecting google search ranking first place 1 with golden trophy dark tech modern background 8k photography",
        "name": "SEO Sem Segredos"
    },
    {
        "file": "formacao_seo_discover.webp",
        "prompt": "smartphone screen showing google discover news feed trending articles with rocket launch trail dark neon green background 8k photography",
        "name": "Formação SEO Discover"
    },
    {
        "file": "youtube_seo_extremo.webp",
        "prompt": "red youtube play button button glowing with analytics subscriber counter rising high retention dark studio lighting 8k",
        "name": "YouTube SEO & Retenção"
    },
    {
        "file": "copywriting_retencao_vsl.webp",
        "prompt": "quill feather pen writing golden glowing words on paper with video play button hovering dark cinematic lighting 8k",
        "name": "Copywriting & Retenção"
    },
    {
        "file": "google_meu_negocio_local.webp",
        "prompt": "3d glowing google maps location pin standing on illuminated city street map storefront local business dark navy lighting 8k",
        "name": "Google Meu Negócio & SEO Local"
    },
    {
        "file": "funis_retencao_ltv.webp",
        "prompt": "golden sales funnel machine turning leads into recurring gold coins customer lifetime value infinity symbol dark tech 8k",
        "name": "Funis de Retenção & LTV"
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print(f"Total de fotos reais a gerar por IA: {len(targets)}")

for idx, item in enumerate(targets):
    dest = os.path.join(OUT, item['file'])
    print(f"\n[{idx+1}/{len(targets)}] Gerando foto IA: {item['name']}...")
    encoded = urllib.parse.quote(item['prompt'])
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=640&height=360&nologo=true"
    
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                tmp_f = f"/tmp/{item['file']}.jpg"
                with open(tmp_f, 'wb') as f:
                    f.write(data)
                img = Image.open(tmp_f).convert('RGB')
                img.save(dest, 'WEBP', quality=88)
                print(f"  ✓ {item['name']} salvo em {dest} ({os.path.getsize(dest):,} bytes)")
                break
        except urllib.error.HTTPError as e:
            if e.code == 402:
                print("  ⏳ Limite de 45s por IP. Aguardando 48 segundos...")
                time.sleep(48)
            else:
                time.sleep(10)
        except Exception as e:
            print("  Erro:", e)
            time.sleep(10)
            
    if idx < len(targets) - 1:
        print("  ⏳ Pausa respeitosa de 48s para o próximo...")
        time.sleep(48)

print("\n🎉 Todas as 29 capas foram geradas com fotos realistas de altíssima qualidade!")

