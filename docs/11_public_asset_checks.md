# 공개 링크·미디어 점검

## 검사 계약

`extract-public-assets --url URL`은 표준입력으로 받은 HTML을 로컬에서만 파싱한다. `.contents_style` 본문이 정확히 한 개이고 닫혀 있어야 성공한다. 본문 밖 메뉴·푸터를 제외하고 `a[href]`, `img[src]`, `iframe[src]`의 출현을 기록한다. 본문 텍스트는 저장하지 않는다. 제목과 원본 HTML 해시·관측일을 함께 기록해 해당 관측의 범위를 추적한다.

`PageAssets`와 `PublicAsset`은 frozen/slotted Python 데이터 계약이다. 출력은 프로젝트의 typed JSON 직렬화를 사용한다. 출력의 `status=extracted`는 파싱 성공이며 링크·이미지 품질 합격을 뜻하지 않는다.

## 접근과 보존

- 웹 조회는 감사 실행의 읽기 전용 curl 작업이며 Python 제품 런타임에 네트워크 의존성을 추가하지 않았다.
- 글 63개의 공개 HTML만 메모리에서 처리했다. 계정 로그인·쿠키·비공개 분석 데이터에 접근하지 않았다.
- 모든 URL query와 fragment를 제거하고 query가 있었는지 별도 표시한다. query 제거 주소는 원주소 대신 조회하지 않는다. 이미지 CDN의 임시 서명값은 저장·출력하지 않는다.
- 자바스크립트·data URL·userinfo·IP 주소·일부 사설 호스트는 추출에서 제외한다. 확인용 주소는 수집된 host 목록을 점검하고 공개 IPv4에 고정해 요청했다.
- robots.txt가 200이면 표준 라이브러리 RobotFileParser의 일반 사용자 에이전트 규칙을 적용한다. robots 404/410은 규칙 없음으로 처리하고, 3xx·접근 제한·연결 오류는 해당 origin 검사를 보류한다.
- 응답 검사는 HEAD 한 번, 연결 5초·전체 12초 제한이며 리디렉션을 자동 추적하지 않는다. 각 순차 작업 사이 최소 0.3초 간격을 둔다. 원문 HTML은 GET 20초·5MB 상한이다. 우회·무한 재시도·미승인 쓰기는 하지 않는다.

## 결과 해석

| 상태 | 의미 | 후속 확인 |
| --- | --- | --- |
| reachable | 해당 HEAD 요청에 2xx 응답 | 실제 본문·soft 404·이미지 표시·영상 재생까지 보증하지 않음 |
| redirect_unresolved | 3xx 응답, 자동 추적하지 않음 | 최종 목적지와 링크 대체 후보를 읽기 전용 검토 |
| missing_candidate | HEAD 404/410 | 일시 오류나 HEAD 제한 가능성이 있으므로 수동 확인 전 삭제 판단 금지 |
| access_limited | 401/403/429 | 로그인·봇 차단·속도 제한 가능성, 링크 고장으로 단정하지 않음 |
| robots_unresolved / robots_disallowed | robots 확인 실패 또는 대상 차단 | 검사를 중단하고 보류 |
| transport_unresolved / http_unresolved | 네트워크 오류 또는 다른 HTTP 응답 | 장애와 영구 소실을 구별하기 위한 후속 검토 |

모든 media_provenance_status는 unknown이다. 호스팅 주소, 출처 문구, HTTP 200만으로 이미지 사용권·원저작자·라이선스를 확인할 수 없다. `출처`라는 단어의 존재는 텍스트 단서일 뿐 이미지별 provenance 연결이 아니다.

alt 속성 누락과 빈 alt를 별도 집계한다. 접근성 원인 후보로 사용하며, 이미지 목적·주변 설명·장식 여부에 대한 판단은 이번 자동 검사에 포함하지 않는다. CSS 배경 이미지, srcset, 동적 DOM, 영상 재생 가능 여부, 모든 본문 사실의 출처 검증은 검사 범위 밖이다.

## 재현

```sh
PYTHONPATH=src python3.11 -m tistory_growth_os extract-public-assets \
  --url https://nedamma.tistory.com/entry/example < sanitized-local-fixture.html
PYTHONPATH=src python3.11 -m pytest -q tests/test_public_assets.py
```

실제 웹 관측은 시간에 따라 달라질 수 있다. 감사 artifact에는 당시 결과를 보존하며 테스트는 합성 HTML로 본문 범위·URL 제거·실패 경계를 재현한다. 최종 집계와 글별 후속 목록은 `.artifacts/public-assets-20260907-report.md`에 기록한다.

이번 네트워크 수집기는 제품 명령이 아닌 일회성 읽기 전용 오케스트레이션이었다. 원문 HTML은 보존하지 않아 당시 전체 원문을 재생할 수 없다. 최종 추출과 응답 JSON을 증거로 남기며, 원문 해시는 동적 서명값을 포함한 수집 응답 해시이지 안정적인 아티클 버전 식별자가 아니다. 설치 없이 사용하는 Python 표준 라이브러리와 합성 테스트만으로 오프라인 추출 계약을 재현할 수 있다.
