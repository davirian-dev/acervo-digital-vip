import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"
dest = os.path.join(OUT, "console_pc_games.webp")

prompt = "gaming pc battle station setup with curved ultrawide monitor displaying action game mechanical keyboard rgb mouse glowing dark modern room studio lighting 8k"
encoded = urllib.parse.quote(prompt)
url = f"https://image.pollinations.ai/prompt/{encoded}?width=640&height=360&nologo=true"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Gerando nova foto IA de PC Games Setup...")
for attempt in range(4):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            tmp_f = "/tmp/console_pc_games.jpg"
            with open(tmp_f, 'wb') as f:
                f.write(data)
            img = Image.open(tmp_f).convert('RGB')
            img.save(dest, 'WEBP', quality=88)
            print(f"✓ PC Games salvo com sucesso em {dest} ({os.path.getsize(dest):,} bytes)")
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

import shutil
shutil.copy2(dest, os.path.join(OUT, "console_pc_steam.webp"))
print("Alias console_pc_steam.webp atualizado!")

