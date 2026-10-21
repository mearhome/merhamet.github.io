# mearhome.com'u yeni siteye bağlama (DNS talimatı)

Kral, bu işi telefondan 10 dakikada yaparız. Site GitHub Pages'te (ücretsiz) duracak; GoDaddy'de sadece "adres tabelasını" ona çeviriyoruz. Alan adı GoDaddy'de kalır, faturası da orada devam eder.

> **Ön koşul:** GitHub hesabı ve site deposu hazır olmalı, GitHub'da *Settings → Pages* ekranında site yayında görünmeli. Aşağıda `KULLANICI` yazan yere GitHub kullanıcı adını yazacağız (örnek: kullanıcı adı `mearhome` ise `mearhome.github.io`).

---

## 1. Önce bilmen gerekenler

| Kayıt türü | Ad (Name / Host) | Değer (Value / Points to) | TTL |
|---|---|---|---|
| A | `@` | `185.199.108.153` | 1 saat (veya varsayılan) |
| A | `@` | `185.199.109.153` | 1 saat |
| A | `@` | `185.199.110.153` | 1 saat |
| A | `@` | `185.199.111.153` | 1 saat |
| CNAME | `www` | `KULLANICI.github.io` | 1 saat |

- `@` = çıplak alan adı (mearhome.com). `www` = www.mearhome.com.
- Sitenin asıl adresi **https://www.mearhome.com**. mearhome.com yazan da otomatik oraya gider.
- **MX, TXT ve e-postayla ilgili diğer kayıtlara dokunma.** GoDaddy e-postası (ör. info@mearhome.com) varsa onlar sayesinde çalışır.

---

## 2. GoDaddy uygulamasından (telefon)

1. **GoDaddy** uygulamasını aç, giriş yap.
2. Alttaki menüden **Alan Adları / Domains**'e dokun, listeden **mearhome.com**'u seç.
3. **DNS** (bazen *"DNS'i Yönet / Manage DNS"*) bölümüne gir.
4. **Var olan A kaydını düzelt:**
   - Türü **A**, adı **@** olan satırı bul (değeri genelde "Parked", "WebsiteBuilder Site" ya da bir IP adresidir).
   - Kalem simgesine (Düzenle / Edit) dokun, değeri **185.199.108.153** yap, kaydet.
   - Birden fazla `@` A kaydı varsa fazlalarını sil (çöp kutusu simgesi).
5. **Üç A kaydı daha ekle:** **Ekle / Add (+)** → Tür **A** → Ad **@** → Değer sırasıyla:
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

   Her birinde **Kaydet / Save**.
6. **www kaydını düzelt:**
   - Türü **CNAME**, adı **www** olan satırı bul (değeri genelde `@` veya `mearhome.com`).
   - Düzenle → değeri **KULLANICI.github.io** yap → Kaydet.
   - Yoksa: Ekle → Tür **CNAME** → Ad **www** → Değer **KULLANICI.github.io**.
7. **Yönlendirme varsa kapat:** Alan adı sayfasında **Yönlendirme / Forwarding** açıksa kapat. Açık kalırsa DNS kayıtlarını ezer.
8. Bitti. Ekrandaki listede 4 tane `A @` ve 1 tane `CNAME www` görünmeli.

## 3. GoDaddy web sitesinden (telefon tarayıcısı veya bilgisayar)

1. **godaddy.com**'a gir, sağ üstten giriş yap → **Ürünlerim / My Products**.
2. **mearhome.com**'un yanındaki **DNS** düğmesine bas (veya alan adına tıklayıp **DNS → DNS Kayıtları / DNS Records** sekmesine geç).
3. Yukarıdaki 4. ve 7. adımların aynısını yap: `@` A kaydını düzenle, 3 A kaydı daha ekle, `www` CNAME'i `KULLANICI.github.io` yap, yönlendirmeyi kapat.

> GoDaddy bazen "Bu değişiklik web sitenizi etkileyebilir" diye uyarı verir; **Devam / Continue** de. GoDaddy Website Builder sitesini kullanmayacağız.

---

## 4. GitHub tarafı (DNS'ten sonra)

1. GitHub'da depo → **Settings → Pages**.
2. **Custom domain** kutusunda `www.mearhome.com` yazmalı (depodaki `CNAME` dosyası bunu otomatik doldurur). Yazmıyorsa yaz, **Save**.
3. "DNS check successful" yazısını bekle (birkaç dakika ile birkaç saat arası).
4. **Enforce HTTPS** kutusunu işaretle. Sertifika hazırlanınca kutu açılır; bu bazen 1 saati bulabilir. Gri ise biraz sonra tekrar bak.

**İsteğe bağlı güvenlik (önerilir):** GitHub hesap ayarlarında *Settings → Pages → Add a domain* ile `mearhome.com`'u doğrula. GitHub sana `_github-pages-challenge-KULLANICI` adında bir **TXT** kaydı ve bir değer verir; aynı GoDaddy DNS ekranından **Ekle → TXT** ile gir. Bu, başkasının alan adını kendi sitesine bağlamasını engeller.

**İsteğe bağlı IPv6 (AAAA):** Tür **AAAA**, Ad **@**, değerler `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`. Eklemesen de site çalışır.

---

## 5. Ne kadar sürer, nasıl kontrol ederim?

- Değişiklikler genelde **15 dakika – 1 saat** içinde yayılır, nadiren 24 saati bulur.
- Kontrol: telefondan **https://www.mearhome.com** aç. Eski GoDaddy sayfası görünüyorsa biraz bekle, mobil veriyle (Wi-Fi'yi kapatıp) tekrar dene.
- Bilgisayardan kontrol: `dnschecker.org` → `mearhome.com` → A kaydı. Dört 185.199.x.153 adresi görünmeli.

---

## 6. Cloudflare Pages kullanırsak değerler farklı

Yukarıdaki değerler **sadece GitHub Pages** içindir. Siteyi Cloudflare Pages'e koyarsak:

- `www` CNAME'i → `PROJE-ADI.pages.dev` olur (Cloudflare panelinde yazan ad).
- Çıplak alan adı (`mearhome.com`) için Cloudflare genelde **nameserver değişikliği** ister: GoDaddy'de *DNS → Nameservers → Değiştir* deyip Cloudflare'in verdiği iki adresi girmek gerekir. O durumda DNS kayıtlarını (e-posta dahil) Cloudflare'de yönetiriz.
- 185.199.x.153 A kayıtlarını **girmeyiz**.

Hangisini seçtiğimizi kesinleştirmeden kayıtları değiştirme; değerleri o gün sana tekrar netleştiririm.

---

## 7. Alan adının süresi: 13.12.2026

- mearhome.com **13 Aralık 2026**'da sona eriyor.
- GoDaddy uygulamasında **Alan Adları → mearhome.com → Otomatik Yenileme / Auto-renew** anahtarını **açık** yap ve kayıtlı kartın güncel olduğundan emin ol.
- Süre dolarsa site ve (varsa) e-posta durur; DNS ayarları da kaybolabilir.
- Yenileme sırasında GoDaddy "gizlilik koruması", "e-posta paketi" gibi ek ürünler önerebilir; gerekmedikçe ekleme.

---

### Kısa özet (ekran görüntüsü alıp yanında tut)

```
A      @     185.199.108.153
A      @     185.199.109.153
A      @     185.199.110.153
A      @     185.199.111.153
CNAME  www   KULLANICI.github.io
Yönlendirme: KAPALI
Otomatik yenileme: AÇIK (bitiş 13.12.2026)
```
