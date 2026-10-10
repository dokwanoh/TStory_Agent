# 독자 workflow 계약
원고:agent-three-1-article.md SHA e7767efb94d3582c6ec3bd92929536284ef290e4107ad2e3b61c941c38805588.
메시지:AI수정파일의비밀값의심점을읽기전용으로점검한뒤책임자가실제키·노출상태에따라조치한다.
노드:files 사람이AI변경파일범위를입력;check 읽기전용AI점검이의심위치를출력(모든키발견보장없음);scope 사람이키종류/책임자/커밋·원격전송을확인;decision 책임자가상황과서비스영향을판단;before 전송전파일·이력처리후재점검;exposed 이미노출된키책임자폐기/교체.
연결:files→check→scope→decision순차. decision→before조건원격전송전;decision→exposed이미원격노출. before→check수정후재점검권고. exposed는책임자조치종료이며자동폐기/재게시보장없음.
시작files;종료before확인또는exposed책임자대응. 미확인범위는사람확인노드에남음,무조건안전종료없음. 신규모델예고/플랜차이는원고에서설명하고GIF숫자비용없음.
타임라인0–2files/2–5check/5–7scope/7–10decision/10–12before와재점검/12–14exposed/14–18전체정지. 설명용18초로실행성능아님.
900×1000 GIF180프레임/10fps;AppKit+ImageIO실제렌더;마지막4초정지;독자과정이며게시절차아님.
