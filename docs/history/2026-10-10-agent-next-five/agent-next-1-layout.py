from pathlib import Path
import re,html,json,subprocess
b=Path('outputs');md=(b/'agent-next-1-article.md').read_text();lines=md.splitlines()[2:];blocks=[];i=0
pstyle='font-size:16px;font-weight:400;line-height:1.85;margin:22px 0;';hstyle='font-size:23px;font-weight:700;line-height:1.55;margin:42px 0 22px;'
def fmt(t):return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',html.escape(t))
while i<len(lines):
 l=lines[i].strip();i+=1
 if not l:continue
 if l.startswith('## '):blocks.append('<h2>'+fmt(l[3:])+'</h2>')
 elif l.startswith('|'):
  rows=[l]
  while i<len(lines) and lines[i].startswith('|'):rows.append(lines[i]);i+=1
  table='<table><tbody>'
  for n,row in enumerate(rows):
   if n==1:continue
   tag='th' if n==0 else 'td';table+='<tr>'+''.join('<'+tag+'>'+fmt(c.strip())+'</'+tag+'>' for c in row.strip('|').split('|'))+'</tr>'
  blocks.append(table+'</tbody></table>')
 elif l.startswith('버튼:'):
  url=lines[i].strip();i+=1;blocks.append('<p><a href="'+html.escape(url,quote=True)+'" target="_blank" rel="noopener">'+fmt(l[3:].strip())+'</a></p>')
 else:blocks.append('<p>'+fmt(l)+'</p>')
copy='\n'.join(blocks);(b/'agent-next-1-native-copy.html').write_text(copy)
s=copy.replace('<p>','<p style="'+pstyle+'">').replace('<h2>','<h2 style="'+hstyle+'">').replace('<table>','<table style="width:100%;border-collapse:collapse;">').replace('<th>','<th style="font-size:16px;padding:10px;border:1px solid #dce8ee;background:#edf5f9;">').replace('<td>','<td style="font-size:16px;font-weight:400;padding:10px;border:1px solid #dce8ee;">')
s=re.sub(r'<a href="([^"]+)" target="_blank" rel="noopener">(.*?)</a>',r'<a href="\1" target="_blank" rel="noopener" style="display:block;padding:14px 18px;background:#173b4b;color:#fff;text-decoration:none;border-radius:12px;text-align:center;">\2 ↗</a>',s)
banner='<div class="coupang-product-banner" style="margin:28px 0;text-align:center;">'+(b/'agent-next-1-banner.html').read_text()+'</div>'
e=s.index('</p>')+4;s=s[:e]+'\n<p class="affiliate-disclosure" style="font-size:14px;font-weight:400;line-height:1.7;margin:24px 0 12px;background:transparent;">이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.</p>\n'+banner+'\n{{cover}}\n'+s[e:]
a=s.index('<h2');e=s.index('</p>',s.index('공식 게시물에 표시된 날짜는'))+4;s=s[:a]+'<div class="thirty-second-summary" style="background:#f6fbfd;border:1px solid #dce8ee;border-radius:18px;padding:22px;margin:28px 0;line-height:1.8;font-size:16px;">'+s[a:e]+'</div>\n{{infographic}}\n'+s[e:]
for n in range(1,4):
 e=s.index('</h2>',s.index(f'>{n}.'))+5;s=s[:e]+'\n{{section'+str(n)+'}}\n'+s[e:]
a=s.rfind('<h2',0,s.index('>3.'));s=s[:a]+banner+'\n'+s[a:]
e=s.index('</p>',s.index('오늘 해볼 행동은'))+4;s=s[:e]+'\n{{workflow}}\n'+s[e:];s+='\n'+banner
(b/'agent-next-1-safe-layout.html').write_text(s)
assets=[]
for role,orig in [('cover','cover'),('infographic','infographic'),('section1','section1'),('section2','section2'),('section3','section3')]:
 out=b/f'agent-next-1-{role}-web.jpg';subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','86','-Z','1024',str(b/f'agent-next-1-{orig}.png'),'--out',str(out)],check=True,stdout=subprocess.DEVNULL)
 assets.append({'role':role,'file':out.name,'link':'https://link.coupang.com/a/hIXSlVMHo4'})
assets.append({'role':'workflow','file':'agent-next-1-workflow.gif','link':'https://link.coupang.com/a/hIXSlVMHo4'})
(b/'agent-next-1-assets.json').write_text(json.dumps({'native_uploads':assets,'review':'5 new subject-specific illustrations inspected; readable Korean and arrows; no official UI' },ensure_ascii=False,indent=2))
print({'media_markers':len(re.findall(r'{{\w+}}',s)),'banners':s.count('coupang-product-banner'),'bold':s.count('<strong>'),'summary_cards':s.count('thirty-second-summary')})
