---
name: eddie-carousel
description: Create branded educational carousels by filling the user's own editable Canva template with original content based on their topic and inspiration. Use for EDDIE Carousel, Canva template carousels, or an explicitly requested recurring inspiration-to-carousel workflow.
---

# EDDIE Carousel 1.0.0

Turn a doctor's topic and inspiration into an original, branded carousel inside that doctor's Canva template. This skill includes no DWC templates, account access, subscriptions or background monitoring service. It is separate from EDDIE Classic and EDDIE Motion; their video layout rules do not apply.

## First use: ask for their template and inspiration

When the required inputs are missing, start with this short request, adapting it to information already supplied:

> To start EDDIE Carousel, share your own Canva template link that you authorize me to edit. The Canva account connected here must have edit access. I will make a working copy so your reusable template stays intact. Also share a few posts or account links for inspiration, your first topic, and who the carousel is for. If you have a preferred tone or call to action, include it.

Ask only for missing essentials. Do not request passwords or suggest making a design publicly editable. A public view link alone does not establish edit access. Use the user's connected Canva account or an authorized signed-in browser. If access fails, explain the specific problem and request an accessible editable copy. Do not substitute the publisher's templates or choose a different design without the user's direction.

If the user has no inspiration examples, use their topic and audience; references are helpful, not a blocker. Infer branding from the supplied template. Ask for specialty, audience, language or CTA only when the template and brief do not establish them. Do not import another doctor's branding, claims, offers or account list.

Save the user's choices in an ignored local project brief so subsequent carousels reuse them without repeating intake. Keep template links, design IDs, account preferences, source notes and outputs under `projects/`, never in the public skill files.

## Inspect and plan

1. Check available Canva tools and their current capabilities. Read the relevant Canva editing skill when installed. Without usable Canva access, prepare slide copy and identify the missing connection; do not claim to have edited the design.
2. Open the supplied design and inspect every page: dimensions, slide roles, text boxes, hierarchy, fonts, colors, imagery, logo, handle and footer. Preserve the template's design language. Use its existing number of slides and layout unless the user asks otherwise; do not impose a generic seven-slide design.
3. Copy the design to a clearly named working design, such as `Topic — EDDIE Carousel — YYYY-MM-DD`, and record both original and working IDs. Use the working ID for all edits. If copying is unsupported, ask for a user-created editable duplicate. If the user explicitly supplied a disposable copy and authorized editing it directly, respect that choice.
4. Create a compact page map: page number, existing role, new headline, body, visual instruction and supporting source. Prefer a strong accurate hook, one idea per slide, a useful progression and a closing takeaway or the user's own CTA. Fit the actual template.

## Research and original writing

Read the supplied inspiration before describing its content. Extract the topic, audience question, hook pattern and teaching structure; create a fresh explanation and wording in the doctor's voice. Do not copy a creator's distinctive wording, branding, artwork or whole slide sequence. Reuse third-party assets only when the user has rights to them. Attribute quotations and distinctive findings where used.

Treat inspiration as an idea source, not evidence for a medical claim. Verify substantive health claims against current primary research or authoritative clinical guidance. Preserve population, limitations and uncertainty; distinguish association from causation and preliminary findings from established care. Do not invent statistics, citations, patient stories, outcomes, credentials or services. If verification is unavailable, omit the unsupported claim or flag it clearly for the doctor rather than presenting it as established fact.

Use short headlines and concise plain-language body copy. Reduce copy before shrinking text. Adapt density to the actual boxes and phone readability. Keep sources in local notes and provide compact citations in suitable template space or the accompanying caption. Produce an original social caption, a fitting CTA and optional alt text. Do not invent a lead magnet, booking URL or promise to send a protocol.

## Fill Canva and verify

Use the supported route for the supplied template: autofill only when real editable fields exist; otherwise inspect the design's actual elements and replace their content. Never invent element IDs or assume every design is an autofill-enabled brand template. Reuse the user's template assets; source new assets only within the user's request and rights.

Honor the installed Canva tool's transaction and approval rules, accounting for authorization already given. Make changes concrete and previewable before requesting any additional approval. A transaction draft is not saved until its commit succeeds. Do not report a local slide plan as a completed Canva design.

Preserve fonts, palette, dimensions, logos, spacing and visual hierarchy. If a tool cannot add pages or text boxes, adapt copy to supported fields or explain the specific limitation; do not silently switch templates. Do not retry an uncertain save blindly: inspect the working design first to avoid duplicate designs or changes.

Inspect every resulting page visually. Fix clipped text, overflow, poor contrast, awkward wraps, placeholder copy, old topic remnants, inconsistent footer information and out-of-order slides. Verify medical wording against the sources and the doctor's brief. Label outputs as a draft for the doctor's review unless the user has already approved the final content.

Return the saved working Canva link, page count, social caption, source notes and any unresolved limitation. Export numbered PNGs and an optional PDF when requested and supported, then verify the exported page count and order. Preserve the editable Canva design. Creating or saving a draft does not authorize posting it to social media or changing its sharing permissions.

## Optional daily inspiration workflow

Only configure recurring monitoring when the user requests it. Ask for the account URLs, review time and time zone, topics to include or avoid, output location, and whether each run should produce ideas or completed Canva drafts. Reuse known preferences. Default to drafts for review, not automatic social posting. Confirm the scope of any ongoing design edits during setup.

Use an available scheduler in the user's own environment. Store the agreed brief and a source ledger in their ignored project. Record each inspected post's URL or ID, author, publication date when available, inspection time, topic, output design ID and status. Check only accessible posts, distinguish posting date from discovery date, skip already processed posts and avoid repeating the same angle. Never claim a daily check happened when the account was inaccessible. Do not bypass login restrictions or access controls.

Each scheduled run should read the brief and ledger, inspect newly available content, select relevant ideas, verify claims, write original copy, fill a fresh working copy when authorized, and update the ledger. Save the working design ID as soon as it exists so a retry can resume instead of creating duplicates. If nothing useful is new, do not create filler. Report access failures or missing tools honestly. Notify only for meaningful new drafts, required review or a blocker, following the user's notification preferences.

Downloading this repository or invoking the skill once does not activate monitoring. Report a schedule as active only after the scheduler confirms creation. If scheduling is unavailable, provide a reusable manual run prompt and say that no automation has been activated.
