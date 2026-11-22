import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"

topicos = [
    {
        "file": "banner_topicos_ia_automacao.webp",
        "prompt": "futuristic artificial intelligence glowing robotic neural network brain cybernetic microchip dark purple and violet studio background 8k realistic cinematic photography",
        "name": "IA & Automação"
    },
    {
        "file": "banner_topicos_trafego_vendas.webp",
        "prompt": "modern stock market trading analytics charts and global sales funnel graphs glowing on digital screens dark moody tech background 8k realistic product photography",
        "name": "Tráfego & Vendas"
    },
    {
        "file": "banner_topicos_copy_lancamentos.webp",
        "prompt": "vintage luxury typewriter illuminated with glowing cybernetic typography floating letters golden ratio dark dramatic lighting 8k photography",
        "name": "Copywriting & Ofertas"
    },
    {
        "file": "banner_topicos_drop_ecommerce.webp",
        "prompt": "modern luxury e-commerce parcel shipping package with golden ribbons high tech warehouse logistics dark amber lighting 8k photography",
        "name": "E-commerce & Dropshipping"
    },
    {
        "file": "banner_topicos_dev_hacking.webp",
        "prompt": "hacker cybersecurity workstation matrix code screen terminal mechanical keyboard neon blue glow dark hoodie background 8k photography",
        "name": "Dev & Cybersecurity"
    },
    {
        "file": "banner_topicos_financas_cripto.webp",
        "prompt": "physical golden bitcoin and crypto coins stack floating with candlestick chart glowing dark emerald green lighting 8k macro photography",
        "name": "Investimentos & Cripto"
    },
    {
        "file": "banner_topicos_youtube_criadores.webp",
        "prompt": "professional cinema camera rig with red recording light on stabilizer gimbal youtube studio neon red lighting 8k photography",
        "name": "YouTube & Redes Sociais"
    },
    {
        "file": "banner_topicos_mentalidade_performance.webp",
        "prompt": "modern luxury executive desk with globe fountain pen hourglass and leather journal dark moody cinematic study lighting 8k photography",
        "name": "Idiomas & Concursos"
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for idx, item in enumerate(topicos):
    dest = os.path.join(OUT, item['file'])
    print(f"[{idx+1}/{len(topicos)}] Gerando foto IA para: {item['name']}...")
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
                print("  ⏳ Limite de 45s. Aguardando 48 segundos...")
                time.sleep(48)
            else:
                time.sleep(10)
        except Exception as e:
            print("  Erro:", e)
            time.sleep(10)
            
    if idx < len(topicos) - 1:
        print("  ⏳ Pausa respeitosa de 48s para o próximo...")
        time.sleep(48)

print("✅ Todos os 8 banners de tópicos gerados com fotos realistas!")

