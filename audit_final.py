#!/usr/bin/env python3
"""Auditoria final: verifica todas as imagens referenciadas no index.html"""
import re, os

html_path = "index.html"
assets_dir = "assets/capas_reais"

with open(html_path, 'r') as f:
    html = f.read()

# Encontrar todas as referências a imagens em capas_reais
refs = re.findall(r'assets/capas_reais/([^"\')\s]+)', html)
refs = list(set(refs))
refs.sort()

existing = set(os.listdir(assets_dir))
missing = []
found = []

print(f"📋 Total de referências únicas no HTML: {len(refs)}")
print(f"📁 Total de arquivos em capas_reais/: {len(existing)}")
print()

for ref in refs:
    if ref in existing:
        found.append(ref)
    else:
        missing.append(ref)
        print(f"  ❌ FALTANDO: {ref}")

if not missing:
    print("✅ TODAS as imagens referenciadas existem!")
else:
    print(f"\n⚠️  {len(missing)} imagens faltando de {len(refs)} referenciadas")

print(f"\n✅ {len(found)} imagens encontradas")

# Verificar JS syntax
js_errors = []
if "\\\'" in html:
    js_errors.append("Barras invertidas \\' encontradas nos onclick")
if "fecharWidgetOferta" in html and "function fecharWidgetOferta" not in html:
    js_errors.append("fecharWidgetOferta referenciada mas não definida")

print(f"\n🔧 JS Check: {len(js_errors)} problemas")
for e in js_errors:
    print(f"  ⚠️  {e}")

# Verificar seções obrigatórias
sections = ['catalogo', 'ferramentas', 'canais-vip', 'games', 'livros', 'topicos', 'checkout', 'como-recebe', 'faq']
print(f"\n📑 Seções:")
for s in sections:
    if f'id="{s}"' in html:
        print(f"  ✓ #{s}")
    else:
        print(f"  ❌ #{s} NÃO ENCONTRADA")
