import AppKit
import ImageIO
import UniformTypeIdentifiers
let output = URL(fileURLWithPath: CommandLine.arguments[1])
let width=900, height=1180, frames=220
func color(_ v:UInt32)->NSColor{NSColor(srgbRed:CGFloat((v>>16)&255)/255,green:CGFloat((v>>8)&255)/255,blue:CGFloat(v&255)/255,alpha:1)}
let ink=color(0x24324A),accent=color(0x307277)
func text(_ s:String,_ x:CGFloat,_ y:CGFloat,_ size:CGFloat,_ bold:Bool=false){NSAttributedString(string:s,attributes:[.font:NSFont.systemFont(ofSize:size,weight:bold ? .semibold:.regular),.foregroundColor:ink]).draw(at:NSPoint(x:x,y:y))}
func line(_ ps:[NSPoint],_ active:Bool=false){let p=NSBezierPath();p.move(to:ps[0]);for(i,b)in ps.dropFirst().enumerated(){let a=ps[i],m=NSPoint(x:(a.x+b.x)/2+1,y:(a.y+b.y)/2-1);p.curve(to:b,controlPoint1:m,controlPoint2:m)};p.lineWidth=active ? 5:2.5;p.lineCapStyle = .round;(active ? accent:ink).setStroke();p.stroke()}
func arrow(_ ps:[NSPoint]){line(ps);let b=ps.last!,a=ps[ps.count-2],angle=atan2(b.y-a.y,b.x-a.x);for d:CGFloat in [-0.5,0.5]{line([b,NSPoint(x:b.x-12*cos(angle+d),y:b.y-12*sin(angle+d))])}}
func box(_ x:CGFloat,_ y:CGFloat,_ w:CGFloat,_ h:CGFloat,_ fill:UInt32,_ active:Bool){color(fill).setFill();NSBezierPath(roundedRect:CGRect(x:x,y:y,width:w,height:h),xRadius:18,yRadius:18).fill();line([NSPoint(x:x+16,y:y),NSPoint(x:x+w-16,y:y+1),NSPoint(x:x+w,y:y+16),NSPoint(x:x+w-1,y:y+h-16),NSPoint(x:x+w-16,y:y+h),NSPoint(x:x+16,y:y+h-1),NSPoint(x:x,y:y+h-16),NSPoint(x:x+1,y:y+16),NSPoint(x:x+16,y:y)],active)}
func travel(_ ps:[NSPoint],_ progress:CGFloat){let p=min(0.999,max(0,progress))*CGFloat(ps.count-1),n=Int(p),t=p-CGFloat(n),a=ps[n],b=ps[n+1];accent.setFill();NSBezierPath(ovalIn:CGRect(x:a.x+(b.x-a.x)*t-9,y:a.y+(b.y-a.y)*t-9,width:18,height:18)).fill()}
guard let dest=CGImageDestinationCreateWithURL(output as CFURL,UTType.gif.identifier as CFString,frames,nil)else{fatalError("GIF destination unavailable")}
CGImageDestinationSetProperties(dest,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFLoopCount as String:0]]as CFDictionary)
for frame in 0..<frames {
let sec=CGFloat(frame)/10,hold=sec>=17
let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:width,pixelsHigh:height,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
color(0xFFFDF5).setFill();NSRect(x:0,y:0,width:width,height:height).fill()
text("Codex 5일차: 다음 요청을 고르는 흐름",38,1110,31,true);text(hold ? "두 경로 모두 사람이 읽고 고쳐 전송" : (sec<12 ? "예시 1: 제안을 받아 읽고 전송" : "예시 2: 직접 써서 읽고 전송"),38,1068,24)
box(38,950,772,90,0xDDECF7,hold||sec<3);text("1. Codex가 현재 요청에 답변",55,1003,25,true);text("현재 대화의 맥락을 바탕으로 이어짐",55,966,22)
box(38,800,772,110,0xE6E0F5,hold||(sec>=3&&sec<6));text("2. 다음 메시지 제안이 나타날 수 있음",55,862,25,true);text("매 답변 뒤 항상 나타나는 것은 아님",55,822,22)
let a=[NSPoint(x:440,y:950),NSPoint(x:440,y:910)];arrow(a)
let paths=[[NSPoint(x:440,y:800),NSPoint(x:230,y:720)],[NSPoint(x:440,y:800),NSPoint(x:630,y:720)]];for p in paths{arrow(p)}
box(38,600,375,120,0xDDF1E7,hold||(sec>=6&&sec<9));text("제안을 쓰려면",58,675,25,true);text("Tab: 입력창에 담기",58,625,23)
box(435,600,375,120,0xF5DFE8,hold||(sec>=12&&sec<15));text("다른 요청이라면",455,675,25,true);text("직접 쓰기 / 제안 수정",455,625,23)
let joins=[[NSPoint(x:230,y:600),NSPoint(x:440,y:530)],[NSPoint(x:630,y:600),NSPoint(x:440,y:530)]];for p in joins{arrow(p)}
box(38,415,772,115,0xFFF0C2,hold||((sec>=9&&sec<12)||(sec>=15&&sec<17)));text("3. 사람이 목적·범위·받을 결과 읽기",55,480,25,true);text("원래 요청과 다르면 문장을 고치기",55,439,22)
let send=[NSPoint(x:440,y:415),NSPoint(x:440,y:355)];arrow(send)
box(38,240,772,115,0xDDECF7,hold||(sec>=10&&sec<12)||(sec>=16&&sec<17));text("4. 사람이 준비됐을 때 직접 전송",55,302,25,true);text("전송된 요청: 일반 사용량·과금 조건 적용",55,262,22)
text("Tab 수락 ≠ 작업 자동 실행",55,173,28,true)
box(38,35,772,106,0xFFF0C2,false);text("개인 Pro·18세 이상 등 이용 조건 필요",55,99,23,true);text("설명용 22초 · 실제 처리 시간 아님",55,58,22)
if !hold {
 if sec>=1&&sec<4{travel(a,(sec-1)/3)}
 if sec>=6&&sec<8{travel(paths[0],(sec-6)/2)}
 if sec>=8&&sec<10{travel(joins[0],(sec-8)/2)}
 if sec>=10&&sec<12{travel(send,(sec-10)/2)}
 if sec>=12&&sec<14{travel(paths[1],(sec-12)/2)}
 if sec>=14&&sec<16{travel(joins[1],(sec-14)/2)}
 if sec>=16&&sec<17{travel(send,sec-16)}
}
NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState();let img=bitmap.cgImage!
if [0,70,130,160].contains(frame){try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("codex-day5-workflow-frame-\(frame).png"))}
CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]]as CFDictionary)
}
guard CGImageDestinationFinalize(dest)else{fatalError("GIF export failed")}
print("Rendered220 frames,22s,last5s hold")
