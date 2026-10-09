# 성공 경로 — post216 저장소 반영

- 결과: 원격 `main`에 커밋 `d13b15c1dfccccde8c783f604e61948ba823aa3f` 반영 완료.
- 범위: `STATUS.md`, `contracts/current-work.tsv`, `docs/162_ai_cvp_20261007_publication.md` 세 파일만 반영.
- 관찰: HTTPS 전송 세 번과 HTTP/1.1 전송 한 번, SSH 전송 한 번 모두 GitHub의 커밋 수신 단계에서 `Internal Server Error`로 거절됐다. 원격 조회와 쓰기 권한 확인은 성공했다. 서버 내부의 상세 원인은 확인되지 않았다.
- **성공 경로**: 인증된 GitHub CLI의 공식 Git API를 통해 부모 트리를 기준으로 세 파일의 트리를 생성하고, 로컬 커밋의 메시지·부모·작성자·커미터·시간을 그대로 전달했다. 트리 SHA와 커밋 SHA가 로컬과 일치하는지 확인한 뒤 `force: false`로 `main`을 갱신했다. 갱신 전 부모 SHA, 갱신 후 최종 SHA를 확인했다.
- 기존 작업 파일과 관련 없는 변경은 포함하지 않았다.

이 경로는 GitHub 수신 오류 발생 시에만 검토한다. 원격 브랜치가 변경됐거나 트리·커밋 SHA가 다르면 갱신을 중단한다.
