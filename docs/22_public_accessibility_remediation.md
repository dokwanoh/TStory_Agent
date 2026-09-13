# 공개74 접근성 개선 — 제한 적용 완료

## 2026-09-09 승인된 다섯 항목 배포

오너 승인 후 원본을 네이티브 스킨 보관함 `TGOS-before-a11y-20260909`에 저장했다. ZIP 다운로드는 실패했으므로 로컬 ZIP 백업을 확보했다고 주장하지 않는다. 아래 실험에 대응하는 다섯 항목만 정상 에디터에서 변경하고, 미리보기 후 Apply 한 번으로 저장 완료 알림을 확인했다. 본문 링크 CSS는 실제 `.entry-content`로 제한했다. 글 본문·광고·계정은 수정하지 않았다.

별도 공개 브라우저에서 /74의 Tab→본문 바로가기 표시→Return→content 포커스, 태그 접근성 제목 수준2, 이미지 대체텍스트4개, 기존 제목/일자/출처 링크를 확인했다. 본문 출처 링크는 진한 파랑·밑줄로 보이며 홈/목록의 카드 배열도 유지된다. 익명 HTTP 재조회에서 viewport/main/skip/style의 정확한 저장 패턴과 중복 없음 확인(exit0). 세부 근거 및 배포 스타일 해시: `.artifacts/skin-a11y-20260909.md`.

판정은 제한된 수정의 배포·공개 readback 확인이다. 실제 모바일 핀치 확대, 저장 후 전체 인쇄/VoiceOver, 새 Lighthouse 점수와 독립 리뷰는 미완료다. 아래 ‘승인 필요/적용 전’ 문구는 당시의 이력이며 이 승인 범위에 대해서는 해소됐다. 광고·보안 변경은 여전히 범위 밖이다.

## 2026-09-09 실행된 수정안 실험

`.artifacts/lighthouse-toolchain/remediation74.mjs`는 새 비로그인 실제 Chrome에서 현재 문제를 재현한 뒤 브라우저 메모리에만 수정안을 적용한다. 서버 저장/에디터/광고 설정 호출은 없다. 종료 시 컨텍스트와 수정은 폐기된다. DESIGN.md의 링크색/포커스색/여백을 사용하는 진단용 후보이며 전체 공개 스킨의 새 디자인 시스템 또는 배포물이 아니다.

관측: main0→1, viewport 확대 제한 문자열→width=device-width, initial-scale=1, 출처 링크 RGB212,188,167→RGB7,95,156. 실제 키보드 Enter로 건너뛰기 링크→content 포커스 확인. 기존 태그H5는 DOM 태그를 교체하지 않고 실험에서 aria-level2를 부여했으므로 물리H5개수는1로 유지된다. 본문 텍스트·모든 링크·이미지 alt 배열은 수정 전후 완전 동일. 375/768/1280에서 scrollWidth=viewport, 이미지4개 로드. 결과 JSON과 전체 캡처3장은 `.artifacts/remediation74-20260909/`.

구문검사 및 실제 실행 exit0. 자동 LSP는 중복 경로 ENOENT로 실행 실패했으므로 LSP PASS 아님. 메인에서 세 캡처를 직접 검수: 큰 문단 사이 여백/광고 영역은 남아 있으며 인쇄·광고 접근성·본문 외부 대비는 해결되지 않았다. 독립 시각 검수 생성은 하네스 fanout67/60한도로 차단; 한도 변경하지 않음. 이 실험은 전체 시각/접근성/Lighthouse PASS가 아니며 새 점수 없음.

다음 배포 경계: 스킨 원본 백업 후 출처 링크 대비, 본문 landmark/skip, viewport 확대, 태그 heading 수준, 한글 줄바꿈의 다섯 항목만 적용하는 명시적 승인 필요. 글 본문·광고·결제·계정·보안 설정은 범위 밖. 홈/목록/글 회귀 검증과 익명 저장상태 확인 후에만 배포 성공을 판단한다. VoiceOver의 보호된 화면 문제는 이 스킨 수정으로 해결됐다고 주장하지 않는다.

2026-09-08. 공개 글·스킨·광고는 변경하지 않았다. 이 문서는 현행 DOM/CSS 측정에 근거한 변경 제안이지, 적용되거나 검증 완료된 스킨이 아니다. 기존 DESIGN.md는 오프라인 패키지 계약이므로 공개 스킨 전체의 디자인 계약으로 전용하지 않는다.

## 이번에 실제 실행한 검사

- 기존 Chrome Stable + Playwright, 새 비로그인 컨텍스트,1280/640/320CSS px, JS/광고 차단 없음. 각 전체 페이지 PNG와 안전한 측정 JSON: `.artifacts/reflow74-20260908/`.
- 세 폭에서 document scrollWidth=viewport width, 본문 제목/문단/이미지/링크 경계 초과0. 이미지4개 로딩·alt 확인. 모든 위젯 기능의 접근성 합격을 의미하지 않는다.
- 학습포털 링크에서 Shift+Tab: 학습 흐름 원문 확인 → 서울시 공식 발표 보기 → 스포츠. 이 실행에는 이전 IAB와 같은 광고 포커스가 나타나지 않아 광고 경로는 동적임을 유지한다.
- Safari 실제 배율100→200→100readback. 메뉴 항목 클릭은100에 남았고, 펼친 메뉴에서 Down5+Return으로200이 확인됐다. 제목·이미지·중간 본문 확대를 실제 확인. ‘추천’이 추/천으로 나뉘는 한글 단어 분리가 보임. 전체 페이지200%인증은 아님.
- Safari 배율 메뉴 최고300%,400%항목 없음.320CSS px는1280기준400%상응 reflow 검사지만 실제400%브라우저 확대라고 기록하지 않는다.

## 우선 수정안과 검증 조건

| 관측 | 최소 변경 제안 | 적용 전후 검증 |
| --- | --- | --- |
|16px 출처 링크 RGB212,188,167 |본문 출처 링크에 명시적 고대비 색·밑줄. 기존 제목 갈색 RGB122,88,58도 후보 |흰 배경 기준 대비1.82→6.39; 일반 글자4.5이상. 배경·hover·focus·visited별 재검사 |
|main/role=main0개 |기존 content 컨테이너에 main 의미 부여, 첫 포커스에 본문 바로가기 |중복 main0, 건너뛰기 키보드 활성화→본문 포커스, 모든 템플릿 확인 |
|H2뒤 태그H5 |태그를 문서 구조에 맞는 제목 또는 일반 레이블로 조정 |디자인 유지, 전체 제목 탐색 순서 검증 |
|user-scalable=no, max/min scale1 |viewport를 width=device-width, initial-scale=1로 정리 |실제 모바일 확대·폼·레이아웃 회귀검사; 다른 태그 중복 확인 |
|200%에서 추/천 단어 분리 |본문·제목 keep-all과 긴 문자열 예외 줄바꿈을 제한적으로 적용 |320/640/1280 및200%에서 어절 유지·가로 넘침 재검사 |
|광고 버튼 cbb/이름 없는 링크 |외부 광고 제공 계층에 별도 결함으로 기록 |임의 광고DOM변조·숨김·광고 설정 변경 없이 개선 경로 판단 |

색 대비 계산은 sRGB 상대 휘도 공식으로 수행했다. 기존 디자인의 링크색 RGB7,95,156은 흰 배경 대비6.72. 이는 색상 후보의 수치 검증일 뿐 실제 변경 스킨의 접근성 합격이 아니다.

## 적용/복구 경계

공개 스킨을 수정하려면 명시적 승인, 현행 스킨 원본 백업, 정확한 템플릿/선택자 확인, 로컬 또는 네이티브 미리보기, 글/홈/목록 페이지 회귀검사, 한 번의 저장, 익명 readback, 원복 경로가 필요하다. 현행 공개HTML을 저장 가능한 스킨 원본이라고 가정하지 않는다. 광고·수익·계정·보안 설정은 범위 밖이다.

VoiceOver는 실제 엔진/자막이 동작해도 보호된 화면을 따라가므로 본문 읽기 미검증. 보호 화면 해제나 권한 허용을 추측으로 수행하지 않는다. 독립 시각 리뷰는 기존 하네스 생성 한도 때문에 이번 결과의 PASS 근거가 없으며, 전체 판정은 NEEDS_WORK다.

공식 기준 확인: [W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [W3C Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). 확인일2026-09-08. 관련 스킨 변경 후 재검사.
# Current scope override — ADR-037, 2026-09-09

Owner has excluded actual screen-reader/VoiceOver/narration testing from the entire project loop. Historical protected-display observations below remain true but are no longer blockers or restoration tasks. Do not infer full accessibility conformance; all other accessibility, print and delivery checks remain.
