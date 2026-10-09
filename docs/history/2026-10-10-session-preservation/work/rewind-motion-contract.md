# Workflow 계약

- message: 되감기는 변경 방식과 복원 대상을 구분한 뒤 실제 파일·동작으로 판단한다.
- source: outputs/rewind-article.md 확정 원고, 2026-10-09.
- start: scope. end: next.
- nodes: scope(독자, 입력=잘못된 변경, 출력=남길 변경·기대 결과); tracked(독자, 추적된 파일 편집, 지점·대상 선택); other(독자, 명령·외부 변경, Git·별도 백업 검토); verify(독자, 선택한 복원 상태, 파일·동작 비교); reconsider(독자, 기대 불일치, 대상·지점·남길 변경 재검토); accept(독자, 기대 일치, 원하는 상태 확인); next(독자, 확인된 상태, 다음 수정).
- edges: scope→tracked/other 조건 분기=변경 방식. 각 경로→verify 순차. verify→reconsider 조건=기대와 다름. reconsider→verify 피드백=재검토 뒤 다시 확인. verify→accept 조건=기대 결과 일치. accept→next 순차.
- 근거: 1절 파일·대화 복원 구분, 2절 계산 수정 전 지점과 11,000원·버튼색 확인, 3절 명령·외부 변경의 별도 이력 및 기대 불일치 재검토.
- omissions: 실제 메뉴 UI와 Git 복원 명령은 환경별 상세가 달라 일반 검토 단계로 묶음. 두 갈래는 선택 조건이며 병렬 작업을 뜻하지 않는다.
- timeline: 0–3초 대상/범위, 3–6초 두 조건 비교, 6–10초 실제 확인, 10–14초 불일치 재검토, 14–17초 일치 결과, 17–22초 전체 정지. 애니메이션은 활성 단계와 화살표 강조만 사용.
- delivery: Swift/AppKit/ImageIO로 제작, outputs/rewind-workflow.gif, 900×1100, 220프레임/22초. 마지막 5초 전체 읽기 구간.
- 검증: 텍스트·화살표·잘림을 최종 프레임에서 확인. 실제 티스토리 업로드 GIF의 단계 전환·분기·피드백·최종 화면을 재생 관찰. 공개 직후 검토 안내는 새로고침 후 정상 원본으로 해제 확인. 앱 재생은 미확인.
