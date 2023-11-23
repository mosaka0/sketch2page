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


## ENGLISH

First, you need to download Python version 3.10. If you download Python 3.10 from the Microsoft Store, the necessary configurations will be automatically made on your computer. This download method is preferable for ease of use.

Then, type - pip install django into the terminal in the project root directory (sketch2page) to include Django in the project.

To download the requirements for the latest YOLOv5 algorithm, type - cd sketch2page/converterApi/yolov5 to go to the appropriate directory, then type - pip install -r requirements.txt to download all the requirements in sketch2page\converterApi\yolov5\requirements.txt.

To run the project, type - python manage.py runserver into the terminal in the project root directory (sketch2page) to run the project. After the project is running, it can be used through the browser at localhost (http://127.0.0.1:8000).

When the user's design is uploaded to the file upload section on the main page that opens at localhost, the output will be obtained directly when the "Upload" button is clicked.