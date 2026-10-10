import AppKit
import ImageIO
import UniformTypeIdentifiers
let output = URL(fileURLWithPath: CommandLine.arguments[1])
let width=900, height=1180, frames=200
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
let sec=CGFloat(frame)/10,hold=sec>=15
let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:width,pixelsHigh:height,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
color(0xFFFDF5).setFill();NSRect(x:0,y:0,width:width,height:height).fill()
text("배포 뒤, 환경별 결과를 읽는 흐름",38,1110,32,true);text("Rollouts의 판정과 사람의 조치를 구분",38,1068,22)
box(38,950,772,90,0xDDECF7,hold||sec<3);text("1. 사람이 관찰 계획·연결 조건 정하기",55,1003,24,true);text("입력: PR · 배포 시스템 · 관측 정보",55,966,22)
box(38,800,772,110,0xE6E0F5,hold||(sec>=3&&sec<6));text("2. 해당 변경 배포 후 Rollouts가 관측",55,862,24,true);text("로그 · 수치 · 요청 경로",55,822,22)
let a=[NSPoint(x:440,y:950),NSPoint(x:440,y:910)];arrow(a)
box(38,650,772,110,0xFFF0C2,hold||(sec>=6&&sec<9));text("3. 환경별로 결과 보고",55,712,24,true);text("시험 환경 통과가 실제 환경 통과는 아님",55,672,22)
let b=[NSPoint(x:440,y:800),NSPoint(x:440,y:760)];arrow(b)
let paths=[[NSPoint(x:440,y:650),NSPoint(x:164,y:570)],[NSPoint(x:440,y:650),NSPoint(x:424,y:570)],[NSPoint(x:440,y:650),NSPoint(x:690,y:570)]];for p in paths{arrow(p)}
box(38,466,244,104,0xDDF1E7,hold||(sec>=9&&sec<11));text("검증된 정상",58,526,24,true);text("관찰 범위의 결과",54,489,20)
box(298,466,248,104,0xEBEDF0,hold||(sec>=11&&sec<13));text("판단 불가",325,526,24,true);text("비어 있는 근거 보기",312,489,19)
box(562,466,248,104,0xF5DFE8,hold||(sec>=13&&sec<15));text("이상 탐지",601,526,24,true);text("작성자에게 알림",584,489,20)
box(38,246,772,136,0xDDECF7,hold||sec>=12);text("4. 사람이 계획·조치 검토",55,330,24,true);text("근거 보완 또는 설정에 따른 되돌림 검토안",55,287,21);text("직접 병합·롤백하지 않음",55,253,22,true)
arrow([NSPoint(x:423,y:466),NSPoint(x:423,y:382)]);arrow([NSPoint(x:688,y:466),NSPoint(x:688,y:415),NSPoint(x:660,y:382)])
let retry=[NSPoint(x:38,y:295),NSPoint(x:18,y:295),NSPoint(x:18,y:850),NSPoint(x:38,y:850)];arrow(retry)
text("조치·근거 보완 뒤 다시 관측",45,181,24,true)
box(38,35,772,100,0xFFF0C2,false);text("Teams·기업 플랜 / 필요한 시스템 연결",55,94,22,true);text("판단 불가를 정상으로 치환하지 않기",55,54,22)
if !hold {if sec>=1&&sec<4{travel(a,(sec-1)/3)};if sec>=4&&sec<7{travel(b,(sec-4)/3)};for i in 0..<3{let start=CGFloat(8+i*2);if sec>=start&&sec<start+2{travel(paths[i],(sec-start)/2)}};if sec>=13&&sec<15{travel(retry,(sec-13)/2)}}
NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState();let img=bitmap.cgImage!
if [0,70,130,160].contains(frame){try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("agent-three-2-workflow-frame-\(frame).png"))}
CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]]as CFDictionary)
}
guard CGImageDestinationFinalize(dest)else{fatalError("GIF export failed")}
print("Rendered200 frames,20s,last5s hold")
