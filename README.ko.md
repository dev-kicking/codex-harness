# Codex Harness

> [English](README.md) | **한국어**

빈 프로젝트나 기존 프로젝트를 **Codex가 반복해서 잘 개발할 수 있는 작업 방식**으로 정리하도록 돕는 도구입니다.

## 이 저장소는 무엇인가요?

Codex Harness는 Android 라이브러리가 아닙니다. 설치한다고 앱 코드가 자동으로 수정되거나 팀 구조가 자동 생성되지는 않습니다.

대신 Codex에게 프로젝트별 개발 규칙을 만들도록 돕는 재사용 가능한 설계 도구입니다. 예를 들어 아키텍처 검토, Compose UI 작업, Gradle 문제 해결, 테스트 계획, 코드 리뷰, 릴리스 준비처럼 반복되는 작업에 사용할 수 있습니다.

쉽게 말하면 다음과 같습니다.

```text
codex-harness 저장소 = 여러 프로젝트에 쓰는 공용 설계도
내 Android 프로젝트  = Codex가 프로젝트 전용 규칙을 만드는 공간
```

## 전체 흐름은 간단합니다

1. 새 프로젝트 또는 기존 프로젝트를 준비합니다.
2. Harness를 프로젝트의 `.codex/skills/`에 설치합니다.
3. 프로젝트 루트에서 Codex를 엽니다.
4. Codex에게 Harness를 사용해 달라고 요청합니다.
5. 생성된 프로젝트 전용 스킬을 검토한 뒤, 필요한 파일만 커밋합니다.

> 설치는 공용 Harness 스킬을 복사하는 단계입니다. 팀 구조 생성이나 Android 코드 수정은 Codex에게 요청한 뒤에만 일어납니다.

## Android 프로젝트에 빠르게 적용하기

### 1. 이 저장소를 한 번만 내려받습니다

```bash
git clone https://github.com/dev-kicking/codex-harness.git ~/tools/codex-harness
```

### 2. 내 Android 프로젝트에 설치합니다

`/path/to/MyAndroidApp`을 실제 프로젝트 경로로 바꾸세요.

```bash
cd ~/tools/codex-harness
python3 scripts/install_harness.py   --scope project   --target /path/to/MyAndroidApp
```

빈 프로젝트와 이미 코드가 있는 프로젝트 모두 같은 명령을 사용합니다.

### 3. Android 프로젝트 폴더에서 Codex를 엽니다

```bash
cd /path/to/MyAndroidApp
```

이 폴더를 기준으로 평소 사용하던 방식으로 Codex를 실행하면 됩니다.

### 4. Codex에 첫 요청을 작성합니다

기존 Android 프로젝트라면 아래 예시를 그대로 시작점으로 사용하세요.

```text
Harness를 사용해서 이 Android 프로젝트의 재사용 가능한 개발 작업 방식을 구성해줘.
먼저 현재 코드와 Gradle 설정을 분석해줘.
그다음 Kotlin, Compose, 아키텍처, 빌드 도구, QA에 필요한 재사용 스킬만 판단해줘.
필요한 파일만 .codex/skills/와 docs/harness/에 생성해줘.
병렬 수정은 파일 소유권이 겹치지 않게 설계해줘.
```

빈 Android 프로젝트라면 목표와 기술 스택을 함께 알려주세요.

```text
Harness를 사용해서 새 Android 앱의 재사용 가능한 개발 방식을 설계해줘.
기술 스택은 Kotlin, Jetpack Compose, Hilt, Room, Retrofit, Gradle이야.
앱의 목적은 ... 이야.
가장 작은 유용한 스킬 세트와 팀 명세를 만들어줘.
```

## Codex가 무엇을 만들 수 있나요?

프로젝트를 분석한 뒤, 필요한 경우에만 아래처럼 프로젝트 전용 파일을 생성합니다.

```text
MyAndroidApp/
├── .codex/
│   └── skills/
│       ├── harness/                # 설치한 공용 Harness
│       ├── android-orchestrator/   # 프로젝트 전용 작업 흐름
│       ├── compose-ui/             # 필요할 때만 생성
│       ├── gradle-build/           # 필요할 때만 생성
│       └── android-qa/             # 필요할 때만 생성
├── docs/
│   └── harness/
│       └── android-development/
│           └── team-spec.md
└── AGENTS.md                       # 짧은 공통 규칙이 도움이 될 때만 생성
```

이 파일들은 앱 소스 코드가 아니라 Codex가 일하는 방식을 위한 안내입니다. 내용을 확인한 뒤 Android 프로젝트 저장소에 함께 커밋하세요.

## 일상적으로 사용하는 방법

프로젝트 전용 스킬이 만들어진 뒤에는 결과를 구체적으로 말하며 Codex에게 평소처럼 요청하면 됩니다.

```text
Android 작업 방식을 사용해서 사용자 프로필 API에 오프라인 캐싱을 추가해줘.
데이터 계층을 수정하고 테스트를 추가한 뒤 QA 단계에서 오류 상태를 검토해줘.
```

Harness는 반복 작업, 명확한 리뷰, 역할 간 인계가 필요한 프로젝트에서 특히 유용합니다. 아주 작은 일회성 수정은 Harness 없이 Codex에게 바로 요청하는 편이 더 낫습니다.

## 공용 Harness 업데이트하기

이 저장소가 업데이트된 뒤, 설치된 공용 Harness만 갱신하려면 다음을 실행하세요.

```bash
cd ~/tools/codex-harness
git pull
python3 scripts/install_harness.py   --scope project   --target /path/to/MyAndroidApp   --force
```

`--force`는 `.codex/skills/harness/`만 교체합니다. 프로젝트 전용 스킬은 이 폴더 바깥에 두면 유지됩니다.

## 이 저장소 검증하기

```bash
python3 scripts/validate.py
```

## 라이선스 및 출처

Apache License 2.0. 이 저장소는 [revfactory/harness](https://github.com/revfactory/harness)와 [SaehwanPark/meta-harness](https://github.com/SaehwanPark/meta-harness)를 바탕으로 독립적으로 구성되었습니다. 자세한 내용은 [NOTICE](NOTICE)를 참고하세요.
