# sketch2page

Öncelikle Python 3.10 sürümü indirilmelidir. Microsoft Store üzerinden Python 3.10'u indirmeniz durumunda bilgisayarınızda gerekli konfigürasyonlar otomatik olarak yapılacaktır, bu indirme yöntemi kolaylık açısından tercih edilebilir.

Daha sonra projenin kök klasöründe (sketch2page) terminale
	- pip install django
yazılarak Django projeye dahil edilir.

En son YOLOv5 algoritması için gerekenleri indirmek için terminale
	- cd sketch2page/converterApi/yolov5
yazılıp uygun klasöre gidildikten sonra
	- pip install -r requirements.txt 
yazılarak sketch2page\converterApi\yolov5\requirements.txt içerisindeki tüm gereksinimler indirilir.

--------------------------------------------------------------------------------------------------

Projenin çalışıtırılması için projenin kök klasöründe (sketch2page) terminale
	- python manage.py runserver
yazılarak proje çalışıtırılabilir. Proje çalıştıktan sonra localhost'ta (http://127.0.0.1:8000)
tarayıcı üzerinden kullanılabilir.

--------------------------------------------------------------------------------------------------

Localhost'ta açılan ana sayfada dosya yükleme bölümüne kullanıcı tasarımı yüklenip "Upload" butonuna basıldığında direkt olarak çıktı elde edilecektir.
