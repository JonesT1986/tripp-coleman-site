(() => {
  const PHONE = '306-209-8861', PHONE_E164 = '+13062098861', EMAIL = 'trippmagic317@gmail.com';

  /* analytics: fires GA4 or Plausible events when either is installed */
  function track(name, params) {
    try { if (window.gtag) window.gtag('event', name, params || {}); } catch (e) {}
    try { if (window.plausible) window.plausible(name, { props: params || {} }); } catch (e) {}
  }
  document.addEventListener('click', e => {
    const a = e.target.closest('a');
    if (!a) return;
    const h = a.getAttribute('href') || '';
    if (h.startsWith('tel:')) track('click_call', { location: a.closest('header,footer,.mobile-bar,main')?.tagName.toLowerCase() || 'page' });
    else if (h.startsWith('mailto:')) track('click_email');
    else if (/gigsalad|agnt\.com/.test(h)) track('click_booking_platform', { platform: h.includes('agnt') ? 'agnt' : 'gigsalad' });
  });

  /* header */
  const top = document.getElementById('top'), menuBtn = document.getElementById('menuBtn');
  const onScroll = () => top && top.classList.toggle('solid', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  menuBtn && menuBtn.addEventListener('click', () => { const o = top.classList.toggle('open'); menuBtn.setAttribute('aria-expanded', o); });
  document.querySelectorAll('#nav a').forEach(a => a.addEventListener('click', () => { top.classList.remove('open'); menuBtn && menuBtn.setAttribute('aria-expanded', false); }));
  const yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* copy buttons */
  document.querySelectorAll('.copy').forEach(b => b.addEventListener('click', () => {
    const v = b.dataset.copy;
    const done = t => { b.textContent = t; setTimeout(() => b.textContent = 'Copy', 1600); };
    if (navigator.clipboard) navigator.clipboard.writeText(v).then(() => done('Copied')).catch(() => done('Press Ctrl+C'));
  }));

  /* booking form: posts to Formspree, which emails the request to Tripp */
  const FORMSPREE_URL = 'https://formspree.io/f/xwlvgywd';
  const form = document.getElementById('bookForm');
  if (!form) return;
  const err = document.getElementById('bErr');
  const btn = form.querySelector('button[type="submit"]');
  form.addEventListener('submit', async e => {
    e.preventDefault();
    err.textContent = '';
    const fd = new FormData(form);
    const d = Object.fromEntries(fd);
    if (!d.name.trim()) { err.textContent = 'Add your name so Tripp knows who to reply to.'; form.bName.focus(); return; }
    if (!/^\S+@\S+\.\S+$/.test(d.email)) { err.textContent = 'Enter an email address like you@example.com.'; form.bEmail.focus(); return; }
    if (d._gotcha) return; // honeypot: bots only
    fd.append('_subject', `Booking request: ${d.type}${d.date ? ' on ' + d.date : ''}`);
    fd.append('_replyto', d.email);
    const label = btn.innerHTML;
    btn.disabled = true; btn.textContent = 'Sending...';
    try {
      const r = await fetch(FORMSPREE_URL, { method: 'POST', body: fd, headers: { Accept: 'application/json' } });
      if (!r.ok) throw new Error('bad status ' + r.status);
      track('generate_lead', { event_type: d.type });
      form.innerHTML = `<div class="done"><h3>Request sent. Thank you!</h3>
        <p>Tripp got your booking request and will reply to ${d.email.replace(/[<>&"]/g, '')} personally. For a faster answer, call or text ${PHONE}.</p></div>`;
    } catch (ex) {
      btn.disabled = false; btn.innerHTML = label;
      err.textContent = `Sorry, that didn't send. Please try again or call or text ${PHONE}.`;
    }
  });
})();
