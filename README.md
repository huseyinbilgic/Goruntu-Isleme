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
Concolution İşlemi

  İlk filtreyi uyguladığımızda, bir Feature Map oluşturuyor ve bir özellik türünü tespit ediyoruz. Ardından, ikinci bir filtre kullanıp başka bir özellik türünü algılayan ikinci bir Feature Map oluştururuz.

