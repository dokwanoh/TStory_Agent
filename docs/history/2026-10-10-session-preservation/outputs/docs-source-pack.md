# Claude Google Docs 새 글 — 주제·근거·상품 검토

조사: 2026-10-08 12:00~12:07 KST. 허용 분야: IT/소프트웨어.

독자 질문: 구글 문서에 쓴 보고서를 Claude로 고칠 때, 중요한 조건은 어떻게 지킬까?
한 문장 결론: 열린 문서에서 한 문단씩 수정을 요청하고 기본 승인 모드에서 변경을 읽은 뒤 날짜·수치·조건을 원문과 대조한다.

## 공식 원문 읽기

1. https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
   웹 전체 본문과 실제 Chrome 페이지를 읽었다. 실제 페이지는 /ko/로 리디렉션하며 날짜 2026-10-06 표시. 정확한 시각·시간대 없음. 엄밀한 36시간 이내 확정은 불가. 전날 업데이트라는 도움말 상대시각도 발표 시각으로 바꾸지 않는다.
   새 공개 베타: 모든 유료 Claude 플랜, Docs/Sheets/Slides 부가기능. 열린 파일 옆 사이드바에서 읽고 직접 수정. 별도 새 커넥터는 Claude 채팅에서 파일을 만들거나 고치는 다른 경로. 기본 Ask before edits는 적용 전에 승인 카드, Accept all edits는 일반 수정 자동 적용. Marketplace 설치 후 Extensions > Claude > Open Claude.
2. https://support.claude.com/en/articles/16951679-use-claude-in-google-docs-sheets-and-slides
   전체 도움말을 읽었다. Pro/Max/Team/Enterprise 베타, Marketplace 설치가 허용된 Google 계정 필요. 조직에서 막히면 관리자 처리. Chrome/Edge/Safari 지원, Firefox 베타 작업 미완료. 열린 파일과 켠 커넥터의 내용이 범위. 자체 수정은 직접 편집이며 Google 기존 제안 수락·거부 불가. 기존 댓글 읽기·응답·해결 불가. 수정은 사용자 이름으로 버전 기록, Undo 또는 이전 버전 복원 가능. 작업 중 사이드바 닫으면 작업 중단. 단일 긴 작업 최대 6분, 큰 작업 분할. Google API 콘텐츠 모델 학습에 사용하지 않지만 요청·파일 내용은 응답 생성을 위해 Claude로 전송. 개인정보 안전 보장으로 표현하지 않는다.
3. https://workspace.google.com/marketplace/app/claude/12459801340
   공식 설치 목록 링크를 읽었다. 실제 설치·권한 부여·서비스 실행은 하지 않음. 본문 예시는 가정으로 표시한다.

## 수요와 차별성

확인 가능한 현재 신호는 Google 업무 파일에 부가기능과 별도 편집 커넥터가 공식 출시됐다는 제품 변화다. 조회수·검색량·사용자 증가율은 확보하지 않았으므로 인기 순위를 주장하지 않는다. 반복 문서 수정이라는 일상 문제와 조직 배포 가능성이 장기 활용 판단의 근거이며 향후 이용 확대는 전망으로만 기록한다.
최근 15개 관리 목록을 실제 읽었다. 222 사진 판별, 221 Haiku 모델 선택, 220 Windows AI, 219 ChatGPT UI, 218 Playground, 217 Decisions API, 216 CVP와 다르다. 이번 글은 Google Docs 파일 안에서 승인하며 문장을 고치는 구체적 사용 판단에 집중한다.
Adobe Acrobat 10/7 후보는 검색 캐시 본문과 실제 404가 충돌하여 제외. 미확인 URL을 확인된 독자 버튼으로 쓰지 않는다.

## 상품

쿠팡 API search '보고서 작성' → HTTP 200, rCode 0. product 5625226928, item 9131604022, vendor 93690303098. 《보고서의 정석: 공무원 공공기관》 임영균/소운서가, 종이책 단권. API 확인가 14,400원은 변동 가능하므로 본문에 적지 않는다.
API deeplink → HTTP200/rCode0, https://link.coupang.com/a/hFIOHJcXzU
실제 파트너스 검색과 링크 생성 URL에서 동일 상품/옵션 확인. 배너 https://coupa.ng/cp0tAU, 120×240. UI 단축 URL은 https://link.coupang.com/a/hFIUyWou8y 로 API 링크와 같은 옵션을 가리킨다. 본문 네이티브 미디어와 댓글에는 API 확인 링크를 일관 사용한다.
서지 ISBN9791185192611: https://library.kaist.ac.kr/search/ctlgSearch/posesn/view.do?bibctrlno=980195&ty=B
출판사 제공 목차: https://www.yes24.com/Product/Goods/98836671
목차에 보고서 구조화, 정확한 문장, 간결한 문장이 있다. 문서 고치기에서 사람이 판단할 구조·표현의 선택적 학습 자료. Claude 확장 설치 안내서·AI 기능 매뉴얼로 주장하지 않는다. 서비스 이용에 책 구매가 필요하지 않음.
댓글 선정 이유 확정: 'AI가 고친 보고서의 구조와 문장이 적절한지 판단하고 싶은 분이, 구조화·정확한 문장·간결한 표현의 기본기를 살펴볼 때 참고할 수 있어 선정했어요.'
관련성이 약한 정관·투자 책, 출간 전 AI 글쓰기 책은 제외.

## 계획

4절: 열린 문서의 수정 / 승인과 실행 조건 / 원문→요청→예시→대조 / 상황별 선택과 되돌림.
정지 이미지 4개는 각각 이 네 내용을 직접 설명. 표지1+인포1+절별4+GIF1 = 7미디어.
모션: 독자 문단 선택→독자 요청→Claude 수정 계획→독자 승인 여부(미승인: 요청 수정으로 되돌림 / 승인: Claude 직접 수정)→독자 조건 대조→문제 있으면 실행 취소·재요청 / 문제 없으면 채택. 6분이 전체 작업시간 보장처럼 보이지 않게 한다.
