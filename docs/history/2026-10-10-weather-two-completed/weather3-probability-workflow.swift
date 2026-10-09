import AppKit
import ImageIO
import UniformTypeIdentifiers

let output = URL(fileURLWithPath: CommandLine.arguments[1])
let width = 900, height = 1000, frames = 180
func color(_ v: UInt32) -> NSColor { NSColor(srgbRed: CGFloat((v >> 16) & 255)/255, green: CGFloat((v >> 8) & 255)/255, blue: CGFloat(v & 255)/255, alpha: 1) }
let ink = color(0x24324A), accent = color(0x2875E8)
func text(_ s: String, _ x: CGFloat, _ y: CGFloat, _ size: CGFloat, _ bold: Bool = false) {
 NSAttributedString(string:s,attributes:[.font:NSFont.systemFont(ofSize:size,weight:bold ? .semibold : .regular),.foregroundColor:ink]).draw(at:NSPoint(x:x,y:y))
}
func line(_ points: [NSPoint], _ active: Bool = false) {
 let p=NSBezierPath(); p.move(to:points[0]); for (i,b) in points.dropFirst().enumerated() { let a=points[i]; let m=NSPoint(x:(a.x+b.x)/2+1.3,y:(a.y+b.y)/2-1); p.curve(to:b,controlPoint1:m,controlPoint2:m) }; p.lineWidth=active ? 5 : 2.5; p.lineCapStyle = .round; (active ? accent : ink).setStroke(); p.stroke()
}
func arrow(_ ps: [NSPoint]) {
 line(ps); let b=ps.last!,a=ps[ps.count-2],angle=atan2(b.y-a.y,b.x-a.x)
 for d: CGFloat in [-0.5,0.5] { line([b,NSPoint(x:b.x-12*cos(angle+d),y:b.y-12*sin(angle+d))]) }
}
func box(_ x: CGFloat,_ y: CGFloat,_ w: CGFloat,_ h: CGFloat,_ fill: UInt32,_ active: Bool) {
 color(fill).setFill(); NSBezierPath(roundedRect:CGRect(x:x,y:y,width:w,height:h),xRadius:18,yRadius:18).fill()
 line([NSPoint(x:x+16,y:y),NSPoint(x:x+w-16,y:y+1),NSPoint(x:x+w,y:y+16),NSPoint(x:x+w-1,y:y+h-16),NSPoint(x:x+w-16,y:y+h),NSPoint(x:x+16,y:y+h-1),NSPoint(x:x,y:y+h-16),NSPoint(x:x+1,y:y+16),NSPoint(x:x+16,y:y)],active)
}
func travel(_ path:[NSPoint],_ progress:CGFloat) {
 let p=min(0.999,max(0,progress))*CGFloat(path.count-1),n=Int(p),t=p-CGFloat(n),a=path[n],b=path[n+1]
 accent.setFill(); NSBezierPath(ovalIn:CGRect(x:a.x+(b.x-a.x)*t-9,y:a.y+(b.y-a.y)*t-9,width:18,height:18)).fill()
}
let path=[NSPoint(x:450,y:750),NSPoint(x:450,y:606),NSPoint(x:450,y:460),NSPoint(x:450,y:310)]
let noPath=[NSPoint(x:626,y:500),NSPoint(x:740,y:500),NSPoint(x:740,y:408),NSPoint(x:624,y:408)]
guard let dest=CGImageDestinationCreateWithURL(output as CFURL,UTType.gif.identifier as CFString,frames,nil) else { fatalError("GIF destination unavailable") }
CGImageDestinationSetProperties(dest,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFLoopCount as String:0]] as CFDictionary)
for frame in 0..<frames {
 let s=CGFloat(frame)/10,hold=s>=14,active=s<2 ? 0 : s<4 ? 1 : s<7 ? 2 : s<10 ? 3 : s<12 ? 4 : 2
 let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:width,pixelsHigh:height,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
 NSGraphicsContext.saveGraphicsState(); NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
 color(0xFFFDF5).setFill(); NSRect(x:0,y:0,width:width,height:height).fill()
 for i in 0..<110 { color(0xF2ECD9).setFill(); NSRect(x:(i*173)%900,y:(i*239)%1000,width:1,height:1).fill() }
 text("비 예보 숫자에서 준비까지",38,936,34,true)
 text("가능성 · 양 · 기간을 나눠 읽어요",38,898,23)
 let ys:[CGFloat]=[730,580,430,280],titles=["1. 목적지 · 이동 시간","2. %와 mm 구별","3. 지역 · 기간 맞추기","4. 준비 · 일정 직접 결정"],notes=["독자가 지역과 이동 시점 선택","가능성과 비의 양은 달라요","내 일정과 같은 범위인가요?","기존 우산 · 도보 구간 고려"],fills:[UInt32]=[0xDDECF7,0xFFF0C2,0xDDF1E7,0xE6E0F5]
 for i in 0..<4 {
  box(38,ys[i],590,108,fills[i],hold || active==i);text(titles[i],55,ys[i]+65,25,true);text(notes[i],55,ys[i]+26,22)
  if i<3 { arrow([NSPoint(x:334,y:ys[i]),NSPoint(x:334,y:ys[i+1]+110)]) }
 }
 box(660,475,210,118,0xF5DFE8,hold || active==4)
 text("범위 밖",680,548,25,true);text("최신 예보로",674,510,19)
 arrow([NSPoint(x:628,y:486),NSPoint(x:650,y:486),NSPoint(x:650,y:545),NSPoint(x:660,y:545)])
 arrow([NSPoint(x:765,y:593),NSPoint(x:765,y:634),NSPoint(x:630,y:634)]);text("돌아가 읽기",670,368,20)
 text("확률만으로 구매나 취소를 정하지 않아요",55,217,21,true)
 text("그림은 설명용 · 실제 예보나 안전 보장 아님",55,184,18)
 box(38,68,832,70,0xFFF0C2,false);text(hold ? "전체 흐름: 목적지 → 숫자 구별 → 기간 → 판단" : "기간이 다르면 내 시간에 맞는 예보로 돌아가요",58,91,25,true)
 if !hold {
  if s>=1 && s<2 { travel([path[0],path[1]],s-1) }
  if s>=3 && s<4 { travel([path[1],path[2]],s-3) }
  if s>=5 && s<7 { travel([path[2],path[3]],(s-5)/2) }
  if s>=8 && s<10 { travel([NSPoint(x:628,y:486),NSPoint(x:650,y:486),NSPoint(x:650,y:545),NSPoint(x:660,y:545)],(s-8)/2) }
  if s>=11 && s<13 { travel([path[2],path[3]],(s-11)/2) }
 }
 NSGraphicsContext.current?.flushGraphics();NSGraphicsContext.restoreGraphicsState()
 let img=bitmap.cgImage!
 if [0,25,55,85,110,140,179].contains(frame) { try NSBitmapImageRep(cgImage:img).representation(using:.png,properties:[:])!.write(to:output.deletingLastPathComponent().appendingPathComponent("weather3-workflow-frame-\(frame).png")) }
 CGImageDestinationAddImage(dest,img,[kCGImagePropertyGIFDictionary as String:[kCGImagePropertyGIFDelayTime as String:0.1]] as CFDictionary)
}
guard CGImageDestinationFinalize(dest) else { fatalError("GIF export failed") }
print("Saved 180-frame, 18-second weather decision flow; final 4 seconds hold the complete flow.")
