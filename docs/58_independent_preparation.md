# 독립 제작 명령

현재 후속 상태(2026-09-21): 사실 항목만 실패한 경우의 1회 본문 수정·새 독립 검수와 통합 명령을 통한97번 실제 공개가 추가되었습니다. 이 문서의005번 증거는 보존하며, 후속 실증과 한계는 docs/61_combined_live_proof.md를 따릅니다. 그 밖의 품질 실패 자동 복구는 여전히 미구현입니다.

## 최종 결과 — 실제 제작 및 재실행 성공

`preparation-20260921-005`가 실제 조사·Astra 선정·원문 작성·신규 이미지 네 장·
독립 검수를 거쳐 `local_package_reviewed`로 종료했다. 최종 검수 11항목 모두 true,
issues는 빈 배열이다. 단, 개발 중 검수 실패를 수정하고 같은 ID로 재개한 결과이며
최초부터 무결점 무인 실행이었다고 주장하지 않는다.

- 패키지: `.artifacts/preparation/preparation-20260921-005/package/`
- 제목: 맨시티 5-3 승리, 다섯 골 넣으면 슈팅도 더 많을까요?
- SHA-256: `690591082101fd05653f9ca64a6d0a3d4f6b3ec40e05949fc26d53325df41171`
- 기존 `load_immediate_package`로 실제 로드: `REVIEW_APPROVED`, media4.
- 같은 명령 재실행: research/selection/writing/media/review 모두 checkpoint_reused,
  동일 패키지 성공; 새 제공자 호출이나 중복 생성 없음.
- 새 글 게시·예약·스케줄러 재개 없음. `external_blog_write_count=0`, STOP 유지.
- 콘텐츠 유효기간: 2026-09-21 22:00 KST. 이 시각 이후 기존 패키지는 재사용 불가.

run005의 첫 검수는 10/11 합격, voice만 실패했다. 내부 검증 메모를 링크 문구로 노출한
렌더러 결함을 회귀 테스트로 고쳤다. 링크는 독자용 섹션 질문/출처 도메인으로 만들고
같은 목적지를 한 번만 표시한다. 실패한 inspection과 review 원본/영수증/시도 파일은
`rejected-review-1/`로 **이동 보존**했다. 본문 JSON·조사·선정·이미지는 변경하지 않았고,
새 바이트를 새 독립 세션에서 검수했다. 이 개발 복구는 불명확한 저장의 자동 재시도가 아니다.

최종 구현: `6c5b61e6753a2cc7064acb3a38bad1048efc3a37` (앞선 수정 e80a737,8c717f6 포함),
feature branch push 확인. 원격 auto-merge/PR 합격은 주장하지 않는다. 남은 범위는
실제 공개 실행기 자동 호출/운영 재개이며 이번 로컬 제작 완료와 별개다.
아래의 실패/미입증 기록은 수정 전 이력으로 보존한다.

최종 코드 검증: 전체 `tests browser_tests` **616 passed / 174.98s**,
fresh basedpyright 전체 src/변경 테스트 **0 errors, 0 warnings**,
no-excuse **12 files pass**. CLI help/dry-run, 잘못된 ID의 exit2 보류,
실제 승인 패키지 로드와 동일 ID 무호출 재실행, compile/diff 검사를 수행했다.
마지막 출처 링크 수정은 두 독립 화면 검수 모두 최신 6/6 캡처에서 PASS였으며,
기록은 최종 코드6c5b61e에 결속했다. 제외된 감사 항목을 복원하지 않았다.

## 2026-09-21 조사 진단 보강

이전 빈 후보 결과는 파서가 후보를 지운 것이 아니라 제공자 응답 자체가 빈 배열이었다.
별도 읽기 전용 실제 조사에서는 원발표가 오래된 과학 기사, 공식 결과 미확인,
원문 열람 실패, 사건 시각 미확인을 구분했다. 이 진단은 이전 실행의 정확한 원인이나
다섯 후보 적격성을 증명하지 않는다. 진단 후보를 제작 입력에 수동 주입하지 않았다.

새 조사 응답은 `search_notes`, `rejected_leads`에 조사 범위와 후보별 탈락 이유·공개 출처를 남긴다.
부족한 후보를 이유 없이 빈 배열로 반환하면 `research_shortfall_undocumented`로 구분한다.
기존 한 차례 확장 조사 한도는 유지한다. 기존 기록 형식은 읽을 수 있지만 새 제공자 스키마는
진단 필드를 요구한다. 정책 검색보다 사건 조사를 먼저 수행하며, 부분 후보도 버리지 않도록 했다.
정확히 다섯 후보, 24시간, 공식·독립 출처, 검수 기준은 변경하지 않았다.

회귀 RED: 새 진단 필드 두 테스트가 기존 계약에서 실패. GREEN: 관련27개 통과.
전체 `pytest tests browser_tests -q`: **608 passed in 179.95s**.
fresh basedpyright src/변경 테스트: **0 errors, 0 warnings**. 4개 파일 no-excuse,
compile, CLI help/dry-run, diff 검사 통과. 실제 개선 실행은
`.artifacts/preparation/preparation-20260921-002`로 분리해 기존001 기록을 보존한다.
새 시각/스키마의 로컬 실증이며 게시·예약·반복 작업 재개가 아니다.

CLI JSONL/구조화 최종 응답 사용 근거는 [공식 비대화형 실행 문서](https://learn.chatgpt.com/docs/non-interactive-mode)에서 재확인했다.

실제002 실행은 후보5건을 반환했으나 `/sources/checked_at`에 `UNKNOWN`을 넣어 차단됐다.
`search_notes`에 현재 UTC를 웹에서 얻지 못했다는 이유가 기록됐다. 실행기의 감사 시각을
모델에게 조회시키던 책임 분리 오류다. 이제 모델은 확인한 출처에 `RUNTIME` 표지만 반환하고,
실행기가 응답 수신 후 UTC를 `research-checked-at.txt`에 한 번 저장해 정규화한 증거에 연결한다.
재실행은 같은 시각을 사용한다. 사건 발생 시각이나 오래된 `UNKNOWN`은 수정하지 않는다.
이 시각은 조사 보고를 받은 시점이며, 출처 내용의 진위를 자동 보증하지 않는다. 별도 검수가 유지된다.
기존002 응답은 그대로 실패 증거로 보존하고 수정 계약의 실증은003으로 분리했다.
시각 경계 RED 후 관련30개 테스트 통과, fresh type 오류0, no-excuse5files 통과.
최신 전체 회귀: **611 passed in 168.49s**. 실제003 초기 조사에서 후보1건을 보존하고
UTC 기록 후 기존 확장 조사로 전환했다. 따라서 시각 수집 결함의 실제 해소는 확인했으나,
다섯 후보 및 본문·미디어·최종검수 완주는 이 관측만으로 증명하지 않는다.

## 범위

후보 조사 → 최고급 모델 최종 선정 → 본문과 네 장 이미지 → 독립 품질검수 → 로컬 패키지.
게시, 예약, 스케줄 재개, 권한 파일 생성은 하지 않는다. 토큰 절감 비교는 이번 작업에서 제외했다.
기존 로그인된 Codex CLI를 사용하며 신규 유료 API나 패키지를 설치하지 않는다.

```sh
PYTHONPATH=src python3 -m tistory_growth_os.preparation --run-id article-20260921-001
PYTHONPATH=src python3 -m tistory_growth_os.preparation --run-id article-20260921-001 --execute
```

첫 명령은 네트워크·모델 호출·파일 생성이 없는 dry-run이다. 두 번째만 제작을 실행한다.
실행 ID를 유지한 재실행은 해시가 일치하는 단계 결과를 재사용한다. 중간 호출의 성공 여부가
불명확하면 자동 재호출하지 않고 `stage_attempt_uncertain`으로 멈춘다. ID를 바꿔 우회하지 않는다.
후보 수가 부족한 정상 응답에는 같은 기준시각에서 한 차례 범위를 넓힌 조사를 수행한다.
확장 조사도 기준을 만족하지 못하면 중단하며 무한 호출하지 않는다.

## 결과와 계약

- 실행 기록: `.artifacts/preparation/<run-id>/`. RSS/과거 글 자료, 원문 JSON 응답,
  요청·응답 해시, 세션·도구 종류, 단계별 시도 기록이 분리된다. 비밀이나 전체 CLI 로그는 저장하지 않는다.
- `inspection/`: 검토 대상이며 게시 허가가 아니다.
- `package/`: 검수를 통과한 정확한 바이트의 HTML, manifest, evidence, quality, 네 장 JPEG.
- `contracts/reviews/<digest>.json`: 기존 게시 실행기가 읽는 로컬 검토 기록. 외부 게시 동의가 아니다.
- 정상 종료: `local_package_reviewed`, exit 0. 실패: `held`와 구체 사유, exit 2.
- stderr 단계 이벤트는 started/response_recorded/checkpoint_reused다. 응답 저장이 품질 합격을 뜻하지 않는다.

## 유지한 검증

1. 다섯 후보, 각 초안·공식 출처·독립 도메인·주장 연결·24시간 시각 검증.
2. 검증된 후보에서만 선정, 허용 출처 링크만 본문에 사용, 실제 분류 라벨.
3. 승인된 post89 기반 요약 상자·문단 간격·친근한 문체·네 문맥별 이미지 자리와 alt.
4. 공식 이미지 출처·사용권·크레딧 또는 실제 내장 생성 도구 사용 증거.
5. 서로 다른 네 JPEG, 로컬 디코드 가능 여부·크기·기존 이미지 바이트 재사용 차단.
6. 제작 세션과 다른 검수 세션, 사실·권리·독창성·문체·이미지·정책 등 11개 항목 전부 통과.
7. 정확한 패키지 해시/유효기간, 검수 후 변조·심볼릭 링크·불명확한 재시도 차단.

실제 screen reader, 모든 print, Lighthouse, 외부 광고, 원격 이미지 픽셀 표시 검사는
소유자 제외 상태 그대로다. 로컬 JPEG 구조 검사는 이를 되살리는 화면 비교가 아니다.
본문 스타일은 `tistory-editorial-cycle`의 post89/editorial baseline을 실행 가능한 렌더러로 옮겼다.
품질 점수를 낮추거나 영업용 주제 선정 사유를 독자 본문에 넣지 않는다.

## 재현 검증과 한계

- 실패 먼저 작성한 테스트로 단계 부재, 파서, 불완전 이미지, 자기 검수, 검수 거절,
  출처·신선도·중복·변조·재실행 경계를 확인했다.
- 별도 프로세스의 실제 CLI 진입점에 명시적 테스트 제공자를 연결해 전체 생성/거절/재실행을 검증했다.
  생성된 패키지를 기존 `load_immediate_package`로 읽고 검토 승인 계약 일치도 확인했다.
  이 fixture는 실재 최신 기사나 실사 제작 품질의 증거가 아니다.
- 실제 CLI 웹 검색에서 `web_search` 이벤트가 `/item/id`를 중복 출력함을 관측했다.
  전송 어댑터의 정확한 해당 형식만 첫 ID를 별도 이름으로 보정한다. 도메인 JSON의 중복 키 금지는 유지한다.
  실제 웹 검색 재실행은 exit 0과 검색 도구 사용으로 확인했다.
- 실제 `preparation-20260921-001` 초기 조사는 적격 후보 0건을 반환했고, 생성으로 넘어가지 않았다.
  과거의 두 전송 실패 시도는 별도 파일로 보존했다. 알려진 전송 결함 수정 후 같은 입력을 사용했다.
  원시 실패 응답 전체를 보존하지 않았으므로 첫 실패의 상세 원인을 단정하지 않는다.
- 기본 실행 환경은 현재 Mac의 Python/Codex와 내장 `/usr/bin/sips`다. 다른 OS 이식은 인증하지 않았다.
- 이미지 생성과 독립 의미검수의 실제 전체 완주는 아직 입증되지 않았다. 테스트 성공과 구분한다.
- 과거 이미지 비교는 최근 수정된 로컬 패키지 최대 다섯 개다. 전체 실제 게시 이력이나 시각적 유사성의
  완전한 자동 검출을 의미하지 않는다. 공식 이미지의 사용권 진위는 별도 의미검수에서도 확인한다.

상주 LSP는 새 모듈의 존재를 찾지 못하는 오래된 import 진단을 반환했다. 별도 fresh basedpyright
프로세스와 실제 Python import/CLI 검사를 사용해 코드 진단을 교차검증했다. 도구 캐시를 정상으로
오인하거나 전역 설정을 바꾸지 않는다.

## 최종 확인 — 2026-09-21

- `PYTHONPATH=.:src:.venv/lib/python3.11/site-packages pytest tests browser_tests -q`:
  **606 passed in 169.93s**. 변경 범위 25개 테스트 포함.
- fresh `basedpyright` 전체 src 및 새 테스트: **0 errors, 0 warnings**.
- Python no-excuse 검사: **no violations in 14 files**. 컴파일과 `git diff --check` 통과.
- CLI help와 dry-run 정상, 잘못된 ID exit2, fixture CLI 생성/거절/재실행 확인.
- 실제 확장 조사도 후보 0건을 반환했다. 같은 명령 재실행 시 초기·확장 조사 모두
  `checkpoint_reused` 후 `five_qualified_candidates_required`; 추가 모델 호출 없이 중단했다.
- 작은 별도 실제 조사에서는 스포츠 사건 한 건의 보도를 찾았지만 공식 원문은 403으로
  열람되지 않았다고 응답했다. 이는 세상에 새 이슈가 없다는 뜻이 아니다. 조사기의 적격
  후보 확보 및 전체 제작 완주가 아직 미입증이라는 한계다. 이 후보를 수동으로 끼워 넣지 않았다.
- 따라서 독립 명령/검증 계약 구현은 완료, 실제 최신 글의 전 단계 성공 인증은 **미완료**다.
  게시·예약·반복 작업은 활성화하지 않았다.

## 2026-09-21 후속 실제 실행 및 원인 수정

- run002는 후보 다섯 개를 찾았으나 실제 확인 시각을 모델이 확보하지 못해
  `checked_at=UNKNOWN`으로 반환했다. 시계 책임을 호스트로 이동했다.
  모델은 실제 확인한 출처만 `RUNTIME`으로 표시하고, 실행기는 완료 UTC를 한 번 기록해
  정규화한다. 기존 UNKNOWN이나 사건 시각은 보정하지 않는다. 재실행도 원래 확인 시각을 유지한다.
- run003은 정규화에는 성공했지만 초기/확장 조사 모두 후보 한 개로 보류됐다.
  이전에 찾은 공개 단서를 버리지 않도록 최근 두 조사, 각 최대 다섯 후보를 다음 조사 입력에
  UNVERIFIED로 전달한다. 새 실행에서 원문·사실·시각을 다시 확인해야 한다.
  과거 검수 기록/게시 권한을 전달하지 않으며 부모 심볼릭 링크를 거부한다.
- run004는 실제 다섯 후보 → Astra 최종 선정 → 한국어 본문 → 새 JPEG 네 장까지 진행했다.
  첫 검수 진입은 `generation_tool_evidence_required`로 차단됐다. 동일 세션의 생성 원본은
  네 장 존재하지만 exec JSONL에는 이미지 생성 이벤트가 없었다.
- Codex rust-v0.155.1의 [exec JSONL 변환기](https://github.com/openai/codex/blob/4e21628f9ec9ee656650cd2b62ef92225725b5ac/codex-rs/exec/src/event_processor_with_jsonl_output.rs)는
  이미지 생성 항목을 매핑하지 않고 `_ => None`으로 버린다. 별도
  [프로토콜](https://github.com/openai/codex/blob/4e21628f9ec9ee656650cd2b62ef92225725b5ac/codex-rs/protocol/src/protocol.rs)에는
  ImageGenerationEnd/status/saved_path가 있다. 따라서 도구 이벤트 이름만 요구하던 어댑터 가정이 잘못됐다.
- 원래 CLI 영수증은 변경하지 않았다. 이벤트가 없을 때만 동일 세션의 Codex 관리
  `generated_images/<session>/exec-*.png`를 읽어 정확한 수, 시도 이후 시각, PNG 서명,
  크기와 비심볼릭 경로를 확인하고 원본 SHA-256을 `media-native-evidence.json`에 기록한다.
  파일이나 모델의 자기 주장만으로는 통과하지 않으며, 다른 세션/오래된 파일/누락/변조는 보류한다.
  이 증거는 로컬 런타임 관리 출력에 대한 신뢰 경계이지 암호학적 원격 증명이 아니다.
- 수정 후 run004 동일 ID 재실행은 네 단계 체크포인트를 재사용하고 새 이미지 생성 없이
  독립 review에 도달했다. 외부 게시나 예약, 스케줄러 활성화는 수행하지 않았다.
- run004 review는 사실·24시간·독창성·독자 가치·정책에 합격했지만 여섯 항목을 보류했다.
  생성 원본/최종 파일 해시와 분류 목록이 검수 입력에서 빠졌고, 이력 조회가 fasttrack의
  manifest 세 개만 읽었다. 반복 링크 문구, 일부 alt의 보이지 않는 시점 추론과 문체 문제도 있었다.
  실패 결과를 보존하고 증거 전달과 본문 지침을 수정했다. 최근 로컬 이력에는 scheduled의
  manifest와 기존 publish-manifest도 포함하되 실제 최신 공개 글 전체라고 주장하지 않는다.
- 링크 수정은 기존 DESIGN.md 범위 안에서 출처 설명/도메인과 keep-all 줄바꿈만 바꿨다.
  실제 Chrome 로컬 캡처375/768/1280과 각 키보드 포커스 상태를 두 독립 검토자가 최종 PASS로 확인했다.
  `.artifacts/preparation-link-qa/review.md`에 e80a7371f76d5e68c8f64d2ff307ee138c82d7f7 코드와
  6/6 캡처 검토 결과를 결속했다. 이는 run004 내용의 발행 승인이나 원격 사진 표시 검증이 아니다.
