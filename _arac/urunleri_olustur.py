"""İlk kurulumda _urunler/ dosyalarını üretti. Sonrası Pages CMS'ten yönetilir; tekrar çalıştırmayın (CMS düzenlemelerinin üzerine yazar)."""
import yaml,os,sys
if os.listdir('_urunler') and '--zorla' not in sys.argv: sys.exit('_urunler dolu; üzerine yazmamak için durdu (--zorla ile çalıştırın).')
B='https://www.trendyol.com/dr-baharat/'; M='?merchantId=1120687'
P=[
('kis-masali-orta','Kış Masalı Hikâyeli Tütsü Seti · Orta','kis-masali','Orta','kis-masali-tu-tsu-seti-40-adet-c-ubuk-tu-tsu-amber-portakal-c-ic-eg-i-tu-tsu-kayig-i-yilbas-i-hediye-p-1219908917',
 'Amber ve Portakal Çiçeği ile kar yağan bir akşam.',['Amber kokulu çubuk tütsü (20 adet)','Portakal Çiçeği kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Kış Masalı" hikâye kartı (10×15 cm)'],1),
('kis-masali-premium','Kış Masalı Hikâyeli Tütsü Seti · Premium','kis-masali','Premium','kis-masali-tu-tsu-seti-60-adet-c-ubuk-tu-tsu-amber-vanilya-portakal-c-ic-eg-i-tu-tsu-lu-k-yilbas-i-hediye-p-1219908453',
 'Amber, Portakal Çiçeği ve Vanilya; kurdeleli hediye sunumu.',['Amber kokulu çubuk tütsü (20 adet)','Vanilya kokulu çubuk tütsü (20 adet)','Portakal Çiçeği kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Kış Masalı" hikâye kartı','Kurdeleli hediye sunumu'],2),
('gece-ninnisi-orta','Gece Ninnisi Hikâyeli Tütsü Seti · Orta','gece-ninnisi','Orta','gece-ninnisi-tu-tsu-seti-40-adet-c-ubuk-tu-tsu-lavanta-mamma-baby-tu-tsu-kayig-i-hediye-p-1219909588',
 'Lavanta ve Mamma & Baby ile ışıkların kısıldığı saat.',['Lavanta kokulu çubuk tütsü (20 adet)','Mamma & Baby kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Gece Ninnisi" hikâye kartı (10×15 cm)'],1),
('gece-ninnisi-premium','Gece Ninnisi Hikâyeli Tütsü Seti · Premium','gece-ninnisi','Premium','gece-ninnisi-tu-tsu-seti-60-adet-c-ubuk-tu-tsu-lavanta-vanilya-mamma-baby-tu-tsu-lu-k-hediye-p-1219910006',
 'Lavanta, Vanilya ve Mamma & Baby; kurdeleli hediye sunumu.',['Lavanta kokulu çubuk tütsü (20 adet)','Vanilya kokulu çubuk tütsü (20 adet)','Mamma & Baby kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Gece Ninnisi" hikâye kartı','Kurdeleli hediye sunumu'],2),
('bereket-sofrasi-orta','Bereket Sofrası Hikâyeli Tütsü Seti · Orta','bereket-sofrasi','Orta','bereket-sofrasi-tu-tsu-seti-40-adet-c-ubuk-tu-tsu-portakal-c-ic-eg-i-rain-forest-kayikli-yeni-ev-hediye-p-1219910437',
 'Portakal Çiçeği ve Rain Forest ile kapısı hep açık bir ev.',['Portakal Çiçeği kokulu çubuk tütsü (20 adet)','Rain Forest kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Bereket Sofrası" hikâye kartı (10×15 cm)'],1),
('bereket-sofrasi-premium','Bereket Sofrası Hikâyeli Tütsü Seti · Premium','bereket-sofrasi','Premium','bereket-sofrasi-tu-tsu-seti-60-adet-c-ubuk-tu-tsu-amber-portakal-c-ic-eg-i-tu-tsu-lu-k-yeni-ev-hediyesi-p-1219910609',
 'Amber, Portakal Çiçeği ve Rain Forest; kurdeleli hediye sunumu.',['Amber kokulu çubuk tütsü (20 adet)','Portakal Çiçeği kokulu çubuk tütsü (20 adet)','Rain Forest kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Bereket Sofrası" hikâye kartı','Kurdeleli hediye sunumu'],2),
('yasemin-aksami-orta','Yasemin Akşamı Hikâyeli Tütsü Seti · Orta','yasemin-aksami','Orta','yasemin-aks-ami-romantik-tu-tsu-seti-40-adet-c-ubuk-tu-tsu-yasemin-vanilya-kayik-sevgiliye-hediye-p-1219910674',
 'Yasemin ve Vanilya ile iki kişilik bir akşam.',['Yasemin kokulu çubuk tütsü (20 adet)','Vanilya kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Yasemin Akşamı" hikâye kartı (10×15 cm)'],1),
('yasemin-aksami-premium','Yasemin Akşamı Hikâyeli Tütsü Seti · Premium','yasemin-aksami','Premium','yasemin-aks-ami-romantik-tu-tsu-seti-60-adet-c-ubuk-tu-tsu-yasemin-vanilya-amber-tu-tsu-lu-k-hediye-p-1219911163',
 'Yasemin, Vanilya ve Amber; kurdeleli hediye sunumu.',['Yasemin kokulu çubuk tütsü (20 adet)','Vanilya kokulu çubuk tütsü (20 adet)','Amber kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Yasemin Akşamı" hikâye kartı','Kurdeleli hediye sunumu'],2),
('sessiz-sabah-orta','Sessiz Sabah Hikâyeli Tütsü Seti · Orta','sessiz-sabah','Orta','sessiz-sabah-meditasyon-tu-tsu-seti-40-adet-c-ubuk-tu-tsu-lotus-adac-ayi-tu-tsu-kayig-i-yoga-hediye-p-1219917408',
 'Lotus ve Adaçayı ile acelesiz bir sabah.',['Lotus kokulu çubuk tütsü (20 adet)','Adaçayı kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Sessiz Sabah" hikâye kartı (10×15 cm)'],1),
('sessiz-sabah-premium','Sessiz Sabah Hikâyeli Tütsü Seti · Premium','sessiz-sabah','Premium','sessiz-sabah-meditasyon-tu-tsu-seti-60-adet-c-ubuk-tu-tsu-lotus-adac-ayi-amber-tu-tsu-lu-k-yoga-hediye-p-1219913468',
 'Lotus, Adaçayı ve Amber; kurdeleli hediye sunumu.',['Lotus kokulu çubuk tütsü (20 adet)','Adaçayı kokulu çubuk tütsü (20 adet)','Amber kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Sessiz Sabah" hikâye kartı','Kurdeleli hediye sunumu'],2),
('kis-masali-aslan','Kış Masalı Aslan Hediye Kutusu','hediye-kutulari','Kutu','kis-masali-aslan-hediye-kutusu-geri-akis-tu-tsu-lu-k-10-koni-40-c-ubuk-tu-tsu-kayik-yilbas-i-hediye-p-1219946654',
 "Bekçi Aslan'ın nefesi aşağı akar: geri akış konisinden çıkan duman çeşmeden havuza süzülür. Yanında Amber ve Portakal Çiçeği çubuklar.",['Aslan çeşme geri akış tütsülük','Vanilya kokulu geri akış konisi (10 adet)','Amber kokulu çubuk tütsü (20 adet)','Portakal Çiçeği kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Kış Masalı" hikâye kartı ve kurdele'],1),
('sessiz-sabah-aslan','Sessiz Sabah Aslan Kutusu','hediye-kutulari','Kutu','sessiz-sabah-aslan-meditasyon-kutusu-geri-akis-tu-tsu-lu-k-10-koni-40-c-ubuk-tu-tsu-kayik-hediye-p-1219946737',
 'Güne acele etmeden başlamak için bir köşe: süzülen duman, Lotus ve Adaçayı, pencere kenarında telefonsuz on dakika.',['Aslan çeşme geri akış tütsülük','Sandal Ağacı kokulu geri akış konisi (10 adet)','Lotus kokulu çubuk tütsü (20 adet)','Adaçayı kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı','"Sessiz Sabah" hikâye kartı ve kum rengi ip'],2),
('dort-hikaye','Dört Hikâye Tütsü Kutusu','hediye-kutulari','Kutu','do-rt-hika-ye-tu-tsu-kutusu-80-adet-c-ubuk-tu-tsu-amber-lavanta-yasemin-portakal-tu-tsu-kayig-i-hediye-p-1219946529',
 '4 akşam, 4 koku, tek kutu: Amber, Lavanta, Portakal Çiçeği, Yasemin. 80 çubuk, kayık ve kurdeleli sunum.',['Amber kokulu çubuk tütsü (20 adet) · Kış Masalı','Lavanta kokulu çubuk tütsü (20 adet) · Gece Ninnisi','Portakal Çiçeği kokulu çubuk tütsü (20 adet) · Bereket Sofrası','Yasemin kokulu çubuk tütsü (20 adet) · Yasemin Akşamı','Ahşap tütsü kayığı','"Dört Hikâye" hikâye kartı','Kurdeleli hediye sunumu'],3),
('3lu-set',"3'lü Tütsü Seti","klasik","Klasik",'tu-tsu-seti-3-farkli-aroma-60-adet-c-ubuk-tu-tsu-adac-ayi-lotus-rain-forest-tu-tsu-kayig-i-hediyeli-p-1219334832',
 'Adaçayı, Lotus ve Rain Forest; 60 çubuk ve ahşap kayık. Otsu ve yeşil bir başlangıç.',["Adaçayı, Lotus, Rain Forest (20'şer çubuk)",'Ahşap tütsü kayığı'],1),
('5li-set',"5'li Tütsü Seti","klasik","Klasik",'tu-tsu-seti-5-farkli-aroma-100-adet-c-ubuk-tu-tsu-hediyeli-tu-tsu-lu-k-kalici-oda-kokusu-ev-ofis-yoga-meditasyon-i-c-in-p-1219339836',
 'Yasemin, Amber, Portakal Çiçeği, Vanilya ve Lavanta; 100 çubuk ve ahşap kayık.',["Yasemin, Amber, Portakal Çiçeği, Vanilya, Lavanta (20'şer çubuk)",'Ahşap tütsü kayığı'],2),
('7li-set',"7'li Tütsü Seti","klasik","Klasik",'tu-tsu-seti-7-farkli-aroma-140-adet-c-ubuk-tu-tsu-hediyeli-tu-tsu-lu-k-kalici-oda-kokusu-ev-ofis-yoga-meditasyon-i-c-in-p-1219340526',
 'Yedi koku, 140 çubuk: hangisinin sana ait olduğunu bulmanın en kolay yolu.',["Adaçayı, Lotus, Rain Forest, Yasemin, Amber, Vanilya, Lavanta (20'şer çubuk)",'Ahşap tütsü kayığı'],3),
]
T=[('amber','Amber','amber-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214940469','Sıcak, reçinemsi ve yoğun. Kar yağan akşam, soba başı.'),
('lavanta','Lavanta','lavanta-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214944533','Temiz ve ferah. Işıkların kısıldığı saat, ütülü çarşaf.'),
('yasemin','Yasemin','yasemin-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214944925','Zarif ve çiçeksi. Yaz akşamı balkonu, iki kişilik sohbet.'),
('vanilya','Vanilya','vanilya-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214941055','Yumuşak ve tatlı. Fırından yeni çıkmış kurabiye, film gecesi.'),
('portakal-cicegi','Portakal Çiçeği','portakal-c-ic-eg-i-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214940097','Taze ve narenciyeli. Misafire ikram edilen kolonya, yılbaşı masası.'),
('lotus','Lotus','lotus-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214939211','Yumuşak ve hafif çiçeksi. Erken sabah, yoga matı.'),
('adacayi','Adaçayı','adac-ayi-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214942709','Kuru, otsu ve temiz. Pencere kenarında ilk çay.'),
('rain-forest','Rain Forest','rain-forest-kokulu-c-ubuk-tu-tsu-20-li-kalici-oda-kokusu-hediye-ahs-ap-tu-tsu-kayig-i-ev-ofis-yoga-meditasyon-p-1214941416','Yeşil yaprak ve nemli toprak. Yeni ev, bitki köşesi.'),
('mamma-baby','Mamma & Baby',None,'Pudramsı ve yumuşak. Temiz çamaşır, çocukluk anısı.')]
def w(fn,d,comment=''):
    s='---\n'+comment+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+'---\n'
    open(f'_urunler/{fn}.md','w').write(s)
HBC='# TODO: hepsiburada_url boşken buton HB mağaza sayfasına gider. Ürün linkini HB panelinden alıp buraya yazın.\n'
for slug,ad,st,v,ty,kisa,ic,sira in P:
    n = 3 if st=='klasik' else 5
    w(slug,{'title':ad,'set':st,'varyant':v,'kisa_aciklama':kisa,'icerik':ic,
      'gorseller':[f'/gorseller/urunler/{slug}-{i}.webp' for i in range(1,n+1)],
      'trendyol_url':B+ty+M,'hepsiburada_url':'','aktif':True,'sira':sira},HBC)
for i,(slug,ad,ty,kisa) in enumerate(T,1):
    w('tek-'+slug,{'title':f'{ad} Kokulu Çubuk Tütsü · 20 Adet','set':'tek-kokular','varyant':'Tek','kisa_aciklama':kisa,
      'icerik':[f'{ad} kokulu çubuk tütsü (20 adet)','Ahşap tütsü kayığı'],'gorseller':[f'/gorseller/urunler/tek-{slug}-1.webp'],
      'trendyol_url':(B+ty+M) if ty else '','hepsiburada_url':'','aktif':True,'sira':i},
      HBC+("# TODO: Bu kokunun Trendyol'da ayrı ürünü yok (API, 21.10.2026); boşken buton Trendyol mağazasına gider.\n" if not ty else ''))
print(len(os.listdir('_urunler')))
