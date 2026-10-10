from pathlib import Path
import re,html,json,subprocess
b=Path('outputs')
links={2:'https://link.coupang.com/a/hIZCptI9jE',3:'https://link.coupang.com/a/hIZCpzJrpc',4:'https://link.coupang.com/a/hIZCpEA4Zw',5:'https://link.coupang.com/a/hIZCpJ9SbQ'}
for n in range(2,6):
 if not (b/f'agent-next-{n}-banner.html').exists():continue
 md=(b/f'agent-next-{n}-article.md').read_text();lines=md.splitlines()[2:];blocks=[];i=0
 def fmt(t):return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',html.escape(t))
 while i<len(lines):
  l=lines[i].strip();i+=1
  if not l:continue
  if l.startswith('## '):blocks.append('<h2>'+fmt(l[3:])+'</h2>')
  elif l.startswith('|'):
   rows=[l]
   while i<len(lines) and lines[i].startswith('|'):rows.append(lines[i]);i+=1
   table='<table><tbody>'
   for j,row in enumerate(rows):
    if j==1:continue
    tag='th' if j==0 else 'td';table+='<tr>'+''.join('<'+tag+'>'+fmt(c.strip())+'</'+tag+'>' for c in row.strip('|').split('|'))+'</tr>'
   blocks.append(table+'</tbody></table>')
  elif l.startswith('버튼:'):
   url=lines[i].strip();i+=1;blocks.append('<p><a href="'+html.escape(url,quote=True)+'" target="_blank" rel="noopener">'+fmt(l[3:].strip())+'</a></p>')
  else:blocks.append('<p>'+fmt(l)+'</p>')
 copy='\n'.join(blocks);(b/f'agent-next-{n}-native-copy.html').write_text(copy)
 s=copy.replace('<p>','<p style="font-size:16px;font-weight:400;line-height:1.85;margin:22px 0;">').replace('<h2>','<h2 style="font-size:23px;font-weight:700;line-height:1.55;margin:42px 0 22px;">').replace('<table>','<table style="width:100%;border-collapse:collapse;">').replace('<th>','<th style="font-size:16px;padding:10px;border:1px solid #dce8ee;background:#edf5f9;">').replace('<td>','<td style="font-size:16px;font-weight:400;padding:10px;border:1px solid #dce8ee;">')
 s=re.sub(r'<a href="([^"]+)" target="_blank" rel="noopener">(.*?)</a>',r'<a href="\1" target="_blank" rel="noopener" style="display:block;padding:14px 18px;background:#173b4b;color:#fff;text-decoration:none;border-radius:12px;text-align:center;">\2 ↗</a>',s)
 banner='<div class="coupang-product-banner" style="margin:28px 0;text-align:center;">'+(b/f'agent-next-{n}-banner.html').read_text()+'</div>'
 e=s.index('</p>')+4;s=s[:e]+'\n<p class="affiliate-disclosure" style="font-size:14px;font-weight:400;line-height:1.7;margin:24px 0 12px;background:transparent;">이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.</p>\n'+banner+'\n{{cover}}\n'+s[e:]
 a=s.index('<h2');e=s.index('<h2',s.index('>1.')-150)
 s=s[:a]+'<div class="thirty-second-summary" style="background:#f6fbfd;border:1px solid #dce8ee;border-radius:18px;padding:22px;margin:28px 0;line-height:1.8;font-size:16px;">'+s[a:e]+'</div>\n{{infographic}}\n'+s[e:]
 for j in range(1,4):
  e=s.index('</h2>',s.index(f'>{j}.'))+5;s=s[:e]+'\n{{section'+str(j)+'}}\n'+s[e:]
 a=s.rfind('<h2',0,s.index('>3.'));s=s[:a]+banner+'\n'+s[a:]
 e=s.index('</p>',s.index('오늘 해볼 행동은'))+4;s=s[:e]+'\n{{workflow}}\n'+s[e:];s+='\n'+banner
 (b/f'agent-next-{n}-safe-layout.html').write_text(s)
 assets=[]
 for role in ['cover','infographic','section1','section2','section3']:
  orig=b/f'agent-next-{n}-{role}.png';out=b/f'agent-next-{n}-{role}-web.jpg'
  if orig.exists():subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','86','-Z','1024',str(orig),'--out',str(out)],check=True,stdout=subprocess.DEVNULL)
  assets.append({'role':role,'file':out.name,'link':links[n]})
 assets.append({'role':'workflow','file':f'agent-next-{n}-workflow.gif','link':links[n]})
 (b/f'agent-next-{n}-assets.json').write_text(json.dumps({'native_uploads':assets},ensure_ascii=False,indent=2))
 print(n,{'media':len(re.findall(r'{{\w+}}',s)),'banners':s.count('coupang-product-banner'),'bold':s.count('<strong>')})
