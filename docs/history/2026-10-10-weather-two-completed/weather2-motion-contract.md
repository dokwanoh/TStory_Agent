# 독자 흐름 계약
source weather2-article.md
message 목적지·이동시간에 맞는 예보를 읽고 출발 전 관측/예측을 구별하여 준비 결정.
nodes: A 독자 목적지·이동시간 선택(input일정/output조회기준); B 독자 시간별예보읽기(input조회기준/output예보); C 독자 관측예측시각구별(input자료/output자료종류·시각·단위); D 독자준비일정결정(input정보·도보구간/output준비); E 범위밖자료면 최신예보로돌아가기.
edges A→B→C→D, C→E 조건찾는시간범위밖/자료오래됨, E→B 최신예보. start A ends D.
omissions: 상세특보지침은 글/공식버튼, 자동판정이나 안전보장 없음.
timeline0–2A,2–4B,4–7C,7–10D,10–14범위밖분기와되돌림,14–18전체정지. 설명용18초900x1000GIF180frames.
