# Solace — Video Walkthrough Script

Target length: 3-5 minutes

---

## INTRO (30 seconds)

**[Screen: Title slide or Solace logo]**

"Hi, I'm Aaron Kim. This is Solace — an astronaut mental wellness companion designed for long-duration deep space missions.

Solace addresses three of NASA's key research areas: behavioral health monitoring, sleep and circadian support, and mindfulness and mental restoration.

One piece of research that shaped this project is Meta FAIR's TRIBE v2 — an open-source model that predicts how the human brain responds to visual, audio, and language stimuli. I used it to validate a specific design decision, which I'll walk through."

---

## SECTION 1: Research & Problem Framing (45 seconds)

**[Screen: FigJam brainstorm boards]**

"I started with research and problem framing in FigJam. This first diagram maps NASA's five problem areas to Solace's five screens — each screen directly addresses a documented challenge astronauts face.

The second diagram shows the astronaut's daily journey through the app, from morning check-in to evening wind-down.

The third diagram is about TRIBE v2. The paper demonstrates that multimodal stimuli — audio and visual together — activate significantly more brain area than either alone, with up to a 50% increase at the temporal-parietal-occipital junction. That finding directly informed the Restore Hub, where we pair nature soundscapes with nature visuals rather than offering them separately.

I also ran screenshots of different UI layouts through the TRIBE v2 Colab demo to compare predicted brain activation — those results are included on this board."

*[Note: Add your Colab experiment screenshots to the FigJam board before recording]*

---

## SECTION 2: Design System (45 seconds)

**[Screen: Design system file in Figma]**

"The design system was built for the space context. The primary color is NASA blue — clean, institutional, high-trust. Warm orange signals attention items like upcoming tasks and Earth messages. Green for positive status.

Typography is IBM Plex Sans with IBM Plex Mono for data readouts — it has that mission-control feel while staying readable.

Touch targets are minimum 48 pixels for glove-friendly operation. The tab bar is 72 pixels wide. All of this is stored as Figma variables — 19 color tokens, 23 spacing tokens, and 10 text styles."

---

## SECTION 3: Core User Flow — 5 Screens (90 seconds)

**[Screen: Prototype — walk through each screen]**

### Screen 1: Home Dashboard
"The dashboard gives astronauts an instant wellness snapshot — wellness score, mood, sleep quality, stress level, and crew status at a glance. Below, today's schedule and AI-powered suggestions like recommending a nature soundscape when stress patterns are elevated."

### Screen 2: Behavioral Check-In
"The daily check-in uses simple visual selectors — colored dots for mood, sliders for energy and stress. A 7-day trend chart shows patterns over time. Optional journaling. This data could, in a real implementation, feed into a system like TRIBE v2 to detect early signs of psychological stress — which is exactly what NASA is researching."

### Screen 3: Restore Hub
"This is the screen most directly informed by the TRIBE v2 research. Nature soundscapes pair audio with visual thumbnails — because the paper shows multimodal stimuli engage more of the brain than either modality alone. There's also guided breathing, journaling, and an Earth-view simulation."

### Screen 4: Sleep Center
"The sleep center shows a 24-hour circadian rhythm visualization comparing actual vs. target rhythms. There's a sleep quality score, light therapy schedule for managing the absence of natural day/night cycles, and weekly trend data breaking down REM, deep, and light sleep."

### Screen 5: Crew Hub
"The crew hub maintains social connection despite isolation. Crew status with mood indicators, async messaging with a clear 22-minute Earth-delay indicator, and a shared gratitude wall. Earth messages are visually distinct so astronauts immediately know the context."

---

## SECTION 4: Prototype Demo (30 seconds)

**[Screen: Live coded prototype in browser]**

"This is also a working coded prototype — HTML, Tailwind CSS, and JavaScript. Navigation between all five screens is fully functional. It's optimized for a 1024x768 tablet viewport, which is realistic for spacecraft-mounted hardware."

---

## CLOSING (15 seconds)

"Solace combines NASA research priorities with a specific neuroscience finding from TRIBE v2 to create a mental wellness tool grounded in evidence. The multimodal restoration approach isn't just a design choice — it's backed by brain imaging data from over 700 subjects.

Thank you for watching."

---

## Shareable Links (include in video description)

- **FigJam Research & Problem Framing:** https://www.figma.com/online-whiteboard/create-diagram/13246845-d2d5-4543-894c-1fa717d34389
- **FigJam User Journey:** https://www.figma.com/online-whiteboard/create-diagram/96b35f9f-f091-42e1-ad17-c0e216528383
- **FigJam TRIBE v2 Research:** https://www.figma.com/online-whiteboard/create-diagram/71fd0bbe-834e-4bd8-b145-44a23ebca355
- **Figma Design System:** https://www.figma.com/design/eWuoOe0kG6PeaQLIPvC9WY
- **Figma Prototype Screens:** https://www.figma.com/design/kRmvBmzSW1EVOBoBkeUwNr
- **Coded Prototype:** Run `python -m http.server 3000` from `prototype/` folder, open http://localhost:3000
- **TRIBE v2 Paper:** https://arxiv.org/abs/2507.22229
- **TRIBE v2 Demo:** https://aidemos.atmeta.com/tribev2/

## Recording Tips

- Use OBS Studio or Loom for screen recording
- Record at 1920x1080, export at 1080p
- Speak clearly and at a moderate pace
- Show FigJam boards first, then design system, then prototype demo
- Switch between Figma and the live coded prototype to show both
- Keep total length under 5 minutes
- BEFORE RECORDING: Run your Colab experiment and add screenshots to the FigJam board
