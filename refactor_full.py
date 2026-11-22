#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Refatoração Completa do index.html para ACERVO DIGITAL VIP
Garante 100% de conformidade com todos os 4 requisitos da solicitação do usuário.
"""

import re
import os

print("Iniciando refatoração completa do index.html...")

def banner_card(badge, title, author, bg_gradient, icon_html, tag_bottom="Liberado no VIP", tag_sub="Imersão VIP"):
    return f"""<div class="relative w-full aspect-video rounded-xl overflow-hidden mb-3 bg-gradient-to-tr {bg_gradient} p-3 flex flex-col justify-between border border-white/10 shadow-inner group-hover:scale-105 transition-transform duration-500">
      <div class="flex items-center justify-between z-10">
        <span class="text-[9px] font-black uppercase px-2 py-0.5 rounded-full bg-black/60 text-white backdrop-blur-md border border-white/10 tracking-wider">{badge}</span>
        <span class="text-[9px] text-emerald-400 font-bold bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/20">VIP</span>
      </div>
      <div class="flex items-center justify-center my-auto z-10 text-3xl filter drop-shadow">
        {icon_html}
      </div>
      <div class="z-10">
        <div class="text-[11px] font-bold text-white drop-shadow truncate">{title}</div>
        <div class="text-[10px] text-zinc-400 font-medium truncate">{author}</div>
      </div>
      <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent pointer-events-none"></div>
    </div>"""

# -------------------------------------------------------------
# 1. HEAD & HEADER (SEO, OG, Twitter, Canonical, Schema Duplo)
# -------------------------------------------------------------
head_html = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ACERVO DIGITAL VIP - Cursos, Ferramentas & Drives Telegram</title>
  <meta name="description" content="Acesse mais de 68 tópicos organizados no Telegram com cursos completos de IA, Tráfego Pago, E-commerce, Dev, Beleza, Concursos e Games por apenas R$ 9,90.">
  <link rel="canonical" href="https://acervo-digital-vip.vercel.app/">
  
  <meta name="color-scheme" content="dark">
  <meta name="darkreader-lock">
  
  <!-- Open Graph / WhatsApp / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://acervo-digital-vip.vercel.app/">
  <meta property="og:title" content="ACERVO DIGITAL VIP - Todos os Cursos e Ferramentas em um Só Lugar">
  <meta property="og:description" content="Acesso vitalício a mais de 68 tópicos no Telegram: IA, Tráfego, Dev, Automações e Games. Pague taxa única de R$ 9,90 via Pix.">
  <meta property="og:image" content="https://acervo-digital-vip.vercel.app/assets/acervo_vip_hero_mockup.webp">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Acervo Digital VIP">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://acervo-digital-vip.vercel.app/">
  <meta name="twitter:title" content="ACERVO DIGITAL VIP - Todos os Cursos e Ferramentas em um Só Lugar">
  <meta name="twitter:description" content="Acesso vitalício a mais de 68 tópicos no Telegram por taxa única de R$ 9,90 via Pix.">
  <meta name="twitter:image" content="https://acervo-digital-vip.vercel.app/assets/acervo_vip_hero_mockup.webp">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              dark: '#06070a',
              card: '#0c0e14',
              border: '#1a1f2c'
            }
          }
        }
      }
    }
  </script>

  <!-- Schema.org JSON-LD: Product -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "ACERVO DIGITAL VIP - Acesso Vitalício",
    "description": "Repositório completo com 68 tópicos de cursos, drives, automações e ferramentas digitais no Telegram com liberação inteligente em 2 fases.",
    "brand": {
      "@type": "Brand",
      "name": "ACERVO DIGITAL VIP"
    },
    "image": "https://acervo-digital-vip.vercel.app/assets/acervo_vip_hero_mockup.webp",
    "offers": {
      "@type": "Offer",
      "url": "https://acervo-digital-vip.vercel.app/",
      "price": "9.90",
      "priceCurrency": "BRL",
      "priceValidUntil": "2027-12-31",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "384",
      "bestRating": "5",
      "worstRating": "1"
    }
  }
  </script>

  <!-- Schema.org JSON-LD: FAQPage -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "O acesso é realmente vitalício por apenas R$ 9,90?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sim! Você paga uma única taxa simbólica de R$ 9,90 e tem acesso para sempre. Não existem mensalidades nem taxas ocultas adicionais."
        }
      },
      {
        "@type": "Question",
        "name": "Como são entregues os cursos e arquivos?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Todo o acervo está organizado em tópicos separados no Telegram (vídeos, PDFs, modelos de código, planilhas e drives na nuvem). Ao confirmar seu Pix de R$ 9,90, nosso bot oficial envia seu link de acesso imediato."
        }
      },
      {
        "@type": "Question",
        "name": "Novos cursos e ferramentas são adicionados?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sim! O acervo recebe atualizações semanais com novos lançamentos do mercado digital, automações e materiais solicitados pelos próprios membros sem cobrar nada a mais por isso."
        }
      },
      {
        "@type": "Question",
        "name": "E se eu não souber usar o Telegram?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "O Telegram é um aplicativo gratuito que funciona no celular e no computador. Temos um tutorial em vídeo de 2 minutos explicando passo a passo como navegar pelas pastas e baixar qualquer aula."
        }
      },
      {
        "@type": "Question",
        "name": "Como funciona o suporte caso eu tenha dúvidas?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Temos atendimento direto no Telegram pelo bot oficial (@AcervoDigitalVIP_bot) pronto para ajudar na liberação do seu acesso e tirar qualquer dúvida rapidamente."
        }
      },
      {
        "@type": "Question",
        "name": "Como funciona a liberação em 2 fases (Dia 1 e 8º Dia)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No Dia 1 (imediato após o Pix de R$ 9,90), você recebe acesso à Comunidade VIP no Telegram, Microcursos principais, ferramentas de IA e packs essenciais para começar a produzir no mesmo minuto. No 8º dia (após o término do período de garantia legal de 7 dias do CDC), nosso sistema libera o download massivo e irrestrito de todos os 68 tópicos, acervos pesados de 4K e bibliotecas inteiras de emuladores."
        }
      }
    ]
  }
  </script>

  <style>
    body {
      background-color: #06070a;
      color: #e4e4e7;
    }
    .glass-panel {
      background: rgba(12, 14, 20, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }
    .glass-card {
      background: rgba(18, 21, 30, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.07);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    .glass-card:hover {
      border-color: rgba(16, 185, 129, 0.4);
      transform: translateY(-4px);
    }
    .carrossel-scroll::-webkit-scrollbar {
      height: 6px;
    }
    .carrossel-scroll::-webkit-scrollbar-track {
      background: rgba(255, 255, 255, 0.02);
      border-radius: 9999px;
    }
    .carrossel-scroll::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 9999px;
    }
    .carrossel-scroll::-webkit-scrollbar-thumb:hover {
      background: rgba(16, 185, 129, 0.4);
    }
    @keyframes marquee {
      0% { transform: translateX(0%); }
      100% { transform: translateX(-50%); }
    }
    .animate-marquee {
      display: inline-flex;
      white-space: nowrap;
      animation: marquee 25s linear infinite;
      will-change: transform;
    }
    .animate-marquee:hover {
      animation-play-state: paused;
    }
  </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between selection:bg-emerald-500 selection:text-black overflow-x-hidden">
  
  <!-- TICKER DE LANÇAMENTOS RECENTES AO VIVO -->
  <div class="bg-black/90 border-b border-white/10 py-2.5 overflow-hidden relative z-40 shadow-inner">
    <div class="max-w-7xl mx-auto px-4 flex items-center gap-3">
      <div class="flex items-center gap-1.5 shrink-0 px-2.5 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-[11px] font-black uppercase tracking-wider">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span> NOVO NO VIP
      </div>
      <div class="overflow-hidden whitespace-nowrap w-full relative">
        <div class="animate-marquee text-xs text-zinc-300 font-medium">
          <span class="mx-3 text-white font-bold">🔍 SEO Sem Segredos (Bruno Medeiros)</span> • 
          <span class="mx-3 text-white font-bold">📈 Google Discover & Tráfego Orgânico</span> • 
          <span class="mx-3 text-white font-bold">💅 Manicure Pro (Faby Cardoso)</span> • 
          <span class="mx-3 text-white font-bold">👁️ Viver de Cílios (Larissa Costa)</span> • 
          <span class="mx-3 text-white font-bold">📊 Hashtag Excel & Python Impressionador</span> • 
          <span class="mx-3 text-white font-bold">🎓 Estratégia Concursos & Mairo Vergara</span> • 
          <span class="mx-3 text-white font-bold">✨ Comunidade Invictus (Adriano Gianini)</span> • 
          <span class="mx-3 text-white font-bold">🚀 Produtor Digital (Alex Vargas)</span> • 
          <span class="mx-3 text-white font-bold">📈 Método Newton (Vinicius Greco)</span> • 
          <span class="mx-3 text-white font-bold">💬 Mentoria X1 no WhatsApp (Rennan Rebouças)</span> • 
          <span class="mx-3 text-white font-bold">🎯 Anúncios Queridinhos da Meta (Marconi Rômulo)</span> • 
          <span class="mx-3 text-white font-bold">🏆 Comunidade Sobral de Tráfego (Pedro Sobral)</span> • 
          <!-- Duplicação para loop contínuo sem espaços vazios -->
          <span class="mx-3 text-white font-bold">🔍 SEO Sem Segredos (Bruno Medeiros)</span> • 
          <span class="mx-3 text-white font-bold">📈 Google Discover & Tráfego Orgânico</span> • 
          <span class="mx-3 text-white font-bold">💅 Manicure Pro (Faby Cardoso)</span> • 
          <span class="mx-3 text-white font-bold">👁️ Viver de Cílios (Larissa Costa)</span> • 
          <span class="mx-3 text-white font-bold">📊 Hashtag Excel & Python Impressionador</span> • 
          <span class="mx-3 text-white font-bold">🎓 Estratégia Concursos & Mairo Vergara</span> • 
          <span class="mx-3 text-white font-bold">✨ Comunidade Invictus (Adriano Gianini)</span> • 
          <span class="mx-3 text-white font-bold">🚀 Produtor Digital (Alex Vargas)</span> • 
          <span class="mx-3 text-white font-bold">📈 Método Newton (Vinicius Greco)</span> • 
          <span class="mx-3 text-white font-bold">💬 Mentoria X1 no WhatsApp (Rennan Rebouças)</span> • 
          <span class="mx-3 text-white font-bold">🎯 Anúncios Queridinhos da Meta (Marconi Rômulo)</span> • 
          <span class="mx-3 text-white font-bold">🏆 Comunidade Sobral de Tráfego (Pedro Sobral)</span> • 
        </div>
      </div>
    </div>
  </div>

  <!-- HEADER -->
  <header class="relative z-20 border-b border-white/10 glass-panel sticky top-0 px-4 sm:px-8 py-3.5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center font-black text-black text-xl shadow-lg shadow-emerald-500/20">
        ⚡
      </div>
      <div>
        <div class="text-sm sm:text-base font-extrabold tracking-tight text-white flex items-center gap-1.5">
          ACERVO DIGITAL <span class="text-emerald-400">VIP</span>
        </div>
        <div class="text-[10px] text-zinc-400 font-medium">Repositório & Comunidade Privada no Telegram</div>
      </div>
    </div>

    <!-- Navegação e CTA Superior -->
    <div class="flex items-center gap-3">
      <div class="hidden sm:flex items-center gap-2 text-xs font-semibold px-3 py-1.5 rounded-xl bg-white/5 border border-white/10 text-emerald-400">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        68 Tópicos Ativos
      </div>
      <button onclick="abrirModalPix()" data-track="cta_header_comprar" class="px-4 py-2 sm:px-5 sm:py-2.5 rounded-xl font-black text-xs uppercase tracking-wider bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-black shadow-lg shadow-emerald-500/20 hover:scale-105 active:scale-95 transition-all">
        Acessar por R$ 9,90
      </button>
    </div>
  </header>

  <!-- Canvas Shader Leve 2D -->
  <canvas id="aurora-bg" class="fixed inset-0 pointer-events-none z-0 opacity-40"></canvas>

  <main class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-20">
"""

print("Processando Hero e Benefícios...")

# -------------------------------------------------------------
# 2. HERO (H1 único, Preço R$ 9,90, Mockup 3D, Video hidden md:block)
# -------------------------------------------------------------
hero_html = """
    <!-- HERO SECTION -->
    <section class="glass-panel rounded-3xl p-6 sm:p-10 mb-16 border border-white/10 relative overflow-hidden shadow-2xl">
      <!-- Vídeo de fundo leve (oculto no mobile para poupar bateria e dados) -->
      <video autoplay muted loop playsinline webkit-playsinline class="hidden md:block absolute inset-0 w-full h-full object-cover opacity-15 pointer-events-none" preload="metadata">
        <source src="/assets/videos/hero_background.mp4" type="video/mp4">
      </video>
      <div class="absolute inset-0 bg-gradient-to-r from-[#06070a]/95 via-[#06070a]/85 to-transparent pointer-events-none"></div>

      <div class="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <!-- Coluna Esquerda: Texto e Oferta -->
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            Acesso Vitalício & Imediato no Telegram
          </div>

          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-[1.1]">
            Todos os Cursos, Ferramentas e Drives que Você Precisa em um <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-300">Só Lugar.</span>
          </h1>

          <p class="text-sm sm:text-base text-zinc-300 max-w-xl leading-relaxed">
            Esqueça mensalidades caras e links quebrados. Receba acesso vitalício ao nosso ecossistema organizado em <strong>68 tópicos no Telegram</strong> com mais de 2.000 treinamentos, ferramentas de IA, robôs prontos, automações e drives massivos.
          </p>

          <!-- Preço de Oferta e CTAs -->
          <div class="p-5 rounded-2xl bg-black/60 border border-emerald-500/30 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
              <div class="flex items-center gap-2">
                <span class="text-xs text-zinc-500 line-through">De R$ 19,90</span>
                <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Taxa Única Simbólica</span>
              </div>
              <div class="text-3xl sm:text-4xl font-black text-emerald-400 font-mono mt-0.5">
                R$ 9,90
              </div>
              <span class="text-[11px] text-zinc-400">Pague uma vez • Sem mensalidade • Acesso vitalício</span>
            </div>

            <div class="flex flex-col sm:flex-row gap-2.5 w-full sm:w-auto">
              <button onclick="abrirModalPix()" data-track="cta_hero_comprar" class="w-full sm:w-auto px-6 py-3.5 rounded-xl font-black text-xs uppercase tracking-wider bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-black shadow-lg shadow-emerald-500/25 hover:scale-105 active:scale-95 transition-all text-center">
                Destravar Acesso Agora ➜
              </button>
              <a href="#catalogo" data-track="cta_hero_catalogo" class="w-full sm:w-auto px-4 py-3.5 rounded-xl font-bold text-xs uppercase tracking-wider bg-white/5 hover:bg-white/10 text-zinc-300 hover:text-white border border-white/10 text-center transition-all">
                Ver Catálogo
              </a>
            </div>
          </div>

          <!-- Micro-provas de Credibilidade -->
          <div class="flex items-center gap-6 pt-1 text-xs text-zinc-400">
            <div class="flex items-center gap-1.5">
              <span class="text-emerald-400">✓</span> Liberação Imediata
            </div>
            <div class="flex items-center gap-1.5">
              <span class="text-emerald-400">✓</span> Garantia Blindada 7 Dias
            </div>
            <div class="flex items-center gap-1.5">
              <span class="text-emerald-400">✓</span> Atualizações Semanais
            </div>
          </div>
        </div>

        <!-- Coluna Direita: Mockup 3D Realista -->
        <div class="lg:col-span-5 relative flex justify-center">
          <div class="relative w-full max-w-md aspect-square rounded-3xl overflow-hidden border border-emerald-500/30 shadow-2xl shadow-emerald-950/40 bg-black/60 p-2">
            <img src="/assets/acervo_vip_hero_mockup.webp" alt="Acervo Digital VIP Mockup 3D" onerror="this.src='/assets/ia_geradas/acervo_vip_hero_mockup.webp'" loading="eager" decoding="async" class="w-full h-full object-cover rounded-2xl hover:scale-105 transition-transform duration-700">
            <div class="absolute bottom-4 inset-x-4 p-3 rounded-xl bg-black/80 backdrop-blur-md border border-white/10 flex items-center justify-between">
              <div>
                <div class="text-[10px] text-zinc-400 uppercase font-semibold">Ecossistema Completo</div>
                <div class="text-xs font-bold text-white">Mais de 68 Tópicos no Telegram</div>
              </div>
              <span class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold text-[10px] border border-emerald-500/30">
                100% ONLINE
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3 BENEFÍCIOS ACIMA DA DOBRA -->
    <section class="mb-16 mt-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="glass-panel p-6 rounded-2xl border border-white/5 hover:border-emerald-500/30 transition-all flex items-start gap-4">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 flex items-center justify-center font-black text-xl shrink-0">
            ⚡
          </div>
          <div>
            <h3 class="font-bold text-white text-base">Microcursos Diretos ao Ponto</h3>
            <p class="text-xs text-zinc-400 mt-1 leading-relaxed">Aulas práticas sem enrolação. Aprenda automações, IA, tráfego e vendas no seu próprio ritmo.</p>
          </div>
        </div>

        <div class="glass-panel p-6 rounded-2xl border border-white/5 hover:border-cyan-500/30 transition-all flex items-start gap-4">
          <div class="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 flex items-center justify-center font-black text-xl shrink-0">
            👥
          </div>
          <div>
            <h3 class="font-bold text-white text-base">Comunidade VIP no Telegram</h3>
            <p class="text-xs text-zinc-400 mt-1 leading-relaxed">Ambiente exclusivo de networking, troca de experiências, ferramentas e materiais complementares diários.</p>
          </div>
        </div>

        <div class="glass-panel p-6 rounded-2xl border border-white/5 hover:border-purple-500/30 transition-all flex items-start gap-4">
          <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/30 text-purple-400 flex items-center justify-center font-black text-xl shrink-0">
            🎁
          </div>
          <div>
            <h3 class="font-bold text-white text-base">Super Combos Prontos</h3>
            <p class="text-xs text-zinc-400 mt-1 leading-relaxed">Packs de prompts, modelos de funis, scripts de Typebot e robôs de atendimento inclusos na mesma taxa.</p>
          </div>
        </div>
      </div>
    </section>
"""

# Ler o index.html atual para extrair os blocos originais de IA, Tráfego, E-commerce, Dev
with open("/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html", "r", encoding="utf-8") as f:
    current_html = f.read()

# Extrair blocos existentes
def extract_block(cat_name):
    pattern = r'(<div class="categoria-bloco" data-cat="' + cat_name + r'">[\s\S]*?)(?=(?:<!-- FILEIRA|<div class="categoria-bloco"|</section>))'
    m = re.search(pattern, current_html)
    if m:
        b = m.group(1).strip()
        # Garantir fechamento de tags div
        open_divs = b.count("<div")
        close_divs = b.count("</div")
        if open_divs > close_divs:
            b += "</div>" * (open_divs - close_divs)
        return b
    return ""

bloco_ia = extract_block("ia")
bloco_trafego = extract_block("trafego")
bloco_ecommerce = extract_block("ecommerce")
bloco_dev = extract_block("dev")

# No bloco dev, substituir o card Figma por um banner SVG visual rico
banner_figma = banner_card("UI/UX DESIGN", "Figma UI/UX Design Pro", "Design System & Interfaces", "from-purple-950 via-violet-900 to-indigo-950", "🎨", "Interfaces Pro", "Design System")
bloco_dev = re.sub(
    r'<div class="relative w-full aspect-video rounded-xl overflow-hidden border border-cyan-500/40 mb-3 bg-black">[\s\S]*?Figma-UI-UX-Design-Pro\.webp[\s\S]*?</div>\s*</div>',
    banner_figma,
    bloco_dev
)

# No bloco dev, substituir Hacking Ético por banner SVG rico
banner_hacking = banner_card("CYBER SECURITY", "Hacking Ético & Pentest", "Kali Linux & Red Team", "from-emerald-950 via-zinc-900 to-cyan-950", "🛡️", "Segurança Defensiva", "Pentest do Zero")
bloco_dev = re.sub(
    r'<div class="relative w-full aspect-video rounded-xl overflow-hidden border border-cyan-500/40 mb-3 bg-black">[\s\S]*?Hacking-Etico[\s\S]*?</div>\s*</div>',
    banner_hacking,
    bloco_dev
)

# Bloco criadores: extrair e garantir fechamento
bloco_criadores = extract_block("criadores")
# Substituir O Novo Mercado e Do Mil ao Milhão por banners ricos
banner_novo_mercado = banner_card("CLÁSSICO ABSOLUTO", "O Novo Mercado", "Ícaro de Carvalho", "from-amber-950 via-zinc-900 to-yellow-950", "🏛️", "Coleção Completa", "Copy & Vendas")
bloco_criadores = re.sub(
    r'<div class="relative w-full aspect-video rounded-xl overflow-hidden border border-teal-500/40 mb-3 bg-black">[\s\S]*?O-Novo-Mercado[\s\S]*?</div>\s*</div>',
    banner_novo_mercado,
    bloco_criadores
)
banner_mil_milhao = banner_card("FINANÇAS PESSOAIS", "Do Mil ao Milhão", "Thiago Nigro (Primo Rico)", "from-emerald-950 via-zinc-900 to-teal-950", "📈", "Investimentos", "Renda & Ações")
bloco_criadores = re.sub(
    r'<div class="relative w-full aspect-video rounded-xl overflow-hidden border border-teal-500/40 mb-3 bg-black">[\s\S]*?Do-Mil-ao-Milhao[\s\S]*?</div>\s*</div>',
    banner_mil_milhao,
    bloco_criadores
)

# -------------------------------------------------------------
# 3. NOVA FILEIRA NO CATÁLOGO: SEO, TRÁFEGO ORGÂNICO & RETENÇÃO
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
          <!-- Card 1: SEO Sem Segredos (Bruno Medeiros) -->
          <div onclick="abrirModalPixCurso('SEO Sem Segredos (Bruno Medeiros)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="SEO Sem Segredos Bruno Medeiros Ranqueamento Topo Google Blogs Lucrativos Backlinks Trafego Organico">
            <div>
              {banner_card("TOPO DO GOOGLE", "SEO Sem Segredos", "Bruno Medeiros", "from-emerald-950 via-zinc-900 to-teal-900", "🔍")}
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
              {banner_card("SEARCH & DISCOVER", "SEO Master & Discover", "Especialistas de Search", "from-cyan-950 via-zinc-900 to-blue-900", "⚡")}
              <h4 class="font-bold text-sm text-white group-hover:text-cyan-400 transition-colors line-clamp-1">Formação SEO Master & Discover</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Tráfego orgânico massivo para sites e e-commerces explorando o algoritmo do Google Discover sem gastar em anúncios.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-cyan-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Escala de Visitas</span>
            </div>
          </div>

          <!-- Card 3: YouTube SEO & Retenção Extrema -->
          <div onclick="abrirModalPixCurso('YouTube SEO & Retenção Extrema')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-rose-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="YouTube SEO Retencao Extrema Algoritmo CTR Titulos Magneticos Thumbnails Roteiros Virais">
            <div>
              {banner_card("ALGORITMO YOUTUBE", "YouTube SEO & Retenção", "Criadores Virais", "from-rose-950 via-zinc-900 to-red-900", "🎬")}
              <h4 class="font-bold text-sm text-white group-hover:text-rose-400 transition-colors line-clamp-1">YouTube SEO & Retenção Extrema</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Como dominar o algoritmo do YouTube: títulos magnéticos, thumbnails de alto CTR e ganchos de alta retenção.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-rose-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Vídeos & Retenção</span>
            </div>
          </div>

          <!-- Card 4: Copywriting & Retenção de Audiência (VSL e Páginas) -->
          <div onclick="abrirModalPixCurso('Copywriting & Retenção de Audiência')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-purple-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Copywriting Retencao de Audiencia VSL Paginas de Vendas Taxa de Conversao CRO Storytelling Persuasao">
            <div>
              {banner_card("RETENÇÃO & CRO", "Copywriting & Retenção", "Copy Masters", "from-purple-950 via-zinc-900 to-indigo-900", "✍️")}
              <h4 class="font-bold text-sm text-white group-hover:text-purple-400 transition-colors line-clamp-1">Copywriting & Retenção de Audiência</h4>
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
              {banner_card("RENDA RECORRENTE", "Google Meu Negócio Local", "Agências Locais", "from-amber-950 via-zinc-900 to-yellow-900", "📍")}
              <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors line-clamp-1">Google Meu Negócio & SEO Local</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Como cobrar mensalidades recorrentes de empresas locais colocando-as nas 3 primeiras posições do Google Maps.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-amber-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Prestação de Serviços</span>
            </div>
          </div>

          <!-- Card 6: Funis de Retenção & LTV (WhatsApp + E-mail) -->
          <div onclick="abrirModalPixCurso('Funis de Retenção & LTV')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-teal-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Funis de Retencao LTV WhatsApp E-mail Pos-Venda Recorrencia Esteira de Produtos Growth">
            <div>
              {banner_card("LTV & RETENÇÃO", "Funis de Retenção & LTV", "Growth Hackers", "from-teal-950 via-zinc-900 to-emerald-900", "🔄")}
              <h4 class="font-bold text-sm text-white group-hover:text-teal-400 transition-colors line-clamp-1">Funis de Retenção & LTV</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Estratégias para fidelizar clientes, criar esteiras de produtos irresistíveis e vender várias vezes para a mesma base.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-teal-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-teal-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Back-End Lucrativo</span>
            </div>
          </div>
        </div>
      </div>
"""

# -------------------------------------------------------------
# 4. BELEZA COM BANNERS SVG RICOS (Eliminando capas erradas)
# -------------------------------------------------------------
bloco_beleza = f"""
      <!-- FILEIRA: BELEZA, PROFISSÕES PRÁTICAS & CULINÁRIA (CAMPEÕES DE VOLUME HOTMART) -->
      <div class="categoria-bloco" data-cat="beleza">
        <div class="flex items-center justify-between mb-3.5">
          <div class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-pink-500/20 text-pink-400 flex items-center justify-center font-bold text-xs">💅</span>
            <h3 class="text-lg sm:text-xl font-bold text-white tracking-tight">Beleza, Profissões Práticas & Culinária Lucrativa</h3>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-pink-500/10 text-pink-300 border border-pink-500/30 uppercase">Mais Vendidos do Brasil</span>
          </div>
          <span class="text-xs text-zinc-500 hidden sm:inline">Tópicos #61 ao #65</span>
        </div>

        <div class="flex gap-4 overflow-x-auto carrossel-scroll snap-x snap-mandatory pb-3 pt-1">
          <!-- Card Faby Cardoso -->
          <div onclick="abrirModalPixCurso('Curso de Manicure e Pedicure (Faby Cardoso)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-pink-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Manicure Pedicure Faby Cardoso Cutilagem Esmaltacao Unhas Profissional">
            <div>
              {banner_card("TOP 1 HOTMART", "Manicure & Pedicure", "Faby Cardoso", "from-pink-950 via-zinc-900 to-rose-900", "💅")}
              <h4 class="font-bold text-sm text-white group-hover:text-pink-400 transition-colors line-clamp-1">Manicure & Pedicure Profissional</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Cutilagem russa, esmaltação perfeita e captação de clientes para faturar alto.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Do Zero ao Pro</span>
            </div>
          </div>

          <!-- Card Larissa Costa -->
          <div onclick="abrirModalPixCurso('Viver de Cílios (Larissa Costa)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-pink-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Viver de Cilios Larissa Costa Extensao Fio a Fio Lash Designer">
            <div>
              {banner_card("ALTA DEMANDA", "Viver de Cílios", "Larissa Costa", "from-purple-950 via-zinc-900 to-pink-900", "👁️")}
              <h4 class="font-bold text-sm text-white group-hover:text-pink-400 transition-colors line-clamp-1">Viver de Cílios (Lash Designer)</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Formação profissional em extensão de cílios, técnicas de volume russo e gestão de estúdio.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Profissão Estética</span>
            </div>
          </div>

          <!-- Card Andreia Venturini -->
          <div onclick="abrirModalPixCurso('Maquiagem na Web (Andreia Venturini)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-pink-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Maquiagem na Web Andreia Venturini Automaquiagem Make Profissional">
            <div>
              {banner_card("CLÁSSICO DA BELEZA", "Maquiagem na Web", "Andreia Venturini", "from-fuchsia-950 via-zinc-900 to-rose-900", "💄")}
              <h4 class="font-bold text-sm text-white group-hover:text-pink-400 transition-colors line-clamp-1">Maquiagem na Web 2.0</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Técnicas de esfumado, preparação de pele resistente, contornos e maquiagem para eventos.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Make Artística</span>
            </div>
          </div>

          <!-- Card Marrara Bortoloti -->
          <div onclick="abrirModalPixCurso('Confeitaria Lucrativa (Marrara Bortoloti)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-pink-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Confeitaria Lucrativa Marrara Bortoloti Bolos Caseiros Doces Gourmet Renda Extra">
            <div>
              {banner_card("RENDA RÁPIDA", "Confeitaria Lucrativa", "Marrara Bortoloti", "from-amber-950 via-zinc-900 to-orange-900", "🎂")}
              <h4 class="font-bold text-sm text-white group-hover:text-pink-400 transition-colors line-clamp-1">Confeitaria Lucrativa & Bolos</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Receitas profissionais de bolos caseiros, recheios econômicos e precificação para faturar em casa.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Gastronomia</span>
            </div>
          </div>
        </div>
      </div>
"""

# -------------------------------------------------------------
# 5. EDUCAÇÃO COM BANNERS SVG RICOS (Eliminando capas erradas)
# -------------------------------------------------------------
bloco_educacao = f"""
      <!-- FILEIRA: EDUCAÇÃO INFANTIL, ALFABETIZAÇÃO & PAIS (ALTO TICKET HOTMART/EDZZ) -->
      <div class="categoria-bloco" data-cat="educacao">
        <div class="flex items-center justify-between mb-3.5">
          <div class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-xs">🎓</span>
            <h3 class="text-lg sm:text-xl font-bold text-white tracking-tight">Idiomas, Concursos & Plataformas Gigantes</h3>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/10 text-blue-300 border border-blue-500/30 uppercase">Carreira & Alto Ticket</span>
          </div>
          <span class="text-xs text-zinc-500 hidden sm:inline">Tópicos #56 ao #60</span>
        </div>

        <div class="flex gap-4 overflow-x-auto carrossel-scroll snap-x snap-mandatory pb-3 pt-1">
          <!-- Card Mairo Vergara -->
          <div onclick="abrirModalPixCurso('Curso de Inglês Mairo Vergara')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-blue-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Mairo Vergara Curso de Ingles Fluencia Minerar Frases Anki">
            <div>
              {banner_card("INGLÊS #1", "Curso de Inglês", "Mairo Vergara", "from-blue-950 via-zinc-900 to-indigo-900", "🇬🇧")}
              <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors line-clamp-1">Curso de Inglês Mairo Vergara</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Método definitivo de mineração de sentenças com Anki para falar inglês fluente com autonomia.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Do Zero à Fluência</span>
            </div>
          </div>

          <!-- Card Estratégia Concursos -->
          <div onclick="abrirModalPixCurso('Estratégia Concursos (Preparatório Geral)')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-blue-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Estrategia Concursos Preparatorio Geral Carreiras Administrativas Fiscais Policiais">
            <div>
              {banner_card("CONCURSOS PÚBLICOS", "Estratégia Concursos", "Carreiras Públicas", "from-slate-900 via-blue-950 to-indigo-950", "⚖️")}
              <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors line-clamp-1">Estratégia Concursos (Geral)</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Apostilas em PDF completas, banco de questões comentadas e videoaulas de direito e português.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Aprovação Rápida</span>
            </div>
          </div>

          <!-- Card Hashtag Programação & Excel -->
          <div onclick="abrirModalPixCurso('Hashtag: Excel, Power BI & Python')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-blue-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Hashtag Treinamentos Excel Power BI Python Impressionador">
            <div>
              {banner_card("IMPRESSIONADOR", "Hashtag Treinamentos", "Excel, Power BI & Python", "from-emerald-950 via-zinc-900 to-teal-900", "📊")}
              <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors line-clamp-1">Hashtag: Excel, Power BI & Python</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Da planilha básica aos dashboards corporativos impressionadores e automações em Python.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Mercado de Trabalho</span>
            </div>
          </div>

          <!-- Card Bilinguismo Infantil & Montessori -->
          <div onclick="abrirModalPixCurso('Bilinguismo Infantil & Método Montessori')" class="curso-card snap-start w-64 sm:w-72 shrink-0 glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-blue-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Bilinguismo Infantil Metodo Montessori Alfabetizacao Materiais Criancas Pais">
            <div>
              {banner_card("DESENVOLVIMENTO", "Bilinguismo & Montessori", "Pedagogia Avançada", "from-cyan-950 via-zinc-900 to-sky-900", "🧩")}
              <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors line-clamp-1">Bilinguismo Infantil & Montessori</h4>
              <p class="text-[11px] text-zinc-400 mt-1 line-clamp-2 leading-relaxed">Atividades lúdicas, cartões de pareamento e rotinas para ensinar inglês aos filhos em casa.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between">
              <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Liberado no VIP</span>
              <span class="text-[10px] font-semibold text-zinc-400">Primeira Infância</span>
            </div>
          </div>
        </div>
      </div>
"""

# Montar o container do catálogo com botões limpos (sem barra invertida)
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
# 6. FERRAMENTAS CONSOLIDADAS COM BANNERS RICOS
# -------------------------------------------------------------
ferramentas_html = f"""
    <!-- SEÇÃO CONSOLIDADA: FERRAMENTAS, BOTS & SOFTWARES INCLUSOS -->
    <section class="mb-14 relative z-10" id="ferramentas">
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
        <!-- Ferramenta 1 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Typebot & Robôs de Atendimento')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Typebot Robos WhatsApp Telegram Automacao Fluxos Atendimento">
          <div>
            {banner_card("BOTS & FLUXOS", "Typebot & Robôs Prontos", "Fluxos de Venda e SAC", "from-purple-950 via-zinc-900 to-indigo-950", "🤖")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Typebot & Robôs de Atendimento</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Modelos prontos de fluxos conversacionais para WhatsApp e Telegram validados para vendas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">JSONs Prontos</span>
            <span class="text-zinc-500">Download Direto</span>
          </div>
        </div>

        <!-- Ferramenta 2 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Canva Pro & Pack de Artes')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Canva Pro Pack Artes Design Templates Editaveis Redes Sociais">
          <div>
            {banner_card("DESIGN VIP", "Canva Pro & Mega Pack", "Artes e Feeds Editáveis", "from-blue-950 via-zinc-900 to-cyan-950", "🎨")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Canva Pro & Super Pack de Artes</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Milhares de templates editáveis para feed, stories, criativos de anúncios e capas magnéticas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Editável em 1 Clique</span>
            <span class="text-zinc-500">10k+ Templates</span>
          </div>
        </div>

        <!-- Ferramenta 3 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Banco de Vídeos Virais 4K')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Banco Videos Virais 4K Cortes Reels TikTok Shorts Lifestyle Carros Viagens">
          <div>
            {banner_card("VÍDEOS 4K", "Acervo de Vídeos Virais", "Banco de Imagens 4K Ultra", "from-red-950 via-zinc-900 to-rose-950", "📹")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Acervo de Vídeos Virais 4K</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Banco com mais de 10.000 takes em ultra resolução sem direitos autorais para Reels, Shorts e TikTok.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">10k Takes 4K</span>
            <span class="text-zinc-500">Sem Direitos</span>
          </div>
        </div>

        <!-- Ferramenta 4 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Páginas de Vendas em Alta Conversão')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Paginas Vendas Elementor HTML Landing Pages Alta Conversao VSL Checkout">
          <div>
            {banner_card("TEMPLATES VSL", "Páginas de Venda Prontas", "Elementor & HTML5 Puro", "from-emerald-950 via-zinc-900 to-teal-950", "🌐")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Páginas de Vendas em Alta Conversão</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Modelos validados em Elementor e HTML com alta retenção, responsivos e otimizados para vendas.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Elementor & HTML</span>
            <span class="text-zinc-500">Pronto para Usar</span>
          </div>
        </div>

        <!-- Ferramenta 5 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Super Pack de Prompts IA')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Prompts IA ChatGPT Midjourney Claude Comandos Secretos Engenharia de Prompt">
          <div>
            {banner_card("PROMPTS MESTRES", "Super Pack Prompts IA", "ChatGPT, Claude & Midjourney", "from-purple-950 via-zinc-900 to-violet-950", "🧠")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Super Pack de Prompts IA</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Engenharia de comandos mestres para gerar copys, imagens realistas, automações e roteiros virais.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Comandos Validados</span>
            <span class="text-zinc-500">Copiar e Colar</span>
          </div>
        </div>

        <!-- Ferramenta 6 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Mega Pack PLRs Validados')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="PLRs Validados Ebooks Paginas Direitos Revenda Produtos Prontos">
          <div>
            {banner_card("REVENDA DIRETA", "Mega Pack PLRs Validados", "Ebooks com Direitos Revenda", "from-amber-950 via-zinc-900 to-orange-950", "📦")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Mega Pack PLRs Validados</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Ebooks nos nichos mais lucrativos com páginas de vendas, criativos e direitos totais de revenda.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">100% dos Lucros</span>
            <span class="text-zinc-500">Direito de Marca</span>
          </div>
        </div>

        <!-- Ferramenta 7 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Planilhas de Gestão & Tráfego')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Planilhas Gestao Trafego ROI Métricas Dashboard Calculadoras Vendas">
          <div>
            {banner_card("GESTÃO & ROI", "Planilhas de Gestão & Tráfego", "Dashboards e Calculadoras ROI", "from-teal-950 via-zinc-900 to-emerald-950", "📊")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Planilhas de Gestão & Tráfego</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Calculadoras de ROI, acompanhamento de métricas de anúncios, precificação e gestão de fluxo de caixa.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Excel & Sheets</span>
            <span class="text-zinc-500">Controle Total</span>
          </div>
        </div>

        <!-- Ferramenta 8 -->
        <div onclick="abrirModalPixCurso('Ferramenta: Base de Leads B2B')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between" data-titulo="Base Leads B2B Prospeccao Contatos CNPJs Segmentados WhatsApp Cold Mail">
          <div>
            {banner_card("LEADS QUALIFICADOS", "Base de Leads B2B", "Prospecção e Segmentação", "from-blue-950 via-zinc-900 to-indigo-950", "🎯")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Base de Leads B2B Segmentados</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Listas de empresas segmentadas por estado e nicho para prospecção no WhatsApp e cold e-mail.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[11px]">
            <span class="text-emerald-400 font-semibold">Leads Validados</span>
            <span class="text-zinc-500">Prospecção B2B</span>
          </div>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 7. BÔNUS: CANAIS VIP
# -------------------------------------------------------------
canais_html = f"""
    <!-- BÔNUS: CANAIS VIP -->
    <section class="mt-20 mb-20 relative">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>🎁 BÔNUS EXCLUSIVO INCLUSO</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">Canais & Comunidades VIP no Telegram</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Acesso direto aos canais privados com atualizações diárias de ferramentas, sinais, saúde e conteúdo.</p>
        </div>
        <span class="text-xs font-bold px-3 py-1.5 rounded-xl bg-white/5 border border-white/10 text-emerald-400 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          8 Canais com Conteúdo Diário
        </span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div onclick="abrirModalPixCurso('Canal VIP: Fábrica de Robôs')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-purple-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("AUTOMAÇÃO VIP", "Fábrica de Robôs", "Bots & Scripts", "from-purple-950 via-zinc-900 to-indigo-950", "🤖")}
            <h4 class="font-bold text-sm text-white group-hover:text-purple-400 transition-colors">Fábrica de Robôs</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Scripts diários de automação, fluxos de chat e robôs prontos para instalar.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-purple-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Apk Premium')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("APPS MODS", "Apk Premium", "Aplicativos Desbloqueados", "from-emerald-950 via-zinc-900 to-teal-950", "📱")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Apk Premium</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Repositório com os apps utilitários mais buscados e versões premium diretas.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-emerald-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Análise de Criptomoeda')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-amber-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("CRIPTO & MERCADO", "Análise de Criptomoeda", "Sinais e Relatórios", "from-amber-950 via-zinc-900 to-yellow-950", "🪙")}
            <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors">Análise de Criptomoeda</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Relatórios de mercado, altcoins promissoras e análises gráficas sem complicação.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-amber-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: NutriTips & Saúde')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-teal-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("NUTRIÇÃO & CORPO", "NutriTips & Saúde", "Dietas e Rotinas", "from-teal-950 via-zinc-900 to-emerald-950", "🥗")}
            <h4 class="font-bold text-sm text-white group-hover:text-teal-400 transition-colors">NutriTips & Saúde</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Dicas práticas de nutrição, planos alimentares saudáveis e ganho de energia.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-teal-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Notas Médicas & Saúde')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-rose-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("MEDICINA PRÁTICA", "Notas Médicas & Saúde", "Resumos e Artigos", "from-rose-950 via-zinc-900 to-red-950", "🩺")}
            <h4 class="font-bold text-sm text-white group-hover:text-rose-400 transition-colors">Notas Médicas & Saúde</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Resumos médicos, fisiologia e bem-estar físico explicados de forma direta.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-rose-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Receitas & Cozinha Fácil')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-orange-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("GASTRONOMIA", "Receitas & Cozinha Fácil", "Pratos Econômicos", "from-orange-950 via-zinc-900 to-amber-950", "🍳")}
            <h4 class="font-bold text-sm text-white group-hover:text-orange-400 transition-colors">Receitas & Cozinha Fácil</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Receitas deliciosas, sobremesas rápidas e pratos econômicos para o dia a dia.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-orange-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Mente Vencedora')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-blue-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("MENTALIDADE", "Mente Vencedora", "Foco & Disciplina", "from-blue-950 via-zinc-900 to-cyan-950", "🏆")}
            <h4 class="font-bold text-sm text-white group-hover:text-blue-400 transition-colors">Mente Vencedora</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Áudios de disciplina, foco mental e hábitos dos maiores empreendedores do mundo.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-blue-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Wallpapers 4K & HD')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-violet-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("WALLPAPERS 4K", "Wallpapers 4K & HD", "Arte Digital e Telas", "from-violet-950 via-zinc-900 to-purple-950", "🖼️")}
            <h4 class="font-bold text-sm text-white group-hover:text-violet-400 transition-colors">Wallpapers 4K & HD</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Imagens e artes geradas por inteligência artificial em altíssima definição para celular e PC.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-violet-400">Canal Ativo Diário</span>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 8. BÔNUS: GAMES & EMULADORES (Layout vertical corrigido)
# -------------------------------------------------------------
games_html = """
    <!-- BÔNUS: BIBLIOTECA DE GAMES & EMULADORES (Layout Vertical Corrigido) -->
    <section class="mt-20 mb-20 relative">
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
          <div>
            <span class="text-xs font-black text-white block group-hover:text-red-400 transition-colors">Nintendo Switch</span>
            <span class="text-[10px] text-zinc-400 font-medium">@Switch_library_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PlayStation 5')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_playstation_5.webp" alt="PS5 Games" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-blue-600 text-white">PS5</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-blue-400 transition-colors">PlayStation 5</span>
            <span class="text-[10px] text-zinc-400 font-medium">@PS5_libr_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PlayStation 4')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_playstation_4.webp" alt="PS4 Games" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-blue-700 text-white">PS4</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-blue-400 transition-colors">PlayStation 4</span>
            <span class="text-[10px] text-zinc-400 font-medium">@PS4_libr_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PlayStation 2')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_playstation_2.webp" alt="PS2 Clássicos" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-indigo-600 text-white">PS2</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-indigo-400 transition-colors">PlayStation 2</span>
            <span class="text-[10px] text-zinc-400 font-medium">@PS2_libr_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PC Games Steam')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_pc_steam.webp" alt="PC Games Steam" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-slate-700 text-white">PC</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-slate-300 transition-colors">PC Games Steam</span>
            <span class="text-[10px] text-zinc-400 font-medium">@PC_libr_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Xbox 360 & Clássico')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_xbox_360.webp" alt="Xbox 360" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-emerald-600 text-white">XBOX</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-emerald-400 transition-colors">Xbox 360 & Clássico</span>
            <span class="text-[10px] text-zinc-400 font-medium">@Xbox360_library_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: VR Oculus Quest')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_vr_oculus.webp" alt="VR Oculus Quest" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-purple-600 text-white">VR</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-purple-400 transition-colors">VR Oculus Quest</span>
            <span class="text-[10px] text-zinc-400 font-medium">@Oculus_library_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PSP & PS Vita')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_psp_psvita.webp" alt="PSP e PS Vita" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-sky-600 text-white">PORTÁTEIS</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-sky-400 transition-colors">PSP & PS Vita</span>
            <span class="text-[10px] text-zinc-400 font-medium">@PSP_libr_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: Nintendo 3DS / DS')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_nintendo_3ds.webp" alt="Nintendo 3DS" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-rose-600 text-white">3DS</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-rose-400 transition-colors">Nintendo 3DS / DS</span>
            <span class="text-[10px] text-zinc-400 font-medium">@N3DS_library_bot</span>
          </div>
        </a>

        <a href="javascript:void(0)" onclick="abrirModalPixCurso('Biblioteca Gamer: PS1 & Retro Arcade')" class="group glass-card p-2.5 rounded-2xl flex flex-col justify-between text-center border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">
          <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-2 bg-black border border-white/5">
            <img src="/assets/capas_reais/console_ps1_retro.webp" alt="PS1 e Retro Arcade" onerror="this.style.display='none'" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-1 left-1 text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-zinc-700 text-white">RETRO</span>
          </div>
          <div>
            <span class="text-xs font-black text-white block group-hover:text-zinc-300 transition-colors">PS1 & Retro Arcade</span>
            <span class="text-[10px] text-zinc-400 font-medium">@PSX_library_bot</span>
          </div>
        </a>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 9. BÔNUS: LIVROS, TEOLOGIA & GOLS
# -------------------------------------------------------------
livros_html = f"""
    <!-- BÔNUS: LIVROS RAROS, TEOLOGIA, GOLS E SOFTWARES -->
    <section class="mt-16 mb-20 relative">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-white/10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-2">
            <span>📚 CULTURA, LIVROS & UTILITÁRIOS</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">Livros Raros, Teologia, Gols e Softwares</h2>
          <p class="text-xs sm:text-sm text-zinc-400 mt-1">Acervo enciclopédico de livros raros, compêndios teológicos, transmissões esportivas e utilitários.</p>
        </div>
        <span class="text-xs font-bold px-3 py-1.5 rounded-xl bg-white/5 border border-white/10 text-emerald-400 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          8 Coleções Especiais
        </span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div onclick="abrirModalPixCurso('Tópico: Teologia & Livros Gospel')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-amber-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("TEOLOGIA", "Teologia & Livros Gospel", "Biblioteca Teológica Completa", "from-amber-950 via-zinc-900 to-yellow-950", "📖")}
            <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors">Teologia & Livros Gospel</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Comentários bíblicos, grego, hebraico, história eclesiástica e livros clássicos.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-amber-400">Coleção Completa</span>
        </div>

        <div onclick="abrirModalPixCurso('Tópico: Livros de Medicina & Saúde')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-rose-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("MEDICINA", "Livros de Medicina & Saúde", "Tratados e Atlas de Anatomia", "from-rose-950 via-zinc-900 to-red-950", "🩺")}
            <h4 class="font-bold text-sm text-white group-hover:text-rose-400 transition-colors">Livros de Medicina & Saúde</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Tratados de farmacologia, atlas de anatomia e guias clínicos para estudantes.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-rose-400">Coleção Completa</span>
        </div>

        <div onclick="abrirModalPixCurso('Tópico: Áudio Livros & Best-Sellers')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-purple-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("ÁUDIO LIVROS", "Áudio Livros & Best-Sellers", "Desenvolvimento e Negócios", "from-purple-950 via-zinc-900 to-indigo-950", "🎧")}
            <h4 class="font-bold text-sm text-white group-hover:text-purple-400 transition-colors">Áudio Livros & Best-Sellers</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Os livros de negócios, finanças e desenvolvimento pessoal narrados na íntegra.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-purple-400">Áudios em MP3</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Gols ao Vivo & Futebol')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-emerald-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("FUTEBOL VIP", "Gols ao Vivo & Futebol", "Melhores Momentos e Lances", "from-emerald-950 via-zinc-900 to-teal-950", "⚽")}
            <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Gols ao Vivo & Futebol</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Vídeos dos gols da rodada, lances em alta definição e análises de partidas.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-emerald-400">Atualização em Tempo Real</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: Cale-se e Leve Meu Dinheiro')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-cyan-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("ACHADINHOS", "Cale-se e Leve Meu Dinheiro", "Produtos Virais de Afiliados", "from-cyan-950 via-zinc-900 to-blue-950", "🛒")}
            <h4 class="font-bold text-sm text-white group-hover:text-cyan-400 transition-colors">Cale-se e Leve Meu Dinheiro</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Achadinhos de e-commerce e produtos virais da Shopee e AliExpress para afiliados.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-cyan-400">Canal Ativo Diário</span>
        </div>

        <div onclick="abrirModalPixCurso('Tópico: Figurinhas Instagram & Tatuagens')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-pink-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("STICKERS & TATTOO", "Figurinhas & Tatuagens", "Flash Arts e Packs PNG", "from-pink-950 via-zinc-900 to-fuchsia-950", "✨")}
            <h4 class="font-bold text-sm text-white group-hover:text-pink-400 transition-colors">Figurinhas & Tatuagens</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Packs de stickers para stories, ilustrações PNG e flash arts para tatuadores.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-pink-400">Downloads Diretos</span>
        </div>

        <div onclick="abrirModalPixCurso('Tópico: Softwares & Utilitários 2026')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-sky-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("SOFTWARES 2026", "Softwares & Utilitários", "Editores e Ferramentas PC", "from-sky-950 via-zinc-900 to-blue-950", "💻")}
            <h4 class="font-bold text-sm text-white group-hover:text-sky-400 transition-colors">Softwares & Utilitários 2026</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Editores de vídeo, conversores, compactadores e programas essenciais para PC.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-sky-400">Softwares Testados</span>
        </div>

        <div onclick="abrirModalPixCurso('Canal VIP: História em Preto e Branco')" class="curso-card glass-card rounded-2xl p-4 transition-all duration-300 group cursor-pointer hover:border-zinc-500/50 hover:scale-[1.02] flex flex-col justify-between">
          <div>
            {banner_card("HISTÓRIA", "História Preto e Branco", "Fotografias Históricas Raras", "from-zinc-900 via-zinc-950 to-black", "📸")}
            <h4 class="font-bold text-sm text-white group-hover:text-zinc-300 transition-colors">História em Preto e Branco</h4>
            <p class="text-xs text-zinc-400 mt-1 line-clamp-2">Fotografias históricas restauradas, fatos curiosos e crônicas do século XX.</p>
          </div>
          <span class="mt-3 text-[11px] font-bold text-zinc-400">Conteúdo Cultural</span>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 10. SEÇÃO 68 TÓPICOS NO TELEGRAM (Banners limpos)
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
        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #01 AO #08", "IA & Automação Inteligente", "Bots, Prompts & Agentes", "from-purple-950 via-zinc-900 to-indigo-950", "🤖")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• ChatGPT, Claude e Midjourney Pro</div>
            <div>• N8N, Typebot & Webhooks Avançados</div>
            <div>• Lovable, Make e Criação de Apps IA</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #09 AO #16", "Tráfego Pago & Escala", "Meta Ads, Google & TikTok", "from-rose-950 via-zinc-900 to-red-950", "📈")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• Sobral, Victor Anjos e Gestão de Tráfego</div>
            <div>• Contingência, Aquecimento e Esteiras</div>
            <div>• Google Ads e Estratégia de Palavras-Chave</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #17 AO #24", "Copywriting & Vendas", "VSLs, Funis e WhatsApp", "from-amber-950 via-zinc-900 to-yellow-950", "✍️")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• O Novo Mercado e Métodos de Copy</div>
            <div>• Vendas no X1 no WhatsApp & Fechamento</div>
            <div>• Roteiros Magnéticos para Criativos</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #25 AO #32", "E-commerce & Dropshipping", "Shopify, Mineração e Fornecedores", "from-emerald-950 via-zinc-900 to-teal-950", "🛒")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• Lojas de Alta Conversão em Shopify</div>
            <div>• Mineração Secreta e Fornecedores Nacionais</div>
            <div>• Mercado Livre, Shopee e Magalu</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #33 AO #40", "Programação & Full Stack", "Web, Mobile & Banco de Dados", "from-cyan-950 via-zinc-900 to-blue-950", "💻")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• JavaScript, React, Node.js e Python</div>
            <div>• Hacking Ético, Segurança e Red Team</div>
            <div>• Figma, Prototipagem e UI/UX Pro</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #41 AO #48", "SEO & Tráfego Orgânico", "Google Discover, Mapas e YouTube", "from-emerald-950 via-zinc-900 to-green-950", "🔍")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• SEO Sem Segredos e Blogs Lucrativos</div>
            <div>• Google Meu Negócio para Empresas Locais</div>
            <div>• Algoritmo do YouTube e Retenção Extrema</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #49 AO #58", "Beleza & Profissões Práticas", "Unhas, Cílios, Make e Confeitaria", "from-pink-950 via-zinc-900 to-fuchsia-950", "💅")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• Manicure e Pedicure Faby Cardoso</div>
            <div>• Viver de Cílios Larissa Costa</div>
            <div>• Confeitaria Lucrativa e Sobremesas</div>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-black/40 border border-white/10 flex flex-col justify-between">
          {banner_card("TÓPICOS #59 AO #68", "Idiomas, Concursos & Games", "Inglês, Concursos Públicos e ROMs", "from-blue-950 via-zinc-900 to-sky-950", "🎮")}
          <div class="space-y-1.5 text-xs text-zinc-400">
            <div>• Curso de Inglês Mairo Vergara Completo</div>
            <div>• Apostilas Estratégia Concursos em PDF</div>
            <div>• Bibliotecas de Nintendo Switch, PS5 e PC</div>
          </div>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 11. COMO VOCÊ RECEBE SEU ACESSO (H2 + Bloco 2 Fases Corrigido)
# -------------------------------------------------------------
receber_html = """
    <!-- SEÇÃO: COMO VOCÊ RECEBE SEU ACESSO -->
    <section class="my-16 glass-panel rounded-3xl p-6 sm:p-10 border border-white/10 relative z-10">
      <div class="text-center max-w-xl mx-auto mb-8">
        <span class="px-3 py-1 rounded-full text-[11px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
          PROCESSO 100% AUTOMATIZADO
        </span>
        <h2 class="text-2xl sm:text-3xl font-black text-white mt-2">Como Você Recebe Seu Acesso</h2>
        <p class="text-xs sm:text-sm text-zinc-400 mt-1">Simples, direto e sem burocracia em apenas 3 passos</p>
      </div>

      <!-- Grid dos 3 Passos -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-black/50 border border-white/10 rounded-2xl p-6 text-center hover:border-emerald-500/40 transition-all">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black text-xl mx-auto mb-4 border border-emerald-500/30">
            1
          </div>
          <h4 class="text-base font-bold text-white mb-2">Faça o Pix de R$ 9,90</h4>
          <p class="text-xs text-zinc-400">Pague a taxa única simbólica no aplicativo do seu banco via Pix Copia e Cola ou Chave Oficial.</p>
        </div>

        <div class="bg-black/50 border border-white/10 rounded-2xl p-6 text-center hover:border-emerald-500/40 transition-all">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black text-xl mx-auto mb-4 border border-emerald-500/30">
            2
          </div>
          <h4 class="text-base font-bold text-white mb-2">Envie no Bot do Telegram</h4>
          <p class="text-xs text-zinc-400">Envie o comprovante no bot oficial do Telegram (@AcervoDigitalVIP_bot). Nosso sistema valida em instantes.</p>
        </div>

        <div class="bg-black/50 border border-white/10 rounded-2xl p-6 text-center hover:border-emerald-500/40 transition-all">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black text-xl mx-auto mb-4 border border-emerald-500/30">
            3
          </div>
          <h4 class="text-base font-bold text-white mb-2">Link VIP Liberado</h4>
          <p class="text-xs text-zinc-400">Você recebe o link de convite exclusivo para todos os tópicos e pastas. Acesso vitalício garantido!</p>
        </div>
      </div>

      <!-- AVISO DE SEGURANÇA E PROTEÇÃO DO ACERVO: CRONOGRAMA EM 2 FASES (LARGURA TOTAL 100%) -->
      <div class="w-full mt-8 p-6 rounded-2xl bg-gradient-to-r from-emerald-950/30 via-black/60 to-emerald-950/30 border border-emerald-500/30 shadow-xl relative overflow-hidden">
        <div class="flex flex-col md:flex-row items-start md:items-center gap-5">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 flex items-center justify-center shrink-0 text-2xl shadow-inner">
            🛡️
          </div>
          <div class="flex-1 w-full">
            <div class="flex items-center gap-2 flex-wrap mb-1.5">
              <span class="text-[10px] font-black uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-500 text-black">Blindagem & Segurança</span>
              <h4 class="text-base sm:text-lg font-black text-white">Como Funciona a Liberação em 2 Fases (Dia 1 e 8º Dia)</h4>
            </div>
            <p class="text-xs sm:text-sm text-zinc-300 leading-relaxed mb-3">
              Para proteger nossa comunidade contra cópias piratas, robôs extratores e golpistas que compram apenas para baixar em massa e pedir reembolso, nosso sistema opera com liberação progressiva inteligente:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs w-full">
              <div class="p-3.5 rounded-xl bg-white/5 border border-white/5">
                <span class="font-bold text-emerald-400 block mb-1 flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  ⚡ Dia 1 (Imediato após Pix):
                </span>
                <span class="text-zinc-400 leading-relaxed block">Acesso à Comunidade VIP Telegram, Microcursos de IA e Tráfego, Top Ferramentas e primeiros Packs de Prompts e PLRs para começar no mesmo minuto.</span>
              </div>
              <div class="p-3.5 rounded-xl bg-white/5 border border-white/5">
                <span class="font-bold text-cyan-400 block mb-1 flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                  🔓 8º Dia (Liberação Total Irrestrita):
                </span>
                <span class="text-zinc-400 leading-relaxed block">Desbloqueio completo dos 68 tópicos, downloads em massa, bibliotecas inteiras de emuladores e acervos pesados de vídeos 4K.</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# -------------------------------------------------------------
# 12. PERGUNTAS FREQUENTES (H2 + 6 Perguntas Completas)
# -------------------------------------------------------------
faq_html = """
    <!-- PERGUNTAS FREQUENTES -->
    <section class="my-16 max-w-3xl mx-auto relative z-10">
      <div class="text-center mb-8">
        <span class="px-3 py-1 rounded-full text-[11px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
          TIRE SUAS DÚVIDAS
        </span>
        <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight mt-2">Perguntas Frequentes</h2>
        <p class="text-xs sm:text-sm text-zinc-400 mt-1">Tudo que você precisa saber antes de adquirir seu acesso</p>
      </div>

      <div class="space-y-3">
        <!-- Item 1 -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>1. O acesso é realmente vitalício por apenas R$ 9,90?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            Sim! Você paga uma única taxa simbólica de R$ 9,90 e tem acesso para sempre. Não existem mensalidades nem taxas ocultas adicionais.
          </div>
        </div>

        <!-- Item 2 -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>2. Como são entregues os cursos e arquivos?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            Todo o acervo está organizado em tópicos separados no Telegram (vídeos, PDFs, modelos de código, planilhas e drives na nuvem). Ao confirmar seu Pix de R$ 9,90, nosso bot oficial envia seu link de acesso imediato.
          </div>
        </div>

        <!-- Item 3 -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>3. Novos cursos e ferramentas são adicionados?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            Sim! O acervo recebe atualizações semanais com novos lançamentos do mercado digital, automações e materiais solicitados pelos próprios membros sem cobrar nada a mais por isso.
          </div>
        </div>

        <!-- Item 4 -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>4. E se eu não souber usar o Telegram?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            O Telegram é um aplicativo gratuito que funciona no celular e no computador. Temos um tutorial em vídeo de 2 minutos explicando passo a passo como navegar pelas pastas e baixar qualquer aula.
          </div>
        </div>

        <!-- Item 5 -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>5. Como funciona o suporte caso eu tenha dúvidas?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            Temos atendimento direto no Telegram pelo bot oficial (@AcervoDigitalVIP_bot) e também canal de triagem (https://t.me/+-gV1v2gZzGozZDFh) prontos para ajudar na liberação do seu acesso.
          </div>
        </div>

        <!-- Item 6 -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>6. Como funciona a liberação em 2 fases (Dia 1 e 8º Dia)?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            No <strong>Dia 1</strong> (imediato após o Pix de R$ 9,90), você recebe acesso à Comunidade VIP no Telegram, Microcursos principais, ferramentas de IA e packs essenciais para começar a produzir no mesmo minuto. No <strong>8º dia</strong> (após o término do período de garantia legal de 7 dias do CDC), nosso sistema libera o download massivo e irrestrito de todos os 68 tópicos, acervos pesados de 4K e bibliotecas inteiras de emuladores. Isso garante a sustentabilidade e velocidade dos nossos servidores para quem realmente é membro fiel!
          </div>
        </div>
      </div>
    </section>

    <!-- DESTAQUES E GARANTIA BLINDADA -->
    <section class="my-16 grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
      <div class="glass-panel p-6 sm:p-8 rounded-3xl border border-purple-500/20 relative overflow-hidden flex flex-col justify-between">
        <div>
          <span class="px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-purple-500/10 text-purple-400 border border-purple-500/30 mb-3 inline-block">
            ⚡ EXCLUSIVO 2026
          </span>
          <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">Agentes Autônomos, N8N & No-Code</h3>
          <p class="text-xs text-zinc-400 mt-2 leading-relaxed">
            Aprenda a construir assistentes que atendem clientes, fecham vendas e operam sozinhos 24 horas por dia através de automações com IA.
          </p>
        </div>
        <div class="mt-6 flex items-center gap-3">
          <button onclick="abrirModalPixCurso('Agentes Autônomos & N8N Pro')" data-track="cta_bloco_agentes" class="px-5 py-2.5 rounded-xl bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-wider transition-colors shadow-lg shadow-purple-500/20">
            Acessar Treinamentos ➜
          </button>
        </div>
      </div>

      <div class="glass-panel p-6 sm:p-8 rounded-3xl border border-emerald-500/20 relative overflow-hidden flex flex-col justify-between">
        <div>
          <span class="px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 mb-3 inline-block">
            🛡️ RISCO ZERO ABSOLUTO
          </span>
          <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">Garantia Blindada de 7 Dias</h3>
          <p class="text-xs text-zinc-400 mt-2 leading-relaxed">
            Se por qualquer motivo você achar que o acervo não valeu os R$ 9,90, basta nos enviar uma mensagem no Telegram dentro de 7 dias e devolvemos seu dinheiro na hora. Sem letras miúdas.
          </p>
        </div>
        <div class="mt-6 flex items-center gap-3 text-xs text-emerald-400 font-bold">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          Conformidade com o Código de Defesa do Consumidor (Art. 49)
        </div>
      </div>
    </section>

    <!-- CHECKOUT FINAL -->
    <section id="checkout" class="mt-20 glass-panel rounded-3xl p-6 sm:p-12 border border-emerald-500/30 text-center max-w-3xl mx-auto shadow-2xl relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-t from-emerald-950/30 via-transparent to-transparent pointer-events-none"></div>

      <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
        ⚡ Oportunidade Limitada
      </span>

      <h2 class="text-3xl sm:text-5xl font-black text-white mt-4 tracking-tight">
        Destrave o Acervo Inteiro Agora
      </h2>
      <p class="text-zinc-300 text-sm sm:text-base mt-2 max-w-lg mx-auto">
        Pague apenas uma vez e tenha acesso irrestrito e vitalício a todos os 68 tópicos no Telegram.
      </p>

      <div class="my-6">
        <span class="text-sm text-zinc-500 line-through block font-medium">De R$ 19,90</span>
        <div class="text-4xl sm:text-6xl font-black text-emerald-400 font-mono my-1">
          R$ 9,90
        </div>
        <span class="text-xs text-zinc-400 block font-medium">Pagamento único via Pix • Sem assinatura • Acesso vitalício</span>
      </div>

      <button onclick="abrirModalPix()" data-track="cta_checkout_final" class="w-full sm:w-auto px-10 py-5 rounded-2xl font-black text-sm uppercase tracking-wide bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-black shadow-xl shadow-emerald-500/30 hover:scale-105 active:scale-95 transition-all mx-auto block">
        Quero Meu Acesso Vitalício por R$ 9,90 ➜
      </button>

      <div class="mt-6 flex flex-wrap items-center justify-center gap-6 text-xs text-zinc-400">
        <span class="flex items-center gap-1.5"><span class="text-emerald-400">⚡</span> Pix Imediato</span>
        <span class="flex items-center gap-1.5"><span class="text-emerald-400">🔒</span> Compra Segura</span>
        <span class="flex items-center gap-1.5"><span class="text-emerald-400">🛡️</span> Garantia de 7 Dias</span>
      </div>
    </section>
  </main>
"""

# -------------------------------------------------------------
# 13. FOOTER (pb-24 sm:pb-8 e link discreto do painel)
# -------------------------------------------------------------
footer_html = """
  <!-- FOOTER -->
  <footer class="relative z-10 border-t border-white/10 glass-panel pt-8 pb-24 sm:pb-8 px-6 text-center text-xs text-zinc-400 max-w-7xl mx-auto w-full">
    <div class="flex flex-col sm:flex-row items-center justify-between gap-4 max-w-5xl mx-auto">
      <div class="text-left">
        <p class="font-bold text-white text-sm">ACERVO DIGITAL VIP</p>
        <p class="text-[11px] text-zinc-400 mt-0.5">Comunidade e repositório de conteúdos organizados no Telegram.</p>
      </div>

      <div class="flex items-center flex-wrap gap-4 text-xs">
        <a href="/privacidade.html" class="hover:text-emerald-400 transition-colors">Política de Privacidade</a>
        <span>•</span>
        <a href="/termos.html" class="hover:text-emerald-400 transition-colors">Termos de Uso</a>
        <span>•</span>
        <a href="https://t.me/AcervoDigitalVIP_bot" target="_blank" rel="noopener noreferrer" class="hover:text-sky-400 transition-colors">Suporte (@AcervoDigitalVIP_bot)</a>
        <span>•</span>
        <a href="https://t.me/+-gV1v2gZzGozZDFh" target="_blank" rel="noopener noreferrer" class="hover:text-cyan-400 transition-colors">Canal de Triagem</a>
        <span>•</span>
        <a href="/painel/" class="hover:text-emerald-400 transition-colors flex items-center gap-1"><span>🔐</span> Painel</a>
      </div>
    </div>
    <div class="mt-6 pt-4 border-t border-white/5 text-[11px] text-zinc-500">
      © 2026 ACERVO DIGITAL VIP. Todos os direitos reservados. Plataforma de acesso a conteúdos digitais.
    </div>
  </footer>
"""

# -------------------------------------------------------------
# 14. MODAIS & STICKY CTA BAR
# -------------------------------------------------------------
modais_html = """
  <!-- MODAL PIX AUTOMÁTICO (CHAVE COPIA E COLA / QR CODE) -->
  <div id="modal-pix" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="glass-panel bg-zinc-950 border border-emerald-500/40 rounded-3xl p-6 sm:p-8 max-w-md w-full relative shadow-2xl max-h-[90vh] overflow-y-auto">
      <button onclick="fecharModalPix()" aria-label="Fechar janela" class="absolute top-4 right-4 text-zinc-400 hover:text-white text-lg w-8 h-8 rounded-full bg-white/5 flex items-center justify-center">
        ✕
      </button>

      <div class="text-center">
        <span class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl mx-auto mb-3">
          ⚡
        </span>
        <h3 id="modal-pix-title" class="text-xl font-bold text-white tracking-tight">Pagamento via Pix</h3>
        <p class="text-xs text-zinc-400 mt-1">Valor com 50% de desconto aplicado:</p>
        <div class="text-3xl font-black text-emerald-400 my-2">R$ 9,90</div>
      </div>

      <!-- SELETOR DE PAGAMENTO PIX (CHAVE COPIA E COLA / QR CODE) -->
      <div class="bg-black/80 rounded-2xl p-4 border border-white/10 my-4 text-center">
        <div class="flex items-center justify-center gap-2 mb-3">
          <button type="button" id="tab-btn-chave" onclick="alternarTabPix('chave')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-500 text-black transition-all">
            🔑 Chave Copia e Cola
          </button>
          <button type="button" id="tab-btn-qr" onclick="alternarTabPix('qr')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-white/5 text-zinc-400 hover:text-white transition-all">
            📱 QR Code (Escanear)
          </button>
        </div>

        <div id="pix-view-chave">
          <label class="text-[11px] font-bold uppercase tracking-wider text-zinc-400 block mb-1.5 text-left">Chave Pix Oficial (Telefone)</label>
          <div class="flex items-center justify-between gap-2 bg-white/5 p-2.5 rounded-xl border border-white/5">
            <span id="chave-pix" class="font-mono text-sm font-bold text-white">71981223348</span>
            <button onclick="copiarPix()" id="btn-copiar" data-track="copiar_pix_modal" class="px-3 py-1.5 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-black text-xs font-black uppercase transition-all">
              Copiar
            </button>
          </div>
        </div>

        <div id="pix-view-qr" class="hidden flex-col items-center justify-center py-2">
          <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=71981223348&color=10-185-129&bgcolor=0-0-0" alt="QR Code Pix" width="160" height="160" class="rounded-xl border border-emerald-500/40 p-2 bg-black mx-auto mb-2 shadow-lg shadow-emerald-500/10">
          <p class="text-[11px] text-zinc-400">Abra o app do seu banco e aponte a câmera para pagar no Pix.</p>
        </div>
        
        <div class="mt-2.5 text-[10px] text-emerald-400 flex items-center justify-center gap-1 font-semibold">
          <span>🛡️</span> Acesso imediato no Dia 1 + Desbloqueio dos 68 tópicos no 8º dia
        </div>
      </div>

      <div class="space-y-3">
        <a id="link-whats-comprovante" href="https://t.me/AcervoDigitalVIP_bot" target="_blank" rel="noopener noreferrer" class="w-full py-3.5 px-4 rounded-xl font-bold text-xs uppercase tracking-wide bg-gradient-to-r from-[#229ED9] to-teal-400 text-white text-center block shadow-lg shadow-sky-500/20 hover:scale-[1.02] transition-all flex items-center justify-center gap-2">
          <span>✈️ 1. Enviar Comprovante no Bot do Telegram</span>
        </a>
        
        <a href="https://t.me/+-gV1v2gZzGozZDFh" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 px-4 rounded-xl font-bold text-xs uppercase tracking-wide bg-white/5 hover:bg-white/10 text-zinc-300 text-center block border border-white/10 transition-colors">
          Canal de Triagem Oficial
        </a>
      </div>

      <p class="text-[11px] text-zinc-400 text-center mt-4">
        🔒 Pagamento protegido • Chave oficial em nome de Davi Rian.
      </p>
    </div>
  </div>

  <!-- POPUP NINJA DE RETENÇÃO (SAÍDA DA PÁGINA) -->
  <div id="modal-popup-ninja" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4 hidden opacity-0 transition-opacity duration-300">
    <div class="glass-panel rounded-3xl border border-emerald-500/50 max-w-md w-full p-6 sm:p-8 relative bg-gradient-to-b from-zinc-950 to-black shadow-2xl shadow-emerald-950/60 transform scale-95 transition-transform duration-300" id="modal-popup-ninja-content">
      <button onclick="fecharModalPopupNinja()" class="absolute top-4 right-4 text-zinc-400 hover:text-white w-8 h-8 rounded-full bg-white/5 border border-white/10 flex items-center justify-center font-bold text-sm transition-colors">✕</button>

      <div class="text-center">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30 text-[11px] mb-3 animate-pulse">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span> OPORTUNIDADE EXCLUSIVA
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight leading-snug">
          Espere! Libere o Acervo Completo por Apenas R$ 9,90
        </h3>
        <p class="text-xs text-zinc-400 mt-2">
          Mais de 2.000 treinamentos, 8 super packs de ferramentas e 68 tópicos organizados no Telegram. Taxa única sem mensalidade.
        </p>

        <button onclick="fecharModalPopupNinja(); abrirModalPix();" data-track="cta_ninja_popup" class="w-full mt-5 py-4 px-6 rounded-2xl font-black text-xs uppercase tracking-wide bg-gradient-to-r from-emerald-500 to-teal-400 text-black shadow-xl shadow-emerald-500/20 hover:scale-105 active:scale-95 transition-all">
          Garantir Meu Acesso Agora por R$ 9,90 ➜
        </button>
      </div>
    </div>
  </div>

  <!-- WIDGET FLUTUANTE DE OFERTA -->
  <div id="widget-oferta-vip" class="fixed bottom-6 right-5 z-40 flex flex-col items-end gap-2 transition-all duration-300">
    <div class="glass-panel p-3.5 rounded-2xl border border-emerald-500/40 bg-black/90 shadow-2xl backdrop-blur-xl max-w-xs flex items-center gap-3 relative group">
      <button onclick="fecharWidgetOferta()" class="absolute -top-2 -left-2 w-5 h-5 rounded-full bg-zinc-800 text-zinc-400 hover:text-white flex items-center justify-center text-[10px] border border-white/10">✕</button>
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center font-black text-black text-lg shrink-0 shadow-lg shadow-emerald-500/30">
        ⚡
      </div>
      <div>
        <div class="flex items-center gap-1.5">
          <span class="text-[10px] font-black uppercase text-emerald-400 tracking-wider">Acesso Vitalício</span>
          <span class="text-[10px] text-zinc-400 line-through">R$ 19,90</span>
        </div>
        <div class="text-xs font-black text-white">
          Apenas <span class="text-emerald-400">R$ 9,90</span> no Pix
        </div>
      </div>
      <button onclick="abrirModalPix()" data-track="cta_widget_oferta" class="ml-1 px-3 py-2 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-black font-black text-xs tracking-wider uppercase transition-colors shrink-0">
        Entrar
      </button>
    </div>
  </div>

  <!-- BARRA FLUTUANTE DE CTA (STICKY CONVERSÃO RÁPIDA COM INTERSECTION OBSERVER) -->
  <div id="sticky-cta-bar" class="fixed bottom-0 inset-x-0 z-40 bg-black/95 border-t border-emerald-500/30 backdrop-blur-xl px-4 py-3 transform translate-y-full transition-transform duration-300 shadow-2xl flex items-center justify-between gap-3 max-w-xl mx-auto sm:rounded-t-2xl sm:bottom-0">
    <div class="flex items-center gap-2.5">
      <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black text-sm shrink-0">
        ⚡
      </div>
      <div>
        <div class="flex items-center gap-1.5">
          <span class="text-[10px] font-black uppercase text-emerald-400 tracking-wider">Acesso Imediato</span>
          <span class="text-[9px] text-zinc-500 line-through">R$ 19,90</span>
        </div>
        <div class="text-xs sm:text-sm font-black text-white">
          Apenas <span class="text-emerald-400 font-bold">R$ 9,90</span> <span class="text-[10px] text-zinc-400 font-normal">(taxa única)</span>
        </div>
      </div>
    </div>
    <button onclick="abrirModalPix()" data-track="cta_sticky_bar" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-black font-black text-xs uppercase tracking-wider shadow-lg shadow-emerald-500/20 hover:scale-105 active:scale-95 transition-all whitespace-nowrap">
      Destravar Agora ➜
    </button>
  </div>

  <!-- TOAST SOCIAL DE COMPRAS -->
  <div id="toast-social" class="fixed bottom-6 left-5 z-40 transform translate-y-32 opacity-0 transition-all duration-500 pointer-events-none">
    <div class="glass-panel py-2.5 px-3.5 rounded-xl border border-emerald-500/30 bg-black/90 shadow-2xl flex items-center gap-2.5 max-w-xs text-xs">
      <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></div>
      <div class="truncate">
        <span id="toast-social-nome" class="text-white text-[11px] block truncate">Carlos M. de São Paulo</span>
      </div>
      <span class="text-[10px] text-zinc-400 shrink-0">• há 2 min</span>
    </div>
  </div>
"""

# -------------------------------------------------------------
# 15. JAVASCRIPT UNIFICADO (SEM DUPLICATAS)
# -------------------------------------------------------------
scripts_unificados_html = """
  <!-- Scripts Interativos Unificados -->
  <script>
    // 1. Shader de Fundo Leve com Canvas 2D
    const canvas = document.getElementById('aurora-bg');
    if (canvas) {
      const ctx = canvas.getContext('2d');
      let t = 0;
      function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }
      resize();
      window.addEventListener('resize', resize);

      function draw() {
        t += 0.003;
        const w = canvas.width;
        const h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        const grad1 = ctx.createRadialGradient(
          w * (0.3 + 0.2 * Math.sin(t)),
          h * (0.3 + 0.2 * Math.cos(t * 0.8)),
          10,
          w * 0.3,
          h * 0.3,
          w * 0.7
        );
        grad1.addColorStop(0, 'rgba(16, 185, 129, 0.07)');
        grad1.addColorStop(1, 'transparent');
        ctx.fillStyle = grad1;
        ctx.fillRect(0, 0, w, h);

        const grad2 = ctx.createRadialGradient(
          w * (0.7 + 0.2 * Math.cos(t * 0.7)),
          h * (0.6 + 0.2 * Math.sin(t)),
          10,
          w * 0.7,
          h * 0.6,
          w * 0.7
        );
        grad2.addColorStop(0, 'rgba(6, 182, 212, 0.05)');
        grad2.addColorStop(1, 'transparent');
        ctx.fillStyle = grad2;
        ctx.fillRect(0, 0, w, h);

        if (!document.hidden) {
          requestAnimationFrame(draw);
        } else {
          setTimeout(() => requestAnimationFrame(draw), 1000);
        }
      }
      draw();
    }

    // 2. Contador Regressivo de Urgência (Persistente em Sessão)
    let tempoRestante = parseInt(sessionStorage.getItem('acervo_timer')) || (14 * 60 + 48);
    const timerEl = document.getElementById('countdown-timer');
    function atualizarTimer() {
      if (tempoRestante > 0) {
        tempoRestante--;
        sessionStorage.setItem('acervo_timer', tempoRestante);
        const min = Math.floor(tempoRestante / 60);
        const sec = tempoRestante % 60;
        if (timerEl) {
          timerEl.textContent = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
        }
      }
    }
    atualizarTimer();
    setInterval(atualizarTimer, 1000);

    // 3. Busca Instantânea de Cursos
    function filtrarCursos() {
      const termo = document.getElementById('input-busca').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.curso-card');
      let visiveis = 0;

      cards.forEach(card => {
        const dados = (card.getAttribute('data-titulo') || '').toLowerCase();
        if (dados.includes(termo)) {
          card.classList.remove('hidden');
          visiveis++;
        } else {
          card.classList.add('hidden');
        }
      });

      const contador = document.getElementById('contador-busca');
      if (contador) contador.textContent = visiveis;
    }

    // 4. Filtro por Categorias (recebe this como btnElement)
    function filtrarCategoria(cat, btnElement) {
      document.querySelectorAll('.btn-categoria').forEach(btn => {
        btn.classList.remove('bg-emerald-500', 'text-black', 'border-emerald-400', 'active');
        btn.classList.add('bg-white/5', 'text-zinc-300', 'border-white/10');
      });

      const targetBtn = btnElement || (window.event && window.event.currentTarget) || (window.event && window.event.target);
      if (targetBtn) {
        targetBtn.classList.add('bg-emerald-500', 'text-black', 'border-emerald-400', 'active');
        targetBtn.classList.remove('bg-white/5', 'text-zinc-300', 'border-white/10');
      }

      const blocos = document.querySelectorAll('.categoria-bloco');
      blocos.forEach(bloco => {
        if (cat === 'todas' || bloco.getAttribute('data-cat') === cat) {
          bloco.style.display = 'block';
        } else {
          bloco.style.display = 'none';
        }
      });
    }

    // 5. Modal Pix Unificado (com suporte a curso específico)
    function abrirModalPix(nomeCurso) {
      const modal = document.getElementById('modal-pix');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        const tit = document.getElementById('modal-pix-title') || modal.querySelector('h3');
        if (tit) {
          tit.textContent = nomeCurso ? ('Destrave: ' + nomeCurso) : 'Pagamento via Pix';
        }
      }
    }

    function abrirModalPixCurso(nomeCurso) {
      abrirModalPix(nomeCurso);
    }

    function fecharModalPix() {
      const modal = document.getElementById('modal-pix');
      if (modal) {
        modal.classList.remove('flex');
        modal.classList.add('hidden');
      }
    }

    // 6. Funções de Widget e Popup Ninja
    function fecharWidgetOferta() {
      const w = document.getElementById('widget-oferta-vip');
      if (w) w.style.display = 'none';
    }

    function abrirModalPopupNinja() {
      const p = document.getElementById('modal-popup-ninja');
      if (p) {
        p.classList.remove('hidden');
        p.classList.add('flex');
        setTimeout(() => { p.classList.remove('opacity-0'); }, 10);
      }
    }

    function fecharModalPopupNinja() {
      const p = document.getElementById('modal-popup-ninja');
      if (p) {
        p.classList.add('opacity-0');
        setTimeout(() => {
          p.classList.remove('flex');
          p.classList.add('hidden');
        }, 300);
      }
    }

    // 7. Fechamento por Backdrop e Tecla Escape
    const modalPixEl = document.getElementById('modal-pix');
    if (modalPixEl) {
      modalPixEl.addEventListener('click', (e) => {
        if (e.target === modalPixEl) fecharModalPix();
      });
    }

    const modalNinjaEl = document.getElementById('modal-popup-ninja');
    if (modalNinjaEl) {
      modalNinjaEl.addEventListener('click', (e) => {
        if (e.target === modalNinjaEl) fecharModalPopupNinja();
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        fecharModalPix();
        fecharModalPopupNinja();
      }
    });

    // 8. Acordeão de FAQ
    function toggleFaq(btn) {
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      const isHidden = content.classList.contains('hidden');

      document.querySelectorAll('.faq-content').forEach(c => c.classList.add('hidden'));
      document.querySelectorAll('.faq-icon').forEach(i => {
        i.textContent = '+';
        i.classList.remove('rotate-45');
      });

      if (isHidden) {
        content.classList.remove('hidden');
        icon.textContent = '×';
        icon.classList.add('rotate-45');
      }
    }

    // 9. Copiar Chave Pix Unificado
    function copiarPix() {
      const chaveEl = document.getElementById('chave-pix');
      if (!chaveEl) return;
      const chave = chaveEl.textContent.trim();
      navigator.clipboard.writeText(chave).then(() => {
        const btn = document.getElementById('btn-copiar');
        if (btn) {
          const original = btn.textContent;
          btn.textContent = 'Copiado!';
          btn.classList.remove('bg-emerald-500', 'text-black');
          btn.classList.add('bg-emerald-400', 'text-black');
          setTimeout(() => {
            btn.textContent = original;
            btn.classList.remove('bg-emerald-400');
            btn.classList.add('bg-emerald-500');
          }, 2500);
        }
      });
    }

    // 10. Alternância de Abas no Modal Pix (Chave / QR Code)
    function alternarTabPix(tab) {
      const viewChave = document.getElementById('pix-view-chave');
      const viewQr = document.getElementById('pix-view-qr');
      const btnChave = document.getElementById('tab-btn-chave');
      const btnQr = document.getElementById('tab-btn-qr');
      if (!viewChave || !viewQr || !btnChave || !btnQr) return;

      if (tab === 'qr') {
        viewChave.classList.add('hidden');
        viewQr.classList.remove('hidden');
        viewQr.classList.add('flex');
        btnQr.classList.remove('bg-white/5', 'text-zinc-400');
        btnQr.classList.add('bg-emerald-500', 'text-black');
        btnChave.classList.remove('bg-emerald-500', 'text-black');
        btnChave.classList.add('bg-white/5', 'text-zinc-400');
      } else {
        viewQr.classList.add('hidden');
        viewQr.classList.remove('flex');
        viewChave.classList.remove('hidden');
        btnChave.classList.remove('bg-white/5', 'text-zinc-400');
        btnChave.classList.add('bg-emerald-500', 'text-black');
        btnQr.classList.remove('bg-emerald-500', 'text-black');
        btnQr.classList.add('bg-white/5', 'text-zinc-400');
      }
    }

    // 11. Barra Flutuante com IntersectionObserver (Esconde no Checkout e Footer)
    const stickyBar = document.getElementById('sticky-cta-bar');
    const checkoutSec = document.getElementById('checkout');
    const footerEl = document.querySelector('footer');
    let checkoutOrFooterVisible = false;

    if ('IntersectionObserver' in window && stickyBar) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.target === checkoutSec || entry.target === footerEl) {
            const checkRect = checkoutSec ? checkoutSec.getBoundingClientRect() : null;
            const footRect = footerEl ? footerEl.getBoundingClientRect() : null;
            const isCheckInView = checkRect && (checkRect.top < window.innerHeight && checkRect.bottom >= 0);
            const isFootInView = footRect && (footRect.top < window.innerHeight && footRect.bottom >= 0);
            checkoutOrFooterVisible = isCheckInView || isFootInView;
            atualizarStickyBar();
          }
        });
      }, { threshold: 0.05 });

      if (checkoutSec) observer.observe(checkoutSec);
      if (footerEl) observer.observe(footerEl);
    }

    function atualizarStickyBar() {
      if (!stickyBar) return;
      if (window.scrollY > 500 && !checkoutOrFooterVisible) {
        stickyBar.classList.remove('translate-y-full');
      } else {
        stickyBar.classList.add('translate-y-full');
      }
    }

    window.addEventListener('scroll', atualizarStickyBar, { passive: true });

    // 12. Notificação Social de Compras Recentes
    const compradores = [
      { nome: 'Carlos M. de São Paulo', curso: 'liberou os 68 Tópicos VIP', tempo: 'há 1 min' },
      { nome: 'Mariana R. de Belo Horizonte', curso: 'liberou Pack de Ferramentas IA', tempo: 'há 3 min' },
      { nome: 'Rodrigo P. de Salvador', curso: 'liberou Acervo de Vídeos Virais 4K', tempo: 'há 4 min' },
      { nome: 'Fernanda L. de Curitiba', curso: 'liberou Formação SEO & Discover', tempo: 'há 2 min' },
      { nome: 'Guilherme B. de Brasília', curso: 'liberou Biblioteca Gamer & Consoles', tempo: 'há 5 min' },
      { nome: 'Beatriz S. de Florianópolis', curso: 'liberou Super Pack de Prompts IA', tempo: 'há 6 min' }
    ];
    let compIdx = 0;

    function mostrarToastSocial() {
      const toast = document.getElementById('toast-social');
      const nomeEl = document.getElementById('toast-social-nome');
      if (!toast || !nomeEl) return;

      const comp = compradores[compIdx % compradores.length];
      compIdx++;
      nomeEl.innerHTML = `<strong>${comp.nome}</strong> • <span class="text-emerald-400">${comp.curso}</span>`;
      const spanEl = toast.querySelector('span');
      if (spanEl) spanEl.textContent = '• ' + comp.tempo;

      toast.classList.remove('translate-y-32', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-32', 'opacity-0');
      }, 4500);
    }
    setTimeout(mostrarToastSocial, 3000);
    setInterval(mostrarToastSocial, 15000);
  </script>
</body>
</html>
"""

# Montagem final
conteudo_completo = f"""{head_html}
{hero_html}
{catalogo_html}
{ferramentas_html}
{canais_html}
{games_html}
{livros_html}
{topicos_html}
{receber_html}
{faq_html}
{footer_html}
{modais_html}
{scripts_unificados_html}
"""

with open("/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html", "w", encoding="utf-8") as f:
    f.write(conteudo_completo)

print("Arquivo index.html refatorado com sucesso!")
