# 🩺 RescueAI

**Emergency navigation and clinical handoff assistant** — built for RescueHacks.

RescueAI has a natural conversation with a bystander during a potential
emergency, extracts structured incident information as they describe what
happened, and runs that information through a **deterministic safety
engine** that decides urgency — independent of whether the AI layer is
even working.

## Why this exists

In an emergency, bystanders are often the first line of response, but
rarely know what information matters or what to do while help is on the
way. RescueAI organizes that information in real time and never lets an
AI outage silence an emergency escalation.

## Architecture

```
┌─────────────────────┐
│   Streamlit UI       │  app.py
│  (chat + assessment  │
│   panel + handoff)   │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  ConversationEngine   │  services/conversation.py
│  - tracks incident     │
│  - merges / detects    │
│    new incidents       │
│  - tracks pending Q     │
└──────────┬───────────┘
           │
   ┌───────┴────────┐
   │                │
┌──▼─────────┐  ┌───▼─────────────┐
│ intake.py   │  │ safety.py         │
│ (Gemini or  │  │ deterministic,     │
│  mock       │  │ rule-based triage   │
│  extraction)│  │ (no AI dependency)  │
└─────────────┘  └────────────────────┘
           │
   ┌───────▼────────┐
   │ response.py     │
   │ - conversational │
   │   replies         │
   │ - first-aid guide  │
   │ - handoff summary  │
   └────────────────┘
```

**Key design decision:** the safety/triage layer (`core/safety.py`) is
100% deterministic and has zero dependency on Gemini. Even if the AI
extraction layer fails (quota exhausted, API outage), the safety engine
still evaluates whatever structured data has already been gathered and
still escalates correctly.

## Features

- Natural-language incident extraction (Gemini, with a rule-based
  offline fallback)
- Structured incident data model (Pydantic)
- Conversation memory — tracks and merges incident details across turns,
  handles corrections and negated follow-ups ("he didn't pass out")
- New-incident detection — won't contaminate an unrelated report with
  stale symptoms from an earlier one
- Deterministic, AI-independent emergency escalation
- Assessment status / severity indicator (color-coded triage pill)
- General first-aid guidance for confirmed red flags
- Structured clinical handoff summary, ready to read to a dispatcher
- Demo/offline mode (`MOCK_MODE=true`) — guarantees zero live API calls
  during a presentation

## Running it

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=your_key_here
MOCK_MODE=false   # set to true for offline/demo mode
```

```bash
streamlit run app.py
```

## Tools & AI disclosure

Built during RescueHacks using Gemini (incident extraction), Claude (AI
coding assistant during development), Streamlit (interface), and
Pydantic (structured data modeling). The safety-evaluation logic is
hand-written and does not depend on any AI model.

## Future vision

See [`FUTURE_VISION.md`](./FUTURE_VISION.md).
