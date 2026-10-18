(() => {
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
/* ---------- card texture painter (shared by 3D scene) ---------- */
function paintCard(kind, rank, suit){
  const c = document.createElement('canvas'); c.width = 256; c.height = 358;
  const g = c.getContext('2d'); const r = 18;
  g.beginPath(); g.roundRect ? g.roundRect(0,0,256,358,r) : g.rect(0,0,256,358); g.closePath();
  if (kind === 'back'){
    g.fillStyle = '#f6efe3'; g.fill();
    g.save(); g.beginPath(); g.rect(12,12,232,334); g.clip();
    g.fillStyle = '#b8352c'; g.fillRect(12,12,232,334);
    g.strokeStyle = 'rgba(255,255,255,.18)'; g.lineWidth = 2;
    for (let i=-400;i<400;i+=13){ g.beginPath(); g.moveTo(i,0); g.lineTo(i+358,358); g.stroke(); g.beginPath(); g.moveTo(i+358,0); g.lineTo(i,358); g.stroke(); }
    g.restore();
    g.strokeStyle = '#f6efe3'; g.lineWidth = 3; g.strokeRect(26,26,204,306);
    g.fillStyle = '#f6efe3'; g.font = 'italic 64px "Bodoni Moda", Georgia, serif'; g.textAlign='center'; g.textBaseline='middle';
    g.fillText('TC', 128, 182);
  } else {
    g.fillStyle = '#f6efe3'; g.fill();
    const red = suit === '♥' || suit === '♦';
    g.fillStyle = red ? '#b0282a' : '#1b1512';
    g.textAlign='center'; g.textBaseline='middle';
    g.font = '500 46px "Bodoni Moda", Georgia, serif'; g.fillText(rank, 34, 40);
    g.font = '36px Georgia, serif'; g.fillText(suit, 34, 84);
    g.save(); g.translate(222,318); g.rotate(Math.PI);
    g.font = '500 46px "Bodoni Moda", Georgia, serif'; g.fillText(rank, 0, 0);
    g.font = '36px Georgia, serif'; g.fillText(suit, 0, 44); g.restore();
    g.font = (rank === 'A' ? '150px' : '120px') + ' Georgia, serif'; g.fillText(suit, 128, 186);
  }
  return c;
}

/* ---------- 3D stage ---------- */
function initStage(){
  const canvas = document.getElementById('stage'), hero = document.getElementById('home');
  let renderer;
  try { renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:false, powerPreference:'high-performance'}); }
  catch(e){ document.documentElement.classList.add('no-webgl'); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0x0d0a09, 1);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, .1, 60);
  camera.position.set(0, 0, 7);

  const loader = new THREE.TextureLoader();
  const tex = loader.load('/img/tripp.webp');
  [tex].forEach(t => { t.minFilter = THREE.LinearFilter; t.generateMipmaps = false; });

  /* smoky backdrop */
  const fog = new THREE.Mesh(new THREE.PlaneGeometry(30, 18), new THREE.ShaderMaterial({
    uniforms:{uTime:{value:0}, uSpot:{value:new THREE.Vector2(.68,.55)}},
    vertexShader:`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.); }`,
    fragmentShader:`
      varying vec2 vUv; uniform float uTime; uniform vec2 uSpot;
      float h(vec2 p){ return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453); }
      float n(vec2 p){ vec2 i=floor(p), f=fract(p); f=f*f*(3.-2.*f);
        return mix(mix(h(i),h(i+vec2(1,0)),f.x), mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x), f.y); }
      float fbm(vec2 p){ float v=0., a=.5; for(int i=0;i<5;i++){ v+=a*n(p); p*=2.03; a*=.5; } return v; }
      void main(){
        vec2 p = vUv*vec2(5.,3.);
        float t = uTime*.035;
        float s = fbm(p + vec2(t, -t*.6) + fbm(p*1.7 - t)*1.4);
        vec3 col = vec3(.051,.039,.035);
        col += vec3(.30,.07,.05) * smoothstep(.45,.95,s) * .55;
        float d = distance(vUv*vec2(1.6,1.), uSpot*vec2(1.6,1.));
        col += vec3(.84,.69,.48) * pow(max(0.,1.-d*1.9), 2.6) * .30;
        col += vec3(.84,.69,.48) * smoothstep(.55,1.,s) * pow(max(0.,1.-d*1.3),2.) * .18;
        gl_FragColor = vec4(col,1.);
      }`
  }));
  fog.position.z = -6; scene.add(fog);

  /* 3D Tripp: displaced, depth-shaded, rim-lit, with a dissolve-in */
  const H = 3.25, W = H * 625 / 1100;
  const rig = new THREE.Group(); scene.add(rig);
  const body = new THREE.Group(); rig.add(body);
  const trippMat = new THREE.ShaderMaterial({
    transparent:true, side:THREE.DoubleSide,
    uniforms:{ map:{value:tex}, uAmp:{value:0}, uReveal:{value: REDUCED ? 1.3 : 0}, uTime:{value:0}, uLight:{value:new THREE.Vector2(.6,.2)} },
    vertexShader:`
      uniform float uAmp; varying vec2 vUv; varying float vD;
      void main(){ vUv=uv; float d=0.; vD=d;
        vec3 p=position; p.z += d*uAmp;
        gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.); }`,
    fragmentShader:`
      uniform sampler2D map; uniform float uReveal, uTime; uniform vec2 uLight;
      varying vec2 vUv; varying float vD;
      float h(vec2 p){ return fract(sin(dot(p,vec2(12.9898,78.233)))*43758.5453); }
      float n(vec2 p){ vec2 i=floor(p), f=fract(p); f=f*f*(3.-2.*f);
        return mix(mix(h(i),h(i+vec2(1,0)),f.x), mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x), f.y); }
      void main(){
        vec4 c = texture2D(map, vUv);
        if (c.a < .35) discard;
        float nz = n(vUv*vec2(14.,24.))*.55 + n(vUv*vec2(40.,70.))*.25;
        float edge = uReveal*1.35 - ((1.-vUv.y)*.8 + nz);
        if (edge < 0.) discard;
        vec2 o = vec2(.012, .007);
        float aL = texture2D(map, vUv-vec2(o.x,0.)).a, aR = texture2D(map, vUv+vec2(o.x,0.)).a;
        float aD = texture2D(map, vUv-vec2(0.,o.y)).a, aU = texture2D(map, vUv+vec2(0.,o.y)).a;
        vec2 outward = vec2(aL-aR, aD-aU);
        float rim = clamp(dot(outward, normalize(uLight)), 0., 1.);
        vec3 col = c.rgb;
        vec3 rimCol = mix(vec3(.85,.25,.18), vec3(.95,.78,.52), step(0., uLight.x));
        col += rimCol * rim * .45;
        col += vec3(.95,.72,.42) * smoothstep(.09, 0., edge) * 1.6;
        gl_FragColor = vec4(col, smoothstep(.0, .2, vUv.y));
      }`
  });
  const tripp = new THREE.Mesh(new THREE.PlaneGeometry(W, H, 1, 1), trippMat);
  body.add(tripp);

  /* spotlight halo behind him */
  const halo = (() => { const c=document.createElement('canvas'); c.width=c.height=256; const g=c.getContext('2d');
    const gr=g.createRadialGradient(128,128,0,128,128,128); gr.addColorStop(0,'rgba(214,176,122,.55)'); gr.addColorStop(.4,'rgba(184,53,44,.18)'); gr.addColorStop(1,'rgba(0,0,0,0)');
    g.fillStyle=gr; g.fillRect(0,0,256,256); return new THREE.CanvasTexture(c); })();
  const haloMesh = new THREE.Mesh(new THREE.PlaneGeometry(5.2,5.2), new THREE.MeshBasicMaterial({map:halo, transparent:true, depthWrite:false, blending:THREE.AdditiveBlending}));
  haloMesh.position.set(0,.5,-1.2); rig.add(haloMesh);

  /* card textures */
  const back = new THREE.CanvasTexture(paintCard('back'));
  const faces = [['A','♥'],['A','♠'],['K','♦'],['Q','♣'],['7','♥'],['J','♠'],['A','♦'],['10','♣']]
    .map(([r,s]) => new THREE.CanvasTexture(paintCard('face', r, s)));
  function makeCard(faceTex, w){
    const g = new THREE.Group(), geo = new THREE.PlaneGeometry(w, w*1.4);
    const f = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({map:faceTex, transparent:true}));
    const b = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({map:back, transparent:true}));
    b.rotation.y = Math.PI; g.add(f, b); return g;
  }

  /* the levitating ace between his hands */
  const handPos = new THREE.Vector3((0.517-.5)*W, (.5-0.56)*H, .62);
  const ace = makeCard(faces[0], .3); ace.position.copy(handPos); body.add(ace);
  const glow = new THREE.Mesh(new THREE.PlaneGeometry(1.1,1.1), new THREE.MeshBasicMaterial({map:halo, transparent:true, depthWrite:false, blending:THREE.AdditiveBlending}));
  glow.position.copy(handPos).add(new THREE.Vector3(0,0,-.08)); body.add(glow);

  /* orbiting ring of cards */
  const ring = new THREE.Group(); ring.rotation.set(.32, 0, -.12); ring.position.y = -.1; rig.add(ring);
  const N = 14, ringCards = [];
  for (let i=0;i<N;i++){
    const c = makeCard(faces[i % faces.length], .26);
    c.userData = { a: i/N*Math.PI*2, spin: (Math.random()*.6+.3)*(Math.random()<.5?-1:1), wob: Math.random()*6.28, start: new THREE.Vector3((Math.random()-.5)*14, (Math.random()-.5)*8, 4+Math.random()*3) };
    ring.add(c); ringCards.push(c);
  }

  /* gold dust */
  const P = 700, pos = new Float32Array(P*3), seed = new Float32Array(P);
  for (let i=0;i<P;i++){ pos[i*3]=(Math.random()-.5)*12; pos[i*3+1]=(Math.random()-.5)*7; pos[i*3+2]=(Math.random()-.5)*5; seed[i]=Math.random(); }
  const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.BufferAttribute(pos,3)); pg.setAttribute('seed', new THREE.BufferAttribute(seed,1));
  const dust = new THREE.Points(pg, new THREE.ShaderMaterial({
    transparent:true, depthWrite:false, blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0}, uPR:{value:renderer.getPixelRatio()}},
    vertexShader:`attribute float seed; uniform float uTime, uPR; varying float vA;
      void main(){ vec3 p=position; p.y = mod(p.y + uTime*(.08+seed*.18) + 3.5, 7.) - 3.5; p.x += sin(uTime*.3+seed*30.)*.15;
        vec4 mv = modelViewMatrix*vec4(p,1.); gl_Position = projectionMatrix*mv;
        vA = .35 + .65*abs(sin(uTime*(1.+seed*2.)+seed*20.));
        gl_PointSize = (1.4 + seed*3.2) * uPR * (6./-mv.z); }`,
    fragmentShader:`varying float vA; void main(){ float d=length(gl_PointCoord-.5); if(d>.5) discard;
      gl_FragColor = vec4(vec3(.95,.76,.48), vA*smoothstep(.5,0.,d)); }`
  }));
  scene.add(dust);

  /* layout */
  let mobile = false;
  function resize(){
    const w = hero.clientWidth, h = hero.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w/h; camera.updateProjectionMatrix();
    mobile = w < 820;
    const visH = 2*camera.position.z*Math.tan(THREE.MathUtils.degToRad(camera.fov/2));
    const visW = visH*camera.aspect;
    if (mobile){ rig.scale.setScalar(Math.min(.95, visW/3.6)); rig.position.set(0, visH*.5 - H*rig.scale.y*.5 - .35, 0); fog.material.uniforms.uSpot.value.set(.5,.72); }
    else { rig.scale.setScalar(Math.min(1.05, visH/3.9)); rig.position.set(Math.min(visW*.24, 2.4), -.08, 0); fog.material.uniforms.uSpot.value.set(.5 + rig.position.x/30, .55); }
  }
  new ResizeObserver(resize).observe(hero); resize();

  /* interaction */
  let tx=0, ty=0, cx=0, cy=0, dragY=0, dragV=0, dragging=false, lastX=0, moved=0, burst=0;
  hero.addEventListener('pointermove', e => {
    const r = hero.getBoundingClientRect();
    tx = ((e.clientX-r.left)/r.width - .5)*2; ty = ((e.clientY-r.top)/r.height - .5)*2;
    if (dragging){ const dx = e.clientX-lastX; dragV = dx*.006; dragY += dragV; moved += Math.abs(dx); lastX = e.clientX; }
  });
  canvas.addEventListener('pointerdown', e => { dragging = true; moved = 0; lastX = e.clientX; canvas.classList.add('drag'); canvas.setPointerCapture(e.pointerId); });
  const end = () => { if (dragging && moved < 6) burst = 1; dragging = false; canvas.classList.remove('drag'); };
  canvas.addEventListener('pointerup', end); canvas.addEventListener('pointercancel', end);

  let visible = true;
  new IntersectionObserver(([en]) => { visible = en.isIntersecting; if (visible && !REDUCED) loop(); }).observe(hero);

  const clock = new THREE.Clock(); let t0 = null, running = false;
  function frame(){
    const t = clock.getElapsedTime(); if (t0 === null) t0 = t; const lt = t - t0;
    const intro = REDUCED ? 1 : Math.min(1, lt/2.6);
    const ease = 1 - Math.pow(1-intro, 3);
    trippMat.uniforms.uReveal.value = REDUCED ? 1.3 : ease*1.3;
    trippMat.uniforms.uTime.value = t; fog.material.uniforms.uTime.value = t; dust.material.uniforms.uTime.value = t;

    cx += (tx-cx)*.05; cy += (ty-cy)*.05;
    if (!dragging){ dragV *= .94; dragY += dragV; dragY *= .995; }
    const sway = Math.sin(t*.5)*.08;
    void sway;
    trippMat.uniforms.uLight.value.set(-cx || .6, .25 - cy*.3);

    const aceIn = THREE.MathUtils.smoothstep(lt, 1.8, 2.8);
    ace.scale.setScalar(REDUCED ? 1 : aceIn);
    ace.position.y = handPos.y + Math.sin(t*1.6)*.06;
    ace.rotation.y = t*1.4; ace.rotation.z = Math.sin(t*.8)*.15;
    glow.material.opacity = (.7 + Math.sin(t*3)*.25) * (REDUCED ? 1 : aceIn);
    glow.position.y = ace.position.y;

    burst *= .955;
    ring.rotation.y = t*.22 + dragY*2.5 + cx*.3; ring.rotation.x = .32 + cy*.08;
    ringCards.forEach((c, i) => {
      const u = c.userData, rad = 1.75 + burst*2.4 + Math.sin(t*.7+u.wob)*.08;
      const target = new THREE.Vector3(Math.cos(u.a)*rad, Math.sin(t*.9+u.wob)*.22 + burst*Math.sin(u.a*3)*.8, Math.sin(u.a)*rad);
      if (REDUCED) c.position.copy(target); else c.position.lerpVectors(u.start, target, ease);
      c.rotation.y = -u.a + Math.PI/2 + t*u.spin; c.rotation.x = Math.sin(t+u.wob)*.3 + burst*u.spin*3;
    });
    dust.rotation.y = cx*.05;
    
    renderer.render(scene, camera);
  }
  function loop(){ if (running) return; running = true;
    (function tick(){ if (!visible || document.hidden){ running = false; return; } frame(); requestAnimationFrame(tick); })(); }
  document.addEventListener('visibilitychange', () => { if (!document.hidden && visible && !REDUCED) loop(); });
  if (REDUCED){ let n=0; (function few(){ frame(); if (++n<20) requestAnimationFrame(few); })(); }
  else loop();
}
if (window.THREE) { if (document.fonts && document.fonts.load) document.fonts.load('400 40px "Bodoni Moda"').finally(initStage); else initStage(); }
else document.documentElement.classList.add('no-webgl');

/* ---------- the trick ---------- */
const S = {s:'♠', h:'♥', d:'♦', c:'♣'};
const SET_A = [['K','s'],['Q','h'],['J','d'],['K','c'],['Q','s'],['J','h']];
const SET_B = [['K','h'],['Q','c'],['J','s'],['K','d'],['Q','d']];
const table = document.getElementById('table'), step = document.getElementById('trickStep'), btn = document.getElementById('trickBtn');
function cardEl([r,s]){
  const red = s==='h'||s==='d', el = document.createElement('div'); el.className='pc';
  el.setAttribute('role','img'); el.setAttribute('aria-label', `${({K:'King',Q:'Queen',J:'Jack'})[r]} of ${({s:'spades',h:'hearts',d:'diamonds',c:'clubs'})[s]}`);
  el.innerHTML = `<div class="f${red?' red':''}"><span class="frame"></span><span class="c tl">${r}<span>${S[s]}</span></span><span class="big">${r}<small>${S[s]}</small></span><span class="c br">${r}<span>${S[s]}</span></span></div><div class="b"></div>`;
  return el;
}
function deal(set, faceDown){ table.innerHTML=''; set.forEach(c => { const e = cardEl(c); if (faceDown) e.classList.add('down'); table.appendChild(e); }); }
let phase = 0;
deal(SET_A, false);
const wait = ms => new Promise(r => setTimeout(r, REDUCED ? 0 : ms));
btn.addEventListener('click', async () => {
  btn.disabled = true;
  if (phase === 0){
    step.innerHTML = 'Concentrating&hellip; <strong>keep picturing your card.</strong>';
    [...table.children].forEach((c,i) => setTimeout(() => c.classList.add('down'), i*90));
    await wait(1100);
    [...table.children].forEach((c,i) => c.animate([{transform:'rotateY(180deg)'},{transform:`translate(${(2.5-i)*40}px,-10px) rotateY(180deg) rotateZ(${(i-2.5)*6}deg)`},{transform:'rotateY(180deg)'}],{duration:REDUCED?1:900,easing:'ease-in-out'}));
    await wait(1000);
    deal(SET_B, true);
    await wait(120);
    [...table.children].forEach((c,i) => setTimeout(() => c.classList.remove('down'), i*110));
    await wait(900);
    step.innerHTML = 'I’ve removed your card from the table. <strong>Look closely. It’s gone.</strong>';
    btn.textContent = 'Do it again'; phase = 1;
  } else {
    step.innerHTML = 'Pick one of these six cards <strong>in your head</strong>. Don’t click it, don’t say it out loud. Just remember it.';
    deal(SET_A, false); btn.textContent = 'I’ve got my card'; phase = 0;
  }
  btn.disabled = false;
});

/* ---------- gallery tilt ---------- */
if (!REDUCED && matchMedia('(hover:hover)').matches){
  document.querySelectorAll('.shot').forEach(s => {
    s.addEventListener('pointermove', e => { const r = s.getBoundingClientRect(), x=(e.clientX-r.left)/r.width, y=(e.clientY-r.top)/r.height;
      s.style.transform = `perspective(900px) rotateX(${(.5-y)*7}deg) rotateY(${(x-.5)*9}deg)`; s.style.setProperty('--mx', x*100+'%'); s.style.setProperty('--my', y*100+'%'); });
    s.addEventListener('pointerleave', () => { s.style.transform = ''; });
  });
}


})();
