# Password Generator Django Rest Service
Bu projede Django Rest ile verilen parametrelere göre **rasgele** password üreten, istenirse üretilen password'lerin db ye kayıt edilmesi ve görüntü olarak kullanıcya 

## Servisin Kurulumu

Kurulum için docker kurulu olmalıdır. Docker kullanılmadan kurulum için requirements.txt içerisinde lib'ler python 3 için kurulmalıdır. Docker ile kurulum için sırası ile;

```
git clone https://github.com/zaferdurkut/password_generator_service.git
```


Projeye gidilir
```
cd password_generator_service
```
Çalışıcak servis için .env dosyasının düzelenmesi gerekmektedir.
```
cp default.env .env
```
env dosyası düzenlendikten sonra servisi başlatmak için
```
docker-compose up --build -d
```
Servis ayağa kalktından sonra servise giriş için aşağıdaki komut çalıştırılır.
```
docker exec -it password_generator_service_app_1 bash
```

## Servisin Çalıştırılması
Servise girildikten sonra django projesine girilmelidir.
```
cd password_generator
```
Servis ilk kez çalıştırılacak ise aşağıdaki komutlar sırası ile çalıştırılmalıdır. Eğer python sürümü 3 değilse (alias python='/usr/bin/python3') komutunu çalıştırınız.

```
python manage.py makemigrations
```
```
python manage.py migrate
```
Admin panele ulaşmak için super user oluşturma işlemini aşağıdaki komut ile yapabilirsiniz. (admin panel endpointini env dosyasından değiştirebilirsiniz.)
```
python manage.py createsuperuser
```
**Servisi çalıştırmak** için (eğer farklı bir porttan çıkılacak ise docker **üzerinden ilgili port dışarıya açılmalıdır.)
```
python manage.py runserver 0.0.0.0:8080
```
## Servisin Kullanımı
Servis endpointlerini görmek için [http://localhost:8080/api-docs](http://localhost:8080/api-docs) adresini kullanbilirsiniz. 
- **postman_collections** dizininde bulunan collections'lar ile servisin end pointlereini test edebilirsiniz.


### passwords - GET 
Bu method üretilip db'ye kayıt edilen kayıtları json formatında döndürür.

### create_password - GET 
Bu method ile aşağıda bulunan body ile gönderildiğinde verdiğiniz parametrelere uygun olarak random password üretir ve string olarak döndürür.
- Request Body
```
{
"use_upper" : "True",
"use_lower" : "True" ,
"use_digits" : "False",
"use_punctuation" : "False" ,
"use_space" : "False",
"additional": "" ,
"blacklist" : "" ,
"length": 22 ,
"max_duplicate_chars" :1
}
```
- Response
```
"sZKzjWfvqgxFemAIOUPXuY"
```

### create_and_save_password - GET 
Bu method ile aşağıda bulunan body ile gönderildiğinde verdiğiniz parametrelere uygun olarak random password üretir ve string olarak döndürür. Buna ek olarak üretilen password'ü db ye kayıt eder.
- Request Body
```
{
"use_upper" : "True",
"use_lower" : "True" ,
"use_digits" : "False",
"use_punctuation" : "False" ,
"use_space" : "False",
"additional": "" ,
"blacklist" : "" ,
"length": 22 ,
"max_duplicate_chars" :1
}
```
- Response
```
"sZKzjWfvqgxFemAIOUPXuY"
```

### create_password_with_image  - GET 
Bu method ile aşağıda bulunan body ile gönderildiğinde verdiğiniz parametrelere uygun olarak random password üretir ve jpeg olarak üretilen password'un bulunduğu resmi döndürür. 
- Request Body
```
{
"use_upper" : "True",
"use_lower" : "True" ,
"use_digits" : "False",
"use_punctuation" : "True" ,
"use_space" : "False",
"additional": "" ,
"blacklist" : "" ,
"length": 22 ,
"max_duplicate_chars" :2
}
```
- Response

![password](password_generator/api/static/password.jpg "password")


### create_and_save_password_with_image - GET 
Bu method ile aşağıda bulunan body ile gönderildiğinde verdiğiniz parametrelere uygun olarak random password üretir ve jpeg olarak üretilen password'un bulunduğu resmi döndürür. Buna ek olarak üretilen password'ü db ye kayıt eder.
- Request Body
```
{
"use_upper" : "True",
"use_lower" : "True" ,
"use_digits" : "False",
"use_punctuation" : "True" ,
"use_space" : "False",
"additional": "" ,
"blacklist" : "" ,
"length": 22 ,
"max_duplicate_chars" :2
}
```
- Response

![password](password_generator/api/static/password.jpg "password")
