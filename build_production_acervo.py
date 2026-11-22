#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_production_acervo.py
Gera o index.html final, ultra otimizado, sem erros e com fotos reais em 100% dos cards.
Combina os módulos de refactor_full.py com o catálogo completo de 73 cursos e seções ricas em fotos reais.
"""

import os
import re
import importlib.util
from bs4 import BeautifulSoup

BASE_DIR = '/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip'
BAK_PATH = os.path.join(BASE_DIR, 'index.html.bak')
OUT_PATH = os.path.join(BASE_DIR, 'index.html')
CAPAS_DIR = os.path.join(BASE_DIR, 'assets/capas_reais')

# Importa as seções base de refactor_full.py
spec = importlib.util.spec_from_file_location('refactor_full', os.path.join(BASE_DIR, 'refactor_full.py'))
rf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rf)

with open(BAK_PATH, 'r', encoding='utf-8') as f:
    bak_soup = BeautifulSoup(f.read(), 'html.parser')

def photo_card(img_filename, badge, title, author, badge_color_class="text-emerald-400 bg-emerald-500/20 border-emerald-500/30"):
    full_path = os.path.join(CAPAS_DIR, img_filename)
    if not os.path.exists(full_path):
        print(f"AVISO: Arquivo não existe no disco: {img_filename}")
    
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

# -------------------------------------------------------------
# 1. FILEIRA DE SEO (6 Treinamentos)
# -------------------------------------------------------------
bloco_seo = f"""
      <!-- FILEIRA: SEO, TRÁFEGO ORGÂNICO & RETENÇÃO (MÁXIMO LTV) -->
      <div class="categoria-bloco" data-cat="seo">
        <div class="flex items-center justify-between mb-3.5">
          <div class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">🔍</span>
            <h3 class="text-lg sm:text-xl font-bold text-white tracking-tight">SEO, Tráfego Orgânico & Retenção de Alta Conversão</h3>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 uppercase">Tráfego Grátis & LTV</span>
          </div>
          <span class="text-xs text-zinc-500 hidden sm:inline">6 Treinamentos Completos</span>
        </div>

        <div class="flex gap-4 overflow-x-auto carrossel-scroll snap-x snap-mandatory pb-3 pt-1">
          <!-- Card 1: SEO Sem Segredos -->
          <div onclick="abrirModalPixCurso('SEO Sem Segredos (Bruno Medeiros)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="SEO Sem Segredos Bruno Medeiros Ranqueamento Topo Google Blogs Lucrativos Backlinks Trafego Organico">
            <div>
              {photo_card("seo_sem_segredos.webp", "TOPO DO GOOGLE", "SEO Sem Segredos", "Bruno Medeiros", "text-emerald-400 bg-emerald-500/20 border-emerald-500/30")}
              <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors line-clamp-1">SEO Sem Segredos</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Ranqueamento no topo do Google, blogs altamente lucrativos e estratégias de SEO on-page/off-page.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Tráfego Orgânico</span>
            </div>
          </div>

          <!-- Card 2: Formação SEO Master & Google Discover -->
          <div onclick="abrirModalPixCurso('Formação SEO Master & Google Discover')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Formacao SEO Master Google Discover Trafego Massivo Organico Portais E-commerce Sem Anuncios">
            <div>
              {photo_card("formacao_seo_discover.webp", "SEARCH & DISCOVER", "SEO Master & Discover", "Especialistas de Search", "text-cyan-400 bg-cyan-500/20 border-cyan-500/30")}
              <h4 class="font-bold text-sm text-white group-hover:text-cyan-400 transition-colors line-clamp-1">Formação SEO Master & Discover</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Tráfego orgânico massivo para sites e e-commerces explorando o algoritmo do Google Discover sem anúncios.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-cyan-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Escala de Visitas</span>
            </div>
          </div>

          <!-- Card 3: YouTube SEO & Retenção Extrema -->
          <div onclick="abrirModalPixCurso('YouTube SEO & Retenção Extrema')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-rose-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="YouTube SEO Retencao Extrema Algoritmo CTR Titulos Magneticos Thumbnails Roteiros Virais">
            <div>
              {photo_card("youtube_seo_extremo.webp", "ALGORITMO YOUTUBE", "YouTube SEO & Retenção", "Criadores Virais", "text-rose-400 bg-rose-500/20 border-rose-500/30")}
              <h4 class="font-bold text-sm text-white group-hover:text-rose-400 transition-colors line-clamp-1">YouTube SEO & Retenção Extrema</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Como dominar o algoritmo do YouTube: títulos magnéticos, thumbnails de alto CTR e ganchos de alta retenção.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-rose-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Vídeos & Retenção</span>
            </div>
          </div>

          <!-- Card 4: Copywriting & Retenção de Audiência -->
          <div onclick="abrirModalPixCurso('Copywriting & Retenção de Audiência')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-purple-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Copywriting Retencao de Audiencia VSL Paginas de Vendas Taxa de Conversao CRO Storytelling Persuasao">
            <div>
              {photo_card("copywriting_retencao_vsl.webp", "RETENÇÃO & CRO", "Copywriting & Retenção", "Copy Masters", "text-purple-400 bg-purple-500/20 border-purple-500/30")}
              <h4 class="font-bold text-sm text-white group-hover:text-purple-400 transition-colors line-clamp-1">Copywriting & Retenção</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Como segurar o visitante na página até o final, eliminar taxa de rejeição e multiplicar a conversão de vendas.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-purple-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Conversão Máxima</span>
            </div>
          </div>

          <!-- Card 5: Google Meu Negócio & SEO Local Pro -->
          <div onclick="abrirModalPixCurso('Google Meu Negócio & SEO Local Pro')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-amber-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Google Meu Negocio SEO Local Pro Empresas Locais Google Maps Mensalidade Recorrente Agencias">
            <div>
              {photo_card("google_meu_negocio_local.webp", "RENDA RECORRENTE", "Google Meu Negócio Local", "Agências Locais", "text-amber-400 bg-amber-500/20 border-amber-500/30")}
              <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors line-clamp-1">Google Meu Negócio & SEO Local</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Como cobrar mensalidades recorrentes de empresas locais colocando-as no topo do Google Maps.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-amber-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Prestação de Serviços</span>
            </div>
          </div>

          <!-- Card 6: Funis de Retenção & LTV -->
          <div onclick="abrirModalPixCurso('Funis de Retenção & LTV')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-teal-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Funis de Retencao LTV WhatsApp E-mail Pos-Venda Recorrencia Esteira de Produtos Growth">
            <div>
              {photo_card("funis_retencao_ltv.webp", "LTV & RETENÇÃO", "Funis de Retenção & LTV", "Growth Hackers", "text-teal-400 bg-teal-500/20 border-teal-500/30")}
              <h4 class="font-bold text-sm text-white group-hover:text-teal-400 transition-colors line-clamp-1">Funis de Retenção & LTV</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Estratégias para fidelizar clientes, criar esteiras de produtos irresistíveis e vender na mesma base.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-teal-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-teal-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Back-End Lucrativo</span>
            </div>
          </div>
        </div>
      </div>
"""

# Extrai os blocos existentes do backup com os cursos intactos
def get_clean_block(cat_name):
    tag = bak_soup.find('div', attrs={'data-cat': cat_name})
    if tag:
        return str(tag)
    return ""

bloco_ia = get_clean_block('ia')
bloco_trafego = get_clean_block('trafego')
bloco_ecommerce = get_clean_block('ecommerce')
bloco_dev = get_clean_block('dev')
bloco_criadores = get_clean_block('criadores')
bloco_beleza = get_clean_block('beleza')
bloco_educacao = get_clean_block('educacao')

# -------------------------------------------------------------
# 2. CATÁLOGO COMPLETO COM 73 CURSOS
# -------------------------------------------------------------
catalogo_html = f"""
    <!-- CATÁLOGO GERAL DE CONTEÚDOS -->
    <section class="space-y-8 relative z-10" id="catalogo">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-white/10 pb-6">
        <div>
          <span class="px-3 py-1 rounded-full text-[11px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 mb-2 inline-block">
            ⚡ 68 TÓPICOS ORGANIZADOS
          </span>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">Catálogo de Conteúdos Liberados</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Navegue pelas capas ou digite o nome do curso para filtrar na hora</p>
        </div>

        <!-- Barra de Busca Instantânea -->
        <div class="w-full md:w-80 relative">
          <input type="text" id="input-busca" oninput="filtrarCursos()" placeholder="🔍 Digite o curso, autor ou ferramenta..." class="w-full py-3 pl-4 pr-10 rounded-xl bg-white/5 border border-white/15 focus:border-emerald-500 focus:bg-white/10 text-white text-xs placeholder:text-zinc-500 focus:outline-none transition-all shadow-inner">
          <span id="contador-busca" class="absolute right-3 top-3 text-[11px] text-zinc-500 font-bold">73</span>
        </div>
      </div>

      <!-- Filtros Rápidos por Categoria (Sem barras invertidas) -->
      <div class="flex items-center gap-2 overflow-x-auto pb-2 text-xs scrollbar-none">
        <button onclick="filtrarCategoria('todas', this)" class="btn-categoria active px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-emerald-500 text-black border-emerald-400">
          🔥 Todos (73)
        </button>
        <button onclick="filtrarCategoria('seo', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-emerald-500/50 hover:text-white">
          🔍 SEO & Retenção (6)
        </button>
        <button onclick="filtrarCategoria('ia', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-purple-500/50 hover:text-white">
          🤖 IA & Automação (10)
        </button>
        <button onclick="filtrarCategoria('trafego', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-rose-500/50 hover:text-white">
          📈 Tráfego & Vendas (15)
        </button>
        <button onclick="filtrarCategoria('ecommerce', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-amber-500/50 hover:text-white">
          🛒 E-commerce & Milhas (10)
        </button>
        <button onclick="filtrarCategoria('dev', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-cyan-500/50 hover:text-white">
          💻 Dev, Gestão & Design (10)
        </button>
        <button onclick="filtrarCategoria('criadores', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-teal-500/50 hover:text-white">
          🎬 Criadores & YouTube (11)
        </button>
        <button onclick="filtrarCategoria('beleza', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-pink-500/50 hover:text-white">
          💅 Beleza & Práticas (4)
        </button>
        <button onclick="filtrarCategoria('educacao', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-indigo-500/50 hover:text-white">
          👶 Educação & Pais (7)
        </button>
      </div>

      <!-- FILEIRAS DO CATÁLOGO -->
      {bloco_seo}
      {bloco_ia}
      {bloco_trafego}
      {bloco_ecommerce}
      {bloco_dev}
      {bloco_criadores}
      {bloco_beleza}
      {bloco_educacao}
    </section>
"""

# -------------------------------------------------------------
# 3. FERRAMENTAS CONSOLIDADAS (8 Super Packs)
# -------------------------------------------------------------
ferramentas_html = f"""
    <!-- SEÇÃO CONSOLIDADA: FERRAMENTAS, BOTS & SOFTWARES INCLUSOS -->
    <section class="mt-20 mb-20 relative z-10" id="ferramentas">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>⚡ ACERVO DE FERRAMENTAS VIP</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">Ferramentas, Bots & Softwares Inclusos</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Economize milhares de reais em assinaturas mensais. Tudo pronto para download e uso imediato.</p>
        </div>
        <span class="text-xs font-bold px-3 py-1.5 rounded-xl bg-white/5 border border-white/10 text-emerald-400 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          8 Super Packs Inclusos
        </span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div onclick="abrirModalPixCurso('Ferramenta: Typebot & Robôs de Atendimento')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Typebot Robos WhatsApp Telegram Automacao Fluxos Atendimento">
          <div>
            {photo_card("ferramenta_typebot_bots.webp", "BOTS & FLUXOS", "Typebot & Robôs Prontos", "Fluxos de Venda e SAC", "text-purple-400 bg-purple-500/20 border-purple-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Typebot & Robôs de Atendimento</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Modelos prontos de fluxos conversacionais para WhatsApp e Telegram validados para vendas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">JSONs Prontos</span>
            <span class="text-zinc-500">Download Direto</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Canva Pro & Pack de Artes')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Canva Pro Pack Artes Design Templates Editaveis Redes Sociais">
          <div>
            {photo_card("ferramenta_canva_pro.webp", "DESIGN VIP", "Canva Pro & Mega Pack", "Artes e Feeds Editáveis", "text-blue-400 bg-blue-500/20 border-blue-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Canva Pro & Super Pack de Artes</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Milhares de templates editáveis para feed, stories, criativos de anúncios e capas magnéticas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Editável em 1 Clique</span>
            <span class="text-zinc-500">10k+ Templates</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Banco de Vídeos Virais 4K')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Banco Videos Virais 4K Cortes Reels TikTok Shorts Lifestyle Carros Viagens">
          <div>
            {photo_card("ferramenta_videos_virais.webp", "VÍDEOS 4K", "Acervo de Vídeos Virais", "Banco de Imagens 4K Ultra", "text-red-400 bg-red-500/20 border-red-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Acervo de Vídeos Virais 4K</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Banco com mais de 10.000 takes em ultra resolução sem direitos autorais para Reels, Shorts e TikTok.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">10k+ Takes 4K</span>
            <span class="text-zinc-500">Sem Copyright</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Páginas de Vendas em Alta Conversão')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Paginas Vendas Alta Conversao Templates Elementor Webflow Landing Pages CRO">
          <div>
            {photo_card("ferramenta_paginas_vendas.webp", "HIGH CRO", "Páginas de Alta Conversão", "Templates Elementor & Webflow", "text-emerald-400 bg-emerald-500/20 border-emerald-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Páginas de Vendas em Alta Conversão</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Modelos de landing pages validadas para infoprodutos, dropshipping e serviços locais prontas para importar.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Elementor & Webflow</span>
            <span class="text-zinc-500">JSON & Import</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Super Pack de Prompts IA')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Super Pack Prompts IA ChatGPT Claude Midjourney Engenharia Prompt Agentes">
          <div>
            {photo_card("ferramenta_prompts_ia.webp", "ENGENHARIA PROMPT", "Super Pack de Prompts IA", "ChatGPT & Midjourney", "text-cyan-400 bg-cyan-500/20 border-cyan-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Super Pack de Prompts IA</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Comandos secretos para destravar copywriting, criação de imagens realistas e automação com LLMs.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Engenharia de Prompt</span>
            <span class="text-zinc-500">Pronto para Copiar</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Mega Pack PLRs Validados')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Mega Pack PLR Validados Ebooks Paginas Vendas Direitos Revenda Lucro 100%">
          <div>
            {photo_card("ferramenta_plrs_revenda.webp", "DIREITOS DE REVENDA", "Mega Pack PLRs Validados", "Páginas, VSLs e E-books", "text-amber-400 bg-amber-500/20 border-amber-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Mega Pack PLRs Validados</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">E-books diagramados, VSLs e criativos de nichos lucrativos prontos para você cadastrar e vender.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Direito de Revenda</span>
            <span class="text-zinc-500">100% do Lucro</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Planilhas de Gestão & Tráfego')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Planilhas Gestao Trafego Dashboards Metricas ROI ROAS Controle Financeiro">
          <div>
            {photo_card("ferramenta_planilhas_gestao.webp", "DASHBOARDS GESTÃO", "Planilhas de Gestão & Tráfego", "Controle Financeiro & ROI", "text-teal-400 bg-teal-500/20 border-teal-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Planilhas de Gestão & Tráfego</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Dashboards completos para cálculo de ROI, ROAS, precificação de produtos e acompanhamento de métricas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Excel & Google Sheets</span>
            <span class="text-zinc-500">Automático</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Ferramenta: Base de Leads B2B Segmentados')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Base Leads B2B Segmentados Prospeccao Empresas Clientes Ativos WhatsApp Email">
          <div>
            {photo_card("ferramenta_leads_prospeccao.webp", "LEADS SEGMENTADOS", "Base de Leads B2B Segmentados", "Listas para Cold Call & Zap", "text-indigo-400 bg-indigo-500/20 border-indigo-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Base de Leads B2B Segmentados</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Milhares de contatos empresariais com WhatsApp e e-mail filtrados por nicho para prospecção ativa.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Segmentação CNPJ</span>
            <span class="text-zinc-500">Pronto para Abordar</span>
          </div>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 4. CANAIS & COMUNIDADES VIP (8 Canais)
# -------------------------------------------------------------
canais_html = f"""
    <!-- BÔNUS: CANAIS & COMUNIDADES VIP NO TELEGRAM -->
    <section class="mt-20 mb-20 relative z-10" id="canais-vip">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>🎁 BÔNUS EXCLUSIVO</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">Canais & Comunidades VIP no Telegram</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Acesso direto e instantâneo aos canais privados do Telegram com atualizações diárias automáticas.</p>
        </div>
        <div class="flex items-center gap-2 text-xs text-emerald-400 font-bold bg-emerald-500/10 px-3 py-1.5 rounded-xl border border-emerald-500/20">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          8 Canais Ativos 24/7
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div onclick="abrirModalPixCurso('Canal VIP: Fábrica de Robôs')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Fabrica de Robos Automacao Bots WhatsApp Telegram">
          <div>
            {photo_card("canal_fabrica_de_robos.webp", "CANAL TELEGRAM", "Fábrica de Robôs", "@FabricaDeRobos_bot", "text-emerald-400 bg-emerald-500/20 border-emerald-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Fábrica de Robôs</h4>
            <p class="text-xs text-zinc-400 mt-1">Fluxos de automação, bots e webhooks atualizados toda semana.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-emerald-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Apk Premium')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Apk Premium Aplicativos Modificados Android Streaming">
          <div>
            {photo_card("canal_apk_premium.webp", "CANAL TELEGRAM", "Apk Premium", "@ApkPremium_bot", "text-cyan-400 bg-cyan-500/20 border-cyan-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-cyan-400 transition-colors">Apk Premium</h4>
            <p class="text-xs text-zinc-400 mt-1">Apps sem anúncios, utilitários Android e ferramentas premium.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-cyan-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Análise de Criptomoeda')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Analise de Criptomoeda Bitcoin Sinais Trading DeFi">
          <div>
            {photo_card("canal_analise_cripto.webp", "CANAL TELEGRAM", "Análise de Criptomoeda", "@AnaliseCripto_bot", "text-amber-400 bg-amber-500/20 border-amber-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors">Análise de Criptomoeda</h4>
            <p class="text-xs text-zinc-400 mt-1">Sinais, relatórios on-chain e alertas de oportunidades DeFi.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-amber-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: NutriTips & Saúde')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="NutriTips Saude Dieta Emagrecimento Nutricao Treino">
          <div>
            {photo_card("canal_nutritips_saude.webp", "CANAL TELEGRAM", "NutriTips & Saúde", "@NutriTips_bot", "text-green-400 bg-green-500/20 border-green-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-green-400 transition-colors">NutriTips & Saúde</h4>
            <p class="text-xs text-zinc-400 mt-1">Protocolos de nutrição, saúde preventiva e biohacking.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-green-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Notas Médicas & Saúde')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Notas Medicas Saude Resumos Medicina Clinica">
          <div>
            {photo_card("canal_notas_medicas.webp", "CANAL TELEGRAM", "Notas Médicas & Saúde", "@NotasMedicas_bot", "text-blue-400 bg-blue-500/20 border-blue-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors">Notas Médicas & Saúde</h4>
            <p class="text-xs text-zinc-400 mt-1">Resumos clínicos, farmacologia e condutas atualizadas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-blue-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Receitas & Cozinha Fácil')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Receitas Cozinha Facil Culinaria Pratica Airfryer">
          <div>
            {photo_card("canal_receitas_cozinha.webp", "CANAL TELEGRAM", "Receitas & Cozinha Fácil", "@ReceitasFaceis_bot", "text-orange-400 bg-orange-500/20 border-orange-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-orange-400 transition-colors">Receitas & Cozinha Fácil</h4>
            <p class="text-xs text-zinc-400 mt-1">Cardápios práticos, marmitas fitness e receitas rápidas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-orange-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Mente Vencedora')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Mente Vencedora Mentalidade Foco Disciplina Estoicismo">
          <div>
            {photo_card("canal_mente_vencedora.webp", "CANAL TELEGRAM", "Mente Vencedora", "@MenteVencedora_bot", "text-purple-400 bg-purple-500/20 border-purple-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-purple-400 transition-colors">Mente Vencedora</h4>
            <p class="text-xs text-zinc-400 mt-1">Pílulas diárias de disciplina, estoicismo e alta performance.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-purple-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Wallpapers 4K & HD')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Wallpapers 4K HD Fundos Tela Celular PC AMOLED">
          <div>
            {photo_card("canal_wallpapers_hd.webp", "CANAL TELEGRAM", "Wallpapers 4K & HD", "@WallpapersVIP_bot", "text-rose-400 bg-rose-500/20 border-rose-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-rose-400 transition-colors">Wallpapers 4K & HD</h4>
            <p class="text-xs text-zinc-400 mt-1">Fundos de tela para celular e desktop em resolução máxima.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-rose-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 5. GAMES & EMULADORES (10 Consoles)
# -------------------------------------------------------------
games_html = """
    <!-- BÔNUS: BIBLIOTECA DE GAMES & EMULADORES (Layout Vertical Corrigido) -->
    <section class="mt-20 mb-20 relative z-10" id="games">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>🎮 MEGA ACERVO GAMER & CONSOLES</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">Bibliotecas de Games & Emuladores</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Acesso aos robôs integrados com milhares de ROMs, ISOs e jogos de todas as gerações para download direto.</p>
        </div>
        <div class="flex items-center gap-2 text-xs font-bold px-3 py-1.5 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-300">
          <span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
          10 Plataformas Disponíveis
        </div>
      </div>

      <!-- Grid com 10 Consoles Empilhados Verticalmente sem Encavalar -->
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3 mb-6">
        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Nintendo Switch')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_nintendo_switch.webp" alt="Nintendo Switch Games" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-red-600 text-white">SWITCH</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">Nintendo Switch</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@nsw_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PlayStation 5')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_playstation_5.webp" alt="PS5 Games" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-blue-700 text-white">PS5</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">PlayStation 5</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@ps5_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PlayStation 4')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_playstation_4.webp" alt="PS4 Games" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-blue-600 text-white">PS4</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">PlayStation 4</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@ps4_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PlayStation 2')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_playstation_2.webp" alt="PS2 Clássicos" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-blue-900 text-white">PS2</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">PlayStation 2</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@ps2_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Xbox 360')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_xbox_360.webp" alt="Xbox 360 Games" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-green-600 text-white">X360</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">Xbox 360</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@x360_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PC Games & Steam')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_pc_games.webp" alt="PC Games & Steam" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-zinc-800 text-white">PC</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">PC Games & Steam</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@pcgames_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Realidade Virtual VR')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_vr_oculus.webp" alt="VR Oculus Quest" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-purple-700 text-white">VR</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">Realidade Virtual (VR)</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@vrgames_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PSP & PS Vita')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_psp_vita.webp" alt="PSP & PS Vita" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-cyan-700 text-white">PSP/VITA</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">PSP & PS Vita</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@psp_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Nintendo 3DS')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_nintendo_3ds.webp" alt="Nintendo 3DS" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-red-700 text-white">3DS</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">Nintendo 3DS</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@3ds_bot</div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Retrô & Emuladores')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_retro_emuladores.webp" alt="PS1 e Retrô Clássicos" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-amber-600 text-white">RETRÔ</span>
          </div>
          <div class="font-bold text-xs text-white group-hover:text-emerald-400 transition-colors">PS1 & Retrô Clássicos</div>
          <div class="text-[10px] text-zinc-500 mt-0.5">@retro_bot</div>
        </a>
      </div>

      <div class="glass-card p-4 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4 border border-white/10 text-center sm:text-left">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-blue-500/10 border border-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-lg shrink-0">
            💾
          </div>
          <div>
            <div class="text-sm font-bold text-white">Mais de 15.000 jogos organizados por console</div>
            <div class="text-xs text-zinc-400">Download direto de ISOs e ROMs em alta velocidade pelo Telegram</div>
          </div>
        </div>
        <button onclick="abrirModalPixCurso('Biblioteca Gamer Completa')" class="w-full sm:w-auto px-5 py-2.5 rounded-xl font-bold text-xs bg-blue-500 hover:bg-blue-400 text-white transition-all shadow-lg shadow-blue-500/20 whitespace-nowrap">
          Liberar Todos os Consoles
        </button>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 6. LIVROS RAROS, TEOLOGIA, GOLS & SOFTWARES (8 Canais Extras)
# -------------------------------------------------------------
livros_html = f"""
    <!-- BÔNUS: LIVROS RAROS, TEOLOGIA, GOLS E SOFTWARES -->
    <section class="mt-20 mb-20 relative z-10" id="livros">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>📚 BIBLIOTECAS & UTILITÁRIOS</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">Livros Raros, Teologia, Gols e Softwares</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Canais complementares inclusos no pacote sem nenhum custo adicional.</p>
        </div>
        <div class="flex items-center gap-2 text-xs text-amber-400 font-bold bg-amber-500/10 px-3 py-1.5 rounded-xl border border-amber-500/20">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
          8 Canais Especiais
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div onclick="abrirModalPixCurso('Canal VIP: Teologia & Livros Gospel')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Teologia Livros Gospel Biblia Comentarios Estudos">
          <div>
            {photo_card("canal_teologia_gospel.webp", "CANAL TELEGRAM", "Teologia & Livros Gospel", "@TeologiaGospel_bot", "text-amber-400 bg-amber-500/20 border-amber-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors">Teologia & Livros Gospel</h4>
            <p class="text-xs text-zinc-400 mt-1">Acervo completo de Bíblias de estudo, comentários e sermões.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-amber-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Livros de Medicina & Saúde')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Livros Medicina Saude Manuais Tratados Resumos">
          <div>
            {photo_card("canal_livros_medicina.webp", "CANAL TELEGRAM", "Livros de Medicina & Saúde", "@LivrosMedicina_bot", "text-blue-400 bg-blue-500/20 border-blue-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors">Livros de Medicina & Saúde</h4>
            <p class="text-xs text-zinc-400 mt-1">Tratados, manuais de bolso e condutas clínicas em PDF.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-blue-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Áudio Livros & Best-Sellers')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Audio Livros Best-Sellers Negocios Mindset Desenvolvimento">
          <div>
            {photo_card("canal_audio_livros.webp", "CANAL TELEGRAM", "Áudio Livros & Best-Sellers", "@AudioLivros_bot", "text-teal-400 bg-teal-500/20 border-teal-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-teal-400 transition-colors">Áudio Livros & Best-Sellers</h4>
            <p class="text-xs text-zinc-400 mt-1">Centenas de audiobooks narrados em alta qualidade de áudio.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-teal-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Gols ao Vivo & Futebol')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Gols ao Vivo Futebol Lances Melhores Momentos">
          <div>
            {photo_card("canal_gols_ao_vivo.webp", "CANAL TELEGRAM", "Gols ao Vivo & Futebol", "@GolsFutebol_bot", "text-emerald-400 bg-emerald-500/20 border-emerald-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Gols ao Vivo & Futebol</h4>
            <p class="text-xs text-zinc-400 mt-1">Vídeos em tempo real de lances e gols das principais ligas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-emerald-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Cale-se e Leve Meu Dinheiro')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Cale-se e Leve Meu Dinheiro Achadinhos Promocoes Shopee AliExpress">
          <div>
            {photo_card("canal_achadinhos_promocoes.webp", "CANAL TELEGRAM", "Cale-se e Leve Meu Dinheiro", "@AchadinhosVIP_bot", "text-yellow-400 bg-yellow-500/20 border-yellow-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-yellow-400 transition-colors">Cale-se e Leve Meu Dinheiro</h4>
            <p class="text-xs text-zinc-400 mt-1">Ofertas bugadas, cupons secretos e produtos virais da internet.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-yellow-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Figurinhas & Tatuagens')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Figurinhas Tatuagens Flash Tattoos Memes WhatsApp">
          <div>
            {photo_card("canal_figurinhas_design.webp", "CANAL TELEGRAM", "Figurinhas & Tatuagens", "@FigurinhasVIP_bot", "text-pink-400 bg-pink-500/20 border-pink-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-pink-400 transition-colors">Figurinhas & Tatuagens</h4>
            <p class="text-xs text-zinc-400 mt-1">Packs de figurinhas para WhatsApp e referências de flash tattoo.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-pink-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Softwares & Utilitários 2026')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Softwares Utilitarios 2026 Programas PC Windows Portateis">
          <div>
            {photo_card("canal_softwares_2026.webp", "CANAL TELEGRAM", "Softwares & Utilitários 2026", "@SoftwaresVIP_bot", "text-cyan-400 bg-cyan-500/20 border-cyan-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-cyan-400 transition-colors">Softwares & Utilitários 2026</h4>
            <p class="text-xs text-zinc-400 mt-1">Programas portáteis essenciais, antivírus e otimizadores de sistema.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-cyan-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: História em Preto e Branco')" class="curso-card glass-card p-4 rounded-2xl border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 group cursor-pointer flex flex-col justify-between" data-titulo="Historia em Preto e Branco Fatos Raros Guerras Arquivos">
          <div>
            {photo_card("canal_historia_bw.webp", "CANAL TELEGRAM", "História em Preto e Branco", "@HistoriaVIP_bot", "text-slate-400 bg-slate-500/20 border-slate-500/30")}
            <h4 class="font-bold text-sm text-white group-hover:text-slate-400 transition-colors">História em Preto e Branco</h4>
            <p class="text-xs text-zinc-400 mt-1">Registros fotográficos históricos raros, conflitos e biografias.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-xs text-zinc-500">
            <span class="text-slate-400 font-bold">@bot liberado</span>
            <span>Acesso Imediato</span>
          </div>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 7. SEÇÃO 68 TÓPICOS NO TELEGRAM (8 Grupos Temáticos)
# -------------------------------------------------------------
topicos_html = f"""
    <!-- 68 TÓPICOS NO TELEGRAM -->
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
    </section>
"""

# Montagem final garantindo a ordem CRO
full_page = f"""{rf.head_html}
{rf.hero_html}
{catalogo_html}
{ferramentas_html}
{canais_html}
{games_html}
{livros_html}
{topicos_html}
{rf.receber_html}
{rf.faq_html}
{rf.footer_html}
{rf.modais_html}
{rf.scripts_unificados_html}
"""

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(full_page)

print("build_production_acervo.py: index.html gerado com sucesso!")
