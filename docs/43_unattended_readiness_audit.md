# 무인 게시 전체 검증 — 2026-09-19

> HISTORICAL: 2026-09-19 당시의 결과를 보존한 문서입니다. 현재 상태와 권한은 STATUS.md 및 AGENTS.md를 따릅니다. 아래 미완료 항목은 현재 backlog가 아닙니다.

## 판정: NOT READY / 실제 무인 E2E 미실행

검증 대상은 대화형 에이전트의 단계별 조작 없이 콘텐츠 준비 → 이미지4장 → 정상 에디터 입력 → 예약 저장 → 정시 공개 확인 → 장애/중복 방지까지 이어지는 경로다. 기존 post89의 보조 게시 성공과 스킬 형식검사는 이 검증의 대체물이 아니다.

검토 기준 HEAD: `456091996f73bd4070473781ca749fa7aa7bb039`. 실제 테스트는 현재 작업트리에서 실행했다. AGENTS.md/DECISIONS.md/DESIGN.md/STATUS.md 기존 변경과 다수 미추적 파일이 있으므로 깨끗한 커밋 전체 승인이나 PR 승인으로 해석하지 않는다. 기존 변경을 수정/삭제하거나 미추적 브라우저 스크립트를 실행하지 않았다.

## 실행 결과

| 실행 | 관측 결과 | 범위 |
| --- | --- | --- |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src pytest -q -p no:cacheprovider tests` | 278 passed, 1 failed, 12.60s | 전체 로컬 회귀 |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q -p no:cacheprovider browser_tests` | 90 passed, 78.33s | 실제 Chrome 엔진 + 가로챈 합성 페이지, 실제 티스토리 E2E 아님 |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src pytest -q -p no:cacheprovider tests/test_save_intents.py tests/test_reservation_execution.py tests/test_reservation_readback.py` | 52 passed, 0.71s | 위278개에 포함되는 중복 실행·중단·읽기 검증 부분집합 |
| `basedpyright` | 0 errors, 0 warnings, exit0 | 현재 소스 타입 검사 |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m tistory_growth_os validate-contracts --root .` | status pass, contracts18/runtime12, external_write_count0 | 계약/fixture 검사 |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m tistory_growth_os --help` | 로컬 명령만 표시, exit0 | 실제 CLI 인터페이스 |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m tistory_growth_os publish` | unknown command: publish, exit2, external_write_count0 | 게시 CLI 미제공 확인 |
| `git diff --check` | exit0 | 공백 오류 검사 |

브라우저 검사의 최초 실행은 시스템 Python에서 Playwright가 없어 수집 오류7건이었다. 기존 승인된 프로젝트 .venv의 site-packages를 프로세스 한정 PYTHONPATH로 사용해 재실행했다. 신규 설치나 프로필/권한 변경은 없었다. 모든 browser_tests는 `page.route('**/*', serve)` 합성 페이지로 실제 계정과 분리한다.

기존 실패: `tests/test_memory_documents.py:91`은 STATUS.md 전체에서 `published` 문자열을 금지하며 과거 `published_verified=false` 기록에도 실패한다. README에 이미 기록된 실패와 동일하다. 테스트를 삭제/완화하거나 역사 기록을 바꾸지 않았다. 전체 회귀 PASS 아님.

## 병목별 근거

| 구간 | 현재 근거 | 판정/필요 작업 |
| --- | --- | --- |
| 조사·작성·이미지 자동 제작 | pipeline/draft.py는 제공된 summary/claims를 조합; 승인된 reader-v5/photo-v3는 에이전트 산출물 | 독립 생성기 통합/평가 미검증. 우선 검수된 적격 패키지를 공급하는 제한 경로부터 |
| 본문 입력 | delivery/playwright_html_input.py:23, 빈 새 에디터만 허용하는 입력 함수와 합성 테스트 | 단일 기능만 구현. 전체 신규 글 작성/모드 전환/미디어 통합 아님 |
| 이미지 업로드·분류·예약 저장 | reservation_execution.py:41의 ReservationSurface는 Protocol. src에서 prepare/save 구현체 및 ReservationExecutor 실행 연결 없음 | 실제 정상 UI adapter 필요. tests/test_reservation_execution.py의 Surface는 로컬 모형 |
| 중복/장애 제어 | SaveIntentJournal, executor의 dry-run/기한/kill-switch/불명 저장 hold 테스트52개 통과 | 로컬 안전장치 확인. 실제 원격 실패/재시작 검증 별도 필요 |
| 예약 확인 | playwright_saved_reservation.py와 비교기, 합성 브라우저 테스트 | 저장된 미래 예약 관측과 공개 확인은 다름 |
| 정시 운영 | 기존 automation3가 ACTIVE heartbeat, 준비05/09/16 및 확인08/12/19 | 대화형 에이전트 호출 일정이며 독립 worker 작동 증거 아님. 변경/추가 실행 없음 |
| 정시 공개·복구·알림 | PLAN.md/docs37에 독립 worker와 전환이 미완료로 기록; 실제 게시 CLI 없음 | 단일 writer, 영속 결과, 재시작/로그인 만료/불명 결과 보류, 실제 공개 readback 연결 필요 |

## 진단 가설과 결론

1. 테스트 환경 문제만 해결하면 무인 실행 가능하다: 일부 환경 문제는 해결했지만 반증됨. 모의 테스트는 통과해도 실행 연결부가 없다.
2. 구현이 완성되어 있고 단지 실제 E2E 증거만 없다: src 검색/CLI 실행/기존 설계 기록이 반증한다. 실제 adapter와 runner가 아직 미구현이다.
3. 보조 게시 성공이 독립 자동화 성공으로 혼동되었다: 최근 CUA 운영 증거와 별도의 offline/Protocol 구현, heartbeat 실행 형태가 이를 뒷받침한다.

이 평가는 구현 공백 확인이지 현재 로그인 실패 진단이 아니다. 로그인/인증은 이번 검증에서 변경하거나 시험하지 않았다. 실제 예약·공개 성공률은 UNKNOWN이다.

## 재검증에 필요한 최소 순서

1. 검수된 신선한 단일 패키지로 정상 입력/파일 업로드/분류/미래 예약 저장/독립 읽기를 연결한다. 신규 identity 할당과 저장 불명 상태를 명확히 처리한다.
2. 모형이 아닌 실제 승인된 한 글로 무인 예약을 수행하고, 동일 identity의 정시 공개를 독립적으로 확인한다. 기존 글89나 만료된 패키지를 재사용하지 않는다.
3. 중복 실행·중간 종료·로그인 만료·시간 초과를 안전한 테스트 환경에서 주입하고, 실제 알림과 보류/재개를 확인한다.
4. 기존 heartbeat와 겹치지 않는 단일 worker의 shadow 검증 후 별도 승인된 cutover를 수행한다. 전체 자동 생성은 오너 우선순위1→3→4→2에 따라 별도 평가 후 통합한다.

## 검증 한계와 부작용

review-work 독립5개 검토는 하네스 fan-out cap으로 첫 spawn이 차단되었고 재사용 가능한 다른 agent도 없었다. Goal/QA/code/security/context 독립 lane 모두 INCONCLUSIVE, PASS 없음. 제한을 높이거나 우회하지 않았다. 주 에이전트의 실제 테스트와 근거 검토만 위에 기록했다. 커밋별 리뷰 인증/전체 자동화 승인 아님.

게시·업로드·예약·스케줄 변경0건. 실제 무인 E2E는 실행 가능한 adapter가 없어 미실행이며, 이를 보조 게시로 대체하지 않았다. 기존 글/프로필/쿠키/보안 설정 변경 없음. 코드 수정/설치/새 비용 없음. 임시 디버거·프록시·추적 로그 생성 없음; pytest가 관리하는 테스트 fixture만 사용했다. Lighthouse/외부광고/인쇄/낭독/웹 이미지 픽셀 검사는 EXCLUDED_BY_OWNER 그대로 유지했다.
