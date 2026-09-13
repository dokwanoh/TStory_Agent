# 게시 운영의 프로그램 자동화 전환 분석

상태: 의사결정용 분석 완료, 구현/채택 전. 기준일 2026-09-13 KST. 산출물은 오너가 승인한 채팅 요약 + Markdown. 설치·신규 API 비용·로그인 프로필 변경·게시·기존 예약 변경은 이번 범위 밖이다.

## 조사 기록과 한계

- 질문: 매 게시마다 사람 및 대화형 에이전트가 개입하지 않고, 현재 품질 계약을 유지할 수 있는 최소 자동화 구조는 무엇인가?
- 비교 축: 기존 구현/운영 간극, 브라우저 입력, 지속 실행/복구, 콘텐츠 생성/검증, 운영·보안·비용.
- 연구 스킬의 추가 에이전트 실행은 기존 fan-out 한도로 차단됐다. 한도/권한을 변경하지 않고 주 에이전트가 읽기 전용 조사를 수행한다. 포화 병렬 조사 완료로 주장하지 않는다.
- 1차: pyproject.toml, docs/05_architecture.md, docs/18_scheduled_publishing.md, STATUS.md, OWNER_INPUT.md, AGENTS.md, pipeline/orchestrator.py, pipeline/draft.py, domain/state.py 확인. Python 무의존성 offline pipeline은 존재하나 실제 모델 생성/브라우저 게시 런타임은 아니다. draft.py는 입력 summary/claim을 조합하며 state는 ready_for_approval에서 끝난다.
- 1차 공식문서: Playwright 입력/프로필, Chrome 원격 디버깅, FastAPI background tasks, Prefect retries/transactions, Temporal, APScheduler. 2차 확장: Stagehand v3 Python/캐시, Browser Use code agent/Cloud v3 script cache, Restate 지속 실행. 새 도구의 일반 기능과 티스토리 실제 호환성은 구분한다.
- 미확정: Tistory용 Playwright의 네 이미지·alt·예약 보존, 세션 수명, 무인 성공률, 소요시간 및 API 비용. 실제 플랫폼에서 이 라이브러리로 시험하지 않았으므로 성능/호환성 숫자를 만들지 않는다.

## 결론 및 상세 비교

### 먼저 구분할 세 가지

1. **오너의 매번 지시 제거**: 목표로 삼는다. 정상 작업은 예약된 프로그램이 스스로 진행하고 오너에게는 결과/예외만 전달한다.
2. **대화형 에이전트의 매 클릭 판단 제거**: 게시·업로드·시각 입력·본문 비교를 고정된 코드로 옮긴다. 스킬은 이 코드를 만드는 명세/복구 지침이지 그 자체가 독립 실행기인 것은 아니다.
3. **LLM 호출 완전 제거**: 현재의 새 이슈 설명·독창적인 문체·주제별 이미지 기준을 그대로 유지한다는 조건에서는 추천하지 않는다. 제한된 생성/의미 검수 호출을 프로그램 안에 넣고, 탐색·클릭·날짜 계산에는 쓰지 않는다. 템플릿만 쓰는 무LLM판은 별도 제품/품질 선택이다.

아래 자동화 수준은 설계 판단이지 측정된 성공률이 아니다. 현재 실측만으로 ‘90% 완성’이나 ‘완전 무인’을 주장할 수 없다.

### 단계별 자동화 지도

| 단계 | 주 실행 | LLM 역할 | 멈춤/예외 조건 |
| --- | --- | --- | --- |
| 05/09/16시 작업 시작·슬롯 할당 | 시계·DB·단일 스케줄러 | 없음 | 중복 실행, 만료 슬롯 |
| 뉴스/공식 발표 수집 | 승인된 RSS·공식 API·허용된 공개 페이지 수집기 | 새 출처 발견 때 제한적 보조 | 접근 제한, 사용 조건 불명 |
| 최근24시간 판단 | UTC/KST 시간·원문 타임스탬프·구간 판정 | 모호한 표현 해석 후보만 | 발생 시점이 확인되지 않으면 제외 |
| 동일 이슈 묶기·기존 글 대조 | canonical URL/본문해시/사건 키 + 유사도 | 검색 의도 중복의 의미 판정 | update/merge/differentiate 결정 없음 |
| 후보 Top5·각 초안 | 규칙 점수 + 구조화 결과 저장 | 독자 관심·설명 방향, 다섯 개별 초안 | 다섯 개 적격 후보 미확보 시 재탐색, 마감 후 skip |
| 출처 묶음·주장 ledger | URL·확인일·인용 위치·권리 기록 | 주장 추출/상충 발견 보조 | 연결 없는 주장·기한 만료·재사용권리 불명 |
| 제목/본문/문체 | 고정 버전 프롬프트·구조화 출력 | 핵심 생성 단계 | 파싱 실패·허위 경험·과장·근거 부족 |
| 이미지4개 | 자산 manifest·배치·alt·파일 검사 | 새 그림 생성/설명 보조 | 권리·개수·내용/수치 오류 |
| 제목 그래픽·비교표 | 검증된 수치를 템플릿에 주입하는 렌더러 후보 | 불필요할 수 있음 | 기존 이미지 스타일과 동등한지 평가 필요 |
| 품질 gate | 링크·날짜·수치·schema·중복 문단·이미지목록 검사 | 주장-출처 의미 일치, 가독성/독창성 rubric | 어느 필수 gate든 fail/unknown |
| 카테고리/홈주제 | 허용 목록 매핑·실제 옵션 확인 | 의미 분류 결과 한 번 | 목록 변경·모호한 분류 |
| 에디터 입력/업로드 | Playwright 전용 어댑터 | 정상 경로에는 없음 | UI 계약 불일치·로그인 보호·업로드 불명 |
| 예약 등록·재열기 | Playwright + 작업 DB | 없음 | 저장 결과 불명: 신규 저장 재시도 금지 |
| 08/12/19시 공개 확인 | 알려진 URL의 비로그인 읽기 + 관리자 상태 | 없음 | 불일치/접근 실패: 제한된 읽기 재확인 |
| 결과·비용·장애 알림 | 이벤트 로그·집계·알림 | 요약은 선택 사항 | 알림 전송 실패도 별도 기록 |
| 성장/리프레시 | 허용된 분석 API·규칙 | 개선안 제안 | 데이터 부족/변경 평가 실패 |

중요: 데이터랩 같은 추세 API는 신호이지 세계 관심도 전체를 보장하지 않는다. 후보별 `event_at`, `source_published_at`, `fetched_at`를 분리한다. 신선도는 선정 시각뿐 아니라 공개 예정 시각에도 `0 <= release_at - event_at < 24h`를 만족해야 한다. 새로운 crawl 시각으로 옛 이슈를 새 것으로 만들지 않는다. 현재 다섯 개 초안 규칙은 유지한다. 비용을 위해 다섯 brief→하나 draft로 바꾸는 제안은 별도 오너 결정 없이는 적용하지 않는다. [현재 계약](18_scheduled_publishing.md)

## 도구 비교와 추천

### 1. Playwright Python: 게시 어댑터의 우선 후보

입력, role/label 기반 요소 조작, 키보드 이벤트, 파일 업로드를 지원한다. `fill`은 input 이벤트를 발생시키며 특수 키 처리에는 순차 키 입력을 사용할 수 있다. 이런 기능은 좌표·AX 번호를 매번 해석하는 대신 동작을 함수로 만드는 기반이다. 다만 일반 기능의 존재가 티스토리 편집기의 이미지/alt/예약 보존 증거는 아니다. [입력 공식 문서](https://playwright.dev/python/docs/input)

추천: `open_editor`, `insert_section`, `upload_asset`, `set_alt`, `classify`, `set_reservation`, `read_candidate`, `save_once`, `reconcile_saved`를 분리한다. Markdown/AST 원본을 단일 진실 원천으로 사용한다. DOM 요소는 실제 페이지에서 확인한 label/role과 프레임 경계를 통해 찾고 일치 수를 검사한다. 숨겨진 API 호출, 내부 에디터 객체 강제 변조, 무작정 force-click을 기본 경로로 삼지 않는다.

79번에서 성공한 기본 편집기 블록별 입력을 첫 후보로 삼는다. HTML 전체 교체는 이미지 유실/본문 중복이 관측됐으므로 복사해서 자동화하지 않는다. 파일 업로드는 허용된 정상 file-input 경로를 검증하고, 런타임 또는 플랫폼이 거부하면 멈춘다. 과거 도구의 `Not allowed`를 새 도구로 우회하는 작업으로 해석하지 않는다. [79번 근거](../content/scheduled/2026-09-13/1200/run.md)

### 2. FastAPI: 운영 API, 작업 실행기의 대체물이 아님

실행 상태 조회, kill switch, 실패 사유, 승인된 재개 요청을 위한 작은 API에 적합하다. `BackgroundTasks`만으로 장시간 제작·예약의 영속 복구를 책임지게 하지 않는다. 공식 문서도 큰 백그라운드 작업에 별도 작업 도구를 고려하도록 설명한다. **초기 CLI worker에는 FastAPI가 없어도 된다.** 모바일 운영판이 필요할 때 추가한다. [공식 문서](https://fastapi.tiangolo.com/tutorial/background-tasks/)

### 3. APScheduler + SQLite: 최소 구성 추천

APScheduler는 정해진 시각에 worker를 깨우는 역할, SQLite는 우리의 슬롯/체크포인트/잠금/증거 저장 역할로 분리한다. 자동으로 중단된 업무 단계까지 복원해 준다고 가정하지 않는다. 3.x 공식 문서의 job stores, 중첩 실행 제한, misfire/coalescing을 기준으로 설계하고 master 문서의 다른 세대 API를 섞지 않는다. 버전 확정/설치는 구현 승인 후 진행한다. [3.x 문서](https://apscheduler.readthedocs.io/en/3.x/userguide.html)

추천 초기 구성: Python worker 하나, 브라우저 writer 하나, SQLite 하나, 스케줄러 하나. FastAPI의 여러 웹 worker 안에서 스케줄러를 각각 시작하면 안 된다. 기존 자동화와 새 worker를 동시에 발행 주체로 두지 않는다. 컷오버 시 한쪽을 shadow/read-only로 전환한 후 단일 writer 소유권을 넘긴다. 현재 스케줄은 이번 조사에서 변경하지 않았다.

### 4. DBOS: 새 대안 중 복구 관점에서 우선 비교할 후보

Python workflow/step의 완료 상태를 저장하고 중단 시 마지막 완료 단계부터 복구하는 구조다. 기본 SQLite와 Postgres를 지원하며, 공식 문서는 분산/프로덕션에는 Postgres를 권한다. 기존 Python 단일 프로젝트에 복구 boilerplate를 얼마나 줄여 주는지 작은 로컬 PoC로 APScheduler+자체 상태머신과 비교할 가치가 있다. [워크플로](https://docs.dbos.dev/python/tutorials/workflow-tutorial), [DB 구성](https://docs.dbos.dev/python/tutorials/database-connection)

추천 판단: 처음부터 DBOS와 APScheduler와 Prefect를 모두 설치하지 않는다. 먼저 아래 저장 불확실성 시험을 통과하는지 비교하고 **실행 엔진 하나만** 고른다. DBOS가 로컬 SQLite를 지원한다는 사실만으로 이 프로젝트의 운영 안전성을 인증할 수는 없다.

### 5. Prefect 3 / Temporal / Restate: 확장 비교군

- **Prefect 3**: task별 재시도, 캐시 및 실행 흐름을 구성할 수 있다. 운영자가 여러 흐름을 관찰하고 관리할 필요가 커지면 비교 가치가 있다. 지금 하루3편에 무조건 도입할 이유는 없다. [재시도](https://docs.prefect.io/v3/how-to-guides/workflows/retries), [트랜잭션](https://docs.prefect.io/v3/advanced/transactions)
- **Temporal**: 장애 후 작업 복구를 중심으로 하는 플랫폼이다. 다중 worker·긴 승인 대기·복잡한 분산 운영이 필요해질 때 검토한다. 초기 구조에 추가할 운영 복잡성이 실제 필요보다 큰지는 별도 평가한다. [공식 소개](https://docs.temporal.io/)
- **Restate**: journal·지속 타이머·상태를 갖춘 지속 실행 후보다. 자체 server와 service를 운영하는 구조이므로 Python+SQLite 최소안보다 구성 요소가 늘어난다. [공식 workflow 설명](https://docs.restate.dev/tour/workflows)

공통 주의: workflow의 재시도/트랜잭션/멱등 키가 **티스토리 외부 게시를 원자적 exactly-once로 바꾸지는 않는다.** 게시 서버와 우리 DB는 같은 트랜잭션이 아니다. 외부 화면 쓰기는 아래 reconciliation 경계가 필수다. 이는 시스템 경계로부터의 설계 판단이며 특정 제품의 결함 주장도 아니다.

### 6. Stagehand v3 / Browser Use: 새로운 브라우저 AI 기능은 보조로

Stagehand v3는 Python SDK 및 로컬 실행 예제를 제공하고, 자연어/코드 혼합과 동작 캐시를 설명한다. 캐시 기능은 client/local과 server 방식, SDK/배포에 따라 조건이 다르므로 ‘Python에서도 전부 같은 기능’이라고 가정하지 않는다. 추천 용도는 selector 변경을 관찰해 **수정 제안**을 만드는 유지보수 보조다. 자동 self-healing이 새 게시 동작을 검수 없이 승격하게 두지 않는다. [Python SDK](https://docs.stagehand.dev/v3/sdk/python), [act와 캐시](https://docs.stagehand.dev/v3/basics/act)

Browser Use도 코드 생성/재사용 예제와 Cloud v3의 `cacheScript`를 제공한다. 후자는 workspace 등 조건이 붙고 클라우드 서비스라는 별도 운영/정보전송 경계가 있다. ‘매번 전체 agent 추론’만 가능한 제품은 아니지만, 캐시 경로의 토큰 절약이 전체 작업 무료·티스토리 성공 보장은 아니다. 초기 단일 블로그 writer로는 직접 Playwright보다 우선할 근거가 아직 없다. [코드 재사용 예제](https://docs.browser-use.com/customize/code-agent/example-products), [Cloud v3](https://docs.browser-use.com/cloud/api-v3/sessions/create-session)

### 7. Pydantic AI: 선택적 생성 어댑터

구조화 출력과 출력 검증을 위한 후보다. 기존 도메인 계약을 갈아엎는 대신 모델 adapter 바깥으로 기존 dataclass/JSON Schema를 유지한다. 단순히 provider SDK와 현재 parser로 해결된다면 이 계층도 생략 가능하다. 출력 schema 통과는 사실성 통과가 아니다. [공식 출력 문서](https://pydantic.dev/docs/ai/core-concepts/output/)

### 8. 트렌드 데이터: 신선도와 관심도는 별도 연결

네이버 데이터랩은 지정한 주제어 묶음의 일/주/월 단위 추세를 반환하며 등록된 클라이언트 자격이 필요하다. 실시간 전체 인기 주제를 자동으로 발견하는 API와는 다르므로 수집한 후보의 보조 신호로 쓴다. [공식 문서](https://developers.naver.com/docs/serviceapi/datalab/search/search.md)

Google Trends API는 2025년 alpha 공지가 있다. 그 공지만으로 현재 우리 계정의 사용 가능성을 보장하지 않으며, 즉시 쓸 수 있는 핵심 의존성으로 넣지 않는다. 접근 자격/현재 제공 범위/데이터 지연을 채택 전에 재확인한다. 이번 조사에서 연결·실제 호출하지 않았다. [공식 alpha 발표](https://developers.google.com/search/blog/2025/07/trends-api)

## 제안 구조: 대화가 아니라 데이터가 다음 단계를 호출

```text
단일 스케줄러
  → 슬롯 잠금 / 체크포인트 DB
  → 출처 수집 → 사건·시간·중복 검사 → Top5 초안
  → 선택 글 생성·이미지 → 결정론적 검사 + 제한된 의미 검수
  → 검수 버전에 묶인 ArticlePackage
  → 단일 Playwright writer → 티스토리 예약
  → 동일 ID 재조회 → 예약 완료 기록
  → 정시 비로그인 공개 확인 → 결과/예외 알림

FastAPI(선택): 상태조회·중지·승인된 재개만 위 흐름에 요청
LLM: 수집 자료의 설명/생성/의미 검수만, 최종 쓰기 권한 없음
```

ArticlePackage는 content_id, slot_id, target_time, article_revision, title, body blocks, source/claim IDs, 네 asset의 해시/alt/순서/대표, category/home, tags, gate report, artifact hash를 가진다. 완료된 생성물을 단계별로 저장하므로 업로드 실패가 조사·이미지 재생성으로 되돌아가지 않는다. 큐 payload는 짧은 artifact 참조이며 전체 과거 대화를 매번 재주입하지 않는다.

현재 `ready_for_approval` 이후를 바꾸려면 별도 publishing 상태/권한 adapter가 필요하다. 기존 offline writer의 immutable-review 경계는 유지한다. 자동 검수 결과를 인간 승인이라고 위장하지 않고, 한 번 승인한 운영정책 버전과 실행별 품질 증거를 분리한다.

### 외부 저장의 안전 상태머신

`PACKAGE_READY → EDITOR_VERIFIED → SAVE_INTENT_RECORDED → SAVE_OUTCOME_UNKNOWN → SCHEDULED_VERIFIED → PUBLIC_VERIFIED`

- 클릭하기 **전** DB에 save intent 및 식별자료를 원자적으로 기록한다. 클릭 이후 로컬 기록 전 장애도 가능하므로, 재시작에서 intent가 보이면 먼저 읽기 reconciliation 한다.
- 동일 slot_id에 unique 제약, 단일 writer lease와 만료 처리. content 수정으로 슬롯 identity를 새로 만들지 않는다. 아직 살았을 수 있는 옛 writer를 배제하지 못하면 새 writer가 쓰지 않는다.
- 저장 성공은 실제 관리 목록/동일 ID/시각/본문/자산/분류 대조로 판정한다. 제목 검색 하나만으로 중복 부재를 단정하지 않는다.
- `SAVE_OUTCOME_UNKNOWN`에서는 저장 버튼 재클릭 금지. 이미 저장된 글을 찾아 ID를 결합하거나, 끝내 불명확하면 예외 알림. 이는 사람을 매번 부르는 운영이 아니라, 실제 모호한 외부 쓰기에서만 개입하는 경계다.
- 플랫폼 측 멱등 키가 없으므로 모든 장애에서 중복0과 무조건 진행을 동시에 보장한다고 약속하지 않는다.
- kill switch는 새 작업/새 쓰기를 막는다. 이미 티스토리에 들어간 예약을 취소하는 기능은 아니며, 기존 글 변경·삭제는 별도 권한이다.

## 로그인과 호스트: 자동화가 해결하지 못하는 경계

Playwright는 지속 프로필을 지원하지만 기본 Chrome 개인 프로필 자동화는 지원하지 않는다고 명시한다. Chrome136부터 기본 데이터 디렉터리에 대한 원격 디버깅 스위치도 제한됐다. 따라서 현재 브라우저의 로그인 세션을 몰래 복사하거나 기존 기본 프로필을 강제 점유하는 방식은 제외한다. [Playwright 프로필](https://playwright.dev/python/docs/api/class-browsertype), [Chrome 변경](https://developer.chrome.com/blog/remote-debugging-port)

추천은 **승인된 전용 지속 프로필에 최초 수동 로그인하고, 하나의 writer가 계속 같은 프로필을 쓰는 것**이다. 이는 새 프로필 도입 시의 승인/초기 인증 작업이며 이번에 수행하지 않았다. 재시작해도 같은 저장소를 사용하되 플랫폼이 세션을 취소하면 다시 인증해야 한다. ‘한 번 로그인하면 영원히 운영’은 약속할 수 없다. CAPTCHA/MFA/계정 선택 혼동/프로필 잠금은 fail closed. 세션 파일은 비밀로 취급하고 repo·trace·클라우드·채팅에 복사하지 않는다.

가정: 처음에는 집 Mac 단일 호스트. 전원·절전·재부팅·네트워크 단절을 포함한 복구 실험이 필요하다. Mac이 꺼져 있으면 제작 자체는 불가능하다. 서버에 이미 저장한 예약과 Mac에서 아직 만들지 않은 글은 구분한다. 안정성 때문에 VPS로 옮길 경우 새 비용·IP/로그인·클라우드 자산 전송 승인을 별도로 검토한다. 이번 분석은 호스트 설정을 변경하지 않는다.

티스토리 Open API는 종료 공지가 확인된다. 해당 공지가 브라우저 자동화의 포괄 허용을 뜻하지는 않는다. 현재 운영정책/서비스 약관, 계정 보호 및 실제 UI 제한에 따라 adapter 범위를 검토하고 불명확하면 축소한다. 공식 게시 API가 부활했다고 가정하거나 내부 요청을 역공학해 쓰지 않는다. [종료 공지](https://notice.tistory.com/2664), [운영정책](https://www.tistory.com/info/policy)

## 검증·비용·운영 원칙

- 유지: 사실/출처/권리/24h, 허위 경험 방지, 의미 중복, 본문 무결성, 네 이미지 identity/alt/대표, 제목·링크·문단·자체 텍스트 가독성, category/home, 예약/실제 공개 확인.
- 오너 제외 유지: 낭독, Lighthouse, 외부 광고 감사, 모든 인쇄 검증, 웹 이미지 픽셀/확대뷰 비교. 빠진 검사를 PASS로 기록하지 않는다. [현행 운영 계약](18_scheduled_publishing.md)
- schema/날짜/숫자/해시는 코드로 검사하고, 근거가 실제로 주장을 뒷받침하는지는 별도 rubric과 표본 감사로 평가한다. LLM 두 개의 동의만으로 사실을 확정하지 않는다.
- 웹 자료는 untrusted data. 지시문·링크를 실행 권한으로 취급하지 않는다. 렌더러는 허용된 HTML 구조만 출력하고 수집 URL은 내부망/로컬 파일 접근을 차단한다. 토큰·세션·서명 URL을 포함할 수 있는 전체 HAR/trace를 기본 저장하지 않는다.
- 비용 식: 하루 총비용 = 모든 후보 작성/검수 토큰비 + 이미지 생성비 + 검색비 + 실패 재시도비 + 호스팅비. 실제 rate와 usage를 연결하기 전 금액/절감률은 UNKNOWN. 3편 완성분만 계산하면 Top5 초안과 실패 비용을 누락한다.
- 캐시는 원문해시+정책/프롬프트/모델/스키마 버전으로 구분한다. 추론 결과의 캐시 적중과 출처의 유효기간을 혼동하지 않는다. 수정 뒤 이전 review를 재사용하지 않는다.
- 생성·의미수정에는 명시적 최대 시도/토큰/시간 예산을 둔다. 후보 탈락은 다른 출처/분야 재탐색으로 돌아가되 마감·예산이 끝나면 skip. 임의로 기준을 낮추거나 지난 슬롯을 다음 슬롯에 누적하지 않는다.
- 사람에게 묻는 경우를 실제 인증·저장 불확실·새 비용/권한·정책변경 등으로 제한한다. 정상 결과는 일일 요약, 예외는 원인코드/현재ID/다음필요행동만 전달한다.

## 구현 우선순위와 합격 기준 — 아직 실행하지 않은 제안

| 순서 | 구현 범위 | 합격 증거 |
| --- | --- | --- |
| A | 기존 검수 package를 받는 writer 계약, 로컬 편집기 fixture | 본문·네 image·alt·분류·예약 roundtrip; 잘못된 날짜/중복·유실 거부 |
| B | Playwright 정상 UI adapter와 전용 프로필 | 별도 승인된 1편에서 agent 판단 없이 예약 및 동일 ID readback; 로그인 만료 시 쓰기0 |
| C | SQLite checkpoint·single writer·crash recovery | 클릭 전/후 프로세스 중단을 주입해 unknown→readonly reconciliation, 중복 저장 없음 |
| D | 실제 생성/검수/수집 adapter | 적격 Top5,24h경계,형식파손,근거부족,비용초과 fixture; golden 문체 비교 |
| E | 단일 스케줄러 연결·기존 실행기 컷오버 | shadow 비교 후 한쪽만 writer;05→08/09→12/16→19; 늦은 실행 skip |
| F | FastAPI 모바일 운영판(필요시)·표본 감사 | 읽기 상태 일치, 인증/권한,중지/재개 기록; 기존 예약 취소로 오인하지 않음 |

일차 목표는 새 이슈 생성까지 한꺼번에 붙이는 것이 아니라 **검수된 고정 package → LLM 브라우저 판단0 → 예약/재열기 확인**이다. 가장 불안정했던 마지막 구간을 먼저 프로그램화한다. 이후 생성기를 붙이면 내용 품질 문제와 UI 문제를 분리해서 고칠 수 있다. 작은 정상 성공1회는 첫 증거이지 무인 운영 승격의 충분조건은 아니다. 반복/장애 시험 후 합의한 관찰 기간·예산으로 승격한다.

다음 구현에 필요한 결정은 설치할 최소 dependency와 전용 프로필/초기 인증, 모델·검색·이미지 비용 상한 및 운영모드 컷오버 승인이다. 현재 recurring 오너 승인을 매편 다시 묻지는 않되, 새 런타임 도입의 설치/비용/보안 경계는 유지한다.

## 근거 검증과 열린 항목

| 기대/주장 | 관측 및 판단 | 상태 |
| --- | --- | --- |
| 기존 코드가 실제 글을 새로 연구·생성·게시한다 | 소스/CLI는 local fixture 파이프라인. draft는 summary/claims 조합, 상태는 ready_for_approval까지 | 반증 |
| 스킬 성공이 독립 publisher 성공이다 |79는 native UI agent 조작 기록, Playwright 프로그램의 E2E 아님 | 반증 |
| FastAPI만 추가하면 영속 자동화가 된다 | background task 문서와 업무 체크포인트 요구 비교 | 불충분 |
| 최신 도구는 항상 LLM을 쓴다 | Stagehand 캐시/Browser Use script cache 공식 설명 확인 | 반증; 티스토리 호환 미검증 |
| workflow 멱등성이 외부 중복 게시까지 자동 해결한다 | 외부 저장과 local commit 사이 장애 창은 남음 | 설계상 채택 불가 |
| 로그인 한 번이면 세션을 영구 보장한다 | 지속 프로필 저장과 플랫폼 인증 유효성은 별개 | 보장 불가 |
| 추천 최소 구조가 실제 더 싸고 빠르다 | 이 프로젝트 벤치마크 없음 | 가설; PoC 필요 |

공식 제공 기능은 공급자 공식 문서 단일 출처를 사용한다(기능 사양의 일차 출처이기 때문). 성능/신뢰성 마케팅은 독립 검증 결과로 승격하지 않았다. 재반박 검색으로 기본 Chrome 프로필 제한, APScheduler3/master 차이, Browser Use cache 조건, Google Trends alpha 접근 한계를 확인해 추천 범위를 좁혔다. DBOS/Stagehand/Browser Use의 새 기능을 실제 계정에서 검증하지 않았으며 정책 포괄 허용도 확정하지 않았다.

실행한 읽기 전용 검증:

- `PYTHONPATH=src python3 -m tistory_growth_os --help`: exit0, local 명령 목록 확인.
- `PYTHONPATH=src python3 -m tistory_growth_os validate-contracts --root .`: exit0, status pass, contract_count18, runtime_contract_count12, valid_fixture_count3, expected_negative_fixture_count1, external_write_count0. 기존 계약 smoke 결과이며 신규 자동화 통과 증거가 아니다.
- `.venv/bin/python*` 확인은 매칭 파일 없음으로 shell exit1. 패키지 전체 설치 상태는 조사하지 않았으며 ‘모든 도구 미설치’라고 주장하지 않는다.

분석 본문에 직접 연결한 공식 웹 근거: 20개 페이지, 15개 hostname(문서 링크를 Ruby로 추출/중복제거해 확인). 로컬 근거는 별도. 비교용 예비 검색 결과는 이 수에 포함하지 않는다. 별도 연구 worker0(한도 차단), 주 에이전트 조사. 소스/설계/기존 CLI smoke까지 확인했으며 포화 연구·신규 브라우저 E2E·보고서 픽셀 인증은 수행하지 않았다. 오너가 승인한 Markdown 범위로 전달하며 인쇄 검증을 재도입하지 않는다. 기록 시계10:03:34→10:08:39KST 구간은5분5초이며 사전 읽기/검색이 포함된 전체 소요시간은 측정하지 않았다. Markdown placeholder 없음 확인; 파일 패널 열기는 queued로 반환되어 실제 렌더링 관측으로 주장하지 않는다.
