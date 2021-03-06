# Django Study Notes3

## 웹페이지 응답 순서

urls(accept request) -> views(data handling) -> template(display response)

```python
> config/urls.py
 urlpatterns = [path("", include("core.urls", namespace="core")),]

> core/urls.py
 urlpatterns = [path("", room_views.all_rooms, name="home")]

> rooms/views.py
def all_rooms(request):
    all_rooms = models.Room.object.get.all()
    return render(request, "all_rooms.html", context={"rooms": all_rooms})

> templates/all_rooms.html

```

## view를 구현하는 3가지 방법

1. Function based view

   1.1 python hard coding

   - 모든 기능을 사용자가 직접 만들어 제어하기는 쉽지만 코딩하기 어려움

     1.2 python with Django API

   - 코딩하기 번거로운 기능은 API로 불러와서 사용하고 동작 로직은 직접 코딩하여 코드만으로 동작을 파악하기 쉽고 커스터마이징 하기도 쉬움

2. Class based view

   - classy class based view (https://ccbv.co.uk/)

   - 많은 부분이 API로 제공되어 단순 설정만으로 View model을 만들 수 있지만 Abstraction 때문에 내부 동작을 파악하기 힘들고 커스터마이징하기 어려움

   - 다양한 View 제공

     - View

     - FormView

     - LoginView

## urls.py

- 사용자의 요청(user request)에 응답하는 방법을 정의함

  - HttpRequest

- url 정의 방법

```python
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
```

## views.py

- URL의 응답의 답, 대응하는 방법을 정의함

  - function 으로 이루어짐

  - HttpRequest(request)를 받아 HttpResponse를 만들어냄

  - HttpResponse로 template을 보냄

- 화면에 표시되는 것에 대한 정의

- Backend data의 형태는 model에서 정의한다

- data는 model 내의 클래스 형태로 DB에 저장된다.

- View에서는 DB의 object를 가져와서 활용하자

## template

- 파이썬이 컴파일해서 만들어 주는 html

  - 파이썬에서 지원하는 Logical 명령들을 쓸수 있음 (if, for 등)

  - 단, Logic 명령은 제한적이고 filter 기능을 통해 다양한 로직 제공 ex. {{value | add:2 }}

- views.py는 template 에세 context를 통해 data를 전달할 수 있음

  - views.py 에서 핸들한 data를 context로 Template 에 보내 html로 표시할 수 있게함

- base.html 을 만들고 확장하여 다른 페이지 적용할 수 있음. 일종의 상속 계념

  ```html
  {% block block_name %} {% endblock block_name %}
  ```

- 반대로 base.html에서 하위 페이지의 내용을 가져올 수 있음

  ```html
  {% include "path/small.html" %}
  ```

## forms.py

- HTTP 형식의 Form을 정의하는 곳

- 기본 forms를 이용하여 만들 수 있음

- Modelform : model의 정보와 연결된 form

* Paginator

# HTML

## form

- 웹페이지의 입력 양식

### input

- 입력 방법 설정

- type 입력 속성, name 이름, value 기본값 등을 지정

### select & option

- 드롭다운 리스트 생성

- option 태그 안에 드롭다운 리스트 요소를 설정하여 사용함

```html
<select>
  <option value="ktx">KTX</option>
  <option value="itx">ITX 새마을</option>
  <option value="mugung">무궁화호</option>
</select>
```
