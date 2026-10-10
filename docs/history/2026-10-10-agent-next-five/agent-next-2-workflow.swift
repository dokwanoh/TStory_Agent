import AppKit
import ImageIO
import UniformTypeIdentifiers
let output = URL(fileURLWithPath: CommandLine.arguments[1])
let width=900, height=1000, frames=180
func color(_ v:UInt32)->NSColor{NSColor(srgbRed:CGFloat((v>>16)&255)/255,green:CGFloat((v>>8)&255)/255,blue:CGFloat(v&255)/255,alpha:1)}
let ink=color(0x24324A),accent=color(0xB04749)
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
text("AI 초안과 전송을 나누는 흐름",38,936,32,true);text("독자의 요청과 판단을 연결한 가정 예시",38,894,22)
box(38,786,772,94,0xDDECF7,hold||sec<2);text("1. 내가 결과와 허용 행동 지정",55,843,24,true);text("초안만 요청 · 외부 입력과 전송은 제외",55,804,21)
box(38,637,772,106,0xE6E0F5,hold||(sec>=2&&sec<5));text("2. AI가 허용 범위에서 초안 작성",55,699,24,true);text("막히면 진행 상태 보고 · 임의 우회하지 않기",55,655,22)
arrow(down1)
box(38,488,772,106,0xFFF0C2,hold||(sec>=5&&sec<7));text("3. 내가 문장과 사실을 검토",55,550,24,true);text("원문과 차이 · 받는 대상 · 보낼 내용 구분",55,506,22);arrow(down2)
box(38,335,772,108,0xDDF1E7,hold||(sec>=7&&sec<10));text("4. 내가 실제 전송을 별도로 판단",55,399,24,true);text("작성 완료와 전송 완료는 서로 다른 단계",55,354,22);arrow(down3)
for a in decisions{arrow(a)}
box(38,181,375,98,0xDDECF7,hold||(sec>=10&&sec<12));text("별도 허용함",60,238,24,true);text("확정한 대상·내용 전송",60,198,22)
box(450,181,360,98,0xF5DFE8,hold||(sec>=12&&sec<14));text("미승인 · 막힘",470,238,24,true);text("멈추고 상태 보고",470,198,21)
text("요청 문구는 기술적 접근 제어의 대체가 아니에요",48,129,23,true)
box(38,35,772,66,0xFFF0C2,false);text(hold ? "전체: 범위 → 초안 → 검토 → 별도 결정":"가정 흐름 · 실제 전송이나 안전 보장 없음",53,57,22,true)
if !hold {if sec>=1&&sec<3{travel(down1,(sec-1)/2)};if sec>=4&&sec<6{travel(down2,(sec-4)/2)};if sec>=6&&sec<8{travel(down3,(sec-6)/2)};if sec>=9&&sec<11{travel(decisions[0],(sec-9)/2)};if sec>=11&&sec<12{travel(decisions[1],sec-11)};}
NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState();let img=bitmap.cgImage!
if [0,65,125,145].contains(frame){try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("agent-next-2-workflow-frame-\(frame).png"))}
CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]]as CFDictionary)
}
guard CGImageDestinationFinalize(dest)else{fatalError("GIF export failed")}
print("Rendered180 frames,18s,last4s hold; request/approval/comparison/feedback.")
