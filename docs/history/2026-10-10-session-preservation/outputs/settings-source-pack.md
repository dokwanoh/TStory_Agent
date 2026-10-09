# 2/5: 설정 저장과 실제 적용

확정 2026-10-09 15:33 KST. IT/소프트웨어. 독자의 질문: Claude Code 설정을 저장했는데 왜 기능이 보이지 않을까? 결론: 어느 파일이 읽혔는지와 플러그인이 현재 세션에 로드됐는지를 따로 확인해야 한다.

신선 근거: v2.1.295 공식 릴리스, GitHub 발표 2026-10-08T19:48:38Z = 10-09 04:48:38 KST. 조사 때 약 10시간 45분. 설치/활성/비활성/마켓플레이스 추가 명령이 현재 읽히지 않는 설정 파일에 쓰는 경우 경고하도록 개선. 적용 범위나 플러그인 로드 자체가 새로 생긴 기능이라고 쓰지 않는다.

- https://github.com/anthropics/claude-code/releases/tag/v2.1.295
- https://code.claude.com/docs/en/settings — 사용자/프로젝트/로컬 범위, /status Setting sources는 파일만 확인하고 개별 키의 최종 출처는 아님.
- https://code.claude.com/docs/en/plugins — 플러그인은 기능 묶음. 로컬 컴퓨터와 클라우드 차이.
- https://code.claude.com/docs/en/plugins/loading — 설정 선언/디스크 가져오기/세션 로드 세 단계, /reload-plugins 또는 새 세션.
- https://code.claude.com/docs/en/plugins/install — /plugin 패널 및 적용 대기·리로드 경고. 무조건 --force를 권하지 않음.
- https://code.claude.com/docs/en/memory — CLAUDE.md는 자연어 지침/문맥, /context로 Memory files 확인. 설정 JSON 및 플러그인 설치와 구분.

중복 확인: 관리센터 제목 ‘설정’ 검색 결과 2개는 Windows11 빌드/네이버 웹마스터도구. 최신 237~240의 완료·폴더분리·복원·권한과 독자 행동이 다름. 수요 근거는 실제 공식 수정과 공식 문제해결 안내의 존재; 조회수·추세 상승 수치는 확인하지 않았으며 주장하지 않음. 업데이트 이후에도 남는 설정 적용 판단 문제라는 관점은 편집상 판단.

상품: API ‘클로드 코드’ 검색 HTTP200/rCode0. 단권 상품 9668507087 / item28907035411 / vendor95844537804. 클로드 코드 제대로 시작하기, 길벗, 주홍철·황진성. 증정품/2권 세트 제외. 공식 출판사 목차 10.2 settings.json, 10.1 CLAUDE.md 확인. https://www.gilbut.co.kr/m/book/view?bookcode=BN004893
제휴 링크 옵션 포함 deeplink HTTP200/rCode0: https://link.coupang.com/a/hHCJ1YFaxM
선정 이유: 설정 파일과 프로젝트 지침의 차이를 익힌 뒤 직접 설정을 정리하려는 독자가 settings.json과 CLAUDE.md 관련 장을 참고할 수 있는 선택형 도서. 2026-08-05 출간, 당일 수정까지 책이 반영한다고 주장하지 않음. API 제목의 ‘최신 완벽 반영’을 본문 사실로 사용하지 않음.

자산 계획: 표지 저장/적용 차이 큰 제목. 절1 적용 범위 세 파일을 설명하는 실사 책상. 절2 선언/디스크/세션 연결 도해. 절3 지침과 환경 점검을 나눈 가정 예시. 인포그래픽 한 번에 어디가 막혔는지 판단, 모션은 읽힌 파일→설치→세션 로드→실제 기능 확인/되돌림. 광고 상중하 각1개.
