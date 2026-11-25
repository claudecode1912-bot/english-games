/* Общая озвучка для всех страниц english-games.
   Эталон — учебник «Читаю по-английски» (chitayu/): британский голос,
   приоритет Sonia / Libby / Maisie / Natural / Online / Neural, затем Google UK English,
   скорость 0.85. Голос и скорость, выбранные в настройках учебника,
   берутся из того же хранилища ('phon-book-v1'), поэтому звучат одинаково везде. */
(function(){
  var KEY='phon-book-v1';
  var voice=null;
  function settings(){
    try{var r=JSON.parse(localStorage.getItem(KEY)||'{}');return r.set||{}}catch(e){return {}}
  }
  function pick(){
    if(!('speechSynthesis' in window))return;
    var vs=speechSynthesis.getVoices()||[];
    var gb=vs.filter(function(v){return /en[-_]GB/i.test(v.lang)});
    var saved=settings().voice;
    var chosen=saved&&vs.find(function(v){return v.name===saved});
    var pref=gb.find(function(v){return /(sonia|libby|maisie|natural|online|neural)/i.test(v.name)})||gb.find(function(v){return /google/i.test(v.name)})||gb[0];
    voice=chosen||pref||vs.find(function(v){return /^en/i.test(v.lang)})||null;
  }
  function rate(){var r=parseFloat(settings().rate);return r>0?r:0.85}
  function speak(text,onend,r){
    if(!('speechSynthesis' in window))return false;
    try{
      if(!voice)pick();
      speechSynthesis.cancel();
      var u=new SpeechSynthesisUtterance(text);
      if(voice)u.voice=voice;
      u.lang=voice?voice.lang:'en-GB';
      u.rate=r||rate();
      if(onend)u.onend=onend;
      speechSynthesis.speak(u);
      return true;
    }catch(e){return false}
  }
  function stop(){try{speechSynthesis.cancel()}catch(e){}}
  if('speechSynthesis' in window){pick();try{speechSynthesis.addEventListener('voiceschanged',pick)}catch(e){speechSynthesis.onvoiceschanged=pick}}
  window.addEventListener('storage',function(e){if(e.key===KEY)pick()});
  window.VOICE={speak:speak,stop:stop,rate:rate};
})();
