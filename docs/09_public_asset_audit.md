# 09. 공개 블로그 자산 감사

Checked: 2026-09-07 KST  
Target: `https://nedamma.tistory.com`  
Mode: public, read-only; `external_write_count=0`

## 범위와 비범위

이 감사는 공개된 글·카테고리·canonical·사이트맵·RSS·robots·응답 상태와 대표적인 freshness/위험 신호만 사용한다. 관리자, 비공개 통계, 로그인 세션, 광고 계정, 쿠키에는 접근하지 않았다. 소유자의 명시적 결정에 따라 과거 문체·제목 습관·주제 취향은 미래 브랜드 보이스나 전략의 학습 데이터로 사용하지 않는다.

## 확인된 공개 인벤토리

| 항목 | 관측 결과 | 해석 한계 |
| --- | --- | --- |
| 블로그 표면 | 홈 200, HTML | 현재 트래픽·품질을 뜻하지 않음 |
| 사이트맵 | 72개 `loc`, 그중 entry 63개, category 경로 7개 | category 7에는 category root가 포함됨 |
| 공개 글 가용성 | sitemap의 63개 entry가 모두 HTTP 200 | 본문 사실이 최신·정확하다는 뜻이 아님 |
| 명명 카테고리 | IT, 경제, 과학, 생활정보, 블로그 운영, 스포츠 | 미래 포트폴리오로 채택하지 않음 |
| RSS | 최근 50개 item 노출 | 63개 전체 inventory가 아님 |
| RSS 최근 50개 상위 분류 | 생활정보 24, 경제 9, IT 7, 스포츠 5, 블로그 운영 3, 과학 2 | RSS의 첫 category 값을 분류로 해석; 나머지 category 요소는 tag |
| 관측 게시 범위 | 2019-12-12 ~ 2020-02-10 | 공개 페이지/순서 기반; 삭제·비공개 이력은 알 수 없음 |
| 대표 SEO 표면 | 표본 entry에 canonical, description, `og:type`, `og:url`, `og:title` 존재 | 전수 메타 품질 검사는 아직 하지 않음 |
| robots | guestbook, manage/owner/admin, search 계열 차단; bingbot crawl-delay 20 | 차단 경로는 조사하지 않음 |

## 대표 표본과 위험 분류

| 표본 | 공개 사실 | 초기 처리 가설 |
| --- | --- | --- |
| [2020년 마블 개봉 예정 글](https://nedamma.tistory.com/entry/2020%EB%85%84-%EB%A7%88%EB%B8%94-Marvel-%EA%B0%9C%EB%B4%89-%EC%98%88%EC%A0%95-%EC%98%81%ED%99%94-%EC%83%81%EC%98%81%EC%9D%BC-%EC%A0%95%EB%A6%AC) | 2020 일정 중심이며 canonical/meta가 노출됨 | `REFRESH_OR_RETIRE_CANDIDATE`; 현재 자료로 전면 재검증 전 재사용 금지 |
| [수익형 블로그 한달 정산](https://nedamma.tistory.com/entry/%EC%88%98%EC%9D%B5%ED%98%95-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EC%A0%95%EC%82%B0-%ED%95%9C%EB%8B%AC-%EC%8B%A4%EC%A0%81-%EC%95%A0%EB%93%9C%EC%84%BC%EC%8A%A4-%EC%95%A0%EB%93%9C%ED%95%8F-%EA%B4%91%EA%B3%A0%EB%8B%A8%EC%9C%84-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EC%9D%B8%EA%B8%B0%EA%B8%80-%EC%88%98%EC%9D%B5-%EA%B4%91%EA%B3%A0%EB%85%B8%EC%B6%9C%EA%B0%9C%EC%88%98-%EA%B4%91%EA%B3%A0%EC%9C%84%EC%B9%98) | 2020-01-12의 공개 자기보고로 AdSense/AdFit, 검색 유입, 특정 KTX 글 집중을 서술 | 과거 증거로만 보존; 현재 monetization/성과로 외삽 금지 |
| [알벤다졸 글](https://nedamma.tistory.com/entry/%EC%95%8C%EB%B2%A4%EB%8B%A4%EC%A1%B8-%EC%95%8C%EA%B3%A0%EB%A8%B9%EC%9E%90-%EB%AF%B8%EA%B5%AD-%EC%8B%9D%EC%95%BD%EC%B2%AD-FDA-%EA%B6%8C%EA%B3%A0%EC%82%AC%ED%95%AD-%EB%B6%80%EC%9E%91%EC%9A%A9-%EB%B3%B5%EC%9A%A9-%EB%B0%A9%EB%B2%95-%ED%94%BC%ED%95%BC%EA%B2%83-Albendazole-%EA%B5%AC%EC%B6%A9%EC%A0%9C-%ED%95%AD%EC%95%94) | 2020-01-11의 건강·약물 복용/부작용 주장을 포함하며 작성자가 비전문가임을 밝힘 | `HIGH_RISK_QUARANTINE`; 자동 refresh/홍보 제외, qualified review 또는 owner-approved retire 판단 필요 |
| [규제 샌드박스 글](https://nedamma.tistory.com/entry/%EA%B7%9C%EC%A0%9C%EC%83%8C%EB%93%9C%EB%B0%95%EC%8A%A4) | 2019-12-12의 제도 설명과 제3자 이미지 출처 표기가 존재 | 법·정책 최신성 및 이미지 license provenance 재검증 필요 |

이 표본은 위험 발견용이며 63개 전체 품질 판정이 아니다. 삭제, 수정, 비공개, noindex 또는 redirect는 모두 외부 변경이므로 이 감사가 승인하지 않는다.

## 현재 결론

1. 블로그는 “빈 출발점”이 아니다. 공개적으로 접근 가능한 legacy entry 63개와 검색 표면이 존재한다.
2. URL 가용성은 양호하지만, 게시 기간과 대표 표본상 freshness debt가 크다.
3. 주제 폭이 넓어 보이지만 이것만으로 권위·유입·수익을 판단할 수 없다.
4. 건강, 규제, 시의성, 제3자 이미지 표본은 신규 글 생산보다 먼저 위험 분류가 필요하다.
5. 공개 과거 정산은 당시 검색·수익 구조의 단서일 뿐 현재 baseline은 `UNKNOWN`이다.

## 결정론적 전수 metadata triage

`classify-public-inventory`는 63개 entry의 canonical, 제목, 게시/수정 시각, 카테고리만 받는다. 본문과 description은 입력·출력 계약에 없고 `style_analysis_performed=false`를 강제한다. 최종 결과는 `.artifacts/public-inventory-20260907-v1.1.0.json`, ID는 `inventory_8038d2f680796f123bc0a4cd1523df353ad044dd86fc4a685caf56c2a0e85976`이다. 전체 목록은 `.artifacts/public-inventory-20260907-report.md`에 있다. 모든 분류는 HYPOTHESIS이며 규칙·재현 명령·정확도 한계는 [분류기 설명](10_inventory_classifier.md)을 따른다.

| 분류 | 결과 | 의미 제한 |
| --- | --- | --- |
| freshness | `time_sensitive_stale=25`, `evergreen_review_due=38` | 제목 신호와 6년 이상 경과에 따른 triage; 사실검증 완료가 아님 |
| risk | `high=3`, `medium=16`, `low=44` | high-risk 키워드와 경제/규제 범주의 보수적 우선순위; 법적·의학적 판정이 아님 |
| intent hint | `schedule=9`, `how_to=4`, `comparison=1`, `explanation=49` | 제목 기반 routing hint; 실제 검색 질의 분석이 아님 |
| link audit | 전부 `not_audited` | 링크 정상으로 간주하지 않음 |
| media provenance | 전부 `unknown` | 이미지 권리 보유를 뜻하지 않음 |

## 다음 읽기 전용 단계

- 깨진 내부/외부 링크와 이미지 상태는 속도 제한·timeout·재시도 상한을 둔 별도 전수 검사로 구현한다.
- 각 미디어의 원출처·license·permission을 확인하기 전 `unknown`을 해제하지 않는다.
- 중복·잠식은 문체가 아니라 query intent와 핵심 질문의 겹침으로 판단한다.
- 실제 성과 우선순위는 승인된 analytics가 있을 때만 결합한다. 없으면 공개 inventory만으로 수익·트래픽 수치를 추정하지 않는다.

## 공개 근거

- Blog: `https://nedamma.tistory.com/`
- Sitemap: `https://nedamma.tistory.com/sitemap.xml`
- RSS: `https://nedamma.tistory.com/rss`
- Robots: `https://nedamma.tistory.com/robots.txt`

재검사 조건: 공개 URL 구조 변화, sitemap/RSS/robots 변경, owner가 private analytics 범위를 정함, 또는 refresh/merge/retire 의사결정 직전.
