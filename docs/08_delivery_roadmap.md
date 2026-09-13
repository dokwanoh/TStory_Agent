# 08. 전달 로드맵

## Milestone 0 — Resurrection Audit

환경·정책 조사와 provisional AS-IS를 만들고 공개 inventory와 private telemetry 접근을 분리한다. 2026-09-07에 URL, sitemap/RSS/robots, 63개 entry의 HTTP 상태와 대표 위험 표본을 읽기 전용으로 확인했다. 이어서 63개 전부에 metadata-only intent hint·freshness·risk·action candidate를 생성했다. 후속 공개 자산 조사에서는 이미지 139개와 query-free 주소 52개를 확인했고, 36개 HEAD 2xx와 16개 미해결을 구분했다. 이미지 권리·실제 렌더링/재생과 현재 performance baseline은 여전히 `UNKNOWN`이다. 과거 문체는 미래 전략 입력에서 제외한다. 완료 조건은 사실·가설·미확정이 구분되고 각 unknown이 무엇을 막는지 설명되는 것이다.

## Milestone 1 — Process Redesign

ASIS-001..012, BDW, ERASK+C, TOBE-001..012, 상태·예외·책임·KPI를 이 문서 세트와 machine catalog로 연결한다. 완료 조건은 모든 AS-IS가 정확히 한 번 매핑되고, 모든 주요 BDW에 baseline 측정법이 있으며, 외부 게시가 자동화됐다고 표현하지 않는 것이다.

## Milestone 2 — Offline Vertical Slice

지원되는 합성 주제 한 개를 TopicCandidate → SourceEvidence/Claim → ContentBrief → ArticleDraft → QualityReport → PublishManifest/HTML package로 변환한다. 테스트와 schema를 먼저 만들고 success bundle과 failure diagnostics를 원자적으로 분리한다. 완료 조건은 happy·unsupported claim·unverified experience·malformed·idempotent replay 테스트, full test/typecheck/compile/audit, 실제 브라우저 preview가 모두 통과하고 `external_write_count=0`인 것이다. 실제 게시 상태는 도달할 수 없다.

## Milestone 3 — Assisted Publishing

사용자가 승인한 한 개 테스트 글을 draft/비공개 경로로 입력한다. 시작 전 최신 공식 지원성·약관, 로그인 방식, selector 변경 위험, rollback을 다시 검토하고 별도 명시 승인을 받는다. 로그인 만료·MFA·게시 실패에서 중단하며 사후 내용을 재검증한다. 이 milestone은 현재 승인·scope 밖이다.

## Milestone 4 — Telemetry & Learning

승인된 property에서만 성과를 수집하고 source/surface/기간/freshness/attribution을 보존한다. 데이터가 실제 topic score 또는 refresh 결정을 바꾸는 사례가 있어야 완료다. 접근 권한이 없으면 synthetic schema 검증만 하고 0 성과로 간주하지 않는다.

## Milestone 5 — Limited Auto-Publish Pilot

저위험 allowlist, 낮은 빈도, 시간대·비용 상한, canary, kill switch, 알림, 자동 강등, 인간 표본 감사가 선행한다. 사전 합의 기간 동안 정책·품질·오류·성과 기준을 모두 통과해도 사용자 승격 승인 전에는 확대하지 않는다.

## Milestone 6 — Portfolio Scale & Evolution

pillar–cluster–supporting article 포트폴리오, 내부 링크 그래프, refresh/merge/retire를 운영한다. Observe → Diagnose → Hypothesize → Eval → one-factor canary → Promote/Reject → Monitor/Rollback 순서를 지킨다. 정책·권한·North Star·비밀 관리·합격선·신규 비용은 자동 변경할 수 없다.

## 의존성과 승인 경계

2026-09-07 전체 준비도 평가는 [15. 전체 진행률과 실전 준비도](15_delivery_readiness.md)에 있다. 전체 약 30~40%는 관리용 추정이며, 좁은 합성 Offline MVP의 완료와 실전 운영의 완료를 구분한다. M0/M1의 구조적 추적성이 실제 과거 운영의 증거 완성을 뜻하지 않는다.

M0의 공개 technical baseline은 완료됐지만 private telemetry는 여전히 owner decision이다. M3 이후 실제 쓰기, 설치, 신규 비용, private telemetry 연결, 계정·광고·도메인·법적 고지 변경은 사용자 승인이 필요하다. 각 milestone 실패는 다음 단계로 이동하지 않고 원인·artifact·재검증 결과를 STATUS.md에 남긴다.
