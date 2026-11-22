import urllib.request, os
from PIL import Image, ImageDraw, ImageFilter

OUT = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais"
W, H = 640, 360

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

targets = [
    ("console_playstation_4.webp", "https://upload.wikimedia.org/wikipedia/commons/8/8c/PS4-Console-wDS4.png", "#002050", "#000818", "PS4"),
    ("console_psp_vita.webp", "https://upload.wikimedia.org/wikipedia/commons/5/5d/Sony-PSP-1000-Body.png", "#101030", "#050510", "PSP"),
    ("console_nintendo_3ds.webp", "https://upload.wikimedia.org/wikipedia/commons/0/0a/Nintendo-3DS-AquaOpen.png", "#400010", "#100005", "3DS"),
    ("console_retro_emuladores.webp", "https://upload.wikimedia.org/wikipedia/commons/9/95/PSX-Console-wController.png", "#202025", "#08080a", "PS1 RETRO")
]

for out_name, url, col1, col2, tag in targets:
    tmp_path = f"/tmp/{out_name}.png"
    print(f"Baixando {tag}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(tmp_path, 'wb') as out_file:
            out_file.write(response.read())
        
        # Abrir foto recortada
        photo = Image.open(tmp_path).convert("RGBA")
        
        # Redimensionar mantendo proporção para caber em W x H com margem
        pw, ph = photo.size
        scale = min((W * 0.75) / pw, (H * 0.70) / ph)
        new_w, new_h = int(pw * scale), int(ph * scale)
        photo = photo.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Criar background studio dark com glow
        bg = Image.new("RGB", (W, H), col2)
        draw = ImageDraw.Draw(bg)
        # gradiente linear vertical
        r1, g1, b1 = int(col1[1:3], 16), int(col1[3:5], 16), int(col1[5:7], 16)
        r2, g2, b2 = int(col2[1:3], 16), int(col2[3:5], 16), int(col2[5:7], 16)
        for y in range(H):
            t = y / H
            c = (int(r1 + (r2 - r1) * t), int(g1 + (g2 - g1) * t), int(b1 + (b2 - b1) * t))
            draw.line([(0, y), (W, y)], fill=c)
            
        # Adicionar glow no centro
        glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_layer)
        cx, cy = W // 2, H // 2
        g_draw.ellipse([cx - 140, cy - 80, cx + 140, cy + 80], fill=(r1, g1, b1, 90))
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(35))
        bg.paste(glow_layer, (0, 0), glow_layer)
        
        # Sombra sob o console
        shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(shadow_layer)
        pos_x = (W - new_w) // 2
        pos_y = (H - new_h) // 2
        s_draw.ellipse([pos_x + 10, pos_y + new_h - 15, pos_x + new_w - 10, pos_y + new_h + 15], fill=(0, 0, 0, 160))
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(15))
        bg.paste(shadow_layer, (0, 0), shadow_layer)
        
        # Colar o console no centro
        bg.paste(photo, (pos_x, pos_y), photo)
        
        # Salvar em WebP com alta qualidade
        final_dest = os.path.join(OUT, out_name)
        bg.save(final_dest, "WEBP", quality=88)
        print(f"✅ Salvo: {final_dest} ({os.path.getsize(final_dest)} bytes)")
    except Exception as e:
        print(f"❌ Erro ao processar {tag}: {e}")

