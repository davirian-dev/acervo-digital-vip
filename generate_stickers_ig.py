import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"
dest_webp = os.path.join(OUT, "canal_figurinhas_design.webp")

prompt = "pack of aesthetic stickers and decorative elements for Instagram stories social media graphics flat design bright colors gradient clean dark background 8k"
encoded = urllib.parse.quote(prompt)
url = f"https://image.pollinations.ai/prompt/{encoded}?width=640&height=360&nologo=true"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Gerando nova imagem de Figurinhas para Instagram...")
for attempt in range(5):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            tmp_f = "/tmp/canal_figurinhas_ig.jpg"
            with open(tmp_f, 'wb') as f:
                f.write(data)
            img = Image.open(tmp_f).convert('RGB')
            img.save(dest_webp, 'WEBP', quality=88)
            print(f"✓ Imagem salva com sucesso em {dest_webp} ({os.path.getsize(dest_webp):,} bytes)")
            break
    except urllib.error.HTTPError as e:
        if e.code == 402:
            print("⏳ Limite de intervalo (45s). Aguardando 48 segundos...")
            time.sleep(48)
        else:
            time.sleep(10)
    except Exception as e:
        print("Erro:", e)
        time.sleep(10)

