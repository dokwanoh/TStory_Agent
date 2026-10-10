from pathlib import Path
import json,hashlib,shutil,subprocess,uuid
out=Path('outputs');root=Path('/Users/yeondu/.codex/generated_images/01a1107e-0797-71b0-af3f-83c510da3a10')
files={'cover':'exec-cb270a09-e3cf-420f-889c-e6ee95653318.png','infographic':'exec-fdf4cbf6-db27-430f-b755-683247be7171.png','section1':'exec-2b815114-b5f9-452e-8ab3-b2afed7d1e65.png','section2':'exec-a2c322b6-c050-4875-8eba-30c18be477a0.png','section3':'exec-d4be9baa-89e1-4730-ac94-e6bd8659fced.png'}
explains={'cover':'다음 요청 제안은 초안이며 전송은 사람의 선택','infographic':'수락 또는 직접 작성과 검토·전송, 대상과 베타 사용량','section1':'Tab으로 입력창에 담기와 전송의 분리','section2':'가정 예약폼의 검토 범위를 유지하는 다음 요청','section3':'제안 생성과 메시지 전송의 비용 조건 구분'}
alt={'cover':'Codex 28일 업데이트 5일차: 다음 요청을 미리 써주지만 Tab은 입력이고 전송은 내 선택임을 보여주는 개념 표지','infographic':'제안 보기, Tab 수락 또는 직접 쓰기, 읽고 고쳐 직접 전송하는 손그림 흐름과 개인 Pro 등 대상·베타 사용량 조건','section1':'Tab 입력창에 담기와 별도의 전송 동작을 키보드·메모로 표현한 생성 설명 사진. 공식 화면이 아님','section2':'검토만 하고 파일을 바꾸지 않는 원래 요청을 문제 후보·위치·근거 표로 명확하게 고치는 설명용 가정 카드','section3':'베타 중 제안 생성은 추가 사용량이 없고 메시지 전송에는 일반 사용량·과금 조건이 적용됨을 보여주는 생성 설명 카드'}
rows=[]; generated=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for role,file in files.items():
 suffix='infographic-v2' if role=='infographic' else role
 original=out/f'codex-day5-{suffix}.png';upload=out/f'codex-day5-{suffix}-web.jpg'
 shutil.copyfile(root/file,original)
 subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','85','--resampleWidth','1200',str(original),'--out',str(upload)],check=True,capture_output=True)
 generated.append({'filename':original.name,'sha256':sha(original),'tool':'image_generation','generated_source':str(root/file)})
 rows.append({'role':role,'original':original.name,'original_sha256':sha(original),'upload':upload.name,'upload_sha256':sha(upload),'explains':explains[role],'alt':alt[role],'affiliate':'https://link.coupang.com/a/hI8X8ATkGG','visual_check':'PASS generated result actually viewed; Korean, labels, explanatory match and crop inspected; no fake official UI'})
shutil.copyfile(root/'exec-c50a5ceb-429e-4a22-986d-28d042d61f09.png',out/'codex-day5-infographic-v1-rejected.png')
p=out/'codex-day5-workflow-v2.gif';rows.append({'role':'workflow','original':p.name,'original_sha256':sha(p),'upload':p.name,'upload_sha256':sha(p),'explains':'제안 수락 또는 직접 작성 후 사람이 검토·전송하는 독자 흐름','alt':'22초 손그림: 제안 수락과 직접 작성의 두 예시를 따로 따라가고 사람이 목적·범위·받을 결과를 읽고 직접 전송. 마지막5초 전체흐름. 설명용 시간','affiliate':'https://link.coupang.com/a/hI8X8ATkGG','visual_check':'Poster checked; actual selected-v2 playback ongoing, public playback pending'})
(out/'codex-day5-assets.json').write_text(json.dumps({'article':'codex-day5-article.md','article_sha256':sha(out/'codex-day5-article.md'),'media':rows,'native_status':'NOT_UPLOADED','publish_status':'NOT_PUBLISHED','failures':[{'asset':'codex-day5-infographic-v1-rejected.png','cause':'Other-request diamond had an unlabeled arrow into Tab stage','repair':'v2 removes incorrect arrow and labels direct-writing branch','reuse':'Only selected v2 from manifest'},{'asset':'codex-day5-workflow.gif','cause':'Both alternative paths animated concurrently, could suggest parallel execution','repair':'v2 shows example1 and example2 sequentially with explicit captions','reuse':'Only codex-day5-workflow-v2.gif'}]},ensure_ascii=False,indent=2)+'\n')
(out/'codex-day5-image-generation.handoff.json').write_text(json.dumps({'kind':'image_generation_handoff','session_id':str(uuid.uuid4()),'tool_kinds':['image_generation'],'generated_files':generated,'generated_count':5,'selected_count':5,'post_generation_copy':True},ensure_ascii=False,indent=2)+'\n')
print('5 actual native-generation originals copied; 5 selected JPEG uploads and GIF recorded by byte hashes.')
