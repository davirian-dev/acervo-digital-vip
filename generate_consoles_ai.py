import urllib.request, urllib.parse, os, time
from PIL import Image

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"
os.makedirs(OUT, exist_ok=True)

consoles = [
    {
        "file": "console_playstation_4.webp",
        "prompt": "photo of original Sony PlayStation 4 console matte black with DualShock 4 controller, studio lighting, dark modern tech background, 8k product photography, sleek",
        "name": "PlayStation 4"
    },
    {
        "file": "console_playstation_2.webp",
        "prompt": "photo of classic Sony PlayStation 2 fat console vertical standing with blue PS2 logo and DualShock 2 controller, studio lighting, dark tech background, retro gaming, product shot",
        "name": "PlayStation 2"
    },
    {
        "file": "console_xbox_360.webp",
        "prompt": "photo of Microsoft Xbox 360 console white design with glowing green power ring and wireless controller, studio lighting, dark clean background, product photography",
        "name": "Xbox 360"
    },
    {
        "file": "console_vr_oculus.webp",
        "prompt": "photo of modern VR virtual reality headset Meta Quest style with touch controllers floating, cinematic studio lighting, dark neon purple and cyan background, future tech",
        "name": "Realidade Virtual"
    },
    {
        "file": "console_psp_vita.webp",
        "prompt": "photo of Sony PSP PlayStation Portable handheld console black sleek body glowing screen displaying game, studio lighting, dark minimalist background, product photography",
        "name": "PSP"
    },
    {
        "file": "console_nintendo_3ds.webp",
        "prompt": "photo of Nintendo 3DS handheld console open dual screens visible blue aqua body, studio product shot, dark background, portable video game console",
        "name": "Nintendo 3DS"
    },
    {
        "file": "console_retro_emuladores.webp",
        "prompt": "photo of original Sony PlayStation 1 PS1 grey console with classic controller and memory card, studio lighting, dark background, nostalgic retro video game collection",
        "name": "PS1 Jogos Retro"
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for item in consoles:
    print(f"Gerando foto IA para: {item['name']}...")
    encoded_prompt = urllib.parse.quote(item['prompt'])
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=640&height=360&nologo=true&seed=42"
    tmp_jpg = f"/tmp/{item['file']}.jpg"
    
    success = False
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=40) as resp, open(tmp_jpg, 'wb') as f:
                f.write(resp.read())
            
            # Converter para WebP qualidade 85
            img = Image.open(tmp_jpg).convert('RGB')
            dest_webp = os.path.join(OUT, item['file'])
            img.save(dest_webp, 'WEBP', quality=85)
            print(f"  ✓ Salvo: {item['file']} ({os.path.getsize(dest_webp):,} bytes)")
            success = True
            break
        except Exception as e:
            print(f"  ⚠️ Tentativa {attempt+1} falhou: {e}")
            time.sleep(3)
            
    if not success:
        print(f"  ❌ Falha crítica ao gerar {item['name']}")

# Atualizar aliases
import shutil
shutil.copy2(os.path.join(OUT, "console_retro_emuladores.webp"), os.path.join(OUT, "console_ps1_retro.webp"))
shutil.copy2(os.path.join(OUT, "console_psp_vita.webp"), os.path.join(OUT, "console_psp_psvita.webp"))
print("\nAliases de PS1 e PSP atualizados com sucesso!")

