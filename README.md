# pyenv virtualenv을 이용하여 poetry로 만들어진 프로젝트를 설치하기

이제 지금까지 설치한 것을 설치한 것을 토대로 이미 poetry로 만들어진 프로젝트를 사용해보겠습니다. 제가 연습하기 위해 만들 프로젝트를 가져와보겠습니다.

```sh
git clone https://github.com/dialektike/poetry_test.git
```

앞 코드의 실행화면은 다음과 같습니다. 코드가 변경되면 내용이 달라질 수도 있으니 참고하세요!

```sh
pi@4:~ $ git clone https://github.com/dialektike/poetry_test.git
Cloning into 'poetry_test'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 14 (delta 3), reused 10 (delta 2), pack-reused 0
Unpacking objects: 100% (14/14), done.
```

현재 제가 사용하고 있는 라즈베리파이에는 다음과 같이 `pip`도 설치 되어 있지 않은 상태입니다.

```sh
pi@4:~ $ pip
pyenv: pip: command not found

The `pip' command exists in these Python versions:
  3.7.9
  3.9.1

Note: See 'pyenv help global' for tips on allowing both
      python2 and python3 to be found.
pi@4:~ $ pip3
pyenv: pip3: command not found

The `pip3' command exists in these Python versions:
  3.7.9
  3.9.1

Note: See 'pyenv help global' for tips on allowing both
      python2 and python3 to be found.
pi@4:~ $
```

현재 프로젝트는 파이썬 3.9 이상을 요구합니다. 그리고 몇가지 패키지도 설치되어 있습니다. 이런 패키지들은 `pip`로 설치해해야 합니다. 그러나 앞에서 본 것처럼 `pip`는 설치되어 있지 않습니다.

```sh
[tool.poetry]
name = "poetry_test"
version = "0.1.0"
description = ""
authors = ["Jaehwan <dialektike@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.25.1"
bs4 = "^0.0.1"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

그래서 직접 설치하려고 앞에서 다운받은 프로젝트를 다음과 같이 인스톨하려고 해도 다음과 같이 에러가 납니다.

```sh
pi@4:~/poetry_test $ poetry install

The currently activated Python version 2.7.16 is not supported by the project (^3.9).
Trying to find and use a compatible version. 

NoCompatiblePythonVersionFound

Poetry was unable to find a compatible version. If you have one, you can explicitly use it via the "env use" command.
```

이제 앞에서 설치한 python 3.9.1을 사용할 차례입니다. `poetry`에서 `pyenv local`을 써서 다른 파이썬을 사용하면, `poetry`이 `kbo-data-Kwn6h-Dl-py3.7`과 같이 괴상한 이름으로 가상환경을 만듭니다. 그래서 직접 `pyenv`을 이용하여 다음과 같은 명령어로 가상환경을 만들어 사용하겠습니다. 

```sh
pyenv virtualenv 3.9.1 poetry_test
```

확인해봅시다. 가상환경이 하나 만들어진 것을 확인할 수 있습니다.

```sh
pi@4:~/poetry_test $ ls ~/.pyenv/versions/
3.7.9  3.9.1  poetry_test
```

그러면 앞에서 만든 python 3.9.1 용 가상 환경인 `poetry\_test`을 다음과 같은 명령어로  활성화(activate)시켜보겠습니다.

```sh
pyenv activate poetry_test
```

결과는 다음과 같습니다. python을 실행시켜 보면 3.9.1 버젼이 작동하는 것을 보실 수 있습니다.

```sh
pi@4:~/poetry_test $ pyenv activate poetry_test
pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
(poetry_test) pi@4:~/poetry_test $ python
Python 3.9.1 (default, Feb 18 2021, 07:10:45) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

그리고 현재 앞에 `(poetry\_test)`이라고 나오는 것도 가상환경이라는 것을 알려주는 것입니다.

```sh
(poetry_test) pi@4:~/poetry_test $
```

자 이제 앞에서 안 된 프로젝트를 설치해보겠습니다. 앞에서 다운받은 프로젝트 폴더에서 `poetry install`이라고 입력하시면 됩니다. 앞에서는 애러가 났지만, 이번에는 다음과 같이 제대로 작동할 것입니다.

```sh
(poetry_test) pi@4:~/poetry_test $ poetry install
Installing dependencies from lock file

Package operations: 8 installs, 0 updates, 0 removals

  • Installing soupsieve (2.2)
  • Installing beautifulsoup4 (4.9.3)
  • Installing certifi (2020.12.5)
  • Installing chardet (4.0.0)
  • Installing idna (2.10)
  • Installing urllib3 (1.26.3)
  • Installing bs4 (0.0.1)
  • Installing requests (2.25.1)
```

현재 이 프로젝트에 설치되 있는 패키지를 이쁘게 보시려면 `poetry show —tree`을 사용하면 됩니다. 터미널에서 보시면 더 이쁘게 보입니다.

```sh
(poetry_test) pi@4:~/poetry_test $ poetry show --tree
bs4 0.0.1 Dummy package for Beautiful Soup
└── beautifulsoup4 *
    └── soupsieve >1.2 
requests 2.25.1 Python HTTP for Humans.
├── certifi >=2017.4.17
├── chardet >=3.0.2,<5
├── idna >=2.5,<3
└── urllib3 >=1.21.1,<1.27
```

자 이제 받은 프로젝트를 실행시킬 시간입니다. `python test.py`을 실행하시면 됩니다. 그러면 `result.json` 파일이 생긴 것을 확인하실 수 있습니다. 이 프로젝트는 크롤링하는 코드를 가지고 있었습니다.

```sh
(poetry_test) pi@4:~/poetry_test $ python test.py
(poetry_test) pi@4:~/poetry_test $ ls
poetry.lock  pyproject.toml  README.md  result.json  test.py
```

`result.json` 파일을 확인하면 다음과 같습니다. `result.json`은 각자 편한 방법으로 보시면 됩니다.

```json
(poetry_test) pi@4:~/poetry_test $ cat result.json |jq
{
  "나만의 웹 크롤러 만들기(4): Django로 크롤링한 데이터 저장하기": "/beomi.github.io_old/python/2017/02/28/HowToMakeWebCrawler-Save-with-Django.html",
  "나만의 웹 크롤러 만들기(3): Selenium으로 무적 크롤러 만들기": "/beomi.github.io_old/python/2017/02/27/HowToMakeWebCrawler-With-Selenium.html",
  "Django에 Social Login 붙이기: Django세팅부터 Facebook/Google 개발 설정까지": "/beomi.github.io_old/python/2017/02/08/Setup-SocialAuth-for-Django.html",
  "Django에 Custom인증 붙이기": "/beomi.github.io_old/python/2017/02/01/Django-CustomAuth.html",
  "나만의 웹 크롤러 만들기(2): Login with Session": "/beomi.github.io_old/python/2017/01/20/HowToMakeWebCrawler-With-Login.html",
  "나만의 웹 크롤러 만들기 with Requests/BeautifulSoup": "/beomi.github.io_old/python/2017/01/19/HowToMakeWebCrawler.html",
  "Celery로 TelegramBot 알림 보내기": "/beomi.github.io_old/2016/12/27/TelegramBot-with-Celery.html",
  "Virtualenv/VirtualenvWrapper OS별 설치&이용법": "/beomi.github.io_old/2016/12/27/HowToSetup-Virtualenv-VirtualenvWrapper.html",
  "[DjangoTDDStudy] #02: UnitTest 이용해 기능 테스트 하기": "/beomi.github.io_old/djangotddstudy/2016/12/26/Django-TDD-Study-02-Using-UnitTest.html",
  "[DjangoTDDStudy] #01: 개발환경 세팅하기(Selenium / ChromeDriver)": "/beomi.github.io_old/djangotddstudy/2016/12/26/Django-TDD-Study-01-Setting-DevEnviron.html",
  "[DjangoTDDStudy] #00: 스터디를 시작하며": "/beomi.github.io_old/djangotddstudy/2016/12/26/Django-TDD-Study-00-Starting-Study.html",
  "Fabric Put 커맨드가 No Such File Exception을 반환할 때 해결법": "/beomi.github.io_old/2016/12/21/Fabric-Put-Command-No-Such-File-Exception.html",
  "CKEditor의 라이센스와 오픈소스 라이센스": "/beomi.github.io_old/2016/12/21/CKEditor-Lisence-and-Pricing.html",
  "ReactNative The Basis 번역을 끝냈습니다.": "/beomi.github.io_old/translation/2016/12/20/ReactNative-Translation-Intro-Finish.html",
  "[React Native 번역]#01: 시작하기": "/beomi.github.io_old/translation/2016/11/15/ReactNative-Translation-01-getting-started.html",
  "[번역] 장고(Django)와 함께하는 Celery 첫걸음": "/beomi.github.io_old/django-celery/programming/python/translation/2016/11/04/eb-b2-88-ec-97-ad-ec-9e-a5-ea-b3-a0django-ec-99-80-ed-95-a8-ea-bb-98-ed-95-98-eb-8a-94-celery-ec-b2-ab-ea-b1-b8-ec-9d-8c.html",
  "Chrome Native Adblockr 대체하기": "/beomi.github.io_old/tech/2016/09/14/chrome-native-adblockr-eb-8c-80-ec-b2-b4-ed-95-98-ea-b8-b0.html",
  "CustoMac 설치 분투기": "/beomi.github.io_old/dev%20env%20setup/mac%20/%20os%20x/tech/2016/08/09/customac-ec-84-a4-ec-b9-98-eb-b6-84-ed-88-ac-ea-b8-b0.html",
  "Ubuntu14.04에 OhMyZsh 설치": "/beomi.github.io_old/dev%20env%20setup/tech/ubuntu%20/%20debian/2016/07/22/ubuntu14-04-ec-97-90-ohmyzsh-ec-84-a4-ec-b9-98.html",
  "Ubuntu14.04에서 pip로 mysqlclient 설치 실패시": "/beomi.github.io_old/programming/python/tech/2016/07/22/ubuntu14-04-ec-97-90-ec-84-9c-pip-eb-a1-9c-mysqlclient-ec-84-a4-ec-b9-98-ec-8b-a4-ed-8c-a8-ec-8b-9c.html",
  "Ubuntu14.04에서 Python3기반 virtualenvwrapper 설치": "/beomi.github.io_old/mac%20/%20os%20x/programming/python/tech/2016/07/22/ubuntu14-04-ec-97-90-ec-84-9c-python3-ea-b8-b0-eb-b0-98-virtualenvwrapper-ec-84-a4-ec-b9-98.html",
  "mac OS X에서 pip virtualenvwrapper 설치 시 uninstalling six 에서 Exception 발생 시": "/beomi.github.io_old/mac%20/%20os%20x/programming/python/tech/2016/07/21/mac-os-x-ec-97-90-ec-84-9c-pip-virtualenvwrapper-ec-84-a4-ec-b9-98-ec-8b-9c-uninstalling-six-ec-97-90-ec-84-9c-exception-eb-b0-9c-ec-83-9d-ec-8b-9c.html",
  "Fabric for Python3 (Fabric3)": "/beomi.github.io_old/programming/python/2016/07/17/fabric-for-python3-fabric3.html",
  "Windows에서 pip로 mysqlclient 설치 실패시(python3.4/3.5)": "/beomi.github.io_old/programming/python/2016/06/04/windows-ec-97-90-ec-84-9c-pip-eb-a1-9c-mysqlclient-ec-84-a4-ec-b9-98-ec-8b-a4-ed-8c-a8-ec-8b-9cpython3-43-5.html",
  "맥에서 윈도RDP로 접속시 한영전환하기.": "/beomi.github.io_old/mac%20/%20os%20x/tech/2016/05/27/eb-a7-a5-ec-97-90-ec-84-9c-ec-9c-88-eb-8f-84rdp-eb-a1-9c-ec-a0-91-ec-86-8d-ec-8b-9c-ed-95-9c-ec-98-81-ec-a0-84-ed-99-98-ed-95-98-ea-b8-b0.html",
  "pip로 mysqlclient설치 중 mac os x에서 egg_info / OSError 발생시 대처방법": "/beomi.github.io_old/programming/python/2016/05/27/pip-eb-a1-9c-mysqlclient-ec-84-a4-ec-b9-98-ec-a4-91-mac-os-x-ec-97-90-ec-84-9c-egg_info-oserror-eb-b0-9c-ec-83-9d-ec-8b-9c-eb-8c-80-ec-b2-98-eb-b0-a9-eb-b2-95.html"
}
```

가상환경에서 나가시려면 `pyenv deactivate`이라고 하시면 됩니다. 나가시면 아래와 같이 `python`이 버젼이 변해있는 것을 확인하실 수 있습니다. 당연히 앞에서 실행되었던 것도 아래와 같이 작동하지 않습니다. 다시 `pyenv activate poetry\_test`로 활성화해서 들어가면 작동합니다.

```sh
(poetry_test) pi@4:~/poetry_test $ pyenv deactivate
pi@4:~/poetry_test $ python
Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
pi@4:~/poetry_test $ python test.py
  File "test.py", line 1
SyntaxError: Non-ASCII character '\xec' in file test.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
