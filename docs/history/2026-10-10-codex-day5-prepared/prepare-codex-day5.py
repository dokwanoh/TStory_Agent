from pathlib import Path
import re, html, json, hashlib
out=Path('outputs'); prefix='codex-day5'
s=(out/f'{prefix}-article.md').read_text();title=s.splitlines()[0][2:]
link='https://link.coupang.com/a/hI8X8ATkGG';name='프롬프트 엔지니어링 교과서'; image='https://thumbnail.coupangcdn.com/thumbnails/remote/492x492ex/image/vendor_inventory/0a33/298d475c1788733daecfbe73e6086a4e9b6e2848e9d036a8dcb9a4959941.jpg'
raw_banner=(out/'agent-three-3-banner.html').read_text().replace('https://link.coupang.com/a/hI6iIY185k',link).replace('한 권으로 끝내는 소프트웨어 공학',name).replace('https://thumbnail.coupangcdn.com/thumbnails/remote/492x492ex/image/vendor_inventory/2eb7/44160eddaaf85b92ae652ac2fd81819a88f3368e1d5cac728b1649a3b368.jpg',image)
banner='<div class="coupang-product-banner" style="margin:28px 0;text-align:center;">'+raw_banner+'</div>'
(out/f'{prefix}-banner.html').write_text(banner)
def inline(x):
 x=html.escape(x,quote=False)
 x=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',x)
 return re.sub(r'\[([^]]+)\]\((https://[^)]+)\)',r'<a href="\2" target="_blank" rel="noopener">\1</a>',x)
native=[];i=1; lines=s.splitlines()
while i<len(lines):
 x=lines[i].strip();i+=1
 if not x:continue
 if x.startswith('## '):native.append('<h2>'+inline(x[3:])+'</h2>')
 elif x.startswith('|'):
  rows=[x]
  while i<len(lines) and lines[i].strip().startswith('|'):rows.append(lines[i]);i+=1
  t='<table><tbody>'
  for j,row in enumerate(rows):
   if re.match(r'\|[\s|:-]+\|$',row):continue
   tag='th' if j==0 else 'td';t+='<tr>'+''.join(f'<{tag}>{inline(v.strip())}</{tag}>' for v in row.strip('|').split('|'))+'</tr>'
  native.append(t+'</tbody></table>')
 else:native.append('<p>'+inline(x.removeprefix('👉 '))+'</p>')
n='\n'.join(native);(out/f'{prefix}-native-copy.html').write_text(n)
pstyle='font-size:16px;font-weight:400;line-height:1.85;margin:22px 0;'
hstyle='font-size:23px;font-weight:700;line-height:1.55;margin:42px 0 22px;'
f=n.replace('<p>',f'<p style="{pstyle}">').replace('<h2>',f'<h2 style="{hstyle}">')
f=f.replace('<table>','<table style="width:100%;border-collapse:collapse;">').replace('<td>','<td style="font-size:16px;font-weight:400;padding:10px;border:1px solid #dce8ee;">').replace('<th>','<th style="font-size:16px;padding:10px;border:1px solid #dce8ee;background:#edf5f9;">')
f=re.sub(r'(<p[^>]*>)<a href="([^"]+)" target="_blank" rel="noopener">([^<]+)</a></p>',r'\1<a href="\2" target="_blank" rel="noopener" style="display:block;padding:14px 18px;background:#173b4b;color:#fff;text-decoration:none;border-radius:12px;text-align:center;">\3 ↗</a></p>',f)
intro=f.index('</p>')+4
notice='<p class="affiliate-disclosure" style="font-size:14px;font-weight:400;line-height:1.7;margin:24px 0 12px;background:transparent;">이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.</p>'
f=f[:intro]+'\n'+notice+'\n'+banner+'\n{{cover}}\n'+f[intro:]
summary=f.index('<h2'); sec1=f.index('<h2',summary+3)
f=f[:summary]+'<div class="thirty-second-summary" style="background:#f6fbfd;border:1px solid #dce8ee;border-radius:18px;padding:22px;margin:28px 0;line-height:1.8;font-size:16px;">'+f[summary:sec1]+'</div>\n{{infographic}}\n'+f[sec1:]
for j in [1,2,3]:
 pattern=re.compile(r'(<h2[^>]*>'+str(j)+r'\..*?</h2>)')
 f=pattern.sub(r'\1\n{{section'+str(j)+'}}',f)
sec2=f.index('<h2',f.index('1. Tab'))
f=f[:sec2]+banner+'\n'+f[sec2:]
sec3=f.index('<h2',f.index('2. 다음 말'))
f=f[:sec3]+'{{workflow}}\n'+f[sec3:]
f+='\n'+banner
(out/f'{prefix}-safe-layout.html').write_text(f)
record={'title':title,'article_sha256':hashlib.sha256(s.encode()).hexdigest(),'visible_characters':3329,'category':'IT','tags':['Codex','28일업데이트','5일차','ComposerPredictions','AI코딩'],'topic_review':'.omo/evidence/codex-day5-topic-review.md','text_review':'.omo/evidence/codex-day5-text-review.md','topic_origin':'OWNER_SUPPLIED','freshness':'EXEMPT_BY_OWNER; exact announcement time UNKNOWN; help display Updated10hoursago not converted to release timestamp','product':{'id':7580731390,'item_id':20010985725,'vendor_item_id':95635610988,'name':name,'isbn':'9791198240828','publication_date':'2023-09-05','pages':196,'type':'single paper book; ebook and two-volume set excluded','api_search':'HTTP200/rCode0','api_deeplink':'HTTP200/rCode0','affiliate':link,'reason':'AI가 제안한 요청을 내 목적과 원하는 답변 형식에 맞게 고치는 기초를 배우려는 분께 참고가 되는 책이에요.','required_purchase':False},'planned_author_comment':name+' — AI가 제안한 요청을 내 목적과 원하는 답변 형식에 맞게 고치는 기초를 배우려는 분께 참고가 되는 책이에요.\n'+link,'publish_status':'NOT_PUBLISHED; daily15 cap remains','editor_status':'Not opened; existing article2 writer preserved','source_status':'official whole body captured','web_status':'NOT_PUBLISHED','app_status':'UNVERIFIED','workflow_playback':'PENDING','goal_scope':'additional day5; remaining2 of existing3 kept'}
(out/f'{prefix}-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('Prepared immutable draft, native transfer, safe late HTML, banner and metadata. No publish.')
