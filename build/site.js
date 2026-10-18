(() => {
  const PHONE = '306-209-8861', PHONE_E164 = '+13062098861', EMAIL = 'timcoleman777@gmail.com';

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

  /* booking form: opens the visitor's email or text app with the request filled in */
  const form = document.getElementById('bookForm');
  if (!form) return;
  const err = document.getElementById('bErr');
  form.addEventListener('submit', e => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    if (!d.name.trim()) { err.textContent = 'Add your name so Tripp knows who to reply to.'; form.bName.focus(); return; }
    if (!/^\S+@\S+\.\S+$/.test(d.email)) { err.textContent = 'Enter an email address like you@example.com.'; form.bEmail.focus(); return; }
    const lines = [`Booking request for Tripp Coleman`, ``, `Name: ${d.name}`, `Email: ${d.email}`];
    if (d.phone) lines.push(`Phone: ${d.phone}`);
    lines.push(`Event: ${d.type}`);
    if (d.date) lines.push(`Date: ${d.date}`);
    if (d.guests) lines.push(`Guests: ${d.guests}`);
    if (d.city) lines.push(`Where: ${d.city}`);
    if (d.message) lines.push('', d.message);
    const text = lines.join('\n');
    const subject = `Booking request: ${d.type}${d.date ? ' on ' + d.date : ''}`;
    const mailto = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(text)}`;
    const sms = `sms:${PHONE_E164}?&body=${encodeURIComponent(text)}`;
    track('generate_lead', { event_type: d.type });
    form.innerHTML = `<div class="done"><h3>Almost done: send it to Tripp.</h3>
      <p>Your email app should open with the request filled in. Press send there. If it didn't open, use a button below or copy the text.</p>
      <pre id="reqText"></pre>
      <div class="ctas"><a class="btn btn-primary" href="${mailto}">Email to Tripp</a><a class="btn btn-ghost" href="${sms}">Text to Tripp</a><button type="button" class="btn btn-ghost" id="copyReq">Copy request</button></div>
      <p>Or call ${PHONE}.</p></div>`;
    document.getElementById('reqText').textContent = text;
    document.getElementById('copyReq').addEventListener('click', ev => {
      const b = ev.currentTarget;
      navigator.clipboard.writeText(text).then(() => { b.textContent = 'Copied'; }).catch(() => {
        const r = document.createRange(); r.selectNodeContents(document.getElementById('reqText'));
        const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Selected, press copy';
      });
    });
    location.href = mailto;
  });
})();
