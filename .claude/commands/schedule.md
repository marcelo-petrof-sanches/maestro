---
description: Fast-lane calendar scheduling — checks conflicts/availability and gives me a one-click prefilled Outlook event
---

Schedule something on my calendar. The M365 connector is READ-ONLY for calendar, so
the flow is: you do all the work, I do one click.

1. **Parse the ask**: title, date/time (or constraint like "this week"), duration
   (default 30 min), attendees (resolve names → emails from brain files or email
   search), location / Teams.
2. **Check before proposing**:
   - My calendar (`outlook_calendar_search`) for conflicts — flag them, respect my
     protected time (19h–21h gym, weekends) and energy map (deep work 9–12h) from
     `brain/profile/working-preferences.md`.
   - If attendees given and time is open: `find_meeting_availability` to find slots
     everyone can make (convert UTC results to BRT).
3. **Deliver a one-click link** — an Outlook compose deeplink with everything
   prefilled, as a clickable markdown link:
   `https://outlook.office.com/calendar/deeplink/compose?subject=<urlencoded>&startdt=<YYYY-MM-DDTHH:mm:ss>&enddt=<...>&body=<urlencoded>&location=<...>&to=<email1,email2>`
   Times in local São Paulo time, URL-encoded. Draft a sharp 1-2 line body (purpose +
   agenda) in the right language (PT for client, per context).
4. If multiple slot options exist, give me 2-3 links (one per slot), best first.
5. After I confirm it's booked, log it if relevant (daily log / project file).

Format: tight — conflicts/availability finding in one line each, then the link(s).
No lecture about the read-only limitation every time.

What to schedule: $ARGUMENTS
