---
name: Caldera Pro
description: "Landing page for Caldera Pro, drawn as one stamped job sheet: cool form paper, printed blue rules and three stamp-pad inks."
colors:
  violet: "#4a25c9"
  violet-deep: "#3a1ba6"
  green: "#0b7a45"
  green-deep: "#086236"
  red: "#c91d38"
  paper: "#f1f4fb"
  paper-deep: "#e2e8f6"
  rule: "#6c88dd"
  form: "#2748b5"
  ink: "#1c1740"
  ink-soft: "#4a4672"
  on-ink: "#f4f6fc"
  tint-violet: "#ddd6ff"
  tint-green: "#d3f5e2"
  tint-red: "#ffe9ec"
  mount: "#ffffff"
  staple: "#565c7a"
typography:
  display:
    fontFamily: "League Gothic, sans-serif"
    fontSize: "clamp(3.3rem, 8.3vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "0.012em"
  headline:
    fontFamily: "League Gothic, sans-serif"
    fontSize: "clamp(2.7rem, 5.6vw, 4.6rem)"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "0.012em"
  numeral:
    fontFamily: "League Gothic, sans-serif"
    fontSize: "6rem"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.012em"
  stamp:
    fontFamily: "League Gothic, sans-serif"
    fontSize: "2.4rem"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "0.012em"
  stamp-sm:
    fontFamily: "League Gothic, sans-serif"
    fontSize: "1.32rem"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "0.05em"
  title:
    fontFamily: "Libre Franklin, sans-serif"
    fontSize: "1.3rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  statement:
    fontFamily: "Libre Franklin, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    letterSpacing: "-0.012em"
  lead:
    fontFamily: "Libre Franklin, sans-serif"
    fontSize: "1.22rem"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Libre Franklin, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  note:
    fontFamily: "Libre Franklin, sans-serif"
    fontSize: "0.92rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Libre Franklin, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.55
    letterSpacing: "0.09em"
rounded:
  sheet: "2px"
  rule: "3px"
  key: "4px"
  tab: "5px"
  button: "6px"
  stamp: "0.2em"
  round: "50%"
spacing:
  tight: "10px"
  field: "14px"
  stack: "18px"
  gutter-narrow: "18px"
  block: "26px"
  gutter: "28px"
  rule-inset: "30px"
  column: "44px"
  line: "46px"
  attach: "56px"
  sub: "104px"
  section: "112px"
  sheet-width: "1180px"
components:
  button-primary:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.button}"
    padding: "0.8em 1.3em"
  button-primary-hover:
    backgroundColor: "{colors.violet-deep}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.violet}"
    rounded: "{rounded.button}"
    padding: "0.8em 1.3em"
  button-line-hover:
    backgroundColor: "{colors.paper-deep}"
  button-green:
    backgroundColor: "{colors.green}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.button}"
    padding: "0.8em 1.3em"
  button-green-hover:
    backgroundColor: "{colors.green-deep}"
  button-small:
    padding: "0.5em 0.95em"
  button-on-flood:
    backgroundColor: "{colors.on-ink}"
    rounded: "{rounded.button}"
    padding: "0.8em 1.3em"
  button-on-flood-hover:
    backgroundColor: "{colors.mount}"
  stamp:
    textColor: "{colors.violet}"
    typography: "{typography.stamp}"
    rounded: "{rounded.stamp}"
    padding: "0.3em 0.55em 0.22em"
  stamp-small:
    textColor: "{colors.violet}"
    typography: "{typography.stamp-sm}"
    rounded: "{rounded.stamp}"
    padding: "0.2em 0.5em 0.12em"
  field-caption:
    textColor: "{colors.form}"
    typography: "{typography.label}"
  letterhead:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-soft}"
    height: "64px"
  tab:
    backgroundColor: "transparent"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.tab}"
    padding: "0.35em 0.8em"
  tab-selected:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.on-ink}"
  schedule-bar:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.rule}"
    height: "28px"
  stepper:
    backgroundColor: "transparent"
    textColor: "{colors.violet}"
    rounded: "{rounded.round}"
    size: "38px"
  stepper-hover:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.on-ink}"
  attachment:
    backgroundColor: "{colors.mount}"
    padding: "34px 10px 10px"
  slip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sheet}"
    padding: "30px 34px 34px"
  flood-violet:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.on-ink}"
  flood-green:
    backgroundColor: "{colors.green}"
    textColor: "{colors.on-ink}"
  flood-red:
    backgroundColor: "{colors.red}"
    textColor: "{colors.on-ink}"
  pin:
    backgroundColor: "{colors.red}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.round}"
    size: "32px"
  pin-hot:
    backgroundColor: "{colors.violet}"
---

# Design System: Caldera Pro

## Overview

**Creative North Star: "The Stamped Job Sheet"**

The page is one sheet of cool form paper, ruled in printed blue, and every fact on it that can change is a rubber-stamp impression: a finish date, a total, a status. Three stamp-pad inks carry fixed meanings, so the colour of a stamp already says what kind of fact it is. When the plan moves, the value is stamped again with a thump and the earlier impression stays underneath as a ghost. That one behaviour is the whole argument of the product, so it is also the whole motion system.

Everything else is printed matter and stays quiet. Structure is drawn with thin blue rules and small blue captions, the way a form is, and content sits on those rules in rows instead of in boxes. Headlines are condensed gothic capitals pressed with uneven ink; text is a Franklin grotesque. Three sections flood edge to edge in one of the inks and print in reverse. Captures of the app, in its own Glass skin, are separate sheets stapled on at a slight lean. They are the only place another visual language appears.

The product record rules out three looks, and the build honours them: a page like every SaaS page, a dark and techy page, and a plain corporate one. It also records that the owner dislikes grids of generic feature cards. The system is light only (`color-scheme: light`); there is no dark variant.

**Key Characteristics:**
- Light, cool paper with visible grain. One deeper paper tone, no dark mode.
- Structure is ruled lines (1.5px blue) and form rows, not filled boxes.
- Three pad inks with fixed meanings: violet for time and the plan, green for money and done, red for changes and attention.
- League Gothic capitals for anything stamped or measured; Libre Franklin for anything read.
- Stamps tilt, sink into the paper (multiply blend) and carry uneven ink. Printed matter stays square, clean and flat.
- Solid means committed. Dashed or hatched means pending.
- One signature motion, the thump. Positions slide; nothing else moves.
- Shadows only under separate objects: stapled captures, the work-order slip, buttons, pins.

**Where the build departs from its direction contract** (`.impeccable/surfaces/index-html.md`). The build is the record.
- The contract names a red REVISED stamp. The build's red revision stamp prints the change itself ("+3 days", "+$1,920").
- The contract has the three hero stamps overprinting the schedule lines. The build sets them in their own column beside the bars, over ruled lines that continue under them; at 640px and below they sit directly under the title.
- The contract ghosts "the old value". In the hero the ghost is always the starting impression (Nov 27, $28,100), not the previous step. In the change and status demos it is the previous impression.
- The contract sets the title full width. The title is capped at 6rem and, from 1240px, shares its block with the lead at bottom right. A four-field strip, not in the contract, sits above it.
- The contract says no cards. The build has one raised paper container, the work-order slip on the violet flood, besides the stapled attachments.
- The contract names three inks. A fourth, neutral stamp colour exists for one status: Open is stamped in Soft Indigo with a dashed frame.

## Colors

A cool blue-white sheet printed in form blue, written on in indigo-black, and stamped in violet, green and red.

### Primary
- **Pad Violet** (`violet`, #4a25c9): time and the plan. The default stamp ink (`--stamp-ink`), headlines on paper, schedule bars, primary buttons, selected tabs, slider track and thumb ring, avatar rings. Also the themed browser surfaces: focus ring, text selection, caret, scrollbar thumb. Floods the AI section.
- **Pressed Violet** (`violet-deep`, #3a1ba6): the primary button's hover fill and border. A literal in the CSS, not a custom property.

### Secondary
- **Pad Green** (`green`, #0b7a45): money and done. The Cost stamp, the Budget term, Received, Done, Approved and Full match stamps, the Price all button, check marks on finished steps and met requirements, bid bars inside the limit, the Complete token. Floods the pricing section.
- **Pressed Green** (`green-deep`, #086236): the green button's hover. A literal in the CSS.

### Tertiary
- **Pad Red** (`red`, #c91d38): changes and attention. The revision stamp, Needed, Tentative and Not a full match stamps (always with a dashed frame), the dashed outline on the schedule line being changed, tentative hatching, annotation pins at rest. Floods the closing band.

### Neutral
- **Cool Form Paper** (`paper`, #f1f4fb): the sheet. Page background under the paper grain, the sticky letterhead, the work-order slip, the slider thumb's fill. Also the `theme-color`.
- **Deep Paper** (`paper-deep`, #e2e8f6): the single tonal step. Line-button hover wash, empty bar tracks, scrollbar track, the base of the search shimmer.
- **Printed Rule Blue** (`rule`, #6c88dd): every rule and box stroke on paper, and the week ticks at 50% alpha. A line colour only (3.07:1 on paper), never text.
- **Form Blue** (`form`, #2748b5): field captions, table headings, axis dates, tool-name boxes, notes inside the slip, the arrows between status stamps.
- **Indigo Black** (`ink`, #1c1740): body text and strong text, gate markers, the limit line. Every shadow on paper is a tint of it.
- **Soft Indigo** (`ink-soft`, #4a4672): leads, notes, nav links, descriptions, secondary figures. The Open stamp and the New token.
- **Reverse White** (`on-ink`, #f4f6fc): text, rules and stamps on a flood, and text on any violet, green or red fill.
- **Flood Tints** (`tint-violet` #ddd6ff, `tint-green` #d3f5e2, `tint-red` #ffe9ec): secondary text on the matching flood. Each is tinted from its flood's hue; none is gray.
- **Mount White** (`mount`, #ffffff): the attachment mount, the ring around a pin, the flood button's hover.
- **Staple Gray** (`staple`, #565c7a): the drawn staple and nothing else.

Measured on the flat hex values (WCAG 2 ratio): on paper, Indigo Black 15.3, Soft Indigo 7.9, Form Blue 7.1, Pad Violet 8.0, Pad Green 4.9, Pad Red 5.1. Reverse White on violet 8.1, on green 5.0, on red 5.2. Tints on their floods 6.3, 4.6 and 4.9. The ink filters thin stamped lettering in patches, to a floor of 82% (88% on the fine filter). Computed at that floor on paper, the thinnest patch of Pad Violet is about 5.5, Pad Red 4.1 and Pad Green 3.6 (4.0 on the fine filter).

### Named Rules
**The Three Pads Rule.** Ink is chosen by what the fact is, never for variety: violet for time and the plan, green for money and done, red for changes and attention. A stamp that changes meaning changes ink, as Tentative in red becomes Approved in green.

**The Printed Blue Rule.** Blue belongs to the form, not to the content. It draws rules and sets captions; it never fills a shape and never inks a stamp.

**The Reverse Print Rule.** On a flood everything prints in Reverse White: headline, stamps, focus ring, and rules at 50% alpha. Secondary text takes that flood's tint. Buttons invert to a Reverse White fill with the flood's ink as their text. A paper slip laid on a flood resets to the paper palette inside its own edges.

## Typography

**Display Font:** League Gothic (with `sans-serif`). Self-hosted, weight 400 only, preloaded.
**Body Font:** Libre Franklin (with `sans-serif`). Self-hosted variable font, 100 to 900; the build uses 400, 500, 600, 700 and 800.
**Label/Mono Font:** none distinct. Captions are Libre Franklin, and there is no monospace face: tool names and the sample list are set in Libre Franklin.

**Character:** A tall condensed gothic that reads as cut rubber type, against a plain workmanlike grotesque. The gothic shouts single facts; the grotesque explains them.

### Hierarchy
- **Display** (400, clamp(3.3rem, 8.3vw, 6rem), 0.96): the page title and the closing line. Capitals, +0.012em, `text-wrap: balance`. Carries the ink filter.
- **Headline** (400, clamp(2.7rem, 5.6vw, 4.6rem), 0.96): section headlines, capitals, max-width 15em, inked.
- **Numeral** (400, 6rem, 0.9; 5rem at 640px and below): prices. The unit beside the figure drops to Libre Franklin 600 at 1.05rem.
- **Stamp** (400, 2.4rem by default, 0.96): framed impressions. Sized by context: 3.2rem for the three hero stamps (2.5rem narrow), 2.3rem for the access level, 2.1rem in the status track and on the yearly plan, 1.95rem for the three-line crew stamp, 1.9rem for a result, 1.7rem beside a demo title. A label line inside a stamp is 0.42em with +0.08em tracking.
- **Small stamp** (400, 1.32rem, +0.05em): status in table rows and against listings; 1.08rem in the table at 640px and below. The revision stamp is 1.05rem, 1.25rem in the hero.
- **Other League Gothic settings:** term names in form rows 2rem at +0.02em; the access heading 2.6rem; live outputs beside a control 1.9rem; bar labels 1.12 to 1.15rem at +0.04 to +0.05em; amounts on bid bars 1.55rem; initials and gate codes 1 to 1.05rem; pin numerals 1.3rem.
- **Title** (700, 1.3rem, 1.25, -0.01em): Libre Franklin sub-headings. Plan names are 1.15rem.
- **Statement** (600 to 700, 1.5rem, 1.2 to 1.3, -0.012em): one line of content shown large: the typed request (600), the hunted item, a demo's title (both 700).
- **Lead** (400, 1.22rem, 1.5; 1.1rem narrow): the paragraph under a headline, Soft Indigo, max 58ch.
- **Body** (400, 1.0625rem, 1.55; 1rem narrow): paragraphs, max 68ch. Field values and list emphasis are 600; names, labels on controls and summaries are 700; the brand name is 800.
- **Note** (400, 0.92rem): sample-data disclosures and hints, Soft Indigo. An aside under a demo is 1.08rem.
- **Label** (700, 0.75rem, +0.09em, uppercase): the field caption, Form Blue on paper and the flood's tint on a flood.

### Named Rules
**The Two Faces Rule.** League Gothic sets what is stamped or measured: headlines, stamps, prices, live outputs, bar labels, initials, pin numbers. Libre Franklin sets everything that is read. League Gothic appears only as capitals and figures, at weight 400, down to 1rem on desktop and about 0.9rem at the smallest on narrow screens.

**The Caption Rule.** The small blue caption names a field, a column, an axis or a control, and sits on the thing it names. No headline in the build has one above it.

**The Tabular Figures Rule.** Anything that is re-stamped or lines up in a column asks for `tabular-nums`: stamps, live outputs, bar labels, the price table, bid amounts.

## Layout

The page is a single sheet 1180px wide (`sheet-width`) with 28px gutters, 18px at 640px and below. The letterhead is sticky at 64px with a rule under it, and anchors land 84px below the top.

**Rhythm.** Sections take 112px above and below (88px at 1020px and below, 68px at 640px and below). A paper section that follows another paper section drops its top padding, so the gap between them is a single 112px; a flood keeps both. Parts inside a section sit 104px apart (80px). A section opens with its headline, 18px, its lead, then 44px to the content. A ruled block starts with a 1.5px rule and 30px of space. Blocks under a rule sit 26px apart. An attachment sits 56px below what it illustrates.

**Ruled lines.** Rows are the grid. Schedule rows are 46px tall on a 46px ruled pitch under a 30px axis, and the ruling continues across the column beside them so stamps land on lines. Form rows, key rows, table rows and questions all divide with a 1.5px rule above each row and one below the last.

**Columns.** Demos pair a narrow side with a wide side in unequal tracks: 1.35fr to 1fr in the hero (44px gap), 0.8fr, auto, 1.7fr for the price run, 0.75fr to 1.75fr for the comparison, 1.25fr to 1fr for changes and status, 1.85fr to 1fr for the annotated capture, 1fr to 1.2fr for the access rack. Columns divide with a rule, not a gutter of colour. Text holds its measure inside a wide column instead of stretching.

**Responsive.** From 1240px the lead tucks into the bottom right of the title block. At 1020px and below every paired grid becomes one column, the nav links hide and the download button stays, the field strip folds to two by two, and the routing diagram wraps. At 640px and below the hero reorders (`display: contents` with `order`) so the stamps come straight after the title, then the lead, the buttons, the control and the schedule; the primary button goes full width, the line button becomes an underlined link, and a one-line note of the trial terms appears under them because the field strip has moved below the schedule; schedule rows stack with the value in text and an 18px unlabelled bar; the price table drops its quantity column; the status track goes two by two; pricing plans stack.

## Elevation & Depth

The sheet is flat. There is one deeper paper tone and no layered surfaces; depth is used only to say that something is a separate object lying on the sheet. Stamps do the opposite of lifting: they blend into the paper with `mix-blend-mode: multiply`, so the rules show through them (normal blend on a flood, multiply again inside a paper slip). Two SVG noise textures give the surfaces tooth: a faint indigo grain on paper and a black grain at 50% over each flood.

### Shadow Vocabulary
- **Button at rest** (`box-shadow: 0 9px 18px -10px rgba(28, 23, 64, .75)`): under filled buttons. Line buttons have none.
- **Button pressed** (`box-shadow: 0 2px 5px -3px rgba(28, 23, 64, .8)`): with the button moved down 3px.
- **Stapled sheet** (`box-shadow: 0 1px 2px rgba(28, 23, 64, .25), 0 22px 44px -22px rgba(28, 23, 64, .55)`): under an attachment's white mount.
- **Slip on a flood** (`box-shadow: 0 2px 3px rgba(12, 6, 60, .3), 0 26px 50px -24px rgba(12, 6, 60, .8)`): under the work-order slip, tinted deeper to hold against violet.
- **Pin** (`box-shadow: 0 0 0 3px #fff, 0 6px 14px rgba(28, 23, 64, .5)`): a white ring to part the pin from the capture, plus a soft drop. Ring only, 2px, at 640px and below.

### Named Rules
**The Separate Sheet Rule.** A shadow means the thing could be picked up: a stapled capture, the work-order slip, a button, a pin. Anything printed or stamped on the sheet has none.

**The Ink Shadow Rule.** Shadows on paper are tints of Indigo Black, offset downward, soft, and pulled in with a negative spread so they sit under the object instead of around it.

## Shapes

Corners are nearly square and get rounder only as things get more hand-sized: 2px on the slip, 3px on ruled boxes, bars and tokens, 4px on keycaps and tool-name boxes, 5px on tabs, 6px on buttons. Floods, attachment mounts and bid bars are square. Circles are kept for things you press or point with: stepper buttons (38px), the slider thumb (24px), avatar rings (30px), annotation pins (32px).

**Line weights.** 1.5px for every printed rule. 2px for heavier divisions (the pricing table, the access rack, the routing diagram) and for every control stroke: button borders, steppers, avatar rings, small stamp frames, dashes. A 4px double rule above a total.

**The stamp frame.** A large stamp has a double frame that scales with its type: a 0.085em border, then a 0.035em outline 0.07em outside it, at 0.2em radius. Small stamps have a single 2px frame. The seal is the round form: three concentric rings with lettering on an arc.

**Tilt.** Stamps are placed by hand. The default is -2deg (`--tilt`), and the build ranges from -5deg to +7deg, with neighbours leaning different ways. Ghosts sit at +3.5deg, the seal at -7deg. Attachments lean 0.5deg one way or the other, and 0 where pins must register on the capture.

**Marks.** Hatching is 45-degree stripes, 7px on and 7px off. A decision gate is a 32px ink diamond on a dashed line. Icons are five authored line drawings (download, checked box, arrow, minus, plus) on a 24 grid with a 2.2 stroke and round caps, sized 1.15em in the current colour.

### Named Rules
**The Pending Is Dashed Rule.** A dashed frame, a dashed outline or hatching means not settled yet: Needed, Open, Tentative, Not a full match, the schedule line being changed, a gate, a limit, the list before it is priced. Solid means committed. Approving a tentative bar redraws it solid and green.

## Components

### Buttons
Plain, solid and pressable. The only printed-looking thing that casts a shadow.
- **Shape:** gently squared (6px radius) with a 2px border in the fill's own colour. Libre Franklin 700 at 1.02rem, padding 0.8em by 1.3em, 0.55em between a leading icon and the label.
- **Primary:** Pad Violet fill, Reverse White text, the rest shadow.
- **Hover / Focus:** hover darkens fill and border to Pressed Violet (0.12s). Active drops the button 3px and tightens the shadow (0.1s). Focus is a 3px violet outline at 3px offset, Reverse White on a flood. Disabled is 55% opacity.
- **Line:** transparent, violet border and text, no shadow; hover washes Deep Paper.
- **Green:** Pad Green fill, Pressed Green on hover. Used once, for the action that fetches prices.
- **Small:** padding 0.5em by 0.95em at 0.93rem, for the letterhead and demo controls.
- **On a flood:** Reverse White fill with the flood's ink as text, pure white on hover. The line variant is a Reverse White border and text with a 14% white wash on hover.
- **Narrow screens:** in the call-to-action row the primary goes full width, the line button reduces to an underlined link, and a note in Soft Indigo states the trial terms beneath.

### Stamps
The signature component. A stamp is a fact that can change.
- **Frame and type:** League Gothic capitals, double frame, 0.3em 0.55em 0.22em padding, centred, never wrapping, tabular figures. An optional label line above the value (0.42em) and a second line below it.
- **Ink:** `--stamp-ink`, violet unless the element or its parent sets green or red; Reverse White on a flood.
- **Impression:** three SVG filters do the inking. Each roughens the edge with a small displacement (scale 1.5 for `ink`, 1.7 for `ink-2`, 1.1 for `ink-fine`) and varies the pressure with slow noise passed through a floored table, so the ink thins in soft patches but never below about 82%, 83% and 88% of full. There are no holes in the ink. Multiply blend then sinks it into the paper. `ink-2` is a second pattern for alternate headlines and stamps, so neighbours never share a blot.
- **Small stamp:** 1.32rem, single 2px frame, no outline, -1.5deg, the `ink-fine` filter. In a table it takes a 4.6em minimum width so the column aligns.
- **Status inks:** Needed in red with a dashed frame; Priced, Ordered and In progress in violet; Received, Done, Approved and Full match in green; Open in Soft Indigo, dashed; Tentative and Not a full match in red, dashed.
- **Ghost:** the earlier impression under a re-stamped one, at 17% opacity, tilted 3.5deg and shifted 7px right and 5px down.
- **Revision stamp:** a small red stamp at +7deg pinned to the top right corner, printing the change itself ("+3 days", "+$1,920"). Single 2px frame, always on `ink-fine`. Hidden while the value is at its starting point.
- **Narrow screens:** the hero stamps switch to `ink-fine`, the finer pattern for smaller type.

### Inked Headlines
The same lettering pressed straight onto the sheet with no frame and no tilt. Colour follows `--stamp-ink` (violet by default; one green and one red headline name their section's subject). Even-numbered sections use `ink-2`.

### Field Captions and Form Rows
How the page presents short facts without cards.
- **Field strip:** a 1.5px ruled box (3px radius) of four cells divided by rules, each a caption over a 600-weight value, padding 8px 14px 9px. Two by two at 1020px and below.
- **Term rows:** a 190px term column and a description, 20px apart, 18px above and below, a rule above each row and under the last. The term is League Gothic at 2rem in the row's ink. The plain variant sets the term in Libre Franklin 700 at 1.1rem in a 310px column. Rows stack at 640px and below.
- **Tool names and keys:** Libre Franklin 600 to 700 at 0.82em inside a 1.5px box with 4px corners; Form Blue for tool names, current colour for keycaps.
- **Sample list:** Libre Franklin 500 at 0.97rem with 1.9 line height in a dashed 1.5px box: the list before it is priced.

### Floods
A section printed in reverse. One ink edge to edge with the black grain over it, Reverse White text, tinted secondary text and captions, rules at 50% Reverse White. Selection and focus invert with it. The build floods three sections, one in each ink, and never two in a row.

### Attachments
App captures as stapled sheets.
- **Mount:** Mount White, square corners, 34px 10px 10px padding (22px 5px 5px narrow), leaning 0.5deg, with the stapled-sheet shadow.
- **Staple:** a drawn diagonal stroke, 30 by 18px, in Staple Gray at the top left.
- **Behaviour:** the mount is a link that opens the capture full size in a new tab. A caption in Soft Indigo (the tint on a flood) at 0.95rem sits 16px below.

### Work-Order Slip
The one raised container: a sheet of the same paper laid on the violet flood, holding the agent demo.
- **Corner Style:** 2px.
- **Background:** Cool Form Paper with Indigo Black text; it restores the paper's rule colour and violet stamp ink inside.
- **Shadow Strategy:** the slip shadow from Elevation.
- **Border:** none. A rule under its header row.
- **Internal Padding:** 30px 34px 34px (22px 18px 26px narrow).
- **Contents:** a captioned request in statement type with a blinking 2px violet caret and a rule beneath; a list of finished steps with green check boxes; a green result stamp at -5deg.

### Inputs
The build has a range slider and steppers, and no text fields.
- **Slider:** a 4px violet line with a 24px thumb, Cool Form Paper inside a 4px violet ring; the thumb fills violet on hover. 210px wide, full width narrow.
- **Steppers:** 38px circles with a 2px violet ring, filling violet with a Reverse White icon on hover.
- **Live output:** League Gothic at 1.9rem in violet beside the control, with a minimum width so the row does not shift as the figure changes.
- **Focus:** the global 3px violet outline. No error or disabled field styles exist.

### Tabs and Segmented Choice
- **Tabs:** Libre Franklin 700 in Soft Indigo, padding 0.35em 0.8em, 5px corners, 2px transparent border. Hover turns the text violet and shows a rule-blue border. Selected is a violet fill with Reverse White text.
- **Segmented choice (on a flood):** four equal buttons 8px apart, 2px Reverse White border, 6px corners; hover is a 14% white wash; the pressed one fills Reverse White with violet text. Choosing one presses a stamp with that label beside it.

### Price Table
A ruled table with no fills and no striping. Captions as headings, a rule above every 53px row, figures right-aligned and tabular, a 4px double rule and bold total in the foot, a small stamp in the status column. A missing value is italic Soft Indigo. While a row is searching its values are replaced by a shimmer bar and its stamp is held back, then stamped in.

### Schedule Lines, Bars and Tokens
- **Row:** a 196px name column (avatar ring with League Gothic initials, then a 700-weight label) and a 28px track with week ticks, 46px tall, rule above.
- **Bar:** Pad Violet with a Reverse White League Gothic label ("8d · $7.0k"), 3px corners. Bars slide to a new position and width.
- **Line being changed:** a 2px dashed red outline 3px outside the bar.
- **Tentative bar:** 2px dashed red border, red hatch at 16%, red label. Approved, it becomes a solid green bar with Reverse White text.
- **Gate:** a 2px dashed ink line with a 32px ink diamond holding its code.
- **Board token:** a 700-weight label on a violet tab (Soft Indigo in New, green in Complete) that slides between three ruled columns.
- **Bid bar:** a 34px Deep Paper track filled green to the price, the amount in white League Gothic on the bar; a near miss is red hatch. A 2px dashed ink line marks the limit.

### Navigation
- **Letterhead:** sticky, 64px, paper with grain, 1.5px rule beneath. The mark at 40px beside the name in Libre Franklin 800 at 1.1rem. Links are 600 at 0.95rem in Soft Indigo, 26px apart; hover turns them violet and underlined. A small primary button closes the row. No active-section state.
- **Narrow:** at 1020px and below the links hide and the mark and button remain. There is no menu.
- **Footer:** a rule above, 0.95rem Soft Indigo, links underlined in the inherited colour (0.18em offset, 0.08em thick).

### Questions
A ruled list of disclosures, 860px at most. Summary in Libre Franklin 700 at 1.15rem, violet on hover. The marker is a plus drawn from two 18 by 2.5px violet bars; the upright bar turns flat when open (0.2s). Answers are Soft Indigo with violet 600 links.

### Pins and Key
Numbered 32px red circles on the capture, each with a white ring, matched to a ruled key beside it. Hovering or focusing either a pin or its key row turns both violet and scales them to 1.2 (0.18s). Pins are 24px at 640px and below.

### The Thump
The signature motion, and almost the only one.
- **Impact:** `thump`, 0.24s on `cubic-bezier(.16, 1, .3, 1)` (`--ease`), from scale 1.24 and opacity 0 to rest. It fires when a stamp's value or label changes.
- **Slides:** bars 0.5s, gates and tentative bars 0.55s, tokens 0.5s, all on the same ease.
- **Loops:** only two, both state indicators: the typing caret (1s, two steps) and the search shimmer (0.9s linear).
- **Playback:** demos start once, when 35% in view. The agent demo types at 26ms a character, ticks off steps 480ms apart and advances every 3.4s until a tab is chosen; price rows resolve 520ms apart.
- **Reduced motion:** every transition and animation is off, the thump is skipped, demos show their finished state, nothing auto-plays and smooth scrolling stops.

**The Thump Rule.** A change of state lands as a stamp impact and a change of position slides. Nothing moves that is not reporting a change.

## Do's and Don'ts

### Do:
- **Do** choose ink by meaning: violet for time and the plan, green for money and done, red for changes and attention (The Three Pads Rule).
- **Do** draw structure with rules: 1.5px Printed Rule Blue, 2px for heavier divisions and control strokes, a 4px double rule above a total.
- **Do** set stamped and measured things in League Gothic capitals at weight 400, and everything that is read in Libre Franklin.
- **Do** give every stamp a tilt between -5deg and +7deg (default -2deg), lean neighbours differently, and alternate the `ink` and `ink-2` filters on adjacent impressions.
- **Do** use the `ink-fine` filter on stamps of about 1.3rem and under, on every revision stamp, and on the hero stamps at 640px and below.
- **Do** mark anything pending with a dashed frame or 45-degree hatching, and redraw it solid when it is committed.
- **Do** re-stamp a changed value with the thump (0.24s, from scale 1.24 and opacity 0) and leave the earlier impression as a ghost at 17% opacity.
- **Do** ask for `tabular-nums` on every figure that changes or aligns.
- **Do** print in Reverse White on a flood, tint secondary text with that flood's tint, and invert the buttons.
- **Do** show app captures as stapled attachments on a white mount, in the app's Glass skin, with a caption beneath.
- **Do** set tool names, keys and sample lists in Libre Franklin inside a ruled box; the build has no monospace face.
- **Do** keep the browser's own surfaces in the palette: violet selection, caret and scrollbar thumb, a 3px violet focus ring at 3px offset, underlines at 0.18em offset.
- **Do** honour reduced motion the way the build does: no transitions, no animations, demos shown finished.

### Don't:
- **Don't** build a grid of feature cards. The owner dislikes them and the build has none; claims are form rows, ruled demos and attachments.
- **Don't** make it look like every SaaS page, dark and techy, or plain and corporate. The system is light only.
- **Don't** add a fourth pad ink, and don't use blue as an ink. Blue draws rules and captions only.
- **Don't** put a caption above a headline. Captions name fields, columns, axes and controls.
- **Don't** tilt, roughen or multiply-blend printed matter. Body text, tables, buttons, form rows and bars stay square and clean; only stamps, inked headlines and the seal carry the ink filter, and only stamps, the seal and attachments lean.
- **Don't** put a shadow under anything printed or stamped on the sheet (The Separate Sheet Rule).
- **Don't** group content on paper with a filled or shadowed box. Rule it.
- **Don't** set sentences or lowercase in League Gothic.
- **Don't** add motion that is not reporting a change: no scroll-reveal entrances and no looping decoration.
- **Don't** use a colour-blend gradient. Gradients in the build are only ruled lines, week ticks, hatching and the search shimmer.
