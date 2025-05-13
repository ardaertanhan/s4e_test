Bu test aşaması, S4E web sitesinin /free-security-tools sayfasının temel kullanıcı arayüzü işlevselliğini ve iş akışlarını Playwright ve pytest kullanarak doğrular. Her bir test, kritik arayüz bileşenleriyle kullanıcı etkileşimlerini taklit eder ve öğelerin doğru şekilde oluşturulduğunu, tıklanabilir olduğunu ve beklendiği gibi davrandığını kontrol eder.

1) Fonksiyonel Testler

Bazı temel yapılması gereken komutlar:
Öncelikle projeyi indirin ve şu komutu kullanarak bir sanal ortam oluşturun:
python -m venv venv
Daha sonra şu komutları gereli çalışma ortamı oluşturulması için kurun:
pip install pytest playwright
python -m playwright install
python -m pytest -s tests/
Bu sanal ortamı çalıştırmak için aşağıdaki komutları kullanın:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Yapılan fonksiyonel testler ve sonuçları
Fonskiyonel Kod Testi Açıklamaları & Sonuçları 
F01 Sayfa yükleniyor ve başlığı doğru 
F02 "Most used" araçlar bölümü mevcut ve görünür 
F03 " Full scan" butonu görünür ve doğru pencereyi açıyor 
F04 "choose your own" bölümü mevcut 
F05 Çıktı formatı seçenekleri (PDF, CSV, HTML, video) başarıyla listeleniyor
 F06 "Latest Tools" bölümü araç kayıtlarını başarıyla gösteriyor 
F07 Bir tarama kartına tıklamak çökme veya sayfadan ayrılmaya neden olmuyor

NOT: Testler, gerçek kullanıcı akışlarını yansıtacak şekilde yazıldı ve görünür kullanıcı arayüzü öğeleri aracılığıyla doğrulandı. Ekranlar, animasyonlar ve modal zamanlamaları Playwright'ın slow_mo ve wait_for_selector özellikleri kullanılarak yönetiliyor. Tüm testler birbirinden bağımsızdır ve tek tek veya toplu olarak çalıştırılabilir.

Dosyaları terminalde çalıştırmak için şu komut kullanılabilir (gerekli dosya ismi ve uzantı ile değiştirilerek):
python -m pytest -s tests/test_tc_f03_fullscan_button.py
Kod satırının en sonunda bulununan bu input, kullanıcının tarayıcı durumunu kapatmadan önce incelemesi için zaman tanır 
input("Press Enter to close the browser...")

2) Edge Testleri

s4e.io/free-security-tools için Edge Testleri
Bu test aşaması, anormal veya potansiyel olarak kötü niyetli kullanıcı girdi koşulları altında girdi doğrulaması, modal davranışları ve kullanıcı arayüzü kararlılığına odaklanan edge testlerini içerir. Playwright ve pytest kullanılır.
Dosyayı doğru şekilde indirdiğinizden emin olun ve terminal/powershellde çalıştırmak için şu talimatı kullanın (dosya uzantısı değiştirilebilir)
python -m pytest -s edge_tests/
Edge Testing & Sonuçları
Edge Test Kodu, Test Açıklaması ve Sonuçları
Boş bir input yolladıktan sonra “Retry” tuşuna basarak modal’in açık kalmasını sağlamak. Başarısız sonuç, modal beklenmedik şekilde kapandı.
“!!!” veya “asdf” gibi inputlrı verip “Retry” butonuna bastıktan sonra modalin açık kalmasını sağlamak. Başarılı sonuç.
Modale 100+ karakteri inputu verip “Retry” butonuna bastıktan sonra modalin açık kalmasını sağlamak. Başarılı sonuç.
Modale XSS inputu verip  (<script>alert(1)</script>)  “Retry” butonuna bastıktan sonra modalin açık kalmasını sağlamak. Başarısız sonuç, modal beklenmedik şekilde kapandı.
Modale emoji inputu verip  >)  “Retry” butonuna bastıktan sonra modalin açık kalmasını sağlamak. Başarısız sonuç, modal beklenmedik şekilde kapandı.
Submit butonuna bas, işlemin ortasında modali kapat, hızlıca tekrar gönder. Başarılı sonuç.
Modale SQL inputu verip  (' OR 1=1 --)  “Retry” butonuna bastıktan sonra modalin açık kalmasını sağlamak. Başarısız sonuç, modal beklenmedik şekilde kapandı.

Bu Testlerin Ortaya Çıkardıkları: Yukarıdaki tüm başarısızlıklar web uygulamasındaki geçerli başarısızlıkları gösterir. Bu testler saldırı örneklerini ve end user kullanıcı davranışlarını (ör. spam tıklamaları, enjeksiyon dizeleri, çöp verileri) simüle eder.

Örnek çalıştırma kodu (dosya ismi ile değiştirin)
python -m pytest -s edge_tests/test_tc_e04_xss_input.py




