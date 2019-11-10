# Password Generator Django Rest Service
Bu Repo . 
- Yapı.

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
Servis ilk kez çalıştırılacak ise aşağıdaki komutlar sırası ile çalıştırılmalıdır.

```
python manage.py makemigrations
```
```
python manage.py migrate
```