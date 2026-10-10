# 새3편 중1편 독립 원고 검토

판정: REVISE — 아래 두 곳의 최소 보강 후 재확인. 주제나 원고 구조 변경 불필요.
검토일:2026-10-10 Asia/Seoul.
파일: outputs/agent-three-1-article.md
SHA256: `e7767efb94d3582c6ec3bd92929536284ef290e4107ad2e3b61c941c38805588`
URL 제외 문자 수: 3455 (공백·Markdown 포함).

## 필수 수정

1. AI push protection 문단에 대상 라이선스와 관리자 조건 추가:
“대상은 GHSP 또는 GHAS를 구매한 GitHub Team·Enterprise Cloud 고객이며, 관리자가 활성화해야 합니다.”
현재 원고는 미리보기와 선택형 비용을 설명하지만, 해당 경로의 유료 보안 라이선스 조건은 생략되어 있다. 일반 Copilot 구독 또는 다른 GitHub 호스팅 플랜만으로 해당 기능을 사용할 수 있다는 오해를 막는 데 필요하다.

2. 고위험 유출 키 문단의 ‘신속한 대응’을 공식 우선조치로 구체화:
“공개된 활성 키나 운영용 인증 정보는 즉시 폐기를 우선합니다. 서비스 중단이 우려되면 책임자가 새 키 적용 후 기존 키를 폐기하는 순서를 정할 수 있어요.”
폐기 의미와 영향 확인은 이미 적절하다. 공개된 유효 키/운영용 인증 정보라는 고위험 상황에서 단순히 ‘책임자가 순서를 판단’한다는 표현만 남기지 않고 폐기 우선순위를 보존한다. 이는 자동 키 조작 권한이나 독자 환경별 단정이 아니다.

## 통과한 내용

- 4행 요약, 3개 주요 절, 절마다 강조 문장1개. 약3000자 분량의 쉬운 해설 구조.
- 10월7일 날짜를 보존하며 오늘 발표/24시간 이내/전체계정제공을 주장하지 않음.
- 전용 모델은 비밀정보 후보를 분류하며 코드·문장 생성과 구별됨. 모든 키 탐지를 보장하지 않음.
- 기존 AI Password 알림 모델 전환과 GHSP/GHAS 포함 요금, AI push private preview, Copilot 새분류기 coming-soon, 기본OFF/별도참여/향후AI Credits가 구별됨.
- 현행 security-review의 읽기전용 성격을 새 분류기 도입과 혼동하지 않음.
- 커밋과 푸시를 구별하고, 원격 전송 차단이 기존 로컬 이력을 제거하지 않음을 명시함.
- 파일 삭제만으로 유출 대응이 완료되지 않음을 설명함. 소유자·키제공자·의존서비스를 확인하며 자동폐기나 무조건안전을 약속하지 않음.
- 메모 앱과 후속 요청은 명시적 가정이며 실제 실행 결과 아님. 비밀값 자체를 답변에 복사하지 말라는 예시가 적절함.
- 도서 광고는 본문에 없음. 주제 gate에서 확인한 커밋·푸시 기초 목차의 관련성을 유지하며 최신 보안 대응의 권위자료로 쓰지 않음.

## 검토 시나리오·호출·관찰

시나리오: 정확한 실제 원고와 제공된 사고대응 원문 전체를 읽기.
호출: exec_command cat outputs/agent-three-1-article.md work/agent-three-1-source-remediation.txt.
관찰: 전체 본문 반환; 위 통과사항과 두 누락을 직접 확인. 캡처 artifact는 이 검토 문서 및 입력 파일이며 입력 해시는 아래에 기록.

시나리오: 공식 현재/예고 조건과 대응 우선순위 대조.
호출: 주제검토에서 직접 web.open한 아래 두 공식URL 및 이번 지정 원문 재독.
관찰: Team/GHEC paidGHSP/GHAS와 관리자 활성화, 고위험 즉시폐기 우선 및 서비스중단 고려 교체순서가 원문에 명시됨. 현재 초안에는 두 지점이 충분히 구체적이지 않음.
https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection/
https://docs.github.com/en/code-security/tutorials/remediate-leaked-secrets/remediating-a-leaked-secret

시나리오: 원고의 보충 링크와 읽기전용 설명 독립 확인.
호출: web.open https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents#built-in-agents
관찰: Built-in agents의 security-review 항목에 읽기전용 및 /security-review 호출이 명시됨. PASS.

시나리오: 정확 바이트에 검토 결과 묶기.
호출: read-only Python hashlib.sha256 및 URL 제거 정규식.
관찰: 위 SHA와 문자 수 출력. 테스트가 아닌 문서 검사. 원고 변경 없음.

실제 제품/계정/키/저장소 조작, 테스트, 매체 제작, 브라우저 UI, 게시 행동 없음. 이 지정 증거 파일만 저장함. 이 판정은 텍스트 gate이며 게시/이미지/요금 설정 확인을 뜻하지 않음.

## 입력 자료 SHA256

- work/agent-three-1-source-github.txt: `b261240af063c58a74051b16446b3aefd9cc823d0104faa122b09f4cc0de9017`
- work/agent-three-1-source-remediation.txt: `aeb709fb69df5b79d0462990bf01958146d7ffbbc25832f1b10491d33fa6effd`
- work/agent-three-1-source-book.txt: `e4a5c57708d2061cd8515f6a9b773a5b9af05ebd8e92ba0615d612ec98a3f903`


---
## 수정본 최종 검토 — READY

이 판정은 아래 새 SHA에 적용되며 이전 SHA의 REVISE를 대체한다.
SHA256: `e7767efb94d3582c6ec3bd92929536284ef290e4107ad2e3b61c941c38805588`
URL 제외 문자 수: 3455 (공백·Markdown 포함; 렌더링 가시 문자 수와는 다른 측정).

시나리오: 수정된 전체 원고를 직접 다시 읽기.
호출: exec_command cat outputs/agent-three-1-article.md.
관찰: AI push protection의 Team/Enterprise Cloud 및 유료 GHSP/GHAS·관리자 활성화 조건이 추가됨. 고위험 공개 활성 키/운영 인증 정보의 즉시 폐기 우선과 중단 우려 시 새 키 적용 후 기존 키 폐기 순서가 명시됨. 두 필수 수정 모두 PASS.

전체 원고의 현재/예고·비용 분리, 원격 전송과 로컬 이력 차이, 가정 예시, 날짜, 한계 설명을 다시 읽었으며 다른 필수 결함 없음. 4행 요약·3절·절마다 강조1개 유지. 원고 바이트는 수정하지 않음.

호출: read-only Python SHA256 및 URL 제외 문자 수 산출. 증거는 이 append 섹션. 미디어, safe-layout, 게시 표면은 이번 exact-text 검토 대상이 아니며 검증했다고 주장하지 않음. 테스트·브라우저UI·키/저장소 변경 없음.
