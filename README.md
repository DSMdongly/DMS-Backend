# Project-DMS-Backend  [![Build Status](https://travis-ci.org/DSM-DMS/Project-DMS-Backend.svg?branch=master)](https://travis-ci.org/DSM-DMS/Project-DMS-Backend) [![Coverage Status](https://coveralls.io/repos/github/DSM-DMS/Project-DMS-Backend/badge.svg?branch=master)](https://coveralls.io/github/DSM-DMS/Project-DMS-Backend?branch=master) [![works badge](https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)
## About
DMS 프로젝트의 2017년 12월 리메이크 일정에 의해 만들어진 백엔드 포지션의 Repository입니다.

### Technical Stacks
- Python
- Flask
- MongoDB
- JWT, ODM, Swagger, Cafe24, etc.

### Infrastructure
- 적용됨 : Git, Travis-CI, Coveralls
- 빠른 시일 내에 적용할 예정 : Docker(서버 형상관리)
- 적용하고 싶음 : JIRA(이슈 관리), AWS CloudFormation(인프라 형상관리), JSON 형태의 logging, ELK 또는 Splunk(실시간 로그 분석), Hadoop(일괄 로그 분석)

### 프로젝트 진행
1. Travis-CI를 이용한 TDD 기반으로 진행하며, 이를 위해 Flask 어플리케이션의 구조를 테스트에 알맞게 설계해 두었습니다.
~~~
|- app/
    |- __init__.py
    |- docs/
        |- __init__.py
    |- models/
        |- __init__.py
    |- static/
        |- css/
        |- img/
        |- js/
    |- templates/
        |- 403.html
        |- 404.html
        |- etc.
    |- views/
        |- __init__.py
    |- middleware.py
|- config/
    |- __init__.py
    |- dev.py
    |- production.py
|- tests/
    |- __init__.py
    |- mocks/
        |- __init__.py
    |- models/
        |- __init__.py
    |- views/
        |- __init__.py
|- server.py
~~~
2. Lint 적용을 위해 Flake8을 사용합니다.
3. requirements.txt 생성을 위해 pigar를 사용합니다.

### Rules
- 무조건 짧은 코드보단 유지보수 가능하며 명시적인 코드 작성을 지향합니다. 컨벤션은 기본적으로 모두 PEP8을 따릅니다.
- API 구현은 Model 검증 - Swagger - TC - API 순으로 작성하는 것을 원칙으로 합니다.
#### Model
- app/models 하위에 구현합니다.
- 상속 가능한 Base Model은 ***Base 형태로 네이밍합니다. Travis 빌드에서 오류가 나지 않도록 meta 필드에서 'abstract'를 True로 두어야 합니다. ex) AccountBase
- Model은 ***Model 형태로 네이밍합니다. ex) StudentModel
- 필드 정의 시 파라미터는 키워드 형태로 넘겨줍니다. ex) ReferenceField(document_type=StudentModel, required=True)
#### Swagger
- app/docs 하위에 구현합니다.
- 딕셔너리 상수는 APINAME_METHOD 방식으로 네이밍합니다. 여기서 APINAME은 해당 API의 클래스 이름에 영향을 받습니다. ex) FAQManaging 클래스의 patch 메소드라면 FAQ_MANAGING_PATCH
- 가독성 높은 Swagger doc을 산출해내기 위해 Swagger template에 명시해두지 않은 태그를 사용하지 않습니다.
#### TC
- tests/ 하위에 구현합니다.
- 모든 TC는 DB가 완전히 비어있다고 가정합니다.
- TC에서 request를 보낼 경우 무조건 Status code assertion을 합니다.
- unittest는 TC들을 사전식으로 실행하므로 TC 작성 시 메소드 네이밍은 test[A|B|C|...]_what으로 합니다. ex) testA_signup(self), testB_getNoticeList(self)
- 모든 TC 메소드에 docstring을 남깁니다. preparations, process, validation으로 나누어 정리하여 테스트 스켈레톤을 작성한 뒤 리뷰를 한 번 거치고 실제로 TC를 작성하도록 합니다.
#### API
- app/views 하위에 구현합니다.
- REST API입니다.
- Flask-restful 패키지를 사용하여 클래스 단위로 URI를, 메소드 단위로 HTTP Method를 분할합니다.
- 메소드는 GET - POST - PUT - PATCH - DELETE 순서로 정리하는 것을 원칙으로 하나, API의 flow가 중요하다면 정렬을 바꾸어도 좋습니다.
- Swagger와 TC에 미리 명시하거나 작성해 두지 않은 구현이 필요하다면, Swagger 단계로 돌아가 처음부터 다시 진행합니다.

### 특수한 전제
#### 연장신청
- 11시 연장신청은 매일 오후 5시 30분부터 8시 30분까지
- 12시 연장신청은 매일 오후 5시 30분부터 10시까지
#### 외출신청
- 확실히 정해진 조건 없음
#### 잔류신청
- 매주 일요일 오후 8시 30분부터 목요일 오후 10시까지
#### 설문조사
- 한번 업로드한 설문조사는 수정 불가능

## Contributors
- <a href="https://github.com/JoMingyu">2기 조민규</a>
- <a href="https://github.com/RISMME">3기 인상민</a>
