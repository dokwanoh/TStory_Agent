# 내담마 공개 게시물·저장소 대조 — 2026-11-02

## 판정

공개 발행 표시와 Git 저장소 기록 사이의 공백은 확인했다. 원본 실행 로그의 유실, 별도 발행 시스템으로의 이전, 현재 자동화의 정상 작동 또는 중단 여부는 확인하지 못했다. 이 문서는 읽기 전용 감사 결과이며 발행 실행 영수증이 아니다.

기준 저장소는 `dokwanoh/TStory_Agent`, main `3fc5bef3ec26ae80f0519d4665a71f01aa803f2a`이다. 조사 중 발행·예약·STOP·작업 스케줄·브라우저 설정을 변경하거나 발행 코드를 실행하지 않았다.

## 먼저 바로잡을 시간과 기존 기록

- 최신 커밋 시각 `2026-10-10T15:25:15Z`는 **2026-10-11 00:25:15 KST**다. UTC 날짜와 한국 날짜를 섞어 10월 10일에서 기록이 끝났다고 판단하면 안 된다.
- STATUS 최상단의 10월 10일 12:02 안내는 뒤에 추가된 문서를 반영하지 않았다.
- [기존 발행 결과](remaining_three_20261011_publication.md)와 [원본 구조화 기록](history/2026-10-11-remaining-three-publication/remaining-three-publication-record.json)이 이미 259·260·261번을 보관한다. 이를 새 실행 기록으로 복제하지 않는다.
- 261번의 당시 플랫폼 미디어 검토 대기·앱 미확인 상태는 이번 메타데이터 조사로 완료 처리하지 않는다.

| 글 | 현재 공개 메타데이터의 발행 표시 KST | 기존 기록 |
| --- | --- | --- |
| [259 Cursor Rollouts](https://nedamma.tistory.com/259) | 2026-10-11 00:03:04 | 기존 기록의 00:03과 일치 |
| [260 Codex 5일차](https://nedamma.tistory.com/260) | 2026-10-11 00:08:27 | 기존 기록의 00:08과 일치 |
| [261 Kiro Workflows](https://nedamma.tistory.com/261) | 2026-10-11 00:10:23 | 기존 기록의 00:10과 일치 |
| [262 Deno](https://nedamma.tistory.com/262) | 2026-10-11 08:46:39 | 기준 main에서 대응 기록 미발견 |
| [430 벤치맥싱](https://nedamma.tistory.com/430) | 2026-10-30 23:19:04 | 기준 main에서 대응 기록 미발견 |
| [437 바이낸스](https://nedamma.tistory.com/437) | 2026-11-02 07:52:42 | 조사 스냅샷의 최신 공개 글; 대응 기록 미발견 |

## 공개 게시물 비교 범위

공개 자료 취득 구간: 2026-11-02T21:59:43+09:00 ~ 2026-11-02T22:03:56+09:00. 이후 추가·수정·삭제는 이 스냅샷에 포함하지 않는다.

공개 홈페이지 목록 1~23페이지에서 링크를 열거했다. 최신 50개는 [RSS](https://nedamma.tistory.com/rss)의 `guid`·`link`·`pubDate`, 나머지는 공개 글 HTML의 `article:txid`·`article:published_time`으로 ID와 발행 표시를 확인했다. 최근 목록에는 10월 10일 글 5편도 있어 날짜로 제외했다.

10월 11일 00:00 KST 이후 조건에 맞는 공개 글은 **179편, 259~437번**이다. ID 중복·범위 공백·날짜 누락·읽기 실패 없이 확인했다. 그중 259~261번은 기존 기록과 일치하며, **262~437번 176편은 기준 main의 추적 텍스트 파일에서 제목 또는 정확한 게시물 URL로 대응 기록을 찾지 못했다.** 숫자 차이만으로 글 수를 추정한 결과가 아니다.

[공개 관찰 대조표 CSV](public_record_reconciliation_20261102.csv)는 이 176편의 제목·ID·공개 URL·발행 표시·근거 필드만 담는다. 기존 259~261번 실행 기록은 다시 만들지 않는다. CSV의 `NOT_FOUND_IN_BASE_MAIN`은 이 Git 스냅샷 안의 검색 결과이며, 운영 Mac이나 모든 저장소에 로그가 없다는 뜻이 아니다.

공개 발행 날짜는 현재 플랫폼이 표시하는 값이다. 최초 저장 트랜잭션 시각, 생성일, 예약 설정일, 실제 실행일, 실행 주체·모델·승인·매체 검증·성공 여부는 이 자료만으로 복원할 수 없다. 예를 들어 10월 18일 날짜가 표시된 글 24편이 있다는 관찰을 그날 24회 새 글 저장을 실행했다는 증거로 사용하지 않는다. 비공개·삭제·목록에서 사라진 글도 조사 범위 밖이다. 본문 주장들의 사실 정확성을 재검증한 감사는 아니다.

## 저장소·자동화·기존 로그 탐색

| 확인 위치 | 관찰 | 판단 한계 |
| --- | --- | --- |
| TStory_Agent main, docs, docs/history, contracts, 추적 실행 기록 | 가장 늦은 확인 발행은 261번; 기존 259~261 기록 발견 | 운영 로컬의 미커밋 자료는 포함하지 않음 |
| 나머지 원격 브랜치 4개 | automation/save-intent-guard, fix/per-run-spawn-budget-20260920, record/post154-ai-agent-safety, record/post163-barclays-ai의 tip은 모두 10월 11일 이전 | 삭제된 브랜치·외부 복제본은 미확인 |
| GitHub Actions runs | 응답 `total_count=0`; 기준 main에 .github/workflows 파일 없음 | GitHub Actions가 아닌 실행 환경의 부재를 뜻하지 않음 |
| GitHub PR·issue 목록 | 기존 PR 1·2 외 후속 발행 기록 미발견 | 대화·로컬 로그 대체 불가 |
| dokwanoh 소유 저장소 검색 | TStory_Agent, Tistory_Agent, Threads_bot 등 확인; 소유자 범위 nedamma·벤치맥싱 코드 검색은 결과 없음 | 검색 인덱스·접근 범위의 한계 때문에 전역 부재 증명은 아님 |
| 별도 [Tistory_Agent README](https://github.com/dokwanoh/Tistory_Agent/blob/main/README.md), STATUS, docs/DISTRIBUTION.md, CI | 운영 글·계정·실행 로그를 제외한 재사용 배포본이라고 명시; CI는 테스트·계약·오프라인 데모 | 내담마의 새 발행 시스템이라는 증거 없음 |
| 현재 계정에서 조회 가능한 ChatGPT 예약 작업 9개 | 티스토리 발행 작업 없음 | 과거 automation3, 다른 작업공간·Mac의 예약 작업 상태는 미확인 |
| 접근 가능한 과거 대화·저장 파일 검색 | 관련 후속 실행 기록 미확보 | 로컬 기록 유실로 간주하지 않음 |

별도 배포본의 docs/DISTRIBUTION.md는 원본 운영 자료가 별도 운영 저장소에 남아 있다고 설명한다. 그 문구는 이번에 해당 운영 자료를 실제 열람했다는 증거가 아니며, 10월 11일 이후 기록의 위치나 최신성도 보장하지 않는다.

## 원본 로그 우선 원칙과 남은 확인

`.gitignore`는 `.artifacts/`, `content/`, SQLite DB를 제외한다. 코드에 지정된 원본 실행 증거 위치는 운영 checkout을 기준으로 다음과 같다.

- `.artifacts/native-runtime/save-intents.sqlite3`: 저장 의도·중복·재개 상태. 코드는 `delivery/native_runner.py`, `delivery/immediate_runner.py`, `delivery/save_intents.py` 참고.
- `.artifacts/native-runtime/checkpoints.jsonl`: 실행 체크포인트.
- `.artifacts/native-runtime/editor-*.json`: 에디터 재개 상태. 세션 자료이므로 Git에 복사하지 않는다.
- `.artifacts/preparation/<run_id>/`, 날짜별 `.artifacts/manual-*/run-record.json`, 각 패키지의 `audit.jsonl`·`review-audit.jsonl`: 준비·검토·발행 결과 후보. 실제 존재와 내용은 운영 환경에서 확인해야 한다.
- `.artifacts/native-runtime/STOP`: 상태 확인 대상일 뿐, 이번 작업의 해제·생성·재시작 대상이 아니다.

이번 클라우드 checkout은 운영 Mac의 파일시스템이 아니다. 따라서 원본 운영 checkout과 로그·OS 스케줄러를 읽지 못했고, 별도 발행 시스템 여부를 확정할 수 없다. 현재 저장소의 `daily-schedule`과 `reservations` 제어 행은 PAUSED이며, 과거 문서의 ACTIVE 표기를 현재 실행 상태로 승격하지 않았다. 실제 Mac의 STOP 존재 여부도 새로 검증했다고 주장하지 않는다.

후속 대조는 운영 환경에서 기존 DB를 읽기 전용으로 열어 URL/ID/시각을 확인하고 체크포인트·날짜별 run-record 및 실제 스케줄러 대상 경로와 연결하는 순서가 적합하다. 원본 기록이 발견되면 그 기록을 우선 인용한다. 모든 접근 가능한 원본 위치에서도 기록이 없다고 확인되기 전에는 이 CSV를 원본 실행 이력으로 승격하거나 승인·모델·발행 성공 영수증을 만들어서는 안 된다.

## 검증

공개 ID/날짜/URL 중복·누락 검사, 기존 기록 3건 일치 및 176건 저장소 미발견 대조를 수행했다. 메모리 관리표 일관성 검사(PASS)와 git diff --check(PASS)를 실행했다. 이 변경은 문서와 공개 메타데이터 대조 자료만 포함하며 런타임·스케줄·STOP 파일은 수정하지 않는다. 환경에 pytest가 없어 전체 pytest 회귀는 실행하지 못했으며 이를 통과로 표시하지 않는다. 원본 실행 주체 확인은 BLOCKED로 유지한다.
