import AppKit
import ImageIO
import UniformTypeIdentifiers
let output = URL(fileURLWithPath: CommandLine.arguments[1])
let width=900, height=1000, frames=180
func color(_ v:UInt32)->NSColor{NSColor(srgbRed:CGFloat((v>>16)&255)/255,green:CGFloat((v>>8)&255)/255,blue:CGFloat(v&255)/255,alpha:1)}
let ink=color(0x24324A),accent=color(0x137D82)
func text(_ s:String,_ x:CGFloat,_ y:CGFloat,_ size:CGFloat,_ bold:Bool=false){NSAttributedString(string:s,attributes:[.font:NSFont.systemFont(ofSize:size,weight:bold ? .semibold:.regular),.foregroundColor:ink]).draw(at:NSPoint(x:x,y:y))}
func line(_ ps:[NSPoint],_ active:Bool=false){let p=NSBezierPath();p.move(to:ps[0]);for(i,b)in ps.dropFirst().enumerated(){let a=ps[i],m=NSPoint(x:(a.x+b.x)/2+1,y:(a.y+b.y)/2-1);p.curve(to:b,controlPoint1:m,controlPoint2:m)};p.lineWidth=active ? 5:2.5;p.lineCapStyle = .round;(active ? accent:ink).setStroke();p.stroke()}
func arrow(_ ps:[NSPoint]){line(ps);let b=ps.last!,a=ps[ps.count-2],angle=atan2(b.y-a.y,b.x-a.x);for d:CGFloat in [-0.5,0.5]{line([b,NSPoint(x:b.x-12*cos(angle+d),y:b.y-12*sin(angle+d))])}}
func box(_ x:CGFloat,_ y:CGFloat,_ w:CGFloat,_ h:CGFloat,_ fill:UInt32,_ active:Bool){color(fill).setFill();NSBezierPath(roundedRect:CGRect(x:x,y:y,width:w,height:h),xRadius:18,yRadius:18).fill();line([NSPoint(x:x+16,y:y),NSPoint(x:x+w-16,y:y+1),NSPoint(x:x+w,y:y+16),NSPoint(x:x+w-1,y:y+h-16),NSPoint(x:x+w-16,y:y+h),NSPoint(x:x+16,y:y+h-1),NSPoint(x:x,y:y+h-16),NSPoint(x:x+1,y:y+16),NSPoint(x:x+16,y:y)],active)}
func travel(_ ps:[NSPoint],_ progress:CGFloat){let p=min(0.999,max(0,progress))*CGFloat(ps.count-1),n=Int(p),t=p-CGFloat(n),a=ps[n],b=ps[n+1];accent.setFill();NSBezierPath(ovalIn:CGRect(x:a.x+(b.x-a.x)*t-9,y:a.y+(b.y-a.y)*t-9,width:18,height:18)).fill()}
let down1=[NSPoint(x:440,y:786),NSPoint(x:440,y:744)]
let down2=[NSPoint(x:440,y:637),NSPoint(x:440,y:595)]
let down3=[NSPoint(x:440,y:488),NSPoint(x:440,y:444)]
let decisions=[[NSPoint(x:440,y:335),NSPoint(x:225,y:280)],[NSPoint(x:440,y:335),NSPoint(x:660,y:280)]]
let retry=[NSPoint(x:805,y:231),NSPoint(x:867,y:231),NSPoint(x:867,y:695),NSPoint(x:810,y:695)]
guard let dest=CGImageDestinationCreateWithURL(output as CFURL,UTType.gif.identifier as CFString,frames,nil)else{fatalError("GIF destination unavailable")}
CGImageDestinationSetProperties(dest,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFLoopCount as String:0]]as CFDictionary)
for frame in 0..<frames {
let sec=CGFloat(frame)/10,hold=sec>=14
let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:width,pixelsHigh:height,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
color(0xFFFDF5).setFill();NSRect(x:0,y:0,width:width,height:height).fill()
text("Hermes 첫 자동화, 작게 시작",38,936,32,true);text("엑셀 세 파일을 합치는 가정 예시",38,894,22)
box(38,786,772,94,0xDDECF7,hold||sec<2);text("1. 내가 원본 복사 · 대상 세 파일 준비",55,843,24,true);text("복사본 준비는 접근 제한 설정의 대체가 아니에요",55,804,21)
box(38,637,772,106,0xE6E0F5,hold||(sec>=2&&sec<5));text("2. AI에 처리 규칙부터 설명 요청",55,699,24,true);text("원본 보존 · 별도 출력 · 중복 삭제 전 확인",55,655,22)
arrow(down1)
box(38,488,772,106,0xFFF0C2,hold||(sec>=5&&sec<7));text("3. 내가 규칙 검토 · 필요한 실행 승인",55,550,24,true);text("대상 파일 · 열 이름 · 저장 위치 대조",55,506,22);arrow(down2)
box(38,335,772,108,0xDDF1E7,hold||(sec>=7&&sec<10));text("4. AI 결과를 내가 입력과 비교",55,399,24,true);text("행 수 · 열 이름 · 중복 규칙 · 누락 확인",55,354,22);arrow(down3)
for a in decisions{arrow(a)}
box(38,181,375,98,0xDDECF7,hold||(sec>=10&&sec<12));text("기준과 일치",60,238,24,true);text("내가 사용 여부 결정",60,198,22)
box(450,181,360,98,0xF5DFE8,hold||(sec>=12&&sec<14));text("차이·누락 있음",470,238,24,true);text("요청 보완 → 다시 검토",470,198,21);arrow(retry)
text("파일 생성만으로 원하는 처리 성공은 아니에요",48,129,23,true)
box(38,35,772,66,0xFFF0C2,false);text(hold ? "전체: 복사 → 규칙 → 승인 → 결과 대조":"설명용 모션 · 실제 처리 속도나 성공 보장 없음",53,57,22,true)
if !hold {if sec>=1&&sec<3{travel(down1,(sec-1)/2)};if sec>=4&&sec<6{travel(down2,(sec-4)/2)};if sec>=6&&sec<8{travel(down3,(sec-6)/2)};if sec>=9&&sec<11{travel(decisions[0],(sec-9)/2)};if sec>=11&&sec<12{travel(decisions[1],sec-11)};if sec>=12&&sec<14{travel(retry,(sec-12)/2)}}
NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState();let img=bitmap.cgImage!
if [0,65,125,145].contains(frame){try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("agent-next-1-workflow-frame-\(frame).png"))}
CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]]as CFDictionary)
}
guard CGImageDestinationFinalize(dest)else{fatalError("GIF export failed")}
print("Rendered180 frames,18s,last4s hold; request/approval/comparison/feedback.")
