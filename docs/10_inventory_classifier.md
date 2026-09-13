# 공개 인벤토리 분류기

## 실행과 재현

현재 입력: `.artifacts/public-inventory-20260907-input.json`

```sh
PYTHONPATH=src python3.11 -m tistory_growth_os classify-public-inventory \
  --input .artifacts/public-inventory-20260907-input.json \
  --output .artifacts/public-inventory-20260907-v1.1.0.json \
  --dry-run
```

`--input -`는 표준입력 JSON을 받는다. 입력에는 blog_url, checked_date, posts와 schema_version이 필요하다. 각 post에는 canonical_url, title, published_at, modified_at, category만 허용한다. 본문·description·쿠키·analytics는 수집하지 않는다. 날짜는 관측 메타데이터이며 내용 최신성의 증명이 아니다.

출력은 등록된 `public-blog-inventory` 스키마를 통과한 뒤 로컬 파일에 원자적으로 저장한다. 중복 canonical, 알려지지 않은 필드, 잘못된 날짜, 미래 수정일, 다른 블로그 URL은 차단한다. malformed 입력으로 재시도해도 기존 정상 결과를 덮어쓰지 않는다. 정규화된 결과와 분류 버전이 ID에 포함되어 입력 순서를 바꿔도 동일한 결과를 얻는다.

## 해석 계약

분류 버전 1.1.0의 모든 intent·freshness·risk·action 값은 **HYPOTHESIS: 검토 순서를 정하는 규칙 기반 후보**다. `status=pass`는 입력·출력 계약 처리 성공이며 콘텐츠 품질 합격이 아니다. 이 출력에서 게시 승인으로 이어지는 연결은 구현하지 않았다.

| 필드 | 규칙 | 한계 |
| --- | --- | --- |
| freshness | 일정·연도 등 제목 신호 + 수정일로부터 90일 이상이면 time_sensitive_stale; 그 외 365일 이상이면 evergreen_review_due; 나머지는 review_required | 90/365일은 잠정 점검 주기다. 실제 오류나 사실 만료 판정이 아니다. 수정일 갱신이 검수를 증명하지 않는다 |
| risk | 약물·세금 등 키워드 high; 경제 카테고리 또는 규제 등 키워드 medium; 그 외 low | low는 탐지 신호가 약하다는 뜻이다. 본문 고위험 주장의 부재를 보장하지 않는다 |
| intent_hint | 제목에서 방법·일정·비교 신호를 탐지하고 나머지 explanation | 검색 데이터나 독자 질문으로 검증한 intent가 아니다 |
| action_candidate | high → high_risk_review; 오래된 시의성 → refresh_or_retire; 그 외 cluster_review | 수정·삭제·발행 명령이 아니며 사람 검토가 필요하다 |
| link/media | not_audited / unknown 고정 | 전수 확인을 수행한 뒤 별도 계약으로 확장해야 한다 |

`src/tistory_growth_os/inventory/classify.py`에 규칙이 저장되며 변경 시 평가·버전을 갱신한다. 경제 카테고리 전체를 medium으로 잡는 보수적 규칙에는 과탐 가능성이 있다. 정확도·재현율은 독립 수동 라벨셋이 없으므로 UNKNOWN이다. 제목만으로 얻은 결과를 사실검증·전문가 검수·검색전략의 대체물로 사용하지 않는다.

## 검증 범위

실제 CLI 표준입력, 파일 입력, 정상 저장, 중복 URL 차단, malformed 재시도 보존, 입력 순서 변경 재현, 출력 JSON Schema, 최근 일정 글 오분류 방지, 관측일·수정일 관계, URL query/fragment 경계를 검사한다. 테스트 픽스처는 합성 데이터이고 실서비스 성과나 분류 정확도 평가셋이 아니다.

전체 63개 메타데이터는 이전 읽기 전용 공개 감사에서 획득했다. 1.1.0 재실행은 저장된 관측값을 사용하며 추가 웹 조회는 하지 않았다. 기존 1.0.0 artifact는 과거 결과로 보존한다.
