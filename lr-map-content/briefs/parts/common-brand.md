## Brand system for social graphics

Use the system of the original graphics (shown in the reference images), but make your own, better layouts.

Colors:
- Band / dark field: #344E73. Brand blue: #3E5F8F. Ink (darkest text): #14243B. Body text: #28364A. Muted text: #5A6B82.
- Paper (page background): #F3F6FA. Wash: #E7EDF5. Card: #FFFFFF. Lines: #C3CEDD.
- Gold accent: #E3C06B. Gold wash (soft highlight fill): #FBF4DF. Gold dark (text on light): #7A5818.
- Use sparingly: pen #A8325E, good #376346, red #984236.

Type (already loaded by the kit, use these exact family names):
- Headlines: Fraunces, weight 550, letter-spacing -0.02em, line-height 1.05 to 1.15.
- Body and lists: Inter, weights 400/500/600/700.
- Eyebrows, labels, slide numbers: 'IBM Plex Mono', weight 500, uppercase, letter-spacing 0.06em.

Logo: `<img class="logo" src="../kit/logo.svg" alt="Germaine Tutoring">` on light backgrounds, `../kit/logo-white.svg` on dark ones. Give `.logo` a height (34 to 48px) and `width:auto`. The build step turns it into inline SVG so it exports.

Layout rules:
- Safe margin of at least 56px inside every artboard. Nothing may touch, cross or clip at an edge.
- Minimum text sizes on a 1080px-wide artboard: body 28px, labels 22px. Scale up proportionally on wider artboards.
- One clear focal point per image. Strong hierarchy: eyebrow, headline, supporting content, footer.
- Never put an accent bar or rail on only one side of a box (no left borders, no top stripes on cards). A highlighted box is enclosed on all sides: a full border, a fill, or a shadow under the whole box.
- No gradients that reduce text contrast. Body text contrast at least 4.5:1.
