import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"

targets = [
    {
        "file": "console_playstation_5.webp",
        "prompt": "Sony PlayStation 5 PS5 console white futuristic body with blue LED lighting and DualSense controller dark tech background 8k studio product photography",
        "name": "PlayStation 5"
    },
    {
        "file": "console_nintendo_switch.webp",
        "prompt": "Nintendo Switch console OLED model with red and blue Joy-Con controllers attached screen glowing dark background studio product photography",
        "name": "Nintendo Switch"
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for idx, item in enumerate(targets):
    dest = os.path.join(OUT, item['file'])
    print(f"Gerando foto IA para: {item['name']}...")
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
                print("  ⏳ Limite de intervalo (45s). Aguardando 48 segundos...")
                time.sleep(48)
            else:
                time.sleep(10)
        except Exception as e:
            print("  Erro:", e)
            time.sleep(10)
            
    if idx < len(targets) - 1:
        print("  ⏳ Pausa de 48s para o próximo...")
        time.sleep(48)

print("Concluído!")

