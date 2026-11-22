import re

with open('/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html.bak', 'r', encoding='utf-8') as f:
    orig = f.read()

# 1. Head & Header
pos_main = orig.find('<main')
pos_main_open_end = orig.find('>', pos_main) + 1
head_and_header = orig[:pos_main_open_end]

head_and_header = re.sub(
    r'@keyframes\s+marquee\s*\{[\s\S]*?\}\s*\}\s*',
    '''@keyframes marquee {
      0% { transform: translateX(0%); }
      100% { transform: translateX(-50%); }
    }
    ''',
    head_and_header
)
head_and_header = re.sub(
    r'\.animate-marquee\s*\{[^}]*\}',
    '''.animate-marquee {
      display: inline-flex;
      white-space: nowrap;
      animation: marquee 25s linear infinite;
      will-change: transform;
    }''',
    head_and_header
)

# Ticker duplicado
ticker_match = re.search(r'(<div\s+class=\"[^\"]*animate-marquee[^\"]*\">)(.*?)(</div>)', head_and_header, re.DOTALL)
if ticker_match:
    t_open, t_content, t_close = ticker_match.groups()
    inner_items = re.findall(r'<span\s+class=\"flex items-center gap-1\.5.*?</span>', t_content)
    if inner_items:
        half = len(inner_items) // 2 if len(inner_items) > 10 else len(inner_items)
        unique_items = ''.join(inner_items[:half])
        new_content = unique_items + unique_items
        head_and_header = head_and_header[:ticker_match.start(2)] + new_content + head_and_header[ticker_match.end(2):]

head_and_header = re.sub(r'<canvas[^>]*id=[\"\']bg-canvas[\"\'][^>]*>.*?</canvas>\s*', '', head_and_header)
head_and_header = head_and_header.replace('65 Tópicos', '68 Tópicos').replace('65 tópicos', '68 tópicos')

# Melhoria 1: Schema.org com aggregateRating e Product enriquecido
schema_enriquecido = '''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "ACERVO DIGITAL VIP - Acesso Vitalício",
    "description": "Repositório completo com 68 tópicos de cursos, drives, automações e ferramentas digitais no Telegram com liberação inteligente em 2 fases.",
    "brand": {
      "@type": "Brand",
      "name": "ACERVO DIGITAL VIP"
    },
    "image": "https://acervo-digital-vip.vercel.app/assets/mockup_3d_acervo_realista.webp",
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
  </script>'''

head_and_header = re.sub(r'<script\s+type=\"application/ld\+json\">[\s\S]*?</script>', schema_enriquecido, head_and_header)

# Seções originais por limites
sec_starts = [m.start() for m in re.finditer(r'<section\b', orig)]
sec_ends = [m.end() for m in re.finditer(r'</section>', orig)]

# 1. Hero (Sec 2) com data-track
sec_hero = orig[sec_starts[1]:sec_ends[1]]
sec_hero = sec_hero.replace('onclick="abrirModalPix()"', 'onclick="abrirModalPix()" data-track="cta_hero_comprar"')
sec_hero = sec_hero.replace('href="#catalogo"', 'href="#catalogo" data-track="cta_hero_ver_catalogo"')

# 2. 3 Benefícios (Sec 1)
sec_beneficios = orig[sec_starts[0]:sec_ends[0]]
sec_beneficios = re.sub(r'class=\"mb-16\s+-mt-6\"', 'class=\"mb-16 mt-4\"', sec_beneficios)

# 3. Catálogo (Sec 4) + blocos beleza & educacao
sec_catalogo = orig[sec_starts[3]:sec_ends[3]]
bloco_extra = orig[sec_ends[8]:sec_starts[9]].strip()

if "filtrarCategoria('beleza'" not in sec_catalogo:
    novos_botoes = '''
        <button onclick="filtrarCategoria('beleza', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-pink-500/50 hover:text-white">
          💅 Beleza & Práticas (4)
        </button>
        <button onclick="filtrarCategoria('educacao', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-indigo-500/50 hover:text-white">
          👶 Educação & Pais (7)
        </button>'''
    filtro_div_end = sec_catalogo.find('</div>\n\n      <!-- CONTEÚDO PRINCIPAL DO CATÁLOGO')
    if filtro_div_end != -1:
        sec_catalogo = sec_catalogo[:filtro_div_end] + novos_botoes + sec_catalogo[filtro_div_end:]

sec_catalogo = re.sub(r'onclick=\"filtrarCategoria\(\'([^\']+)\'\)\"', r'onclick="filtrarCategoria(\'\1\', this)"', sec_catalogo)

if 'data-cat="beleza"' not in sec_catalogo:
    last_div_cat = sec_catalogo.rfind('</div>')
    sec_catalogo = sec_catalogo[:last_div_cat] + '\n\n' + bloco_extra + '\n' + sec_catalogo[last_div_cat:]

sec_catalogo = re.sub(r'id=\"contador-busca\"[^>]*>93<', 'id="contador-busca" class="absolute right-3 top-3 text-[11px] text-zinc-500 font-bold">67<', sec_catalogo)
sec_catalogo = sec_catalogo.replace('Todos (93)', 'Todos (67)')

# 4. Ferramentas (Sec 10 consolidada)
sec_ferramentas = orig[sec_starts[9]:sec_ends[9]]
sec_ferramentas = re.sub(r'^<section[^>]*>', '<section class="mb-14 relative z-10" id="ferramentas">', sec_ferramentas)
sec_ferramentas = re.sub(r'<h2[^>]*>.*?</h2>', '<h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">Ferramentas, Bots & Softwares Inclusos</h2>', sec_ferramentas, flags=re.DOTALL)
sec_ferramentas = re.sub(r'<span class=\"px-3 py-1 rounded-full text-\[10px\].*?</span>', '<span class="px-3 py-1 rounded-full text-[11px] font-bold uppercase tracking-wider bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 mb-2 inline-block">🛠️ RECURSOS PRONTOS PARA USAR</span>', sec_ferramentas, flags=re.DOTALL)

# 5. Canais VIP (Sec 11)
sec_canais = orig[sec_starts[10]:sec_ends[10]]

# 6. Games (Sec 12) com abrirModalPixCurso
sec_games = orig[sec_starts[11]:sec_ends[11]]
console_names = {
    'Switch_library_bot': 'Nintendo Switch',
    'PS5_libr_bot': 'PlayStation 5',
    'PS4_libr_bot': 'PlayStation 4',
    'PS2_libr_bot': 'PlayStation 2',
    'PC_libr_bot': 'PC Games Steam',
    'Xbox360_library_bot': 'Xbox 360 & Clássico',
    'Oculus_library_bot': 'VR Oculus Quest',
    'PSP_libr_bot': 'PSP & PS Vita',
    'N3DS_library_bot': 'Nintendo 3DS / DS',
    'PSX_library_bot': 'PS1 & Retro Arcade'
}
for bot, cname in console_names.items():
    sec_games = re.sub(
        r'<a\s+href=\"https://t\.me/' + bot + r'\"[^>]*>',
        f'<a href="javascript:void(0)" onclick="abrirModalPixCurso(\'Biblioteca Gamer: {cname}\')" class="group glass-card p-4 rounded-2xl flex items-center justify-between border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all duration-300 cursor-pointer">',
        sec_games
    )

# 7. Livros Raros (Sec 13)
sec_livros = orig[sec_starts[12]:sec_ends[12]]

# 8. 68 Tópicos (Sec 14)
sec_topicos = orig[sec_starts[13]:sec_ends[13]]
sec_topicos = re.sub(r'^<section[^>]*>', '<section id="topicos" class="mt-16 mb-20 glass-panel rounded-3xl p-6 sm:p-10 border border-white/10 relative overflow-hidden shadow-2xl">', sec_topicos)
sec_topicos = sec_topicos.replace('65 Tópicos', '68 Tópicos').replace('65 tópicos', '68 tópicos')

# 9. Como Funciona (Sec 6)
sec_como_funciona = orig[sec_starts[5]:sec_ends[5]]

bloco_fases_seguranca = '''
      <!-- AVISO DE SEGURANÇA E PROTEÇÃO DO ACERVO: CRONOGRAMA EM 2 FASES (DIA 1 & DIA 8) -->
      <div class="mt-10 p-6 rounded-2xl bg-gradient-to-r from-emerald-950/30 via-black/60 to-emerald-950/30 border border-emerald-500/30 shadow-xl relative overflow-hidden">
        <div class="flex flex-col md:flex-row items-start md:items-center gap-5">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 flex items-center justify-center shrink-0 text-2xl shadow-inner">
            🛡️
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2 flex-wrap mb-1.5">
              <span class="text-[10px] font-black uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-500 text-black">Blindagem & Segurança</span>
              <h4 class="text-base sm:text-lg font-black text-white">Como Funciona a Liberação em 2 Fases (Dia 1 e 8º Dia)</h4>
            </div>
            <p class="text-xs sm:text-sm text-zinc-300 leading-relaxed mb-3">
              Para proteger nossa comunidade contra cópias piratas, robôs extratores e golpistas que compram apenas para baixar em massa e pedir reembolso, nosso sistema opera com liberação progressiva inteligente:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div class="p-3 rounded-xl bg-white/5 border border-white/5">
                <span class="font-bold text-emerald-400 block mb-0.5">⚡ Dia 1 (Imediato após Pix):</span>
                <span class="text-zinc-400">Acesso à Comunidade VIP Telegram, Microcursos de IA e Tráfego, Top Ferramentas e primeiros Packs de Prompts e PLRs.</span>
              </div>
              <div class="p-3 rounded-xl bg-white/5 border border-white/5">
                <span class="font-bold text-cyan-400 block mb-0.5">🔓 8º Dia (Liberação Total Irrestrita):</span>
                <span class="text-zinc-400">Desbloqueio completo dos 68 tópicos, downloads em massa, bibliotecas de emuladores e acervos de vídeos 4K.</span>
              </div>
            </div>
          </div>
        </div>
      </div>
'''
if 'Liberação em 2 Fases' not in sec_como_funciona:
    last_div_pos = sec_como_funciona.rfind('</div>')
    sec_como_funciona = sec_como_funciona[:last_div_pos] + bloco_fases_seguranca + '\n' + sec_como_funciona[last_div_pos:]

# 10. FAQ (Sec 7)
sec_faq = orig[sec_starts[6]:sec_ends[6]]

faq_item_fases = '''
        <!-- Item 6: Liberação em 2 Fases -->
        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
          <button onclick="toggleFaq(this)" class="w-full p-5 text-left flex items-center justify-between font-bold text-sm text-white hover:text-emerald-400 transition-colors">
            <span>6. Como funciona a liberação em 2 fases (Dia 1 e 8º Dia)?</span>
            <span class="faq-icon text-lg text-emerald-400 font-black transition-transform duration-300">+</span>
          </button>
          <div class="faq-content hidden px-5 pb-5 text-xs text-zinc-400 leading-relaxed border-t border-white/5 pt-3">
            No <strong>Dia 1</strong> (imediato após o Pix de R$ 9,90), você recebe acesso à Comunidade VIP no Telegram, Microcursos principais, ferramentas de IA e packs essenciais para começar a produzir no mesmo minuto. No <strong>8º dia</strong> (após o término do período de garantia legal de 7 dias do CDC), nosso sistema libera o download massivo e irrestrito de todos os 68 tópicos, acervos pesados de 4K e bibliotecas inteiras de emuladores. Isso garante a sustentabilidade e velocidade dos nossos servidores para quem realmente é membro fiel!
          </div>
        </div>
'''
if 'Liberação em 2 Fases' not in sec_faq:
    # Inserir antes do último fechamento de div dentro do container de FAQ
    last_div_faq = sec_faq.rfind('</div>\n    </section>')
    if last_div_faq == -1:
        last_div_faq = sec_faq.rfind('</div>')
    sec_faq = sec_faq[:last_div_faq] + faq_item_fases + '\n' + sec_faq[last_div_faq:]

# 11. Destaques / Garantia (Sec 8)
sec_destaques = orig[sec_starts[7]:sec_ends[7]]

# 12. Checkout Final (Sec 9) com data-track
sec_checkout = orig[sec_starts[8]:sec_ends[8]]
sec_checkout = sec_checkout.replace('65 tópicos', '68 tópicos').replace('65 Tópicos', '68 Tópicos')
sec_checkout = sec_checkout.replace('onclick="abrirModalPix()"', 'onclick="abrirModalPix()" data-track="cta_checkout_final"')

# Footer e Modais
pos_main_close = orig.find('</main>', sec_ends[13])
pos_footer = orig.find('<footer')
pos_footer_close = orig.find('</footer>')

modals_and_widgets = orig[pos_main_close+7:pos_footer].strip()
footer_html = orig[pos_footer:pos_footer_close+9]

# Adicionar link do painel no rodapé
footer_html = footer_html.replace(
    'Suporte via Telegram (@AcervoDigitalVIP_bot)</a>',
    'Suporte via Telegram (@AcervoDigitalVIP_bot)</a>\n        <span>•</span>\n        <a href="/painel/" class="hover:text-emerald-400 transition-colors flex items-center gap-1"><span>🔐</span> Painel</a>'
)

# Aprimorar Modal Pix com abas Chave Copia e Cola / QR Code
bloco_pix_tabs = '''<!-- SELETOR DE PAGAMENTO PIX (CHAVE COPIA E COLA / QR CODE) -->
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
          <p class="text-[11px] text-zinc-400">Abra o app do seu banco e aponte a câmera para a chave telefone.</p>
        </div>
        
        <div class="mt-2.5 text-[10px] text-emerald-400 flex items-center justify-center gap-1 font-semibold">
          <span>🛡️</span> Acesso imediato no Dia 1 + Desbloqueio dos 68 tópicos no 8º dia
        </div>
      </div>'''

modals_and_widgets = re.sub(
    r'<div class=\"bg-black/80 rounded-2xl p-4 border border-white/10 my-4 text-left\">.*?</div>\s*</div>',
    bloco_pix_tabs,
    modals_and_widgets,
    flags=re.DOTALL
)

# Adicionar Barra Flutuante de CTA (Sticky Mobile CTA)
sticky_bar_html = '''
  <!-- BARRA FLUTUANTE DE CTA (STICKY CONVERSÃO RÁPIDA) -->
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
'''
modals_and_widgets += sticky_bar_html

# Script 1: Canvas Aurora
script1_start = orig.find('// Shader de Fundo Leve com Canvas 2D')
script1_end = orig.find('</script>', script1_start)
script1_body = orig[script1_start:script1_end]

# Adicionar pausa de render quando documento oculto no canvas
script1_body = script1_body.replace(
    'requestAnimationFrame(draw);',
    '''if (!document.hidden) {
        requestAnimationFrame(draw);
      } else {
        setTimeout(() => requestAnimationFrame(draw), 1000);
      }'''
)

# Script 2 Refatorado
script2_body = """
    // 1. Contador Regressivo de Urgência (Persistente em Sessão)
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

    // 2. Busca Instantânea de Cursos
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

    // 3. Filtro por Categorias (com passagem de this/btnElement)
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

    // 4. Modal Pix (Geral e Específico por Curso)
    function abrirModalPix(nomeCurso) {
      const modal = document.getElementById('modal-pix');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        const tit = modal.querySelector('h3');
        if (tit) {
          tit.textContent = nomeCurso ? ('Destrave: ' + nomeCurso) : 'Acesso Completo ao Acervo Digital VIP';
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

    // 5. Funções de Widget e Popup Ninja
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

    // 6. Fechamento por Backdrop e Tecla Escape
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

    // 7. Acordeão de FAQ
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

    // 8. Copiar Chave Pix
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

    // 9. Alternância de Abas no Modal Pix (Chave / QR Code)
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

    // 10. Barra Flutuante de Conversão (Sticky CTA ao rolar)
    const stickyCta = document.getElementById('sticky-cta-bar');
    window.addEventListener('scroll', () => {
      if (!stickyCta) return;
      if (window.scrollY > 420) {
        stickyCta.classList.remove('translate-y-full');
      } else {
        stickyCta.classList.add('translate-y-full');
      }
    }, { passive: true });

    // 11. Notificação Social de Compras Recentes
    const compradores = [
      { nome: 'Carlos M. de São Paulo', curso: 'liberou os 68 Tópicos VIP', tempo: 'há 1 min' },
      { nome: 'Mariana R. de Belo Horizonte', curso: 'liberou Pack de Ferramentas IA', tempo: 'há 3 min' },
      { nome: 'Rodrigo P. de Salvador', curso: 'liberou Acervo de Vídeos Virais 4K', tempo: 'há 4 min' },
      { nome: 'Fernanda L. de Curitiba', curso: 'liberou a Formação Lovable & Make', tempo: 'há 2 min' },
      { nome: 'Guilherme B. de Brasília', curso: 'liberou a Biblioteca Gamer & Emuladores', tempo: 'há 5 min' },
      { nome: 'Larissa T. de Fortaleza', curso: 'liberou Super Pack de Prompts IA', tempo: 'há 6 min' }
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
"""

# Montagem do arquivo final
novo_conteudo = f"""{head_and_header}
    {sec_hero}

    {sec_beneficios}

    {sec_catalogo}

    {sec_ferramentas}

    {sec_canais}

    {sec_games}

    {sec_livros}

    {sec_topicos}

    {sec_como_funciona}

    {sec_faq}

    {sec_destaques}

    {sec_checkout}
  </main>

  {footer_html}

  {modals_and_widgets}

  <!-- Scripts Interativos -->
  <script>
{script1_body}
  </script>

  <script>
{script2_body}
  </script>
</body>
</html>
"""

with open('/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html', 'w', encoding='utf-8') as f:
    f.write(novo_conteudo)

print('Arquivo index.html gerado com sucesso via script python dedicado!')
