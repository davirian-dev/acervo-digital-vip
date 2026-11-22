#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script apply_photos_full.py
Aplica capas fotográficas WebP reais a TODOS os cards do index.html
e elimina todos os placeholders SVG/CSS vazios.
"""

import os
import re

INDEX_PATH = '/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html'
CAPAS_DIR = '/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/assets/capas_reais'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

def photo_card(img_filename, badge, title, author, badge_color_class="text-emerald-400 bg-emerald-500/20 border-emerald-500/30"):
    # Verifica se arquivo existe no disco
    full_path = os.path.join(CAPAS_DIR, img_filename)
    if not os.path.exists(full_path):
        print(f"AVISO: Arquivo não encontrado no disco: {img_filename}")
    
    return f"""<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-zinc-950 border border-white/10 shadow-inner group-hover:scale-105 transition-transform duration-500">
      <img src="/assets/capas_reais/{img_filename}" alt="{title}" loading="lazy" decoding="async" class="w-full h-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent flex flex-col justify-between p-2.5 pointer-events-none">
        <div class="flex items-center justify-between z-10">
          <span class="text-[9px] font-black uppercase px-2 py-0.5 rounded-full bg-black/70 {badge_color_class} backdrop-blur-md border tracking-wider">{badge}</span>
          <span class="text-[9px] text-emerald-400 font-bold bg-emerald-500/20 px-1.5 py-0.5 rounded border border-emerald-500/30">VIP</span>
        </div>
        <div class="z-10">
          <div class="text-[11px] font-bold text-white drop-shadow truncate">{title}</div>
          <div class="text-[10px] text-zinc-300 font-medium truncate">{author}</div>
        </div>
      </div>
    </div>"""

# 1. SEO (6 cards)
seo_cards = [
    ('seo_sem_segredos.webp', 'TOPO DO GOOGLE', 'SEO Sem Segredos', 'Bruno Medeiros', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30'),
    ('formacao_seo_discover.webp', 'SEARCH & DISCOVER', 'SEO Master & Discover', 'Especialistas de Search', 'text-cyan-400 bg-cyan-500/20 border-cyan-500/30'),
    ('youtube_seo_extremo.webp', 'ALGORITMO YOUTUBE', 'YouTube SEO & Retenção', 'Criadores Virais', 'text-rose-400 bg-rose-500/20 border-rose-500/30'),
    ('copywriting_retencao_vsl.webp', 'RETENÇÃO & CRO', 'Copywriting & Retenção', 'Copy Masters', 'text-purple-400 bg-purple-500/20 border-purple-500/30'),
    ('google_meu_negocio_local.webp', 'RENDA RECORRENTE', 'Google Meu Negócio Local', 'Agências Locais', 'text-amber-400 bg-amber-500/20 border-amber-500/30'),
    ('funis_retencao_ltv.webp', 'LTV & RETENÇÃO', 'Funis de Retenção & LTV', 'Growth Hackers', 'text-teal-400 bg-teal-500/20 border-teal-500/30')
]

# Substitui os cards do bloco SEO
for img, badge, title, author, color in seo_cards:
    pc = photo_card(img, badge, title, author, color)
    # Busca pelo card com este título
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 2. DEV & DESIGN (Figma e Hacking)
dev_cards = [
    ('Figma-UI-UX-Design-Pro.webp', 'UI/UX DESIGN', 'Figma UI/UX Design Pro', 'Design System & Interfaces', 'text-purple-400 bg-purple-500/20 border-purple-500/30'),
    ('Hacking-Etico-Pentest-do-Zero.webp', 'CYBER SECURITY', 'Hacking Ético & Pentest', 'Kali Linux & Red Team', 'text-cyan-400 bg-cyan-500/20 border-cyan-500/30')
]
for img, badge, title, author, color in dev_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 3. CRIADORES (O Novo Mercado e Do Mil ao Milhão)
criadores_cards = [
    ('O-Novo-Mercado-Icaro-de-Carvalho.webp', 'CLÁSSICO ABSOLUTO', 'O Novo Mercado', 'Ícaro de Carvalho', 'text-amber-400 bg-amber-500/20 border-amber-500/30'),
    ('Do-Mil-ao-Milhao-Thiago-Nigro.webp', 'FINANÇAS PESSOAIS', 'Do Mil ao Milhão', 'Thiago Nigro (Primo Rico)', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30')
]
for img, badge, title, author, color in criadores_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 4. BELEZA (4 cards)
beleza_cards = [
    ('Faby-Cardoso-Manicure-Pedicure.webp', 'MANICURE & PEDICURE', 'Manicure & Pedicure Pro', 'Faby Cardoso', 'text-pink-400 bg-pink-500/20 border-pink-500/30'),
    ('Larissa-Costa-Viver-de-Cilios.webp', 'LASH DESIGNER', 'Viver de Cílios Pro', 'Larissa Costa', 'text-pink-400 bg-pink-500/20 border-pink-500/30'),
    ('Andreia-Venturini-Maquiagem-na-Web.webp', 'MAKEUP ARTIST', 'Maquiagem na Web 2.0', 'Andreia Venturini', 'text-rose-400 bg-rose-500/20 border-rose-500/30'),
    ('Confeitaria-Lucrativa-Marmitas-Fitness.webp', 'DOCES & MARMITAS', 'Confeitaria & Marmitas Fit', 'Chef Confeiteiro', 'text-amber-400 bg-amber-500/20 border-amber-500/30')
]
for img, badge, title, author, color in beleza_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 5. EDUCAÇÃO (4 cards)
educacao_cards = [
    ('Mairo-Vergara-Ingles.webp', 'INGLÊS COMPLETO', 'Curso de Inglês 5.0', 'Mairo Vergara', 'text-indigo-400 bg-indigo-500/20 border-indigo-500/30'),
    ('Estrategia-Concursos-Preparatorio.webp', 'CONCURSOS PÚBLICOS', 'Estratégia Concursos', 'Professores Oficiais', 'text-blue-400 bg-blue-500/20 border-blue-500/30'),
    ('Hashtag-Excel-Impressionador.webp', 'DADOS & GESTÃO', 'Excel, Power BI & Python', 'Hashtag Treinamentos', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30'),
    ('Bilinguismo-Montessori.webp', 'MÉTODO MONTESSORI', 'Bilinguismo Infantil & Método', 'Educação Infantil', 'text-amber-400 bg-amber-500/20 border-amber-500/30')
]
for img, badge, title, author, color in educacao_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 6. FERRAMENTAS (8 packs)
ferramentas_cards = [
    ('ferramenta_typebot_bots.webp', 'BOTS & FLUXOS', 'Typebot & Robôs Prontos', 'Fluxos de Venda e SAC', 'text-purple-400 bg-purple-500/20 border-purple-500/30'),
    ('ferramenta_canva_pro.webp', 'DESIGN VIP', 'Canva Pro & Mega Pack', 'Artes e Feeds Editáveis', 'text-blue-400 bg-blue-500/20 border-blue-500/30'),
    ('ferramenta_videos_virais.webp', 'VÍDEOS 4K', 'Acervo de Vídeos Virais', 'Banco de Imagens 4K Ultra', 'text-red-400 bg-red-500/20 border-red-500/30'),
    ('ferramenta_paginas_vendas.webp', 'HIGH CRO', 'Páginas de Alta Conversão', 'Templates Elementor & Webflow', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30'),
    ('ferramenta_prompts_ia.webp', 'ENGENHARIA PROMPT', 'Super Pack de Prompts IA', 'Engenharia Reversa ChatGPT & Midjourney', 'text-cyan-400 bg-cyan-500/20 border-cyan-500/30'),
    ('ferramenta_plrs_revenda.webp', 'DIREITOS DE REVENDA', 'Mega Pack PLRs Validados', 'Páginas, VSLs e E-books Prontos', 'text-amber-400 bg-amber-500/20 border-amber-500/30'),
    ('ferramenta_planilhas_gestao.webp', 'DASHBOARDS GESTÃO', 'Planilhas de Gestão & Tráfego', 'Controle Financeiro & ROI', 'text-teal-400 bg-teal-500/20 border-teal-500/30'),
    ('ferramenta_leads_prospeccao.webp', 'LEADS SEGMENTADOS', 'Base de Leads B2B Segmentados', 'Listas Quentes para Cold Call & Zap', 'text-indigo-400 bg-indigo-500/20 border-indigo-500/30')
]
for img, badge, title, author, color in ferramentas_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 7. CANAIS VIP (8 canais)
canais_cards = [
    ('canal_fabrica_de_robos.webp', 'CANAL TELEGRAM', 'Fábrica de Robôs', '@FabricaDeRobos_bot', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30'),
    ('canal_apk_premium.webp', 'CANAL TELEGRAM', 'Apk Premium', '@ApkPremium_bot', 'text-cyan-400 bg-cyan-500/20 border-cyan-500/30'),
    ('canal_analise_cripto.webp', 'CANAL TELEGRAM', 'Análise de Criptomoeda', '@AnaliseCripto_bot', 'text-amber-400 bg-amber-500/20 border-amber-500/30'),
    ('canal_nutritips_saude.webp', 'CANAL TELEGRAM', 'NutriTips & Saúde', '@NutriTips_bot', 'text-green-400 bg-green-500/20 border-green-500/30'),
    ('canal_notas_medicas.webp', 'CANAL TELEGRAM', 'Notas Médicas & Saúde', '@NotasMedicas_bot', 'text-blue-400 bg-blue-500/20 border-blue-500/30'),
    ('canal_receitas_cozinha.webp', 'CANAL TELEGRAM', 'Receitas & Cozinha Fácil', '@ReceitasFaceis_bot', 'text-orange-400 bg-orange-500/20 border-orange-500/30'),
    ('canal_mente_vencedora.webp', 'CANAL TELEGRAM', 'Mente Vencedora', '@MenteVencedora_bot', 'text-purple-400 bg-purple-500/20 border-purple-500/30'),
    ('canal_wallpapers_hd.webp', 'CANAL TELEGRAM', 'Wallpapers 4K & HD', '@WallpapersVIP_bot', 'text-rose-400 bg-rose-500/20 border-rose-500/30')
]
for img, badge, title, author, color in canais_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 8. LIVROS, TEOLOGIA & GOLS (8 canais extras)
livros_cards = [
    ('canal_teologia_gospel.webp', 'CANAL TELEGRAM', 'Teologia & Livros Gospel', '@TeologiaGospel_bot', 'text-amber-400 bg-amber-500/20 border-amber-500/30'),
    ('canal_livros_medicina.webp', 'CANAL TELEGRAM', 'Livros de Medicina & Saúde', '@LivrosMedicina_bot', 'text-blue-400 bg-blue-500/20 border-blue-500/30'),
    ('canal_audio_livros.webp', 'CANAL TELEGRAM', 'Áudio Livros & Best-Sellers', '@AudioLivros_bot', 'text-teal-400 bg-teal-500/20 border-teal-500/30'),
    ('canal_gols_ao_vivo.webp', 'CANAL TELEGRAM', 'Gols ao Vivo & Futebol', '@GolsFutebol_bot', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30'),
    ('canal_achadinhos_promocoes.webp', 'CANAL TELEGRAM', 'Cale-se e Leve Meu Dinheiro', '@AchadinhosVIP_bot', 'text-yellow-400 bg-yellow-500/20 border-yellow-500/30'),
    ('canal_figurinhas_design.webp', 'CANAL TELEGRAM', 'Figurinhas & Tatuagens', '@FigurinhasVIP_bot', 'text-pink-400 bg-pink-500/20 border-pink-500/30'),
    ('canal_softwares_2026.webp', 'CANAL TELEGRAM', 'Softwares & Utilitários 2026', '@SoftwaresVIP_bot', 'text-cyan-400 bg-cyan-500/20 border-cyan-500/30'),
    ('canal_historia_bw.webp', 'CANAL TELEGRAM', 'História em Preto e Branco', '@HistoriaVIP_bot', 'text-slate-400 bg-slate-500/20 border-slate-500/30')
]
for img, badge, title, author, color in livros_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 9. 68 TÓPICOS NO TELEGRAM (8 grupos principais)
topicos_cards = [
    ('banner_topicos_ia_automacao.webp', 'TÓPICOS #01 AO #08', 'IA & Automação Inteligente', 'Bots, Prompts & Agentes', 'text-purple-400 bg-purple-500/20 border-purple-500/30'),
    ('banner_topicos_trafego_vendas.webp', 'TÓPICOS #09 AO #20', 'Tráfego Pago & Performance', 'Meta, Google & TikTok Ads', 'text-rose-400 bg-rose-500/20 border-rose-500/30'),
    ('banner_topicos_copy_lancamentos.webp', 'TÓPICOS #21 AO #28', 'Copywriting & Ofertas', 'VSL, Páginas & Lançamentos', 'text-cyan-400 bg-cyan-500/20 border-cyan-500/30'),
    ('banner_topicos_drop_ecommerce.webp', 'TÓPICOS #29 AO #36', 'E-commerce & Dropshipping', 'Shopify, Mineração & Fornecedores', 'text-amber-400 bg-amber-500/20 border-amber-500/30'),
    ('banner_topicos_dev_hacking.webp', 'TÓPICOS #37 AO #44', 'Programação & Cyber Security', 'Full-Stack, Python & Pentest', 'text-emerald-400 bg-emerald-500/20 border-emerald-500/30'),
    ('banner_topicos_financas_cripto.webp', 'TÓPICOS #45 AO #52', 'Investimentos, Cripto & Milhas', 'Renda Passiva, Bitcoin & Cartões', 'text-yellow-400 bg-yellow-500/20 border-yellow-500/30'),
    ('banner_topicos_youtube_criadores.webp', 'TÓPICOS #53 AO #60', 'YouTube & Redes Sociais', 'Canais Dark, Edição & Retenção', 'text-indigo-400 bg-indigo-500/20 border-indigo-500/30'),
    ('banner_topicos_mentalidade_performance.webp', 'TÓPICOS #61 AO #68', 'Idiomas, Livros & Hábitos', 'Inglês, Best-Sellers & Alta Performance', 'text-teal-400 bg-teal-500/20 border-teal-500/30')
]
for img, badge, title, author, color in topicos_cards:
    pc = photo_card(img, badge, title, author, color)
    pattern = r'<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr[\s\S]*?' + re.escape(title) + r'[\s\S]*?</div>\s*</div>'
    html = re.sub(pattern, pc, html, count=1)

# 10. Atualiza o preload do hero no <head>
if 'rel="preload" as="image"' not in html:
    html = html.replace('<!-- Open Graph', '<link rel="preload" as="image" href="/assets/acervo_vip_hero_mockup.webp">\n  <!-- Open Graph')

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html atualizado com todas as capas fotográficas reais!")
