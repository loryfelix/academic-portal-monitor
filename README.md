# Academic Portal Monitor 🎓

An automated tool designed to eliminate the need for manual checks on university platforms. It monitors the student portal for updates regarding exams, new lecture recordings, and uploaded course materials.

## Tech Stack (In Progress)
- **Language:** Python 3.x
- **Scraping:** Selenium / Playwright (exploring session-handling to bypass authentication)
- **Notifications:** Telegram Bot API

## Status: Work in Progress
Currently expanding the script's capabilities:
- [ ] **Exam Tracker:** Monitor new exam sessions and dates.
- [ ] **Material Notifier:** Detect newly uploaded slides, PDFs, or lecture recordings.
- [ ] **Lesson Update:** Notify when a new lesson link or schedule is posted.
- [ ] **Auth Research:** Implementing a workaround for SPID/SSO authentication (manual session injection).

## Why this project?
Managing university deadlines is a challenge. By automating the monitoring of "new content" (materials and lessons), I can focus on studying rather than refreshing the portal. From a QA perspective, this involves handling complex navigation flows and session persistence.
