import re

file_path = "/home/daviemari/.gemini/antigravity/scratch/acervo-digital-vip/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. FAVICON & THEME-COLOR NO <HEAD>
favicon_theme = """  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
  <meta name="theme-color" content="#06070a">
  <meta name="color-scheme" content="dark">"""

content = content.replace('  <meta name="color-scheme" content="dark">', favicon_theme, 1)

# 2. BOTAO FILTRO EDUCACAO
old_btn = """<button onclick="filtrarCategoria('educacao', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-indigo-500/50 hover:text-white">
          👶 Educação & Pais (7)
        </button>"""
new_btn = """<button onclick="filtrarCategoria('educacao', this)" class="btn-categoria px-4 py-2 rounded-xl font-bold border transition-all whitespace-nowrap bg-white/5 text-zinc-300 border-white/10 hover:border-indigo-500/50 hover:text-white">
          🎓 Concursos, Idiomas & Tech (7)
        </button>"""
content = content.replace(old_btn, new_btn)

# 3. CONTAINER DE BUSCA VAZIA
empty_state_html = """      <!-- Estado Vazio da Busca -->
      <div id="busca-vazia" class="hidden py-12 px-6 rounded-2xl border border-white/10 bg-black/40 text-center max-w-lg mx-auto my-8">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-2xl mx-auto mb-3">
          🔍
        </div>
        <h4 class="text-base font-bold text-white mb-1">Nenhum curso encontrado</h4>
        <p class="text-xs text-zinc-400 mb-4 leading-relaxed">Não encontrou o que procurava? Peça o curso diretamente no nosso Bot VIP ou limpe os filtros para navegar.</p>
        <div class="flex items-center justify-center gap-2">
          <button onclick="limparBusca()" class="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white text-xs font-bold transition-all">
            Limpar Busca
          </button>
          <a href="https://t.me/AcervoDigitalVIP_bot" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-black text-xs font-bold transition-all">
            Pedir no Bot VIP ➜
          </a>
        </div>
      </div>
"""
# Inserir antes de <!-- FILEIRAS DO CATÁLOGO -->
content = content.replace("      <!-- FILEIRAS DO CATÁLOGO -->", empty_state_html + "\n      <!-- FILEIRAS DO CATÁLOGO -->")

# 4. WIDGET OFERTA VIP (restringir a telas grandes xl e esconder quando sticky aparecer)
content = re.sub(
    r'<div id="widget-oferta-vip" class="fixed bottom-6 right-5 z-40 flex flex-col items-end gap-2 transition-all duration-300">',
    '<div id="widget-oferta-vip" class="fixed bottom-6 right-5 z-40 hidden xl:flex flex-col items-end gap-2 transition-all duration-300">',
    content
)

# 5. TOAST SOCIAL (adicionar hidden sm:block e id="toast-social-tempo")
old_toast = """  <!-- TOAST SOCIAL DE COMPRAS -->
  <div id="toast-social" class="fixed bottom-6 left-5 z-40 transform translate-y-32 opacity-0 transition-all duration-500 pointer-events-none">
    <div class="glass-panel py-2.5 px-3.5 rounded-xl border border-emerald-500/30 bg-black/90 shadow-2xl flex items-center gap-2.5 max-w-xs text-xs">
      <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></div>
      <div class="truncate">
        <span id="toast-social-nome" class="text-white text-[11px] block truncate">Carlos M. de São Paulo</span>
      </div>
      <span class="text-[10px] text-zinc-400 shrink-0">• há 2 min</span>
    </div>
  </div>"""

new_toast = """  <!-- TOAST SOCIAL DE COMPRAS -->
  <div id="toast-social" class="fixed bottom-6 left-5 z-40 transform translate-y-32 opacity-0 transition-all duration-500 pointer-events-none hidden sm:block">
    <div class="glass-panel py-2.5 px-3.5 rounded-xl border border-emerald-500/30 bg-black/90 shadow-2xl flex items-center gap-2.5 max-w-xs text-xs">
      <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></div>
      <div class="truncate">
        <span id="toast-social-nome" class="text-white text-[11px] block truncate">Carlos M. de São Paulo</span>
      </div>
      <span id="toast-social-tempo" class="text-[10px] text-zinc-400 shrink-0">• há 2 min</span>
    </div>
  </div>"""

content = content.replace(old_toast, new_toast)

# 6. SCRIPT: LIMPAR TIMER ORFÃO, AJUSTAR MOSTRAR TOAST SOCIAL, ADICIONAR LIMPARBUSCA E EXIT-INTENT NINJA
old_script_block = """    // 2. Contador Regressivo de Urgência (Persistente em Sessão)
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
    setInterval(atualizarTimer, 1000);"""

new_script_block = """    // 2. Funções Auxiliares de Navegação
    function limparBusca() {
      const input = document.getElementById('input-busca');
      if (input) {
        input.value = '';
        filtrarCursos();
      }
    }"""
content = content.replace(old_script_block, new_script_block)

# 7. FILTRAR CURSOS: ATUALIZAR ESTADO VAZIO
old_filtrar = """    // 3. Busca Instantânea de Cursos
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
    }"""

new_filtrar = """    // 3. Busca Instantânea de Cursos
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

      const emptyState = document.getElementById('busca-vazia');
      if (emptyState) {
        if (visiveis === 0 && termo.length > 0) {
          emptyState.classList.remove('hidden');
        } else {
          emptyState.classList.add('hidden');
        }
      }
    }"""
content = content.replace(old_filtrar, new_filtrar)

# 8. ATUALIZAR ATUALIZARSTICKYBAR PARA ESCONDER WIDGET OFERTA EM SCREENS GRANDES
old_sticky = """    function atualizarStickyBar() {
      if (!stickyBar) return;
      if (window.scrollY > 500 && !checkoutOrFooterVisible) {
        stickyBar.classList.remove('translate-y-full');
      } else {
        stickyBar.classList.add('translate-y-full');
      }
    }"""

new_sticky = """    function atualizarStickyBar() {
      if (!stickyBar) return;
      const widgetOferta = document.getElementById('widget-oferta-vip');
      if (window.scrollY > 500 && !checkoutOrFooterVisible) {
        stickyBar.classList.remove('translate-y-full');
        if (widgetOferta) widgetOferta.classList.add('opacity-0', 'pointer-events-none');
      } else {
        stickyBar.classList.add('translate-y-full');
        if (widgetOferta) widgetOferta.classList.remove('opacity-0', 'pointer-events-none');
      }
    }"""
content = content.replace(old_sticky, new_sticky)

# 9. ATUALIZAR MOSTRAR TOAST SOCIAL
old_toast_fn = """    function mostrarToastSocial() {
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
    }"""

new_toast_fn = """    function mostrarToastSocial() {
      const toast = document.getElementById('toast-social');
      const nomeEl = document.getElementById('toast-social-nome');
      const tempoEl = document.getElementById('toast-social-tempo');
      if (!toast || !nomeEl) return;

      const comp = compradores[compIdx % compradores.length];
      compIdx++;
      nomeEl.innerHTML = `<strong>${comp.nome}</strong> • <span class="text-emerald-400">${comp.curso}</span>`;
      if (tempoEl) tempoEl.textContent = '• ' + comp.tempo;

      toast.classList.remove('translate-y-32', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-32', 'opacity-0');
      }, 4500);
    }"""
content = content.replace(old_toast_fn, new_toast_fn)

# 10. GATILHO INTELIGENTE DE INTENÇÃO DE SAÍDA (EXIT-INTENT)
exit_intent_code = """
    // 13. Gatilho de Intenção de Saída no Desktop (Exit-Intent Popup Ninja)
    document.addEventListener('mouseleave', function(e) {
      if (e.clientY <= 0 && window.innerWidth >= 768) {
        const modalPix = document.getElementById('modal-pix');
        const pixAberto = modalPix && !modalPix.classList.contains('hidden');
        const jaExibido = sessionStorage.getItem('ninja_popup_shown');
        if (!pixAberto && !jaExibido) {
          sessionStorage.setItem('ninja_popup_shown', 'true');
          abrirModalPopupNinja();
        }
      }
    });
"""
content = content.replace("  </script>\n</body>", exit_intent_code + "  </script>\n</body>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Todas as correções cirúrgicas foram aplicadas com sucesso!")
