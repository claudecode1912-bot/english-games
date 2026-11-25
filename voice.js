/* Общая озвучка для всех страниц english-games.
   Эталон — учебник «Читаю по-английски» (chitayu/): записанные MP3 британским
   нейроголосом en-GB-SoniaNeural (edge-tts), слова -5%, фразы и тексты -10%.
   Файлы лежат в audio/ в корне репозитория, имена считаются той же функцией akey,
   что и в учебнике. Если файла нет, звучит голос браузера с тем же выбором,
   что в учебнике: Sonia / Libby / Natural, затем Google UK English, скорость 0.85.
   Скорость (обычная/медленная) и голос берутся из настроек учебника ('phon-book-v1'). */
(function(){
  var KEY='phon-book-v1';
  var BASE=(function(){var s=document.currentScript&&document.currentScript.src;return s?s.replace(/voice\.js(\?.*)?$/,''):'../'})();
  var AUD={},cur=null,voice=null;
  function settings(){try{var r=JSON.parse(localStorage.getItem(KEY)||'{}');return r.set||{}}catch(e){return {}}}
  function rate(){var r=parseFloat(settings().rate);return r>0?r:0.85}
  function akey(t){t=String(t).replace(/\*/g,'').replace(/\s+/g,' ').trim();if(/^[A-Z]$/.test(t))return 'letter-'+t.toLowerCase();var n=t.toLowerCase(),h=0x811c9dc5;for(var c of n){h^=c.codePointAt(0);h=Math.imul(h,16777619)>>>0}var s=n.normalize('NFKD').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,40);return (s||'x')+'-'+h.toString(36)}
  try{fetch(BASE+'audio/manifest.json').then(function(r){return r.ok?r.json():{}}).then(function(j){AUD=j||{}}).catch(function(){})}catch(e){}
  function pick(){
    if(!('speechSynthesis' in window))return;
    var vs=speechSynthesis.getVoices()||[];
    var gb=vs.filter(function(v){return /en[-_]GB/i.test(v.lang)});
    var saved=settings().voice;
    var chosen=saved&&vs.find(function(v){return v.name===saved});
    var pref=gb.find(function(v){return /(sonia|libby|maisie|natural|online|neural)/i.test(v.name)})||gb.find(function(v){return /google/i.test(v.name)})||gb[0];
    voice=chosen||pref||vs.find(function(v){return /^en/i.test(v.lang)})||null;
  }
  function stop(){if(cur){cur.pause();cur=null}try{speechSynthesis.cancel()}catch(e){}}
  function tts(text,onend){
    if(!('speechSynthesis' in window))return false;
    try{if(!voice)pick();speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(text);if(voice)u.voice=voice;u.lang=voice?voice.lang:'en-GB';u.rate=rate();if(onend)u.onend=onend;speechSynthesis.speak(u);return true}catch(e){return false}
  }
  function speak(text,onend){
    var k=akey(text);stop();
    if(AUD[k]){
      var a=new Audio(BASE+'audio/'+k+'.'+AUD[k]);a.playbackRate=rate()<0.7?0.75:1;a.preservesPitch=true;
      if(onend)a.onended=onend;cur=a;
      a.play().catch(function(){delete AUD[k];tts(text,onend)});return true;
    }
    return tts(text,onend);
  }
  if('speechSynthesis' in window){pick();try{speechSynthesis.addEventListener('voiceschanged',pick)}catch(e){speechSynthesis.onvoiceschanged=pick}}
  window.addEventListener('storage',function(e){if(e.key===KEY)pick()});
  window.VOICE={speak:speak,stop:stop,akey:akey};
})();
