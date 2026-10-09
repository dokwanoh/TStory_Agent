# 작성기 재시작 기록

첫 작성기959319716, 2026-10-09 00:15~00:19.
- native HTML paste 원고 입력 성공.
- 표지 사진 native AX 클릭+filechooser 업로드 및 링크 팝업 적용 성공.
- 이미지 위치 선택 도중 잘못된 role name selector(no_matches), stale AX번호 text선택실패, filechooser10초 timeout이 이어짐.
- 같은 미디어 삽입 단계가 3번 실패해 기존 창 닫고 새 작성기에서 재입력. 원고·6자산 재사용.
- Mac 잠김 증거 없음. 원인은 현재 UI의 요소 선택 및 사진 메뉴 호출 불일치. 역할 이름 추정 및 확인 전 번호 재사용 금지.
- 이후: 최신 AX에서 번호 찾기→native click 사진→filechooser. Promise reject를 즉시catch하여 kernel reset 방지.
- 새 작성기959319723 복원창 취소가 browser wrapper에서 CDP focus timeout을 일으켰다. getJsDialog는 undefined였지만 실제 Chrome native AX에 복원 확인창이 남아 있었다. 게시봇 창의 해당 글쓰기 탭을 native 클릭→실제 취소 버튼을 클릭한 뒤 작성기 응답이 돌아왔다. Mac잠김이 아니라 native 확인창이었다.
- 새 작성기에서 모든6미디어 upload와 link는 native AX사진 메뉴+filechooser와 image-link dialog로 성공했다. marker 선택 전 fullAX에서현재 body번호, 메뉴열기후photo번호를 매번찾았다. Playwright 사진메뉴click과 role명추정을 반복하지 않는다.
- 이미지 ALT 보조작업에서 iframe contentDocument 접근 불가와 좌표/포커스 불일치가 발생했다. native표지ALT만 완료. 이 보조작업을 이미지링크실패로 오인하거나 이미완료된업로드를 반복하지 않음.
- HTML 전환은 mode-confirm 동시확인으로 성공. HTML→기본모드는 wrapper부모버튼click효과없음, 실제 화면855,35버튼click후 관찰된 editor-mode-kakao-tistory를 mode-confirm으로선택해성공.
- local file browser GIF 재생은 URL 정책 거부. 우회하지 않음. 정상 요청된 Tistory업로드 후 HTTPS미디어의 실제 재생으로 확인 예정.
