import AppKit
import ImageIO
import UniformTypeIdentifiers
let output=URL(fileURLWithPath:CommandLine.arguments[1])
func color(_ n:UInt32)->NSColor {NSColor(srgbRed:CGFloat((n>>16)&255)/255,green:CGFloat((n>>8)&255)/255,blue:CGFloat(n&255)/255,alpha:1)}
func text(_ s:String,_ x:CGFloat,_ y:CGFloat,_ size:CGFloat,_ bold:Bool=false) {NSAttributedString(string:s,attributes:[.font:NSFont.systemFont(ofSize:size,weight:bold ? .semibold:.regular),.foregroundColor:color(0x263247)]).draw(at:NSPoint(x:x,y:y))}
func line(_ points:[NSPoint],_ hot:Bool=false) {let p=NSBezierPath();p.move(to:points[0]);for v in points.dropFirst(){p.line(to:v)};p.lineWidth=hot ? 5:2.5;p.lineCapStyle = .round;(hot ? color(0x2875E8):color(0x263247)).setStroke();p.stroke()}
func arrow(_ points:[NSPoint],_ hot:Bool=false) {line(points,hot);let b=points.last!,a=points[points.count-2],t=atan2(b.y-a.y,b.x-a.x);for d:CGFloat in [-0.5,0.5]{line([b,NSPoint(x:b.x-12*cos(t+d),y:b.y-12*sin(t+d))],hot)}}
func box(_ x:CGFloat,_ y:CGFloat,_ w:CGFloat,_ h:CGFloat,_ fill:UInt32,_ hot:Bool) {color(fill).setFill();let p=NSBezierPath(roundedRect:CGRect(x:x,y:y,width:w,height:h),xRadius:18,yRadius:18);p.fill();p.lineWidth=hot ? 5:2.5;(hot ? color(0x2875E8):color(0x263247)).setStroke();p.stroke();line([NSPoint(x:x+12,y:y+3),NSPoint(x:x+w-15,y:y+1)],hot)}
guard let dest=CGImageDestinationCreateWithURL(output as CFURL,UTType.gif.identifier as CFString,260,nil) else {fatalError("output")}
CGImageDestinationSetProperties(dest,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFLoopCount as String:0]] as CFDictionary)
for f in 0..<260 {
 let s=Double(f)/10,hold=s>=21,stage=s<4 ? 0:s<8 ? 1:s<13 ? 2:s<17 ? 3:4
 let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:900,pixelsHigh:1100,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
 NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
 color(0xFFFDF5).setFill();NSRect(x:0,y:0,width:900,height:1100).fill()
 text("빠른 모드, 작은 요청으로 판단하기",47,1038,33,true)
 text("가정 예시 · 독자가 선택하고 결과를 확인해요",61,994,27)
 box(100,855,700,100,0xD8F0EE,hold || stage==0)
 text("같은 작은 요청과 비교 기준 정하기",131,909,31,true)
 text("입력: 할 일 3개 · 저장 없음 · 초기화",187,869,27)
 arrow([NSPoint(x:450,y:855),NSPoint(x:450,y:812)],stage==1)
 box(110,716,570,90,0xFFF0C2,hold || stage==1)
 text("계정 자격과 비용 조건 살피기",126,767,29,true)
 text("Ultrafast 이용 대상과 사용량 확인",178,730,26)
 arrow([NSPoint(x:450,y:716),NSPoint(x:450,y:672)],stage==2)
 box(220,571,460,94,0xDDECF7,hold || stage==2)
 text("지원하며 비용을 감수할 만한가요?",229,623,26,true)
 text("속도 안내만으로 업그레이드하지 않기",229,585,24)
 text("아니요",707,676,23)
 arrow([NSPoint(x:680,y:620),NSPoint(x:874,y:620),NSPoint(x:874,y:770),NSPoint(x:815,y:770)],stage==3)
 text("현재 모드로",695,768,23)
 text("작은 요청부터",697,738,23)
 text("예",459,542,26,true)
 arrow([NSPoint(x:450,y:571),NSPoint(x:450,y:505)],stage==3)
 box(115,384,680,115,0xF8DFDF,hold || stage==3)
 text("AI에게 요청 → 필요하면 추가 지시",137,450,31,true)
 text("결과: 3개 · 저장 없음 · 체크 초기화",180,404,27)
 text("수정 필요",23,347,22)
 arrow([NSPoint(x:110,y:225),NSPoint(x:20,y:225),NSPoint(x:20,y:445),NSPoint(x:115,y:445)],stage==3)
 text("AI 수행 후",402,346,25,true)
 arrow([NSPoint(x:450,y:384),NSPoint(x:450,y:292)],stage==4)
 box(110,166,680,120,0xE7E2FA,hold || stage==4)
 text("독자 확인 → 대기·결과·비용 비교",132,232,31,true)
 text("미충족 → 구체적 수정 / 충족 → 모드 선택",133,188,25)
 text("빠른 생성 ≠ 원하는 결과 보장",216,99,29,true)
 text("가정 예시 · 결과는 직접 확인",155,44,25)
 NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState();let img=bitmap.cgImage!
 if [0,100,200,259].contains(f){try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("codex4-workflow-frame-\(f).png"))}
 CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]] as CFDictionary)
}
guard CGImageDestinationFinalize(dest) else {fatalError("finalize")}
print("260 frames;26 seconds;final5seconds hold")
