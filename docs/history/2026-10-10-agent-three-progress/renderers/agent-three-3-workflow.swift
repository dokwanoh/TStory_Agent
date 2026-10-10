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
text("Kiro: 앱 수정의 흐름을 다시 쓰기",38,1110,32,true);text("입력·출력·승인·멈출 조건을 함께 저장",38,1068,22)
box(38,950,772,90,0xDDECF7,hold||sec<3);text("1. 사람이 요구사항과 상한 정하기",55,1003,24,true);text("입력: 작업 범위 · 원하는 결과 · 레시피",55,966,22)
box(38,800,772,110,0xE6E0F5,hold||(sec>=3&&sec<6));text("2. 구현 단계가 변경과 결과 남기기",55,862,24,true);text("다음 단계가 읽을 출력물을 연결",55,822,22)
let a=[NSPoint(x:440,y:950),NSPoint(x:440,y:910)];arrow(a)
box(38,650,772,110,0xFFF0C2,hold||(sec>=6&&sec<9));text("3. 별도 세션에서 검토 · 결과 합치기",55,712,24,true);text("병렬 검토라면 필요한 결과 모두 기다리기",55,672,21)
let b=[NSPoint(x:440,y:800),NSPoint(x:440,y:760)];arrow(b)
let paths=[[NSPoint(x:440,y:650),NSPoint(x:230,y:570)],[NSPoint(x:440,y:650),NSPoint(x:630,y:570)]];for p in paths{arrow(p)}
box(38,450,375,120,0xDDF1E7,hold||(sec>=9&&sec<12));text("승인",63,525,25,true);text("최초 요구사항과 대조",58,478,22)
box(435,450,375,120,0xF5DFE8,hold||(sec>=12&&sec<15));text("수정 필요",463,525,25,true);text("상한 미만: 구현으로 돌아감",451,478,19)
let retry=[NSPoint(x:810,y:508),NSPoint(x:844,y:508),NSPoint(x:844,y:854),NSPoint(x:810,y:854)];arrow(retry)
box(38,260,772,125,0xDDECF7,hold||sec>=12);text("미승인 상태에서 상한에 도달하면 중단",55,333,25,true);text("해결하지 못한 항목을 남겨 사람 판단",55,286,22);arrow([NSPoint(x:628,y:450),NSPoint(x:628,y:385)])
text("횟수를 다 쓴 것 ≠ 검증된 성공",50,188,25,true)
box(38,35,772,108,0xFFF0C2,false);text("최대 3회는 공식 예시의 설정",55,101,23,true);text("모든 작업의 공통 규칙 아님",55,60,22)
if !hold {if sec>=1&&sec<4{travel(a,(sec-1)/3)};if sec>=4&&sec<7{travel(b,(sec-4)/3)};for i in 0..<2{let start=CGFloat(8+i*3);if sec>=start&&sec<start+3{travel(paths[i],(sec-start)/3)}};if sec>=12&&sec<15{travel(retry,(sec-12)/3)}}
NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState();let img=bitmap.cgImage!
if [0,70,130,160].contains(frame){try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("agent-three-3-workflow-frame-\(frame).png"))}
CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]]as CFDictionary)
}
guard CGImageDestinationFinalize(dest)else{fatalError("GIF export failed")}
print("Rendered200 frames,20s,last5s hold")
