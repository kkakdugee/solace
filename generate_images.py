from PIL import Image, ImageDraw, ImageFont
import random, os

W, H = 1024, 768
OUT = r"C:\Users\aaron\Desktop\GitHub Repositories\figma"

def font(size, bold=False, mono=False):
    try:
        if mono: return ImageFont.truetype("C:/Windows/Fonts/consola.ttf", size)
        if bold: return ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", size)
        return ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", size)
    except:
        return ImageFont.load_default()

# ============================================================
# DESIGN A: MULTIMODAL — nature imagery, audio indicators
# ============================================================
img = Image.new("RGB", (W, H), "#F7F8FA")
d = ImageDraw.Draw(img)

# Sidebar
d.rectangle([0, 0, 64, H], fill="#FFFFFF")
d.line([64, 0, 64, H], fill="#E2E5EA")
for y, act in [(100,0),(150,0),(200,1),(250,0),(300,0)]:
    if act: d.rounded_rectangle([8, y-4, 56, y+36], radius=8, fill="#E8F0FE")
    c = "#0B3D91" if act else "#B0B5C3"
    d.ellipse([22, y+2, 42, y+22], outline=c, width=2)

d.text((84, 20), "MENTAL RESTORATION", font=font(10, mono=True), fill="#7A8198")
d.text((84, 38), "Restore", font=font(24, bold=True), fill="#1A1F2B")

# Breathing card (left)
d.rounded_rectangle([84, 80, 420, 410], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.text((200, 96), "Guided Breathing", font=font(14, bold=True), fill="#4A5066")
cx, cy = 252, 240
d.ellipse([cx-65, cy-65, cx+65, cy+65], outline="#0B3D91", width=2)
d.ellipse([cx-48, cy-48, cx+48, cy+48], outline="#4A90D9", width=1)
d.ellipse([cx-32, cy-32, cx+32, cy+32], fill="#E8F0FE")
d.text((cx-20, cy-8), "Inhale", font=font(14, bold=True), fill="#0B3D91")
d.rounded_rectangle([192, 335, 312, 370], radius=10, fill="#0B3D91")
d.text((202, 343), "Begin Session", font=font(12, bold=True), fill="#FFFFFF")
d.text((195, 382), "4-7-8 technique  |  5 min", font=font(10, mono=True), fill="#7A8198")

# Soundscape cards with nature visuals
d.text((440, 80), "Nature Soundscapes", font=font(14, bold=True), fill="#4A5066")

# Forest
d.rounded_rectangle([440, 108, 652, 245], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.rounded_rectangle([450, 118, 642, 178], radius=8, fill="#E8F5E9")
random.seed(10)
for tx in range(470, 630, 28):
    h2 = random.randint(12, 22)
    d.polygon([(tx, 178-h2), (tx-10, 178), (tx+10, 178)], fill="#4CAF50")
    d.polygon([(tx, 178-h2-8), (tx-7, 178-h2+5), (tx+7, 178-h2+5)], fill="#66BB6A")
d.text((450, 185), "Forest Rain", font=font(13, bold=True), fill="#1A1F2B")
d.text((450, 203), "Rainfall through canopy", font=font(10), fill="#7A8198")
d.ellipse([450, 222, 463, 235], fill="#E8F0FE")
d.polygon([(454, 225), (454, 233), (461, 229)], fill="#0B3D91")
d.text((468, 223), "10 min", font=font(10, mono=True), fill="#0B3D91")

# Ocean
d.rounded_rectangle([662, 108, 874, 245], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.rounded_rectangle([672, 118, 864, 178], radius=8, fill="#E3F2FD")
for wy in [138, 150, 162]:
    pts = [(672+x, wy + 4*((x//15)%2)) for x in range(0, 192, 4)]
    for j in range(len(pts)-1):
        d.line([pts[j], pts[j+1]], fill="#42A5F5", width=2)
d.text((672, 185), "Ocean Waves", font=font(13, bold=True), fill="#1A1F2B")
d.text((672, 203), "Rhythmic shoreline", font=font(10), fill="#7A8198")
d.ellipse([672, 222, 685, 235], fill="#E8F0FE")
d.polygon([(676, 225), (676, 233), (683, 229)], fill="#0B3D91")
d.text((690, 223), "15 min", font=font(10, mono=True), fill="#0B3D91")

# Mountain
d.rounded_rectangle([440, 258, 652, 395], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.rounded_rectangle([450, 268, 642, 328], radius=8, fill="#FFF3E0")
d.polygon([(500, 325), (545, 278), (590, 325)], fill="#FF9800")
d.polygon([(560, 325), (595, 285), (630, 325)], fill="#FFB74D")
d.polygon([(530, 290), (545, 278), (560, 290)], fill="#FFFFFF")
d.text((450, 335), "Mountain Dawn", font=font(13, bold=True), fill="#1A1F2B")
d.text((450, 353), "Bird song at sunrise", font=font(10), fill="#7A8198")
d.ellipse([450, 372, 463, 385], fill="#E8F0FE")
d.polygon([(454, 375), (454, 383), (461, 379)], fill="#0B3D91")
d.text((468, 373), "10 min", font=font(10, mono=True), fill="#0B3D91")

# Night
d.rounded_rectangle([662, 258, 874, 395], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.rounded_rectangle([672, 268, 864, 328], radius=8, fill="#EDE7F6")
random.seed(42)
for _ in range(20):
    sx, sy = random.randint(680, 855), random.randint(273, 322)
    r = random.choice([1, 1, 2])
    d.ellipse([sx-r, sy-r, sx+r, sy+r], fill="#7E57C2")
d.text((672, 335), "Night Garden", font=font(13, bold=True), fill="#1A1F2B")
d.text((672, 353), "Crickets and breeze", font=font(10), fill="#7A8198")
d.ellipse([672, 372, 685, 385], fill="#E8F0FE")
d.polygon([(676, 375), (676, 383), (683, 379)], fill="#0B3D91")
d.text((690, 373), "20 min", font=font(10, mono=True), fill="#0B3D91")

# Journal + Earth
d.rounded_rectangle([440, 410, 652, 462], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.rounded_rectangle([450, 420, 480, 452], radius=8, fill="#FFF3E0")
d.text((490, 421), "Journal", font=font(12, bold=True), fill="#1A1F2B")
d.text((490, 440), "Free-write or guided", font=font(10), fill="#7A8198")

d.rounded_rectangle([662, 410, 874, 462], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.rounded_rectangle([672, 420, 702, 452], radius=8, fill="#E8F0FE")
d.text((712, 421), "Earth View", font=font(12, bold=True), fill="#1A1F2B")
d.text((712, 440), "Live-rendered planet", font=font(10), fill="#7A8198")

# Label
d.rounded_rectangle([84, 720, 500, 752], radius=6, fill="#E8F0FE")
d.text((96, 728), "DESIGN A: Multimodal — Visual imagery + audio cues + minimal text", font=font(11, bold=True), fill="#0B3D91")

img.save(os.path.join(OUT, "design_a_multimodal.png"))
print("Saved design_a_multimodal.png")


# ============================================================
# DESIGN B: TEXT-HEAVY — same features, walls of text
# ============================================================
img = Image.new("RGB", (W, H), "#F7F8FA")
d = ImageDraw.Draw(img)

# Sidebar
d.rectangle([0, 0, 64, H], fill="#FFFFFF")
d.line([64, 0, 64, H], fill="#E2E5EA")
for y, act in [(100,0),(150,0),(200,1),(250,0),(300,0)]:
    if act: d.rounded_rectangle([8, y-4, 56, y+36], radius=8, fill="#E8F0FE")
    c = "#0B3D91" if act else "#B0B5C3"
    d.ellipse([22, y+2, 42, y+22], outline=c, width=2)

d.text((84, 20), "MENTAL RESTORATION", font=font(10, mono=True), fill="#7A8198")
d.text((84, 38), "Restore", font=font(24, bold=True), fill="#1A1F2B")

# Left: dense breathing text block
d.rounded_rectangle([84, 80, 490, 480], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.text((100, 96), "Guided Breathing Exercise", font=font(15, bold=True), fill="#1A1F2B")
lines = [
    "The 4-7-8 breathing technique is a relaxation method",
    "developed by Dr. Andrew Weil based on pranayama, an",
    "ancient yogic practice. It involves controlled breathing",
    "in a specific pattern: inhale for 4 seconds, hold your",
    "breath for 7 seconds, and exhale slowly for 8 seconds.",
    "This pattern activates the parasympathetic nervous",
    "system, lowering heart rate and blood pressure.",
    "",
    "Instructions:",
    "1. Place the tip of your tongue against the ridge of",
    "   tissue behind your upper front teeth.",
    "2. Exhale completely through your mouth, making a",
    "   whoosh sound.",
    "3. Close your mouth and inhale quietly through your",
    "   nose to a mental count of four.",
    "4. Hold your breath for a count of seven.",
    "5. Exhale completely through your mouth, making a",
    "   whoosh sound, to a count of eight.",
    "6. This is one breath. Now inhale again and repeat",
    "   the cycle three more times for a total of four.",
    "",
    "Recommended session length: 5 minutes (approx. 8 cycles)",
    "Recommended frequency: twice daily, morning and evening",
    "Contraindications: none reported for healthy adults",
]
y = 120
for line in lines:
    if line.startswith("Instructions") or line.startswith("Recommended") or line.startswith("Contra"):
        d.text((100, y), line, font=font(11, bold=True), fill="#1A1F2B")
    elif line == "":
        pass
    else:
        d.text((100, y), line, font=font(11), fill="#4A5066")
    y += 16

d.rounded_rectangle([100, y+5, 230, y+32], radius=8, fill="#0B3D91")
d.text((120, y+10), "Start Timer", font=font(11, bold=True), fill="#FFFFFF")

# Right: text-only activity list
d.rounded_rectangle([510, 80, 930, 480], radius=12, fill="#FFFFFF", outline="#E2E5EA")
d.text((526, 96), "Available Restoration Activities", font=font(15, bold=True), fill="#1A1F2B")

activities = [
    ("Forest Rain Soundscape", "10 min | Nature audio",
     "Ambient recording of rainfall filtered through dense\nforest canopy. Recorded in Olympic National Park,\nWashington. Best during work breaks or pre-sleep."),
    ("Ocean Waves Soundscape", "15 min | Nature audio",
     "Rhythmic shoreline recording from Big Sur coastline.\nConsistent wave patterns with minimal variation.\nRecommended for extended relaxation sessions."),
    ("Mountain Dawn Soundscape", "10 min | Nature audio",
     "Bird song recordings captured at sunrise in Rocky\nMountain National Park. Contains varied species calls.\nGood for morning restoration and alertness."),
    ("Night Garden Soundscape", "20 min | Nature audio",
     "Cricket and ambient nighttime recordings from\nShenandoah Valley. Includes gentle wind rustling.\nIdeal for pre-sleep and circadian alignment."),
    ("Journaling Module", "Variable | Reflective writing",
     "Free-write or guided prompt-based journaling.\nPrompts rotate daily. Entries stored locally."),
    ("Earth View Simulation", "Variable | Visual",
     "Live-rendered view of Earth from current spacecraft\nposition. Updated based on mission trajectory."),
]

y = 122
for title, meta, desc in activities:
    d.line([526, y, 914, y], fill="#E2E5EA")
    y += 6
    d.text((526, y), title, font=font(11, bold=True), fill="#1A1F2B")
    y += 17
    d.text((526, y), meta, font=font(9, mono=True), fill="#7A8198")
    y += 14
    for dl in desc.split("\n"):
        d.text((526, y), dl, font=font(10), fill="#4A5066")
        y += 14
    y += 4

# Label
d.rounded_rectangle([84, 720, 500, 752], radius=6, fill="#FFF3E0")
d.text((96, 728), "DESIGN B: Text-heavy — Dense descriptions, no visual imagery", font=font(11, bold=True), fill="#C67A1A")

img.save(os.path.join(OUT, "design_b_textheavy.png"))
print("Saved design_b_textheavy.png")
