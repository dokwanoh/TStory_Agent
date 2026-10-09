# Coding Agent 새 글 — 주제 확정

조사: 2026-10-09 14:05 KST. 현재 목표 시작 13:54 KST.

## 질문과 결론

- 질문: AI에게 사이트 수정 두 가지를 동시에 맡길 때 파일이 섞이지 않게 하려면?
- 결론: Git worktree로 작업 폴더를 나누고, 결과는 각 폴더에서 검사한 뒤 선택해 합친다. 폴더 분리가 정확성·보안·자동 병합을 보장하지 않는다.
- 범위: IT/소프트웨어. 기존237은 Claude 완료 판정·입력검사,228은 Codex 저장된 상태 초기화,223은 속도·자동검토. 이번은 작업 폴더 분리와 병합 판단. 현재 홈237~230 실제 확인, 이전 기록223/228 참고.
- 관심 근거: Codex가 CLI에 관리형 worktree 생성·목록 도구를 추가함. 실제 검색량/인기 순위는 미확인. 사이트 수정과 병행 실험이라는 실용성·지속성은 편집 판단이며 미래 인기 사실로 쓰지 않는다.

## 근거

1. https://learn.chatgpt.com/docs/changelog — 2026-10-08 CLI0.162.0. trusted local project + worktrees feature enabled 조건에서 생성·목록 도구 추가. worktree 자체가 최초 발명되었다고 쓰지 않는다.
2. https://github.com/openai/codex/releases/tag/rust-v0.162.0 — 공식 GitHub API published_at 2026-10-08T18:55:59Z = 10월9일03:55:59 KST. 조사시 약10시간 경과,36h 내. PR50148 합친 날짜10월2일은 릴리스 날짜와 구분.
3. https://learn.chatgpt.com/docs/environments/git-worktrees — Git 저장소 필요, 각 checkout의 파일 분리·공유 history, 앱Worktree/startingbranch/지정조건, Handoff와ignoredfiles, 현재문서의localchanges옵션. CLI 신기능과 앱 기존 UI 구분. 원고에서는 이 페이지에서 약200단어 이내 정보만 요약.
4. https://git-scm.com/docs/git-worktree — 각 worktree별HEAD/index, 여러branch checkout, 같은branch동시checkout제약. 원고에서 약200단어 이내 사용.

## 상품 검토

API search HTTP200/rCode0. 앞 두 검색결과 깃발은 관련 없어 제외. 세 번째 도서8334335964/item24064191002/vendor91095922729.
그림과 실습으로 배우는 깃 & 깃허브 입문, 한재원, 위키북스. 출판사 https://wikibook.co.kr/git/ 실제 목차:3장commit,4장branch/merge/충돌,5장PR,7장복원. worktree 전용 교재라고 주장하지 않는다.
필요 상황: AI 수정본을 채택할 때 branch·변경 기록·합치기 개념이 낯선 독자의 학습 자료. 추가구매 필수 아님.
작성자 댓글: ‘그림과 실습으로 배우는 깃 & 깃허브 입문 — AI 수정본을 합치기 전에 브랜치·병합·충돌 해결을 배우고 싶을 때 참고할 입문서예요.’
제휴 단축링크(API HTTP200/rCode0): https://link.coupang.com/a/hHwdDCLYJg

현재 상태: 주제/근거/상품 관련성 확정. 새 원고·자산 제작 전. 게시·전체 성공 미확인.
