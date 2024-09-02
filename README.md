# 소개

이 저장소는 동국대학교 대학원에서 개발한 치안현장 맞춤형 연구개발사업(폴리스랩 2.0)을 위해 개발된 인공지능 모델 통합 시스템의 대시보드입니다.

![thumbnail](/resource/thumb.png)

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
