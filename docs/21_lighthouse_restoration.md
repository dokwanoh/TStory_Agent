# Lighthouse 검사 복구

## 2026-09-09 저장된 스킨 재측정

모바일·데스크톱 각3회 실행 완료(exit0). 중앙값은54/96/73/100 및70/96/73/100. 접근성은 기존86/81에서 양쪽96으로 상승했지만, 모든 회차에 색 대비 실패가 남는다. 원격 광고/네트워크 변동을 포함하므로 성능 상승을 스킨 수정의 인과적 효과로 단정하지 않는다. 결과 `.artifacts/lighthouse-74-20260909-postskin/`. 아래 수정 전 viewport/main 관측은 과거 이력이다.

audit.mjs의 첫 인자로 새 출력 경로를 지정할 수 있도록 최소 변경했다. 존재하는 경로는 브라우저 실행 전에 거부하며 실패경로와 구문검사 실행을 확인했다. 기존 결과를 덮어쓰지 않는다. 전체 접근성·인쇄·화면낭독·예약 인증은 별도이며 여전히 미완료다.

2026-09-08 오너가 프로젝트 내부 설치를 승인했다. 전역 npm/Chrome 설치, 로그인 프로필 연결, 스킨·광고·게시글 변경 권한은 포함하지 않는다.

## 실행 계약

- Lighthouse13.4.1, Node26.5.0. 기존 Chrome Stable152와 기존 Playwright1.62.1을 사용한다.
- Chrome Launcher의 새 임시 프로필에 Playwright CDP와 Lighthouse Node API를 연결한다. 사용자 Safari/Chrome 프로필·쿠키를 복사하지 않는다.
- 대상은 공개74번. 모바일/데스크톱 각3회 측정하고 중앙값을 비교한다. 이는 실험실 측정이며 실제 독자 지표나 유입 성과가 아니다.
- 점수·실패 audit ID·측정 시각만 저장한다. 원시 네트워크/쿠키/서명 URL/HTML 보고서를 저장하지 않는다.
- 비정상 페이지·측정 오류는 통과로 처리하지 않는다. 측정 완료와 품질 합격을 구분한다. 접근성 점수는 실제 화면낭독기 검사를 대신하지 않는다.
- 이 작업은 검사 도구 복구이지 스킨 최적화 작업이 아니다. 스킨/광고/기존 글 수정이 필요하면 별도 승인을 받는다.

## 설치물 경계

초기 tools/lighthouse/node_modules가 기존 저장소 비밀 패턴 검사에 포함되어135건을 검출했다. 모든 경로가 새 의존성 내부임을 값 노출 없이 확인했다. 설치 의존성은 기존 로컬 도구/생성물 경계인 .artifacts로 이동하고 검사·테스트를 변경하지 않는다. 실제 이동 및 재검증 결과는 STATUS에 기록한다.

## 직접 확인한 보완 대상

최종 설치 위치: `.artifacts/lighthouse-toolchain/` (package.json, package-lock.json, node_modules, audit.mjs). 의존성과 감사 도구는 프로젝트 안에 있으며 전역 환경은 변경하지 않았다. 설치 시 lifecycle scripts를 실행하지 않았고 npm audit 결과 알려진 취약점0건이다.

실행: 프로젝트 루트에서 `TISTORY_AUDIT_PLAYWRIGHT=file://${USER_HOME}/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs node .artifacts/lighthouse-toolchain/audit.mjs`. 현재 스크립트는74번 및20260908출력 경로에 고정된 복구 리허설이다. 결과 파일 존재 시 덮어쓰기하지 않으므로 다른 실행 전에는 별도 실행 ID/경로를 지정하도록 수정·검증해야 한다. 범용 자동 품질 게이트는 아니다.

모바일3회:54/86/73/100,54/86/73/100,54/86/73/100. 데스크톱3회:54/81/73/100,69/86/73/100,54/81/73/100 (성능/접근성/권장사항/SEO). 각 중앙값은54/86/73/100 및54/81/73/100. 결과 `.artifacts/lighthouse-74-20260908/summary.json`과6개 측정 JSON. 품질 전체 합격 아님. 측정 후 Chrome 임시 프로필 종료, 원격 변경 없음.

공개74번 HTML에 `user-scalable=no`, `maximum-scale=1.0`이 존재하며 `<main>` 요소는0개다. Lighthouse가 확대 제한과 main landmark 부재를 별도로 보고했다. 이것은 스킨 차원의 후보 수정이지 원고의 사실 오류가 아니다. 본문 H2와 사이트 태그 H5 등 전체 heading 구조도 감사 대상이다. 현재 스킨/광고 설정은 변경하지 않았다.

공개 네트워크와 광고가 포함된 측정이므로 결과에는 변동성이 있다. 광고를 차단하거나 이미지를 숨겨 점수를 올리지 않았다. Lighthouse가 성공적으로 실행됐다는 사실은 화면낭독기, 상세 인쇄, 네이티브 예약 E2E의 성공을 의미하지 않는다.

근거: [공식 Lighthouse 저장소](https://github.com/GoogleChrome/lighthouse), 확인2026-09-08. Node API는 설치된13.4.1의 실제 코드/설정도 확인했다. 사용한 frontend 성능 지침은 실제 Chrome/복수회 측정에 적용했으며, 이를 이유로 운영 사이트 변경 권한이나 새 합격 기준을 임의로 부여하지 않는다.
