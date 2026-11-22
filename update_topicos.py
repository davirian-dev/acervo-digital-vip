#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atualiza a seção #topicos no index.html para ter 8 cards perfeitos
com imagens WebP reais para todos os grupos de tópicos.
"""

import re

INDEX_PATH = '/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

def photo_card(img_filename, badge, title, author, badge_color_class):
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

topicos_section = f"""    <!-- 68 TÓPICOS NO TELEGRAM -->
    <section id="topicos" class="mt-16 mb-20 glass-panel rounded-3xl p-6 sm:p-10 border border-white/10 relative overflow-hidden shadow-2xl">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>📁 ORGANIZAÇÃO IMPECÁVEL</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">68 Tópicos Exclusivos no Telegram</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Nada de arquivos jogados ou links quebrados. Cada categoria possui um tópico dedicado com busca e download direto.</p>
        </div>
        <div class="flex items-center gap-2 text-xs text-emerald-400 font-bold bg-emerald-500/10 px-3 py-1.5 rounded-xl border border-emerald-500/20">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Todos os 68 Tópicos Ativos
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Tópicos 01 a 08: IA & Automação -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-purple-500/40 transition-all">
          {photo_card("banner_topicos_ia_automacao.webp", "TÓPICOS #01 AO #08", "IA & Automação Inteligente", "Bots, Prompts & Agentes", "text-purple-400 bg-purple-500/20 border-purple-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• ChatGPT, Claude e Midjourney Pro</div>
            <div>• N8N, Typebot & Webhooks Avançados</div>
            <div>• Lovable, Make e Criação de Apps IA</div>
          </div>
        </div>

        <!-- Tópicos 09 a 18: Tráfego & Performance -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-rose-500/40 transition-all">
          {photo_card("banner_topicos_trafego_vendas.webp", "TÓPICOS #09 AO #18", "Tráfego Pago & Performance", "Meta, Google & TikTok Ads", "text-rose-400 bg-rose-500/20 border-rose-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• Comunidade Sobral de Tráfego 2026</div>
            <div>• Meta Ads Avançado & Escala 7 Dígitos</div>
            <div>• Google Ads, YouTube Ads & TikTok Ads</div>
          </div>
        </div>

        <!-- Tópicos 19 a 26: Copywriting & VSL -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-cyan-500/40 transition-all">
          {photo_card("banner_topicos_copy_lancamentos.webp", "TÓPICOS #19 AO #26", "Copywriting & Ofertas", "VSL, Páginas & Lançamentos", "text-cyan-400 bg-cyan-500/20 border-cyan-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• Copywriting de Alta Conversão & VSL</div>
            <div>• Páginas de Vendas com 15%+ Conversão</div>
            <div>• Gatilhos Mentais & Lançamentos Digitais</div>
          </div>
        </div>

        <!-- Tópicos 27 a 34: E-commerce & Drop -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-amber-500/40 transition-all">
          {photo_card("banner_topicos_drop_ecommerce.webp", "TÓPICOS #27 AO #34", "E-commerce & Dropshipping", "Shopify, Mineração & Fornecedores", "text-amber-400 bg-amber-500/20 border-amber-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• Lojas de Dropshipping Shopify Prontas</div>
            <div>• Mineração Secreta de Produtos Vencedores</div>
            <div>• Fornecedores Nacionais e Internacionais</div>
          </div>
        </div>

        <!-- Tópicos 35 a 42: Dev & Cyber Security -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-emerald-500/40 transition-all">
          {photo_card("banner_topicos_dev_hacking.webp", "TÓPICOS #35 AO #42", "Programação & Cyber Security", "Full-Stack, Python & Pentest", "text-emerald-400 bg-emerald-500/20 border-emerald-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• Alura Formação Programação & Python</div>
            <div>• Hacking Ético, Pentest & Kali Linux</div>
            <div>• Figma UI/UX Design System Pro</div>
          </div>
        </div>

        <!-- Tópicos 43 a 50: Finanças & Cripto -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-yellow-500/40 transition-all">
          {photo_card("banner_topicos_financas_cripto.webp", "TÓPICOS #43 AO #50", "Investimentos, Cripto & Milhas", "Renda Passiva, Bitcoin & Cartões", "text-yellow-400 bg-yellow-500/20 border-yellow-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• Do Mil ao Milhão (Thiago Nigro)</div>
            <div>• Análise de Cripto, DeFi & Bitcoin</div>
            <div>• Milhas Aéreas & Salas VIP Gratuitas</div>
          </div>
        </div>

        <!-- Tópicos 51 a 58: Criadores & YouTube -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-indigo-500/40 transition-all">
          {photo_card("banner_topicos_youtube_criadores.webp", "TÓPICOS #51 AO #58", "YouTube & Redes Sociais", "Canais Dark, Edição & Retenção", "text-indigo-400 bg-indigo-500/20 border-indigo-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• O Novo Mercado (Ícaro de Carvalho)</div>
            <div>• Canais Dark no YouTube & Monetização</div>
            <div>• Edição Profissional Premiere & CapCut</div>
          </div>
        </div>

        <!-- Tópicos 59 a 68: Concursos, Idiomas & Habilidades -->
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between group hover:border-teal-500/40 transition-all">
          {photo_card("banner_topicos_mentalidade_performance.webp", "TÓPICOS #59 AO #68", "Idiomas, Concursos & Práticas", "Inglês, Beleza, Concursos & Games", "text-teal-400 bg-teal-500/20 border-teal-500/30")}
          <div class="space-y-1.5 text-xs text-zinc-400 mt-1">
            <div>• Curso de Inglês Mairo Vergara 5.0</div>
            <div>• Estratégia Concursos & Hashtag Treinamentos</div>
            <div>• Manicure, Cílios, Make & ROMs Gamer</div>
          </div>
        </div>
      </div>
    </section>"""

# Substitui a seção inteira no HTML
pattern = r'<!-- 68 TÓPICOS NO TELEGRAM -->[\s\S]*?</section>'
if re.search(pattern, html):
    html = re.sub(pattern, topicos_section, html, count=1)
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Seção #topicos atualizada com 8 cards com imagens reais!")
else:
    print("ERRO: Padrão da seção #topicos não encontrado")
