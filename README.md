# Solace
Won the Figma Challenge at Build4Good 2026. Mental wellness for astronauts, designed by how the brain actually works. 

> https://devpost.com/software/solace-4lrmw3

## Inspiration

Astronauts on deep space missions face some of the most psychologically demanding conditions any human has ever experienced. They're isolated in a tiny spacecraft for years, millions of miles from home, with no nature, no privacy, and 16 sunrises a day throwing off their sleep. Current mental health tools for astronauts rely on clinical questionnaires that feel like medical paperwork. We wanted to build something that feels more like a personal wellness companion. Something that brings the calming, restorative power of nature into a spacecraft, backed by actual neuroscience. This is where Solace comes in.

## Overview

Solace is a tablet app that supports astronauts throughout their entire day:

- **Morning check-in**: A quick, visual mood check using emoji-style selectors instead of clinical scales. Tracks mood, stress, and energy in under 30 seconds and updates a personal wellness score.
- **Restore Hub**: Immersive nature soundscapes (ocean, rain, forest, night sounds) and a guided 4-7-8 breathing exercise with an animated breathing ring. Designed to activate restorative brain networks.
- **Sleep Center**: Light therapy scheduling, sleep quality tracking, and a 24-hour circadian rhythm timeline to help astronauts manage the extreme sleep disruption of orbital environments.
- **Smart nudges**: When the wellness score dips, Solace gently suggests a restoration activity instead of waiting for the astronaut to seek help.

The app uses a dark navigation with a light content area, NASA blue accents, IBM Plex typography, and 48px minimum touch targets for glove-friendly operation.

## How we built it

1. **Research**: Studied NASA's identified psychological risks for long-duration missions and selected three focus areas.
2. **Neuroscience mapping**: Used Meta FAIR's TRIBE v2 brain encoder ([paper](https://ai.meta.com/research/publications/a-foundation-model-of-vision-audition-and-language-for-in-silico-neuroscience/)) to predict how different design stimuli activate the brain. TRIBE v2 takes in video, audio, or text and outputs predicted fMRI activation across the entire cortex. We fed it different design variations (nature imagery vs. clinical layouts, warm palettes vs. harsh ones, soundscapes vs. silence) and compared the predicted brain responses. From those comparisons, we derived six design principles.
3. **User flow**: Mapped an astronaut's full daily journey in FigJam to identify every touchpoint where Solace fits in.
4. **Design system**: Built a complete design system in Figma Design with color tokens, typography scales, spacing, components, and accessibility notes, all purpose-built for the space context.
5. **Prototype**: Developed a fully functional HTML/CSS/JS prototype with 5 navigable screens, immersive soundscape overlays with ambient audio, an animated breathing exercise, and URL-parameter-driven state management for easy screen capture.
6. **Validation**: Built a "bad" version of the prototype that uses clinical anti-patterns (harsh white background, alarm-red accents, dense text, no nature imagery) and ran both versions through TRIBE v2 in Google Colab. Compared the predicted brain activation maps side by side to measure how differently the brain responds to each design.

## Challenges

- **Bringing nature into a spacecraft**: The hardest design challenge was figuring out how to recreate the restorative feeling of nature in an interface. We landed on immersive full-screen soundscape overlays that combine ambient audio with nature imagery.
- **Balancing science and usability**: We had deep neuroscience research backing our decisions, but the app still needed to feel simple and intuitive. Finding that balance took several iterations.
- **TRIBE v2 caching issues**: When running brain encoder predictions in Colab, stale video encoder caches caused all predictions to return identical results. Took significant debugging to identify that the cache key didn't include file content.
- **Circadian design for space**: Designing a sleep tracker for an environment with 16 sunrises per day required rethinking assumptions about how humans relate to time and light.

## Accomplishments

- Every design token in the system traces back to neuroscience research. Nothing was chosen because it "looks calming."
- The prototype is fully functional with real audio playback, animated breathing exercises, and immersive overlays.
- We validated our design decisions using an actual brain encoder, showing measurable differences in predicted cortical activation between our neuroscience-informed design and a clinical anti-pattern version.
- The design system is genuinely purpose-built for space: low-light legibility, glove-friendly touch targets, and minimal cognitive load.

## Takeaways

- Neuroscience research can be a practical design tool. Mapping brain networks to design principles gave us a framework for making decisions that would otherwise be subjective.
- The difference between "looks calming" and "is calming at a neurological level" is real and measurable.
- Designing for extreme environments forces you to question every assumption. Why is this font size right? Why is this touch target big enough? Why does this animation exist? That discipline makes the design better even for normal contexts.
- Clinical tools and personal wellness tools solve the same problem but feel completely different. The framing matters as much as the functionality.

## What's Next?

- **More restoration activities**: Expanding the Restore Hub with reflective journaling and an Earth view simulation for visual connection to home.
- **Adaptive recommendations**: Using wellness score trends over time to proactively suggest activities before stress compounds.
- **Mission control dashboard**: A crew-level view that lets ground teams monitor behavioral health trends without compromising individual privacy.
- **Real brain validation**: Moving from predicted cortical activation to actual EEG/fNIRS studies with the prototype.

## Figma Links

- **Research & Problem Framing (FigJam):** https://www.figma.com/board/RnUu9NLglw8Zts62jvMERb/Research---Problem-Framing-%E2%80%94-Solace-App?t=LizHa06X6CnUFgdZ-1

- **User Flow (FigJam):** https://www.figma.com/board/RVUiawY80TxptQzLv3PAMs/Astronaut-Daily-Journey-%E2%80%94-Solace-App-User-Flow?t=LizHa06X6CnUFgdZ-1

- **TRIBE v2 Neuroscience Mapping (FigJam):** https://www.figma.com/board/NAnVQkYIe5ZfHAEGVxeEXh/TRIBE-v2-Neuroscience-to-Design-System-Mapping-%E2%80%94-Solace-App?t=LizHa06X6CnUFgdZ-1

- **Design System Starter (Figma Design):** https://www.figma.com/design/dQ8yy4v20s0VXq4lDonrip/Solace-%E2%80%94-Design-System-Starter?m=auto&t=LizHa06X6CnUFgdZ-1

- **Prototype for Tablet (Figma Design):** https://www.figma.com/design/mOBG6BBiAefTpxVN6ZJA2g/Solace-%E2%80%94-Tablet-Prototype?m=auto&t=LizHa06X6CnUFgdZ-1 

- **Prototype for Mobile (Figma Design):** https://www.figma.com/design/9yq9bwYSbJljnkGtpnjw96/Solace-%E2%80%94-Mobile-Prototype?m=auto&t=LizHa06X6CnUFgdZ-1

## GitHub & Colab Notebook

- **Source Code (GitHub):** https://github.com/kkakdugee/figma

- **TRIBE v2 Notebook (Colab):** https://colab.research.google.com/drive/1lORIiWLmeV7MZgWfMRcmwHdqyKpkIPx_?usp=sharing
