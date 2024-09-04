![thumbnail](/resource/thumb.png)

# 소개

이 저장소는 동국대학교 대학원에서 개발한 치안현장 맞춤형 연구개발사업(폴리스랩 2.0)을 위해 개발된 인공지능 모델 통합 시스템의 대시보드입니다.

### 폴리스랩 2.0이란?

-   국민, 경찰, 연구자 등이 협업하여 치안 현장에서 발생하는 문제를 발굴하고 첨단과학기술과 ICT융합을 통해 문제해결 및 실증
-   연구자와 사용자(경찰)간 상호작용을 촉진하기 위해 실제 환경에서 기술개발이 가능한 실증 실험실(폴리스랩\*) 구축

*   > 치안을 뜻하는 폴리스(Police)와 리빙랩(Living-Lab)의 합성어

-   치안 현장의 문제해결을 위해 실제 적용 및 검증할 수 있도록 현장에서 실증연구를 강화하여 완결성 제고

![PoliceLab 2.0](/resource/introduction.png)

## 주요기능

### 1. 시스템 모니터링

-   **CPU** : CPU 사용률을 수치 및 그래프로 시각화합니다.
-   **GPU** : GPU 사용률을 수치 및 그래프로 시각화합니다.
-   **메모리** : 메모리 사용률을 수치 및 그래프로 시각화합니다.
-   **저장소** : 저장소 사용률을 수치 및 그래프로 시각화합니다.

### 2. 컨테이너 모니터링

> 폴리스랩 2.0 시스템 구성요소(web, was, module, mysql, redis)는 Docker를 사용하여 컨테이너로 구동됩니다. 이를 모니터링하기 위한 기능입니다.

-   **pls-web** : 웹 호스팅을 위한 컨테이너 상태를 시각화합니다.
-   **pls-was** : 서비스 구동을 위한 컨테이너 상태를 시각화합니다.
-   **pls-module** : 인공지능 모듈 구동을 위한 컨테이너 상태를 시각화합니다.
-   **pls-mysql** : 기반 데이터 저장을 위한 컨테이너 상태를 시각화합니다.
-   **pls-redis** : 임시 및 캐싱 데이터 저장을 위한 컨테이너 상태를 시각화합니다.

### 3. 모듈 모니터링

-   **falldown** : 낙상을 감지하는 모듈 상태를 시각화합니다.
-   **longterm** : 장시간 고정 자세를 감지하는 모듈 상태를 시각화합니다.
-   **selfharm** : 자살 및 자해 행동을 감지하는 모듈 상태를 시각화합니다.
-   **emotion** : 감정을 분석하는 모듈 상태를 시각화합니다.
-   **violence** : 폭행을 감지하는 모듈 상태를 시각화합니다.

### 4. 엣지카메라 모니터링

> 폴리스랩 2.0 시스템은 엣지카메라로부터 원천데이터를 수집합니다. 엣지카메라는 실상 카메라, 열화상 센서, 레이더 센서, 화장실 레이더 센서를 포함하며 이를 모니터링하기 위한 기능입니다.

-   **실상 카메라** : 실상 카메라와 서버간 연결 상태를 시각화합니다.
-   **열화상 센서** : 열화상 센서와 서버간 연결 상태를 시각화합니다.
-   **레이더 센서** : 레이더 센서와 서버간 연결 상태를 시각화합니다.
-   **화장실 레이더 센서** : 화장실 레이더 센서와 서버간 연결 상태를 시각화합니다.

# 설치

### 1. 라이브러리 설치

```
python install.py
```

오프라인 환경에서 /package 디렉토리 하위에 있는 패키지로 설치됩니다. 설치가 올바르게 되지 않을 겅우 아래 명령어를 실행합니다.

```
pip install --no-index -f ./package fastapi
pip install --no-index -f ./package uvicorn
pip install --no-index -f ./package jinja2
pip install --no-index -f ./package psutil
pip install --no-index -f ./package docker
pip install --no-index -f ./package ping3
pip install --no-index -f ./package prettytable
```

대시보드 실행을 위해 아래 라이브러리가 필요합니다.

-   fastapi
-   uvicorn
-   jinja2
-   psutil
-   docker
-   ping3
-   prettytable

> 2024.09.04 수정됨

### 2. Config 수정

config.json

```
{
    "log": {
        "level": "INFO" // 개발모드 : DEBUG, 실행모드 : INFO
    },
    "edgecam": {
        "엣지카메라명": {
            "camera": "실상 카메라 IP",
            "thermal": "열화상 센서 IP",
            "rader": "레이더 센서 IP",
            "toilet_rader": "화장실 레이더 센서 IP"
        },
        ...
    }
}

```

# 실행

### 대시보드 & 모니터링

-   서버의 상태 시각화 기능을 실행합니다.
-   서버의 상태 모니터링 및 데이터베이스 기록 기능을 실행합니다.
-   Docker Desktop이 실행상태가 아니라면 자동으로 실행됩니다.(Windows만 지원)

```
uvicorn main:app --reload
```

다음 링크로 대시보드에 접속합니다.
[DASHBOARD](http://localhost:8000)
또는 https://localhost:8000

> 2024.09.04 수정됨

# 설명

### 전체 UI

![ui](/resource/ui.png)

1. 관제 화면으로 돌아가기: 클릭시 관제화면으로 이동합니다.
2. 시스템: 실시간 시스템 상태(CPU, GPU, 메모리, 저장소)를 시각화합니다.
3. 컨테이너: 실시간 컨테이너 상태를 시각화합니다.
4. 모듈: 실시간 인공지능 모듈 상태를 시각화합니다.
5. 엣지카메라: 엣지카메라 연결상태를 주기적으로 확인하여 시각화합니다.

### 시스템 컴포넌트

![system](/resource/component1.png)

1. 시스템 상태: 시스템 상태를 표시합니다. (정상: 모든 요소의 사용률 90% 미만, 위험: 일부 요소의 사용률 90~95%, 오류: 일부 요소의 사용률 95% 이상)
2. 상세 로그 보기: 시스템 로그를 불러옵니다.
3. 시스템 시각화: 실시간 시스템 사용률 및 사용률 그래프를 시각화합니다. (최근 90초동안의 데이터를 시각화합니다.)

### 컨테이너 컴포넌트

![container](/resource/component2.png)

1. 컨테이너 상태: 컨테이너 상태를 표시합니다. (정상: 모든 컨테이너 동작, 위험: 일부 컨테이너 꺼짐)
2. 상세 로그 보기: 컨테이너 로그를 불러옵니다.
3. 컨테이너 시각화: 실시간 컨테이너 동작 여부를 시각화합니다.

### 모듈 컴포넌트

![module](/resource/component3.png)

1. 모듈 상태: 모듈 상태를 표시합니다. (정상: 모든 모듈 동작, 위험: 일부 모듈 꺼짐)
2. 상세 로그 보기: 모듈 로그를 불러옵니다.
3. 모듈 시각화: 실시간 모듈 동작 여부를 시각화합니다.

### 엣지카메라 컴포넌트

![edgecam](/resource/component4.png)

1. 엣지카메라 상태: 엣지카메라 상태를 표시합니다. (정상: 모든 엣지카메라 동작, 위험: 일부 엣지카메라 꺼짐)
2. 상세 로그 보기: 엣지카메라 로그를 불러옵니다.
3. 엣지카메라 시각화: 실시간 엣지카메라 동작 여부를 시각화합니다. (Online: 연결됨, Offline: 연결 실패, None: 해당 센서 또는 정보 없음)
