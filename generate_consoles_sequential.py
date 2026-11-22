import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"
os.makedirs(OUT, exist_ok=True)

# Se já temos o test_ps4.jpg, usar ele para o PS4!
if os.path.exists('/tmp/test_ps4.jpg') and os.path.getsize('/tmp/test_ps4.jpg') > 5000:
    try:
        img = Image.open('/tmp/test_ps4.jpg').convert('RGB')
        dest = os.path.join(OUT, 'console_playstation_4.webp')
        img.save(dest, 'WEBP', quality=85)
        print(f"✓ PlayStation 4 reaproveitado do cache e salvo em {dest} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print("Erro ao reaproveitar PS4:", e)

consoles = [
    {
        "file": "console_playstation_2.webp",
        "prompt": "Sony PlayStation 2 console fat vertical standing with controller dark tech background product shot",
        "name": "PlayStation 2"
    },
    {
        "file": "console_xbox_360.webp",
        "prompt": "Microsoft Xbox 360 console white design with green ring light and wireless controller dark background studio shot",
        "name": "Xbox 360"
    },
    {
        "file": "console_vr_oculus.webp",
        "prompt": "Meta Quest VR virtual reality headset with controllers studio lighting dark purple neon background",
        "name": "Realidade Virtual"
    },
    {
        "file": "console_psp_vita.webp",
        "prompt": "Sony PSP PlayStation Portable handheld console glowing screen dark background studio photography",
        "name": "PSP"
    },
    {
        "file": "console_nintendo_3ds.webp",
        "prompt": "Nintendo 3DS handheld video game console opened dual screens dark studio background",
        "name": "Nintendo 3DS"
    },
    {
        "file": "console_retro_emuladores.webp",
        "prompt": "Original classic Sony PlayStation 1 PS1 grey console with controller retro gaming collection dark background",
        "name": "PS1 Jogos Retro"
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for idx, item in enumerate(consoles):
    dest_webp = os.path.join(OUT, item['file'])
    print(f"\n[{idx+1}/{len(consoles)}] Gerando foto IA para: {item['name']}...")
    encoded = urllib.parse.quote(item['prompt'])
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=640&height=360&nologo=true"
    
    success = False
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                tmp_f = f"/tmp/{item['file']}.jpg"
                with open(tmp_f, 'wb') as f:
                    f.write(data)
                
                img = Image.open(tmp_f).convert('RGB')
                img.save(dest_webp, 'WEBP', quality=85)
                print(f"  ✓ Sucesso! {item['file']} ({os.path.getsize(dest_webp):,} bytes)")
                success = True
                break
        except urllib.error.HTTPError as e:
            if e.code == 402:
                print(f"  ⏳ Limite de intervalo (45s). Aguardando 50 segundos...")
                time.sleep(50)
            else:
                print(f"  ⚠️ HTTP Error {e.code}: aguardando 15s...")
                time.sleep(15)
        except Exception as e:
            print(f"  ⚠️ Erro de conexão ({e}): aguardando 15s...")
            time.sleep(15)
            
    if not success:
        print(f"  ❌ Não foi possível gerar {item['name']}")
    else:
        # Aguardar 46 segundos antes do próximo para não bater no rate limit de 1 a cada 45s
        if idx < len(consoles) - 1:
            print("  ⏳ Pausa respeitosa de 48s para próxima requisição...")
            time.sleep(48)

# Atualizar aliases
import shutil
if os.path.exists(os.path.join(OUT, "console_retro_emuladores.webp")):
    shutil.copy2(os.path.join(OUT, "console_retro_emuladores.webp"), os.path.join(OUT, "console_ps1_retro.webp"))
if os.path.exists(os.path.join(OUT, "console_psp_vita.webp")):
    shutil.copy2(os.path.join(OUT, "console_psp_vita.webp"), os.path.join(OUT, "console_psp_psvita.webp"))
print("\n✅ Todos os consoles concluídos e aliases atualizados!")

