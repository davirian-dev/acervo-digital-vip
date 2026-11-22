#!/usr/bin/env python3
"""
Gera 10 capas de consoles com visual premium usando Pillow.
Cada console tem cores e formas distintas que remetem ao design real.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

OUT = "assets/capas_reais"
os.makedirs(OUT, exist_ok=True)
W, H = 640, 360

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def gradient(draw, w, h, c1, c2):
    for i in range(h):
        draw.line([(0,i),(w,i)], fill=lerp(hex_to_rgb(c1), hex_to_rgb(c2), i/h))

def glow(img, cx, cy, r, color, a=50):
    ov = Image.new('RGBA', img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    rgb = hex_to_rgb(color)
    for i in range(r, 0, -3):
        al = int(a * (i/r)**2)
        d.ellipse([cx-i,cy-i,cx+i,cy+i], fill=rgb+(al,))
    ov = ov.filter(ImageFilter.GaussianBlur(25))
    return Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')

def font(sz):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

def center_text(draw, text, y, f, fill=(255,255,255)):
    bb = draw.textbbox((0,0), text, font=f)
    x = (W - (bb[2]-bb[0])) // 2
    draw.text((x+2, y+2), text, font=f, fill=(0,0,0,160))
    draw.text((x, y), text, font=f, fill=fill)

def draw_console_body(draw, x, y, w, h, color, radius=15):
    """Desenha corpo retangular arredondado do console"""
    r,g,b = hex_to_rgb(color)
    draw.rounded_rectangle([x,y,x+w,y+h], radius=radius, fill=(r,g,b))
    # Highlight superior
    draw.rounded_rectangle([x+3,y+3,x+w-3,y+8], radius=5, fill=(r+30,g+30,b+30) if r<225 else (255,255,255))

def draw_controller_shape(draw, cx, cy, color, scale=1.0):
    """Desenha forma simplificada de controle"""
    r,g,b = hex_to_rgb(color)
    s = scale
    # Corpo principal
    draw.ellipse([cx-40*s, cy-20*s, cx+40*s, cy+20*s], fill=(r,g,b))
    # Grips
    draw.ellipse([cx-55*s, cy-10*s, cx-30*s, cy+25*s], fill=(r,g,b))
    draw.ellipse([cx+30*s, cy-10*s, cx+55*s, cy+25*s], fill=(r,g,b))
    # Botões
    draw.ellipse([cx-10*s, cy-8*s, cx-4*s, cy-2*s], fill=(60,60,60))
    draw.ellipse([cx+15*s, cy-10*s, cx+21*s, cy-4*s], fill=(60,60,60))

def make_ps5(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#080818', '#000008')
    img = glow(img, W//2, H//2, 180, '#0040ff', 35)
    d = ImageDraw.Draw(img)
    # PS5 body - futuristic white wings
    cx, cy = W//2, H//2 - 20
    # Centro preto
    d.rounded_rectangle([cx-30, cy-80, cx+30, cy+60], radius=8, fill='#111111')
    # Asa esquerda branca
    pts_l = [(cx-30, cy-80), (cx-70, cy-60), (cx-65, cy+50), (cx-30, cy+60)]
    d.polygon(pts_l, fill='#e8e8e8')
    # Asa direita branca
    pts_r = [(cx+30, cy-80), (cx+70, cy-60), (cx+65, cy+50), (cx+30, cy+60)]
    d.polygon(pts_r, fill='#e8e8e8')
    # Blue LED strip
    d.line([(cx-28, cy-78), (cx-28, cy+58)], fill='#0088ff', width=2)
    d.line([(cx+28, cy-78), (cx+28, cy+58)], fill='#0088ff', width=2)
    # PS logo
    center_text(d, "PS5", cy+80, font(36), fill=(255,255,255))
    center_text(d, "PlayStation 5", cy+120, font(16), fill=(150,180,220))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(0,80,255,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_ps4(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#0a0a1a', '#000005')
    img = glow(img, W//2, H//2, 160, '#003399', 30)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 20
    # PS4 Slim - angular black slab
    d.polygon([(cx-100, cy-25), (cx+100, cy-30), (cx+110, cy+30), (cx-90, cy+30)], fill='#1a1a2a')
    d.polygon([(cx-100, cy-25), (cx+100, cy-30), (cx+100, cy-28), (cx-100, cy-23)], fill='#333355')
    # Light bar
    d.line([(cx-95, cy-24), (cx+95, cy-29)], fill='#0066ff', width=2)
    # Controller abaixo
    draw_controller_shape(d, cx, cy+70, '#222244', 1.2)
    center_text(d, "PS4", cy+100, font(36), fill=(255,255,255))
    center_text(d, "PlayStation 4", cy+140, font(16), fill=(130,160,210))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(0,60,200,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_ps2(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#0a0a15', '#000008')
    img = glow(img, W//2, H//2, 150, '#1a1aaa', 25)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 30
    # PS2 vertical tower
    d.rounded_rectangle([cx-35, cy-90, cx+35, cy+60], radius=5, fill='#1a1a30')
    # Disc tray line
    d.line([(cx-33, cy-20), (cx+33, cy-20)], fill='#333366', width=2)
    # PS2 blue badge
    d.rounded_rectangle([cx-20, cy-85, cx+20, cy-70], radius=3, fill='#0033aa')
    d.text((cx-12, cy-83), "PS2", font=font(10), fill=(200,220,255))
    # Ports
    for i in range(4):
        d.rounded_rectangle([cx-30+i*17, cy+40, cx-18+i*17, cy+50], radius=2, fill='#2a2a50')
    center_text(d, "PS2", cy+80, font(36), fill=(255,255,255))
    center_text(d, "PlayStation 2 Classic", cy+120, font(16), fill=(120,140,200))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(30,30,150,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_switch(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#0a0a0a', '#050505')
    img = glow(img, W//2-80, H//2, 120, '#ff0000', 30)
    img = glow(img, W//2+80, H//2, 120, '#0088ff', 30)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 20
    # Tablet central
    d.rounded_rectangle([cx-80, cy-55, cx+80, cy+55], radius=8, fill='#1a1a1a')
    # Screen
    d.rounded_rectangle([cx-70, cy-45, cx+70, cy+45], radius=5, fill='#111122')
    # Joy-Con esquerdo (neon red)
    d.rounded_rectangle([cx-110, cy-55, cx-78, cy+55], radius=10, fill='#e60012')
    # Joy-Con direito (neon blue)  
    d.rounded_rectangle([cx+78, cy-55, cx+110, cy+55], radius=10, fill='#0ab9e6')
    # Buttons
    d.ellipse([cx-100, cy-30, cx-90, cy-20], fill='#cc0000')
    d.ellipse([cx+90, cy-10, cx+100, cy], fill='#0099cc')
    # Analog sticks
    d.ellipse([cx-100, cy+10, cx-88, cy+22], fill='#aa0000')
    d.ellipse([cx+88, cy+20, cx+100, cy+32], fill='#0088aa')
    center_text(d, "Nintendo Switch", cy+80, font(32), fill=(255,255,255))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(230,0,18,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_3ds(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#0a0a1a', '#000008')
    img = glow(img, W//2, H//2, 140, '#cc0000', 25)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 10
    # Tela superior (articulada)
    d.rounded_rectangle([cx-70, cy-80, cx+70, cy-15], radius=8, fill='#cc0000')
    d.rounded_rectangle([cx-60, cy-72, cx+60, cy-22], radius=4, fill='#111122')
    # Hinge
    d.rounded_rectangle([cx-75, cy-17, cx+75, cy-13], radius=3, fill='#aa0000')
    # Tela inferior + body
    d.rounded_rectangle([cx-75, cy-13, cx+75, cy+65], radius=8, fill='#cc0000')
    d.rounded_rectangle([cx-45, cy-5, cx+20, cy+35], radius=4, fill='#111122')
    # D-pad
    d.rounded_rectangle([cx-65, cy, cx-50, cy+25], radius=2, fill='#990000')
    # Botões ABXY
    d.ellipse([cx+30, cy+5, cx+40, cy+15], fill='#ffcc00')
    d.ellipse([cx+42, cy, cx+52, cy+10], fill='#ff0000')
    d.ellipse([cx+30, cy+18, cx+40, cy+28], fill='#00cc00')
    d.ellipse([cx+42, cy+13, cx+52, cy+23], fill='#0088ff')
    center_text(d, "Nintendo 3DS", cy+85, font(32), fill=(255,255,255))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(200,0,0,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_xbox(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#080a08', '#000500')
    img = glow(img, W//2, H//2, 160, '#00aa00', 30)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 20
    # Xbox 360 body - curved white
    d.rounded_rectangle([cx-60, cy-70, cx+60, cy+50], radius=20, fill='#e0e0e0')
    # Faceplate division
    d.line([(cx-55, cy-10), (cx+55, cy-10)], fill='#cccccc', width=2)
    # Power ring (green!)
    d.ellipse([cx-20, cy-55, cx+20, cy-15], outline='#00cc00', width=3)
    d.ellipse([cx-15, cy-50, cx+15, cy-20], outline='#00aa00', width=2)
    # Center X button
    d.text((cx-6, cy-45), "X", font=font(16), fill='#008800')
    # Disc tray
    d.ellipse([cx-25, cy+5, cx+25, cy+35], outline='#bbbbbb', width=2)
    # Side vents (gray)
    d.rounded_rectangle([cx+62, cy-60, cx+72, cy+40], radius=5, fill='#c0c0c0')
    center_text(d, "Xbox 360", cy+70, font(36), fill=(255,255,255))
    center_text(d, "Live • Green Ring", cy+110, font(16), fill=(100,220,100))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(0,180,0,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_pc(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#080810', '#000005')
    # Multiple RGB glows
    img = glow(img, W//2-100, H//2, 120, '#ff0066', 25)
    img = glow(img, W//2+100, H//2, 120, '#0066ff', 25)
    img = glow(img, W//2, H//2-50, 100, '#00ff88', 20)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 20
    # Monitor
    d.rounded_rectangle([cx-100, cy-70, cx+100, cy+20], radius=8, fill='#1a1a2a')
    d.rounded_rectangle([cx-90, cy-62, cx+90, cy+12], radius=4, fill='#0a0a1a')
    # Monitor stand
    d.polygon([(cx-15, cy+20), (cx+15, cy+20), (cx+25, cy+40), (cx-25, cy+40)], fill='#222233')
    # Tower case (right side)
    d.rounded_rectangle([cx+120, cy-65, cx+180, cy+40], radius=6, fill='#1a1a2a')
    # RGB strips on tower
    for i, color in enumerate(['#ff0066', '#00ff88', '#0066ff']):
        y = cy - 50 + i * 25
        d.line([(cx+125, y), (cx+175, y)], fill=color, width=2)
    # Keyboard
    d.rounded_rectangle([cx-80, cy+50, cx+80, cy+70], radius=4, fill='#222233')
    # RGB keyboard glow
    d.line([(cx-75, cy+55), (cx+75, cy+55)], fill='#ff0066', width=1)
    d.line([(cx-75, cy+60), (cx+75, cy+60)], fill='#00ff88', width=1)
    d.line([(cx-75, cy+65), (cx+75, cy+65)], fill='#0066ff', width=1)
    # Mouse
    d.ellipse([cx+90, cy+50, cx+110, cy+70], fill='#222233')
    center_text(d, "PC Gaming", cy+85, font(32), fill=(255,255,255))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(160,0,255,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_vr(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#0a0a1a', '#050510')
    img = glow(img, W//2, H//2, 180, '#7c3aed', 35)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 20
    # VR headset body
    d.rounded_rectangle([cx-80, cy-40, cx+80, cy+40], radius=25, fill='#e8e8e8')
    # Visor/lens area
    d.rounded_rectangle([cx-70, cy-30, cx+70, cy+25], radius=15, fill='#1a1a2a')
    # Lenses
    d.ellipse([cx-40, cy-20, cx-5, cy+15], fill='#111122', outline='#333355', width=2)
    d.ellipse([cx+5, cy-20, cx+40, cy+15], fill='#111122', outline='#333355', width=2)
    # Strap
    d.arc([cx-120, cy-50, cx+120, cy+30], start=200, end=340, fill='#cccccc', width=4)
    # Purple light accent
    d.line([(cx-78, cy-5), (cx-78, cy+5)], fill='#7c3aed', width=3)
    d.line([(cx+78, cy-5), (cx+78, cy+5)], fill='#7c3aed', width=3)
    center_text(d, "VR / Oculus", cy+60, font(36), fill=(255,255,255))
    center_text(d, "Realidade Virtual", cy+100, font(16), fill=(160,140,230))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(124,58,237,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_psp(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#0a0a15', '#000008')
    img = glow(img, W//2, H//2, 150, '#0044aa', 25)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2 - 20
    # PSP body - wide handheld
    d.rounded_rectangle([cx-130, cy-40, cx+130, cy+40], radius=20, fill='#1a1a2a')
    # Screen
    d.rounded_rectangle([cx-80, cy-30, cx+80, cy+30], radius=5, fill='#0a0a15')
    # D-pad (left)
    d.rounded_rectangle([cx-120, cy-10, cx-90, cy+10], radius=3, fill='#222244')
    # Buttons (right)
    d.ellipse([cx+95, cy-15, cx+105, cy-5], fill='#ff88aa')
    d.ellipse([cx+108, cy-5, cx+118, cy+5], fill='#8888ff')
    d.ellipse([cx+95, cy+5, cx+105, cy+15], fill='#88ccff')
    d.ellipse([cx+82, cy-5, cx+92, cy+5], fill='#88ff88')
    # Speaker grills
    d.rounded_rectangle([cx-125, cy+20, cx-95, cy+30], radius=3, fill='#151530')
    d.rounded_rectangle([cx+95, cy+20, cx+125, cy+30], radius=3, fill='#151530')
    center_text(d, "PSP / PS Vita", cy+60, font(32), fill=(255,255,255))
    center_text(d, "Handhelds Sony", cy+95, font(16), fill=(130,160,210))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(0,60,180,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

def make_retro(filename):
    img = Image.new('RGB', (W,H))
    d = ImageDraw.Draw(img)
    gradient(d, W, H, '#1a0a0a', '#050200')
    img = glow(img, W//2-100, H//2, 100, '#ff6600', 25)
    img = glow(img, W//2+100, H//2, 100, '#ff0066', 25)
    d = ImageDraw.Draw(img)
    # SNES (top left)
    d.rounded_rectangle([80, 60, 220, 120], radius=8, fill='#c8c0b8')
    d.rounded_rectangle([100, 70, 200, 85], radius=3, fill='#8080a0')
    d.text((115, 90), "SNES", font=font(14), fill='#444444')
    # NES (top right)
    d.rounded_rectangle([380, 60, 530, 115], radius=5, fill='#c0b8b0')
    d.rounded_rectangle([390, 70, 520, 85], radius=3, fill='#333333')
    d.text((425, 88), "NES", font=font(14), fill='#444444')
    # Mega Drive (bottom left)
    d.rounded_rectangle([100, 160, 260, 220], radius=8, fill='#1a1a1a')
    d.rounded_rectangle([120, 170, 240, 182], radius=3, fill='#cc0000')
    d.text((115, 192), "MEGA DRIVE", font=font(12), fill='#cc0000')
    # PS1 (bottom right)
    d.rounded_rectangle([360, 160, 520, 220], radius=8, fill='#c8c8c8')
    d.text((395, 175), "PlayStation", font=font(14), fill='#333333')
    d.ellipse([400, 192, 420, 212], outline='#0044aa', width=2)
    # Center title
    center_text(d, "RETRO GAMING", 260, font(32), fill=(255,200,100))
    center_text(d, "SNES • NES • Mega Drive • PS1", 300, font(16), fill=(200,180,140))
    d.rounded_rectangle([2,2,W-3,H-3], radius=12, outline=(255,100,0,80), width=1)
    img.save(os.path.join(OUT, filename), 'WEBP', quality=85)
    print(f"  ✓ {filename}")

# =====================================================
# GERAR TODOS OS 10 CONSOLES
# =====================================================
print("\n🎮 CONSOLES:")
make_ps5("console_playstation_5.webp")
make_ps4("console_playstation_4.webp")
make_ps2("console_playstation_2.webp")
make_switch("console_nintendo_switch.webp")
make_3ds("console_nintendo_3ds.webp")
make_xbox("console_xbox_360.webp")
make_pc("console_pc_games.webp")
make_vr("console_vr_oculus.webp")
make_psp("console_psp_vita.webp")
make_retro("console_retro_emuladores.webp")

# Criar aliases necessários
import shutil
aliases = [
    ("console_pc_games.webp", "console_pc_steam.webp"),
    ("console_psp_vita.webp", "console_psp_psvita.webp"),
    ("console_retro_emuladores.webp", "console_ps1_retro.webp"),
]
print("\n🔗 ALIASES:")
for src, dst in aliases:
    shutil.copy2(os.path.join(OUT, src), os.path.join(OUT, dst))
    print(f"  ✓ {src} → {dst}")

print("\n✅ 10 consoles + 3 aliases gerados!")
