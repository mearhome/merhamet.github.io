// Mobil menü aç/kapa (tek görev; takip/izleme kodu yok)
document.addEventListener('DOMContentLoaded',function(){var b=document.querySelector('.menu-dugme'),m=document.getElementById('menu');if(!b||!m)return;b.addEventListener('click',function(){var a=m.classList.toggle('acik');b.setAttribute('aria-expanded',a)})});
