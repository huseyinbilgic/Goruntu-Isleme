# CNN

## Convolutional Layer

  Bu katman CNN’nin ana yapı taşıdır. Resmin özelliklerini algılamaktan sorumludur. Bu katman, görüntüdeki düşük ve yüksek seviyeli özellikleri çıkarmak için resme bazı fitreler uygular. Örneğin, bu filtre kenarları algılayacak bir filtre olabilir. Bu filtreler genellikle çok boyutludur ve piksel değerleri içerirler.(5x5x3) 5 matrisin yükseklik ve genişliğini, 3 matrisin derinliğini temsil eder.

Filtrenin uygulamasına bakacak  olursak;

![ornek1](https://user-images.githubusercontent.com/24252338/71308836-47c00800-2412-11ea-90c7-230ffa82ffe8.png) --->
Örnek resim

  Resimin 5×5 boyutunda ve 1 ve 0 ‘lardan oluşan bir resim olduğunu varsayalım. Filtremizi 3×3 boyutunda oluşturalım.

![filtre](https://user-images.githubusercontent.com/24252338/71308846-61614f80-2412-11ea-8b15-839951d0b71a.png) --->
Filtre

Şimdi, filtrenin nasıl uygulandığına bir bakalım,

![orr](https://user-images.githubusercontent.com/24252338/71308880-a4bbbe00-2412-11ea-9798-13e582b9f7f3.gif) ---> 
Filtrenin Uygulaması

  Öncelikle, filtre görüntünün sol üst köşesine konumlandırılır. Burada, iki matris arasında (resim ve filtre) indisler birbirisi ile çarpılır ve tüm sonuçlar toplanır, daha sonra sonucu çıktı matrisine depolanır. Ardından, bu filtreyi sağa 1 piksel (“basamak” olarak da bilinir) kadar hareket ettirip işlemi tekrarlanır. 1. Satır bittikten sonra 2 satıra geçilir ve işlemler tekrarlanır. Tüm işlemler bittikten sonra çıktı matrisi oluşturulur. Burada çıktı matrisinin 3×3 olmasının nedeni 5×5 matrisinde 3×3 filtresi yatayda ve dikeyde 3 kez hareket etmesinden kaynaklanır.
Eğer resim 6×4 ve filtre 3×3 boyutunda olsaydı çıkış matrisi 4×2 boyutunda olurdu.

  Oluşan bu matrise genellikle Feature Map denir. Filtre tarafından temsil edilen özellikte görüntünün bulunduğu yeri gösterir. Kısacası, filtreyi görüntü üzerinden hareket ettirerek ve basit matris çarpımını kullanarak, özelliklerimizi tespit ediyoruz.
Genellikle, birden çok özelliği tespit etmek için birden fazla filtre kullanlır, yani bir Cnn ağında birden fazla Convolutional katman bulunur.


![uygulaması](https://user-images.githubusercontent.com/24252338/71308926-15fb7100-2413-11ea-925f-bb517af79ead.gif) --->
Convolution İşlemi

 İlk filtreyi uyguladığımızda, bir Feature Map oluşturuyor ve bir özellik türünü tespit ediyoruz. Ardından, ikinci bir filtre kullanıp başka bir özellik türünü algılayan ikinci bir Feature Map oluştururuz.

![ornekfiltreler](https://user-images.githubusercontent.com/24252338/71308979-a8037980-2413-11ea-8033-c6b0bb457f0b.png) --->
Örnek Filtreler

 ### Stride (büyük adım) 
 
 Bu terim genellikle padding terimi ile birlikte kullanılır. Stride, filtrenin giriş görüntüsünün etrafında nasıl evrildiğinini denetler. Yukarıdaki örnekte Stride 1 piksel idi, ancak daha büyük olabilir. Bu, Feature Map’in çıktısının boyutunu etkiler.
 
  Cnn’nin ilk aşamalarında, ilk filtreleri uygularken, diğer Convolutional Katmanlar için mümkün olduğunca çok bilgiyi korumamız gerekir. İşte padding bu nedenden dolayı kullanılır. Feature Map’in orijinal giriş görüntüsünden daha küçük olduğu fark edilebilir. Bu nedenle Padding, (aşağıdaki resimde olduğu gibi)resmin boyutunu korumak için bu haritaya sıfır değerler katacaktır.
  
  
![paddingli](https://user-images.githubusercontent.com/24252338/71309020-2d872980-2414-11ea-9ce2-b740d3ccc424.png) --->
Padding

### Non-linearity
  
Tüm Convolutional katmanlarından sonra genellikle Non-Linearity(doğrusal olmayan) katmanı gellir. Peki görüntüdeki doğrusallık neden bir problemdir? Sorun şu ki, tüm katmanlar doğrusal bir fonksiyon olabildiğinden dolayı Sinir Ağı tek bir perception gibi davranır, yani sonuç, çıktıların linear kombinasyonu olarak hesaplanabilir.
Bu katman aktivasyon katmanı (Activation Layer) olarak adlandırılır çünkü aktivasyon fonksiyonlarından birini kullanılır. Geçmişte, sigmoid ve tahn gibi doğrusal olmayan fonksiyonlar kullanıldı, ancak Sinir Ağı eğitiminin hızı konusunda en iyi sonucu Rectifier(ReLu) fonksiyonu verdiği için artık bu fonksiyon kullanılmaya başlanmıştır.

#### ReLu Fonksiyonu f (x) = max (0, x)

ReLu fonksiyonunun Feature Map’a uygulandığında aşağıdaki gibi bir sonuç üretilir.


![off](https://user-images.githubusercontent.com/24252338/71309063-979fce80-2414-11ea-8618-3e40f2b361ce.png)

Feature Map’taki siyah değerler negatiftir. Relu fonksiyonu uygulandıktan sonra siyah değerler kaldırılır onun yerine 0 konur.


