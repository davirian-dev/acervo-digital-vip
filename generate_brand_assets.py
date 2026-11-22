import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets"
os.makedirs(OUT, exist_ok=True)

assets = [
    {
        "file": "logo_acervo_digital_vip.png",
        "prompt": "minimalist luxury modern tech brand logo emblem for ACERVO DIGITAL VIP glowing emerald lightning bolt inside golden cybernetic hexagon dark sleek metallic background 8k vector app icon design centered",
        "name": "Logotipo / Ícone do Acervo Digital VIP",
        "size": (512, 512)
    },
    {
        "file": "perfil_acervo_digital_vip.png",
        "prompt": "premium avatar profile picture for Telegram VIP channel, futuristic glowing green and cyan neon vault lock digital archive cybernetic shield dark background dramatic cinematic studio 8k profile photo",
        "name": "Foto de Perfil Oficial (Telegram/Redes)",
        "size": (512, 512)
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for idx, item in enumerate(assets):
    dest = os.path.join(OUT, item['file'])
    print(f"Gerando: {item['name']}...")
    encoded = urllib.parse.quote(item['prompt'])
    url = f"https://image.pollinations.ai/prompt/{encoded}?width={item['size'][0]}&height={item['size'][1]}&nologo=true"
    
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                tmp_f = f"/tmp/{item['file']}.jpg"
                with open(tmp_f, 'wb') as f:
                    f.write(data)
                img = Image.open(tmp_f).convert('RGB')
                img.save(dest, 'PNG')
                print(f"  ✓ Salvo em {dest} ({os.path.getsize(dest):,} bytes)")
                break
        except urllib.error.HTTPError as e:
            if e.code == 402:
                print("  ⏳ Limite de requisições atingido. Aguardando 48 segundos...")
                time.sleep(48)
            else:
                time.sleep(10)
        except Exception as e:
            print("  Erro:", e)
            time.sleep(10)
            
    if idx < len(assets) - 1:
        print("  ⏳ Pausa de 48s para o próximo asset...")
        time.sleep(48)

print("Concluído!")
