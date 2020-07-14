# Django Study notes2

- 프로그래머는 Library 불러와서 자신의 코드가 Library를 쓸 수 있음

- 프로그래머는 Framework에 코드를 작성하여 Framework가 자신의 코드를 실행할 수 있게함

## ORM(object relational mapper)

- python code를 SQL문으로 바꿔 DB에 저장함

## Python skills

### Method Override

- 이미 존재하는 class를 상속받아서 class 내부에 있는 method를 재정의하는 것

### super()

- 자식 class가 부모 class에 접근하여 method 접근 가능

- 주로 override를 통해 재정의 후 부모 클래스의 원본 클래도 같이 활용하기 위해 사용

### try & except

- error 처리를 위한 루틴

- try 를 해보고 error가 발생하면 except이 실행됨

## settings.py

- from django.conf import settings : 다른 모델, 파일에서 settings.py를 import를 하고 싶을 떄 사용

## urls.py

- url과 관련된 설정을 함

### media 파일 관리

- MEDIA_ROOT: media 파일의 루투를 지정

- MEDIA_URL: MEDIA_ROOT 폴더의 이름을 지정할 수 있음 -> Media root 를 상대경로로 사용할 수 있게 됨

- 모델에서 파일을 다루는 필드를 다룰때, upload_to 옵션을 주면 파일을 업로드할 저장소를 지정할 수 있음

- 개발모드 (DEBUG= True) 일때는 서버 소스 코드 저장공간에 저정할 수 있지만,

- 프로덕션 모드 (DEBUG= False) 일때는 서버 내 다른 저장공간을 이용하는 것이 좋음 -> 소스코드와 사용자 데이터를 구분!

## Models.py

- models.Model : Django에서 정의한 DB와 소통하기 위한 구조체

- models 안애는 Textfield, Emailfield 등 많은 데이터형식이 미리 정의되어 있음.

- 각 필드는 필드에 맞는 적절한 데이터 유효성 및 포멧을 정하고 있고 입력 방법을 제공함(imagefiled, datefield 등..)

- 각 필드는 default="" 값을 갖거나 null=True 로 정의하여 비워둘 수 있도록 정의해야 함

- file과 관련된 필드는 upload_to 옵션을 이용해서 파일을 저장할 위치를 정할 수 있음(ex. ImageField)

1. models 안에 정의된 필드를 앱의 models."class" 안에 정의하고

2. python manage.py makemigrations 로 migration 파일을 만들고

3. python manage.py migrate로 SQLight3 DB에 적용하면 웹페이지 표시됨

### Abstract model

- 다른 앱의 모델에서 상속받아 공통으로 사용할 모델을 정의함

- abstract model은 DB에 포함되지 않음

### Foreign Key

- 서로 다른 앱의 모델끼리 연결해줌

- many-to-one 관계 (Many rooms - One user)

- Foreign key를 사용하면 다른 앱의 모델에 있는 데이터를 가져와서 쓸 수 있음(가여오는 모델의 id 번호를 가져와서 링크함)

- 따라서, one 에 종속된 many 객체들의 데이터를 one 이 지워질때 같이 지울지(CASCADE), 보호할지(PROTECT) 등을 지정할 수 있음

```python
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
```

위와 같이 접근하면 room 객체를 통해 rooms.Room의 모델내에 있는 데이터를 모두 접근하여 사용할 수 있음

- relation은 chain 처럼 엮어서 사용할 수 있음

  "app1.var -> (app2.var -> app3.var)" 이런식의 관계를 가지면 app1 이 app3의 정보까지 접근가능

- app1.var1 -> app2.var2 으로 ForeignKey를 생성하면 app2.var2 또한 app1.var1에 접근할 수 있게 됨

  -> Django의 app2.var2 모델이 python Object로 변환되면서 var1_set 형태로 DB 정보를 갖게 됨

  -> var1_set은 모델에서 ForeignKey를 사용할 때 "related_name" 으로 이름을 재정의 할 수 있다.

  --> 따라서 아래와 같이 related_name을 지정하는 것은 현재 app1.var1 이 아닌 app2.var2 에서 app1.var1의 이름을 지정하는 것이라 이애할 수 있다

  ```python
      host = models.ForeignKey(
      "users.User", related_name="rooms", on_delete=models.CASCADE
  )
  ```

### ManytoManyField

- 서로 다른 앱의 모델끼리 연결해줌 -> 데이터를 가져다 쓸 수 있음

- many-to-many 관계에 쓸수 있음 -> 다른 데이터에서 여러개의 데이터를 선택하여 적용

- manytomany 도 ForeignKey와 마찬가지로 app1.va1 -> app2.var2 으로 지정하면 역방향으로도 정보 접근이 가능

  -> var1 이름으로 바로 접근가능

## admin.py

- Django가 제공하는 기본 사용자 웹페이지

- models.py에 정의된 데이터를 표시할 수 있음

  1. models."class_name"을 등록하고

  2. admin.py 내에 "custom class"를 정의하여 어떤 방식으로 표현할 지를 코딩할 수 있음

```python
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    pass
```

- admin.py 에 함수를 넣으면 admin에서만 쓸 수 있지만 models.py에 넣으면 모든 곳에 쓸수 있다.

### list

- 기본적으로 Django.contrib 에 정의된 항목들이 있어 사용할 수 있음(auth, user, group 등)

- list_display, list_filter 로 admin 패널 1차 페이지에 나오는 정보를 수정할 수 있음

### serch_fields

- 검색 창

```python
    search_fields = ("city", "host__username")
```

        - city 를 검색대상에 넣음

        - host는 app1에서 app2의 models를 가져온 것으로 가져온 model 내의 username을 검색 대상으로 함

### filter_horizontal

- 검색하여 원하는 항목만 선택하여 적용 수 있음

### fieldsets

- models.py 의 항목들을 그룹으로 묶어서 나타낼 수 있음

### raw_id_fields

- 리스트에 항목이 너무 많을 때 id로 관리할 수 있게 해줌

- 적용하면 별도의 작은 admin panel이 따로 생성됨

### Inline Admin

- Admin panel 안에 또 다른 모델의 admin 패널을 불러와 조작할 수 있음

- 하나의 Admin panel은 하나의 모델을 등록하여 사용하는데, 외부의 모델을 InlineAmin 클래스를 만들어서 표시하고자 하는 Admin panel에서 Inlines 으로 등록하면 외부 모델의 정보를 조회, 수정할 수 있음

- 이를 위해서는, 사용하는 두 모델이 foreignKey로 연결되어 있어야 하며, 나머지는 Django가 처리해 줌

- InlineAdmin 클래스는 TabularInline, StackInline 등의 종료가 있음 -> 표시 방식의 차이

```python
class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)
```

## save() & save_model() Overrideing

- save() 함수는 모든 모델에 기존적으로 존재하는 method

- 자신의 model 이 저장되는 시점에 데이터를 변경하거나 데이터의 내용에 따라 다른 반응을 주기 위해 save() 함수를 overriding 해서 사용함

- save() 함수는 admin, view, consloe 모든 곳에서 저장할 때마다 호출된다.

- save_model()은 admin panel에서 저장시 호출되는 것으로 admin에서 데이터를 저장할 때만 호출되어 먼저 실행되고 save() 함수를 실행하여 모델의 데이터를 저장한다.

- save_model()의 경우, admin panel을 사용하는 사용자에 따라 저장시 다른 동작을 취할 때 많이 사용됨. (ex. 특정 사용자가 저장하면 이메일로 알림 등..)

- overriding 할 때는 commit=False 옵션을 통해 object만 생성한 후 DB에 올리지 않은 상태에서 object내의 인자값을 수정하고 추가한 후 super.save()를 실행하여 저장한다.

```python
def save(self, *args, **kwargs):
        #object 생성
        user = super().save(commit=False)

        #저장할 값 읽어오기
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        #object에 값 넣기
        user.username = email
        user.set_password(password)

        #object를 DB에 저장
        user.save()
```

## Custom command 만들기

1. "app_name"/management/commands/ 폴더 만들기

2. 새로 만든 폴더에 "**init**.py" 를 추가해서 python 폴더로 인식되게 하기

3. commands 폴더내에 원하는 command 이름으로 py 파일 만들기 "command_name".py

4. BaseCommand 를 활용해서 command 만들기

   4.1 add_arguments 로 옵션 넣을 수 있음(parser 지원함)

   4.2 handle에 원하는 동작 코딩

```python
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'This command tells me "love you"'

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times tell you?")

    def handle(self, *args, **options):
        times = options.get("times")

        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I Love you"))

```

### seed_amenities.py 예제

[핵심코드]

- Amenity.objects.create: Amenity 모델의 object를 만듬

```python
from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    amenities = [
        "TV",
        "aircon",
        ...
    ]

    for a in amenities:
            Amenity.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Amenities Created!"))
```

## Django_seed

```bash
 pipenv install django_seed
```

- Third party app 으로 가짜 데이터를 랜덤하게 만들어주는 역할을 함

- faker 모듈을 사용함

- model의 필드 종류를 인식하고 적당히 데이터를 넣어줌

- 랜덤으로 생성시 고정하길 원하는 옵션은 지정하여 넣을 수 있음

  > seed_users.py 참고

- 단, foreignkey로 연결된 모델의 object 정보까지는 알 수 없기 때문에, 해당 항목은 직접 작성이 필요함

  > seed_rooms.py 참고
