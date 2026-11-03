---
name: eddie-post
description: Prepare and schedule approved videos in Vista Social with script-based descriptions, correct brand profiles, first comments, and linked comment-to-DM automations. Use for EDDIE POST and video publishing batches; editing footage belongs to EDDIE MASTER EDITOR.
---
# EDDIE POST

Turn approved video files and their scripts/transcripts into verified Vista Social scheduled posts. Training this skill is not a request to publish a batch. Draft, schedule, publish-now and automation activation are distinct actions; carry out the action authorized in the current task. Do not make a Codex recurring task to implement a Vista Social posting calendar.

## Intake and routing

Identify the exact approved version of each video; revisions of one topic are alternatives, not separate daily posts unless requested. Match its script to the final audio/transcript: a removed line must not appear as a claim in the description. Preserve approved video and audio; no re-export solely to upload. Respect a review-only label or unresolved release issue; ask only about unresolved choices needed for the actual publishing run.

Resolve the brand/account and connected profiles using live Vista Social data. Read [the Haris/Telemed example](references/haris-example.md) for this user's demonstrated settings. Do not select every connected account: similar display names can belong to different brands. Store exact platform/profile IDs in the private batch record. Verify selected profiles before submission.

Prefer the Vista Social MCP for supported operations. Discover its actual tools and schemas; do not invent endpoints or assume it supports local-file upload, first comments or automation duplication. Use the authenticated browser for missing operations. Read the existing live automation before copying it; screenshots establish the desired treatment, not current account state.

## Description and first comment

For each video, draft a short opening hook, a clear summary based on what is actually said, the recorded CTA/keyword and the practice's approved education/service footer. Keep meaningful qualifications; do not introduce stronger medical claims, invented outcomes or new treatment instructions. If researching new medical explanations, verify authoritative sources before adding them. Do not invent guides, downloadable resources or links.

Adapt length and formatting to each platform's actual limits. Use the same CTA keyword in the spoken video, description, first comment and automation. If any disagree, resolve before scheduling or activation. The first comment is the practice's initial comment on the post; the automation's public reply is a different field. Populate first comments only on supported platforms, and report omissions rather than pretending cross-platform support. A DM CTA must only promise delivery on accounts where that delivery is configured; adapt other channels appropriately.

## Daily scheduling

Default cadence: one distinct video per calendar day at 09:00. Use the practice's configured IANA timezone; this user's provisional default is America/Los_Angeles (9 AM Pacific), subject to a current user override or account mismatch clarification. Use local wall-clock time across daylight-saving changes, not a fixed UTC offset.

Inspect the calendar first. Use an explicit requested start date; otherwise use the next future unoccupied 9 AM slot and show the resulting dates in the batch summary. Skip occupied days for the selected brand instead of silently replacing existing posts. Cross-posts of the same video on its selected channels count as one daily video. Preserve user order; if unspecified, use numbered video order.

Schedule each video separately with its description, first comments and correct media. Wait for upload/processing completion and check platform errors. Record source path/hash, topic, profile IDs, local date/time/timezone, UTC instant, post IDs, caption, first comment and automation ID in a private batch manifest. After a timeout, inspect the calendar/posts before retrying; never blindly submit a duplicate. Resume from verified records on partial failure.

## Link the comment automation

When authorized, duplicate the specified existing automation (the demonstrated template is `B2C Comment "Protocol" to DM`). Preserve the original automation and its post associations. In the new copy, use Specific posts and replace the inherited target with the newly scheduled post belonging to the automation's exact profile. Do not select All posts. If Vista cannot target the scheduled post yet, record the dependency and leave the automation pending; do not attach a similar-looking reel.

Preserve the live template's keyword matching, followers setting, exclusions, delivery limits, action order, reply variations, full DM and button URL unless the task calls for changes. Name the copy with the keyword and video title. Check for an existing matching copy before creating one. Protocol is not the default keyword for unrelated CTAs: different keywords/resources need matching approved content, not an unchanged fertility checklist.

The supplied screenshots establish the Protocol trigger configuration; do not ask the user to teach it again or mark the automation setup generically pending. Use the settings in the reference. Partial screenshots do not establish the unseen remainder of the DM or other reply variants. Retrieve those from the live Protocol template; if unavailable, report only that specific missing content. Do not reconstruct unseen medical advice. Test with Vista's built-in preview/test where available; do not send a real DM to a person as an unapproved test. Save/activate only within the user's authorized scope. Record activation status separately from scheduling status.

## Verify and hand back

Read back every scheduled post: correct video version/thumbnail, selected account IDs, description, first comment where supported, 09:00 date and timezone, and scheduled status. Check each automation's exact target post, keyword, complete actions and status. A scheduled post is not a published post; a saved automation is not proof a DM was delivered. Capture UI evidence when using the browser.

Return a compact list/table of title, date/time/timezone, selected channels, post link/ID and automation status. Report partial failures precisely, with no duplicate retries or edits to unrelated posts. Keep account IDs, screenshots, private scripts, media and live manifests out of public reusable skill packages.
