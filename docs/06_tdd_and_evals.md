# 06. TDD와 평가 전략

## 실패 우선 계약

중요 동작은 Red → Green → Refactor 순서로 개발한다. 테스트는 자연어 문구를 고정하지 않고 상태, ID, schema field, error code, hash, 파일 존재/부재처럼 기계가 소비하는 계약을 검증한다. 각 마일스톤 전 test, typecheck, compile, audit, dry-run을 실행하고 결과와 artifact path를 STATUS.md에 남긴다.

| 계층 | 우선 검증 |
|---|---|
| Unit | opportunity 점수의 unknown 처리, 상태 전이, slug/날짜, retry/stop, idempotency |
| Schema | TopicCandidate부터 EvolutionProposal까지 입출력·버전·unknown field |
| Contract | 모델·검색·분석·이미지·Tistory adapter 오류 envelope; 미구현 adapter는 호출 불가 |
| Golden | evidence, brief, draft, HTML의 구조와 invariant; 산문 전체 snapshot은 금지 |
| Model eval | 근거율, claim-source 일치, 의도, 독창성, 브랜드, 정책, 비용·지연 |
| Integration | fixture topic → evidence → brief → draft → QA → package dry-run |
| E2E | CLI의 happy, unsupported claim, owner experience, malformed, replay |
| Failure injection | JSON 파손, 부분 결과, 정책 evidence 만료, 이미지 실패, idempotency 충돌 |
| Regression | 운영 incident와 발견된 결함을 영구 재현 |

## 핵심 불변 조건

1. `dry_run=true`에서 외부 쓰기는 0이다.
2. quality gate 실패 콘텐츠는 bundle/publish manifest를 만들 수 없다.
3. 동일 idempotency key 재실행은 새 글이나 다른 body hash를 만들지 않는다.
4. 핵심 사실 주장은 유효 SourceEvidence 없이 통과하지 않는다.
5. 실제 경험 표시는 owner evidence 없이는 차단한다.
6. 중복 의도는 update/merge/differentiate 결정 없이 통과하지 않는다.
7. 게시 성공은 클릭 완료가 아니라 공개 상태·본문 hash·링크·이미지 재검증으로 정의한다.
8. 평가 합격선·정책·권한을 낮추는 EvolutionProposal은 자동 승격하지 않는다.
9. 검토용 candidate JSON 생성은 승인 기록이나 승인 패키지를 만들지 않는다. 정상 run은 원본 요청으로 재생성하고 별도 검수와의 일치를 확인한다.

## Milestone 2 acceptance 시나리오

- 지원 fixture와 일치하는 유효한 별도 검수가 있을 때만 `READY_FOR_APPROVAL`, `approval_required`, `external_write_count=0`인 완전한 editor-ready bundle을 만든다. 합성 검수는 임시 테스트 프로젝트에만 둔다.
- evidence 없는 핵심 주장은 `CLAIM_EVIDENCE_REQUIRED`, owner 증거 없는 체험은 `OWNER_EVIDENCE_REQUIRED`로 종료하고 bundle을 만들지 않는다.
- malformed fixture는 `CONTRACT_INVALID`로 fail closed하고 diagnostics 외의 산출물이 없다.
- 같은 key를 두 번 실행하면 manifest와 body hash가 같고 두 번째 audit event는 replay를 나타낸다.
- 생성된 HTML은 실제 loopback browser에서 제목, 목차, 출처 링크, alt가 있는 placeholder를 보이며 서버 종료 후 포트가 닫힌다.

## 의미 평가의 통제

LLM만으로 LLM을 신뢰하지 않는다. 날짜·URL·필수 필드·evidence coverage·링크·alt·금지 광고 형식은 결정론적으로 검사한다. 검색 의도 충족, 독창성, 브랜드 같은 의미 판단은 독립 rubric grader와 표본 인간 검수를 결합하고 disagreement를 기록한다. 모델 출력 parse 실패율, 재시도 횟수, 비용, 지연을 관측하며 같은 품질이면 더 단순하고 저렴한 구성을 택한다.

## 다음 로컬 증분: 원고별 검수와 최신성 결합

상태: 2026-09-07 로컬 writer/CLI 게이트 구현과 합성 회귀 검증 완료. 실제 파일럿의 최종 표현물 검수·권리 허가·인간 승인은 아직 아님.

| ID | Given / When | 요구되는 Then |
| --- | --- | --- |
| RB-01 | 검수한 기준 원고·근거·정책 버전과 현재 산출물이 일치하고 모든 게이트가 충족될 때 | 로컬 패키지 후보만 허용, 외부 쓰기 0 |
| RB-02 | 검수 후 제목·본문·주장 연결·출처 또는 렌더 버전이 바뀌었을 때 | 이전 검수 무효; 승인 패키지 없음; 변경 대상 진단 |
| RB-03 | 필수 검수 누락·보류·거절·검수 대상 해시 불일치일 때 | fail closed. 단순히 supported 또는 점수가 높다는 이유로 우회 불가 |
| RB-04 | 평가 시각이 검수/근거 유효기간 직전·정확한 경계·직후일 때 | 명시된 경계 규칙대로 처리; 경계 및 이후 차단; 시간대가 다른 동일 순간은 같은 결과 |
| RB-05 | 입력 확인일은 과거이지만 실제 평가 시각에는 만료됐을 때 | 과거 입력 시각을 재사용해 통과하지 못함 |
| RB-06 | 내용 검수를 통과했지만 source review_required 또는 권한 보류가 남았을 때 | 기존 보류 유지. 의미 검수는 이용 허가나 외부 행동 승인이 아님 |
| RB-07 | 정확히 같은 입력과 유효한 검수로 재실행하거나 만료 후 재실행할 때 | 전자는 기존 멱등성 유지; 후자는 과거 성공을 근거로 새 승인 허용 금지. 과거 산출물 삭제/변조 없음 |

해시는 내용의 동일성만 증명하며 사실성·저작권 허가를 증명하지 않는다. 승인 필드 조작을 막는 신뢰 경계와 인간/독립 에이전트 검수의 구분은 구현 설계에서 명시한다. 새로운 검수 게이트의 happy/blocked/malformed/replay CLI와 기존 회귀 테스트를 모두 실행한 뒤에만 이 항목을 통과로 기록한다.

실행 근거: `test_package_review.py`는 검수 부재와 상대 root, `test_review_decisions.py`는 19개 결정/시각/계약 사례, `test_review_replay.py`는 14개 만료/파일 변조/정책 결과 조작/입력 및 카탈로그 변경 사례, `test_review_cli.py`는 누락·만료·파손된 검수의 CLI 차단과 감사 경로를 검증한다. 기존 bundle/CLI/text-only 테스트는 임시 검수로 happy/replay를 검증하고 source-rights 테스트는 보류 유지(RB-06)를 검증한다. 전체 207개 통과. 변경 대상 진단은 현재 digest와 결과 코드 수준이며 필드별 차이 설명 UI는 미구현이다. 검수 기록은 로컬 신뢰 데이터이고 신원·사실성 검증기가 아니다. 구체 명령/실행 산출물/제약은 STATUS.md와 ADR-020에 기록한다.

## 검토용 후보 전달 경로 — 2026-09-07

`tests/test_prepare_review.py`의 10개 사례는 inspectable envelope, 실제 승인 writer와 10개 파일 전체 바이트 일치, 검토만으로 승인 불가, 주장/권리/JSON 차단, 덮어쓰기·상대경로 탈출·symlink 거절, 필수 dry-run을 검증한다. 최초 새 명령 RED 4개 뒤 구현했으며 기존 실패 경계를 유지한다. 전체 217개 통과. CLI의 REVIEW_CANDIDATE_CREATED는 검토 자료 생성 성공이지 승인/사실 검증 성공이 아니다. 실제 생성물은 Ruby 별도 구현으로 subject digest를 재계산했다. 렌더러는 변경하지 않았고, 후보 원문 열람을 새 브라우저/시각 검수로 주장하지 않는다. ADR-021 참조.
# Evaluation scope override — ADR-037

Actual screen-reader/VoiceOver/narration testing is EXCLUDED_BY_OWNER from the whole project loop, not an outstanding test or PASS. This explicit owner policy change is not autonomous self-evolution lowering a threshold. Preserve all other tests, including alt/semantics/contrast/keyboard, content/rights, print and delivery verification. Do not remove generic accessibility validation or change historical artifacts.
