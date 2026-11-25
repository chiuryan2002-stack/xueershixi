/* 語義眼鏡 Semantic Glasses — highlights 原/前/舊/老 + workplace identity nouns on any page
   and explains each one with the clues in its sentence. Used by: the Chrome extension, the bookmarklet,
   and the 學而時習 app. No network, no data collection. */
(function(){
'use strict';
if(window.YQGlasses&&window.YQGlasses.version) return;
const M=['原','前','舊','老'];
const COL={原:'#3f7fc0',前:'#7a6bc4',舊:'#b0559f',老:'#d1574a'};
const NOUNS=('同事 校長 員工 長官 董事長 主席 領導 部屬 上司 執行長 夥伴 伙伴 老闆 搭檔 社長 主任 總經理 成員 主管 秘書 下屬 會長 院長 秘書長 雇主 僱主 職員 同僚 助理 廠長 所長 委員 理事長 領班 系主任 經理 董事 負責人 幕僚 前輩 處長 雇員 僱員 合夥人 顧問 戰友 郵差 組長 副院長 監事 同仁 部下 副署長 副校長 副主任 總經濟師 發言人 副主席 大使 總裁 行長 副行長 班底 幹部 '+
 '總統 副總統 部長 次長 政務次長 市長 縣長 議員 立委 立法委員 議長 院長 署長 局長 司長 科長 課長 股長 襄理 協理 副理 副總 總監 總編輯 主編 編輯 記者 主播 教練 國手 球員 隊長 老師 教授 講師 醫師 醫生 護理師 律師 法官 檢察官 警察 司機 工程師 設計師 店長 店員 客戶 顧客 客人 主顧 股東 東家 師傅 學徒 徒弟 部門 單位 公司 團隊 對手 合作夥伴 長輩 職位 職務').split(' ').filter(Boolean).sort((a,b)=>b.length-a.length);
/* characters before the modifier that make it part of another word (目前, 依舊, 草原, 古老…) */
const BEFORE={前:'目之以先提眼面當生事從空向往跟日年月天週周幾',原:'草平高還復中荒',舊:'依仍照懷守陳老新念敘',老:'古養元敬長父終衰防年蒼'};
/* nouns that, followed by these chars, are part of a longer word (原委員會, 老師傅 handled by length) */
const AFTER_BAD={委員:'會',部長:'會',公司:'法',單位:'元'};
const NOTE={
 原:{zh:'原本的、原來擔任的。正式、偏書面，常見於新聞和人事異動；人可能還在，只是換了位置。',en:'Original; the one who held the post before. Formal, common in news and reassignments; the person may still be around in a new role.',typ:'過去・中止（語料 99%）'},
 前:{zh:'先前的、已卸任的。最通用的「前任」，強調那個身分或關係已經結束，語氣中性。',en:'Former; no longer in the role. The general-purpose word; the role or tie has ended; neutral.',typ:'過去・中止（語料 100%）'},
 舊:{zh:'以前的、往日的。多接關係名詞，指過去的關係，但情誼可能還在，常帶懷念。',en:'Old, from before. Mostly with relational nouns: a past tie, often with lingering warmth.',typ:'多為過去（語料約 80%）'},
 老:{zh:'長久的、資深的。關係或身分延續很久、多半仍在持續，常帶親切或敬重（也可能是「倚老賣老」的負面）。',en:'Long-standing, senior. A long tie that usually still continues; warm or respectful (sometimes negative).',typ:'多為延續（語料 62%）'}};
const CUES=[
 [/離職|卸任|退休|辭職|請辭|去職|下台|下臺|離開|被資遣|資遣|解僱|開除|拆夥|退役|退出|已經不|不再是|曾任|曾是|曾經/,'end','關係已結束','the tie has ended'],
 [/當年|以前|過去|昔日|往日|那時|那時候|從前/,'past','指向過去','points to the past'],
 [/懷念|想念|敘舊|重逢|老友|久別|回憶/,'warm','帶懷念、情誼','nostalgic, warm'],
 [/多年|至今|迄今|到現在|一直|仍然|仍是|還是|依然|資深|共事|長年|[一二三四五六七八九十兩幾數\d]+[十百]?多?年(?![前後初底中度級紀輕])(了|來|以上)?/,'cont','延續很久、仍持續','long and still ongoing'],
 [/轉任|調任|改組|合併|併購|改制|接任|繼任|新任|上任|到任|續任|異動|調職|升任/,'move','人事異動（正式）','a formal change of post'],
 [/公告|宣布|宣佈|指出|報導|據了解|官方|記者會|新聞/,'formal','正式、新聞語氣','formal or news register'],
 [/倚老賣老|老油條|擺老|資格老/,'neg','帶負面評價','negative evaluation']];
const FIT={原:['end','move','formal'],前:['end','past','formal','move'],舊:['past','warm','end'],老:['cont','neg']};
const SKIP='script,style,noscript,textarea,input,select,code,pre,svg,canvas,mark.yqg,.yqg-tip,.yqg-panel,[contenteditable=""],[contenteditable=true],ruby rt';
const RE=new RegExp('(['+M.join('')+'])('+NOUNS.map(n=>n.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|')+')','g');

function sentenceAround(text,i,j){ const L=text.slice(0,i), R=text.slice(j); const a=Math.max(L.lastIndexOf('。'),L.lastIndexOf('！'),L.lastIndexOf('？'),L.lastIndexOf('\n'),L.lastIndexOf('；')); const bs=R.search(/[。！？\n；]/); return text.slice(a+1,bs<0?text.length:j+bs+1); }
function cuesIn(ctx){ const out=[]; for(const [re,k,zh,en] of CUES){ const m=ctx.match(re); if(m) out.push({k,word:m[0],zh,en}); } return out; }
function analyze(text,ctxText){
  const res=[]; RE.lastIndex=0; let m;
  while((m=RE.exec(text))){
    const mod=m[1], noun=m[2], i=m.index, j=i+m[0].length;
    const prev=text[i-1]; if(prev&&BEFORE[mod].includes(prev)) continue;
    if(AFTER_BAD[noun]&&text[j]&&AFTER_BAD[noun].includes(text[j])) continue;
    if(mod==='老'&&noun==='闆') continue;
    const ctx=sentenceAround(ctxText||text,i,j).trim();
    const cues=cuesIn(ctx.replace(m[0],'＿'));
    const fits=cues.filter(c=>FIT[mod].includes(c.k)), clash=cues.filter(c=>!FIT[mod].includes(c.k)&&!['formal','move'].includes(c.k));
    res.push({start:i,end:j,m:mod,n:noun,ctx,cues,fits,clash});
  }
  return res;
}

/* ---------- DOM highlighting ---------- */
let tip=null, panel=null, count={原:0,前:0,舊:0,老:0}, observer=null, enabled=false;
function css(){
  if(document.getElementById('yqg-style')) return;
  const s=document.createElement('style'); s.id='yqg-style';
  s.textContent=`mark.yqg{background:transparent;color:inherit;border-bottom:2.5px solid var(--yqg);padding:0 1px;border-radius:2px;cursor:help;box-shadow:inset 0 -0.5em 0 color-mix(in srgb,var(--yqg) 16%,transparent)}
mark.yqg b.yqg-m{color:var(--yqg);font-weight:800}
.yqg-tip{position:absolute;z-index:2147483646;max-width:340px;padding:12px 14px;border-radius:14px;background:#161a2e;color:#eef0fa;font:14px/1.6 "Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;box-shadow:0 18px 40px -12px rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.12)}
.yqg-tip .h{display:flex;align-items:center;gap:8px;margin-bottom:6px}.yqg-tip .h b{font-size:22px;font-family:"Noto Serif TC",serif}.yqg-tip .h span{font-size:12px;opacity:.7}
.yqg-tip p{margin:4px 0}.yqg-tip .en{font-size:12.5px;opacity:.72}.yqg-tip .cue{margin-top:8px;padding-top:8px;border-top:1px solid rgba(255,255,255,.14);font-size:13px}
.yqg-tip .cue i{font-style:normal;padding:1px 6px;border-radius:8px;background:rgba(255,255,255,.12);margin-right:4px}.yqg-tip .warn{color:#f8c9a6}
.yqg-tip a{color:#a5cde2}
.yqg-panel{position:fixed;right:16px;bottom:16px;z-index:2147483645;display:flex;align-items:center;gap:10px;padding:8px 10px 8px 14px;border-radius:24px;background:#161a2e;color:#eef0fa;font:13px/1.4 "Noto Sans TC",sans-serif;box-shadow:0 12px 30px -10px rgba(0,0,0,.5)}
.yqg-panel b{font-weight:700}.yqg-panel s{text-decoration:none;font-weight:800;margin-left:6px}.yqg-panel button{all:unset;cursor:pointer;width:24px;height:24px;border-radius:50%;display:grid;place-content:center;background:rgba(255,255,255,.12)}`;
  (document.head||document.documentElement).appendChild(s);
}
function wrapText(node){
  const text=node.nodeValue; if(!RE.test(text)){ RE.lastIndex=0; return 0; } RE.lastIndex=0;
  const ctxText=(node.parentElement&&node.parentElement.textContent)||text;
  const off=ctxText.indexOf(text);
  const hits=analyze(text,null).map(h=>{ const g=off>=0?analyze(ctxText).find(x=>x.start===h.start+off&&x.m===h.m):null; return g?Object.assign(h,{ctx:g.ctx,cues:g.cues,fits:g.fits,clash:g.clash}):h; });
  if(!hits.length) return 0;
  const frag=document.createDocumentFragment(); let k=0;
  for(const h of hits){
    if(h.start>k) frag.appendChild(document.createTextNode(text.slice(k,h.start)));
    const mk=document.createElement('mark'); mk.className='yqg'; mk.style.setProperty('--yqg',COL[h.m]);
    mk.innerHTML=`<b class="yqg-m">${h.m}</b>${h.n}`; mk._yqg=h; frag.appendChild(mk); count[h.m]++; k=h.end;
  }
  if(k<text.length) frag.appendChild(document.createTextNode(text.slice(k)));
  node.parentNode.replaceChild(frag,node); return hits.length;
}
function scan(root){
  root=root||document.body; if(!root) return 0; css(); let n=0;
  const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode(t){ if(!/[原前舊老]/.test(t.nodeValue)) return 2; const p=t.parentElement; if(!p||p.closest(SKIP)) return 2; return 1; }});
  const list=[]; while(w.nextNode()) list.push(w.currentNode);
  for(const t of list) n+=wrapText(t);
  updatePanel(); return n;
}
function esc(s){ return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function showTip(mk){
  const h=mk._yqg; if(!h) return; hideTip();
  tip=document.createElement('div'); tip.className='yqg-tip'; const N=NOTE[h.m];
  const cue=h.cues.length?`<div class="cue">${h.cues.map(c=>`<div><i>${esc(c.word)}</i>${c.zh}<span class="en"> · ${c.en}</span></div>`).join('')}${h.clash.length&&!h.fits.length?`<div class="warn">這裡的線索和「${h.m}」的典型用法不太一樣，值得細看。</div>`:''}</div>`:`<div class="cue en">句子裡沒有明顯線索，靠典型用法判斷。 · No explicit clue in this sentence.</div>`;
  tip.innerHTML=`<div class="h"><b style="color:${COL[h.m]}">${h.m}</b><b>${esc(h.n)}</b><span>${N.typ}</span></div><p>${N.zh}</p><p class="en">${N.en}</p>${cue}`;
  document.body.appendChild(tip);
  const r=mk.getBoundingClientRect(); const tw=tip.offsetWidth, th=tip.offsetHeight;
  let x=r.left+scrollX, y=r.bottom+scrollY+8; if(x+tw>scrollX+innerWidth-8) x=scrollX+innerWidth-tw-8; if(r.bottom+th+8>innerHeight) y=r.top+scrollY-th-8;
  tip.style.left=Math.max(8,x)+'px'; tip.style.top=y+'px';
}
function hideTip(){ if(tip){ tip.remove(); tip=null; } }
function onOver(e){ const mk=e.target.closest&&e.target.closest('mark.yqg'); if(mk) showTip(mk); }
function onOut(e){ const mk=e.target.closest&&e.target.closest('mark.yqg'); if(mk&&!(e.relatedTarget&&mk.contains(e.relatedTarget))) hideTip(); }
function onClick(e){ const mk=e.target.closest&&e.target.closest('mark.yqg'); if(mk){ e.preventDefault(); showTip(mk); } else if(tip&&!e.target.closest('.yqg-tip')) hideTip(); }
function updatePanel(){
  if(!enabled||!document.body||window.YQG_NO_PANEL) return;
  const total=M.reduce((a,m)=>a+count[m],0);
  if(!panel){ panel=document.createElement('div'); panel.className='yqg-panel'; document.body.appendChild(panel); }
  panel.innerHTML=`<span>👓 <b>語義眼鏡</b>　找到 ${total} 處</span><span>${M.map(m=>`<s style="color:${COL[m]}">${m}</s>${count[m]}`).join(' ')}</span><button title="關閉 Close" aria-label="關閉">✕</button>`;
  panel.querySelector('button').onclick=()=>disable();
}
function enable(opts){
  opts=opts||{}; if(opts.noPanel) window.YQG_NO_PANEL=true;
  enabled=true; css(); scan(document.body);
  document.addEventListener('mouseover',onOver,true); document.addEventListener('mouseout',onOut,true); document.addEventListener('click',onClick,true);
  let t=null; observer=new MutationObserver(ms=>{ if(ms.every(m=>[...m.addedNodes].every(n=>n.nodeType===1&&(n.classList.contains('yqg-tip')||n.classList.contains('yqg-panel')||n.matches('mark.yqg'))))) return; clearTimeout(t); t=setTimeout(()=>scan(document.body),400); });
  observer.observe(document.body,{childList:true,subtree:true,characterData:true});
  return M.reduce((a,m)=>a+count[m],0);
}
function clear(root){ (root||document).querySelectorAll('mark.yqg').forEach(mk=>{ mk.replaceWith(document.createTextNode(mk.textContent)); }); (root||document.body).normalize(); }
function disable(){ enabled=false; if(observer) observer.disconnect(); observer=null; clear(); hideTip(); if(panel){ panel.remove(); panel=null; } count={原:0,前:0,舊:0,老:0};
  document.removeEventListener('mouseover',onOver,true); document.removeEventListener('mouseout',onOut,true); document.removeEventListener('click',onClick,true); }
let bound=false;
function bind(){ if(bound) return; bound=true; css(); document.addEventListener('mouseover',onOver,true); document.addEventListener('mouseout',onOut,true); document.addEventListener('click',onClick,true); }
function resetCount(){ count={原:0,前:0,舊:0,老:0}; }
function toggle(){ return enabled?(disable(),false):(enable(),true); }
function stats(){ return Object.assign({},count,{enabled}); }
window.YQGlasses={version:1,analyze,scan,enable,disable,toggle,stats,clear,bind,resetCount,NOTE,COL};
if(window.YQG_AUTO) enable();
})();
