"""Kaynak görselleri site için küçültür ve WebP/JPG olarak gorseller/ altına yazar.
Sadece ilk kurulumda kullanıldı; yeni görseller Pages CMS'ten doğrudan yüklenebilir."""
from PIL import Image, ImageOps
import os, glob
W='/workspace'; G=W+'/godaddy_magaza/gorseller/'; IG=W+'/instagram/buyume/'
OUT=W+'/mearhome_site/gorseller/'
def save(im, path, maxw=1200, q=80):
    im = ImageOps.exif_transpose(im)
    if im.mode not in ('RGB','RGBA'): im = im.convert('RGB')
    if im.width > maxw: im = im.resize((maxw, round(im.height*maxw/im.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(OUT+path), exist_ok=True)
    if path.endswith('.webp'): im.save(OUT+path, 'WEBP', quality=q, method=6)
    else: im.convert('RGB').save(OUT+path, 'JPEG', quality=q, optimize=True, progressive=True)
    return im.size
urun = {'kis-masali-orta':'MEARHOMEKMO01','kis-masali-premium':'MEARHOMEKMP01','gece-ninnisi-orta':'MEARHOMEGNO01','gece-ninnisi-premium':'MEARHOMEGNP01',
 'bereket-sofrasi-orta':'MEARHOMEBSO01','bereket-sofrasi-premium':'MEARHOMEBSP01','yasemin-aksami-orta':'MEARHOMEYAO01','yasemin-aksami-premium':'MEARHOMEYAP01',
 'sessiz-sabah-orta':'MEARHOMESSO01','sessiz-sabah-premium':'MEARHOMESSP01','dort-hikaye':'MEARHOMEDHB01','kis-masali-aslan':'MEARHOMEKAA01','sessiz-sabah-aslan':'MEARHOMESAA01'}
for slug,sku in urun.items():
    for i,f in enumerate(sorted(glob.glob(G+sku+'/0[1-5].jpg')),1):
        save(Image.open(f), f'urunler/{slug}-{i}.webp', 1000)
for slug,sku,picks in [('3lu-set','MEARHOME3TS01',['01','05','02']),('5li-set','MEARHOME5TS01',['01','05','02']),('7li-set','MEARHOME7TS01',['01','06','02'])]:
    for i,p in enumerate(picks,1): save(Image.open(f'{G}{sku}/{p}.jpg'), f'urunler/{slug}-{i}.webp', 1000)
# Tek kokular: kayıksız kutu fotoğrafı, krem zemin
for key,slug in [('amber','amber'),('lavanta','lavanta'),('yasemin','yasemin'),('vanilya','vanilya'),('portakal','portakal-cicegi'),('lotus','lotus'),('adacayi','adacayi'),('rainforest','rain-forest'),('mammababy','mamma-baby')]:
    b = Image.open(f'{W}/hikayeli_setler_upload/_kaynak/box_{key}.png').convert('RGBA')
    b = b.resize((round(b.width*820/b.height), 820), Image.LANCZOS)
    c = Image.new('RGBA',(1000,1000),(250,247,240,255)); c.alpha_composite(b,((1000-b.width)//2,90))
    save(c.convert('RGB'), f'urunler/tek-{slug}-1.webp', 1000)
# Site görselleri
hero = Image.open(W+'/ty_magaza_banner/banner_04_bes_hikaye_1830x900.jpg').convert('RGB').crop((612,0,1830,900))
save(hero,'site/hero-bes-hikaye.webp',1600,82)
og = ImageOps.fit(hero,(1200,630),centering=(0.5,0.45)); save(og,'site/og-mearhome.jpg',1200,85)
save(Image.open(W+'/ty_magaza_banner/banner_02_aslan_kutulari_1830x900.jpg'),'site/banner-aslan-kutulari.webp',1600)
tuti = Image.open(IG+'profil_foto/profil_A_tuti.png').convert('RGB'); save(tuti,'site/tuti.webp',800,85)
for n,p in enumerate(['hafta1/gun1/post_b_carousel_tanisin_tuti','hafta1/gun2/carousel_bolum2_kis_masali','hafta1/gun3/carousel_koku_gunlugu_5_aksam','hafta1/gun5/carousel_bekci_aslanin_sirri','hafta1/gun1/post_c_carousel_sezon1','hafta1/gun7/carousel_senin_hikayen'],1):
    save(Image.open(f'{IG}{p}/01.jpg'), f'site/instagram-{n}.webp', 540)
for name,src in [('tuti-uyanis','sahne1_uyanis_04'),('tuti-lavanta','sahne3_lavanta_06'),('defne','misafir_hikaye_15sn_01'),('tuti-kayik','tuti_tanitim_05')]:
    save(Image.open(f'{IG}_kaynak/frames/{src}.jpg'), f'karakterler/{name}.webp', 480, 82)
save(Image.open(IG+'hafta1/gun5/carousel_bekci_aslanin_sirri/01.jpg'),'karakterler/bekci-aslan.webp',540)
# Blog kapakları (OG için JPG)
for slug,src in [('aksam-hangi-koku',G+'MEARHOME7TS01/01.jpg'),('geri-akis-tutsu',G+'MEARHOMEKAA01/01.jpg'),('tutsu-kayigi',G+'MEARHOME3TS01/05.jpg'),
                 ('yilbasi-hediye',W+'/ty_magaza_banner/banner_02_aslan_kutulari_1830x900.jpg'),('kis-masali-bolum-2',IG+'hafta1/gun2/carousel_bolum2_kis_masali/01.jpg')]:
    save(Image.open(src), f'blog/{slug}.jpg', 1200, 80)
# Favicon
f = tuti.crop((140,140,940,940))
os.makedirs(W+'/mearhome_site/assets/ikon',exist_ok=True)
f.resize((180,180),Image.LANCZOS).save(W+'/mearhome_site/apple-touch-icon.png')
for s in (192,512): f.resize((s,s),Image.LANCZOS).save(W+f'/mearhome_site/assets/ikon/icon-{s}.png')
f.resize((32,32),Image.LANCZOS).save(W+'/mearhome_site/assets/ikon/favicon-32.png')
f.save(W+'/mearhome_site/favicon.ico', sizes=[(16,16),(32,32),(48,48)])
print('ok')
