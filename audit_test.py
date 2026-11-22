from bs4 import BeautifulSoup
import re

with open("/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html") as f:
    text = f.read()

soup = BeautifulSoup(text, "html.parser")

barras = re.findall(r"filtrarCategoria\(\\", text)
print(f"1. Barras invertidas em filtrarCategoria: {len(barras)}")

cat = soup.find("section", id="catalogo")
blocos = [b["data-cat"] for b in cat.find_all("div", attrs={"data-cat": True})]
print(f"2. Blocos dentro de catalogo: {blocos}")
criadores = cat.find("div", attrs={"data-cat": "criadores"})
filhos_de_criadores = [b["data-cat"] for b in criadores.find_all("div", attrs={"data-cat": True})]
print(f"   Filhos dentro de criadores (deve ser vazio): {filhos_de_criadores}")

blindagem = soup.find(lambda e: e.name == "div" and "Como Funciona a Liberação em 2 Fases" in e.text)
grid3 = soup.find(lambda e: e.name == "div" and "grid-cols-1 md:grid-cols-3" in " ".join(e.get("class", [])))
is_outside = blindagem not in grid3.descendants if (blindagem and grid3) else False
print(f"3. Bloco Blindagem fora do grid-cols-3: {is_outside}")

games_a = soup.find_all("a", onclick=lambda c: c and "Biblioteca Gamer:" in c)
print(f"4. Total de cards de games: {len(games_a)}")
if games_a:
    print("   Classes do card de games:", " ".join(games_a[0].get("class", [])))

funcs = re.findall(r"function\s+([a-zA-Z0-9_]+)", text)
from collections import Counter
counts = Counter(funcs)
dup = {k: v for k, v in counts.items() if v > 1}
print(f"5. Funcoes duplicadas no JS: {dup}")

seo_btn = soup.find("button", onclick=lambda c: c and "seo" in c)
print(f"6. Botao SEO: {seo_btn.get_text(strip=True) if seo_btn else None}")
seo_bloco = soup.find("div", attrs={"data-cat": "seo"})
print(f"   Cards no bloco SEO: {len(seo_bloco.find_all(class_=lambda c: c and 'curso-card' in c)) if seo_bloco else 0}")

canonical = soup.find("link", rel="canonical")
og_url = soup.find("meta", property="og:url")
og_img = soup.find("meta", property="og:image")
og_locale = soup.find("meta", property="og:locale")
tw_card = soup.find("meta", attrs={"name": "twitter:card"})
print(f"7. Canonical: {canonical['href'] if canonical else None}")
print(f"   OG URL: {og_url['content'] if og_url else None}")
print(f"   OG Image: {og_img['content'] if og_img else None}")
print(f"   OG Locale: {og_locale['content'] if og_locale else None}")
print(f"   Twitter Card: {tw_card['content'] if tw_card else None}")

h1s = soup.find_all("h1")
print(f"8. Total de H1: {len(h1s)}")
h2_receber = soup.find(lambda e: e.name == "h2" and "Como Você Recebe" in e.text)
h2_faq = soup.find(lambda e: e.name == "h2" and "Perguntas Frequentes" in e.text)
print(f"   Como Você Recebe é H2: {bool(h2_receber)}")
print(f"   Perguntas Frequentes é H2: {bool(h2_faq)}")

sticky = soup.find("div", id="sticky-cta-bar")
print(f"9. Sticky Bar presente: {bool(sticky)}")
footer = soup.find("footer")
f_classes = " ".join(footer.get("class", []))
print(f"   Footer com pb-24 sm:pb-8: {'pb-24 sm:pb-8' in f_classes}")

video = soup.find("video")
v_classes = " ".join(video.get("class", []))
print(f"10. Video com hidden md:block: {'hidden md:block' in v_classes}")
