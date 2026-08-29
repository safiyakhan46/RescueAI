import streamlit as st

from theme import apply_theme


st.set_page_config(
    page_title="RescueAI — About",
    page_icon="🩺",
    layout="wide",
)

apply_theme()

st.markdown('<div class="rai-header-card">', unsafe_allow_html=True)
st.markdown(
    '<div class="rai-title">🩺 About RescueAI</div>'
    '<div class="rai-subtitle">Problem, mission fit, and what '
    "comes next</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------------
# Problem & Impact
# ---------------------------------------------------------

with st.container():
    st.markdown(
        '<div class="rai-card">'
        '<div class="rai-section-label">Problem &amp; Impact</div>'
        "<p>In an emergency, bystanders are often the first "
        "line of response — but they rarely know what "
        "information matters, what counts as a red flag, or "
        "what to actually do while help is on the way. Critical "
        "seconds are lost to panic, disorganized information, "
        "and uncertainty.</p>"
        "<p><strong>RescueAI</strong> is a prototype emergency "
        "navigation and clinical handoff assistant. It has a "
        "natural conversation with a bystander, extracts "
        "structured incident information as they describe what "
        "happened, runs that information through a "
        "<strong>deterministic safety engine</strong> (not just "
        "an AI guess), and — critically — escalates to an "
        "emergency recommendation the moment a red flag "
        "appears, independent of whether the AI layer is even "
        "working.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# Mission fit
# ---------------------------------------------------------

with st.container():
    st.markdown(
        '<div class="rai-card">'
        '<div class="rai-section-label">RescueHacks Mission Fit</div>'
        "<p>RescueHacks asks for technology that could help "
        "save a life — not the most technically complex build. "
        "RescueAI is squarely an "
        "<strong>emergency response helper</strong> and "
        "<strong>medical navigation helper</strong>, two of the "
        "suggested project categories, built around a simple "
        "idea: pair a conversational AI layer with a "
        "deterministic safety layer that never depends on the "
        "AI actually working.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# How it works
# ---------------------------------------------------------

with st.container():
    st.markdown(
        '<div class="rai-card">'
        '<div class="rai-section-label">How It Works</div>'
        "<ol>"
        "<li><strong>Conversational intake</strong> — the user "
        "describes what happened in plain language.</li>"
        "<li><strong>Structured extraction</strong> — an AI "
        "model (Gemini) extracts symptoms and safety fields "
        "into a structured incident record, tracking context "
        "across the conversation so follow-up answers "
        "(including corrections and negations) update the "
        "record correctly.</li>"
        "<li><strong>Deterministic safety evaluation</strong> "
        "— a separate, rule-based engine evaluates the "
        "structured record for red flags. This layer runs "
        "identically whether or not the AI extraction "
        "succeeded, so an API outage never silences an "
        "emergency escalation.</li>"
        "<li><strong>Guidance</strong> — the assistant asks for "
        "the single most important missing detail, surfaces "
        "general first-aid guidance for any confirmed red "
        "flag, and can generate a structured clinical handoff "
        "summary for arriving responders.</li>"
        "</ol>"
        "</div>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# Future potential
# ---------------------------------------------------------

with st.container():
    st.markdown(
        '<div class="rai-card">'
        '<div class="rai-section-label">Future Potential</div>'
        "<ul>"
        "<li>Multi-language support for non-English speakers "
        "during an emergency</li>"
        "<li>Direct integration with local dispatch / 911 "
        "systems for automatic structured handoff</li>"
        "<li>Offline-first mode for areas with poor "
        "connectivity</li>"
        "<li>Voice input for hands-free use during an active "
        "incident</li>"
        "<li>Expanded red-flag coverage beyond the current "
        "safety fields</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# Disclosure
# ---------------------------------------------------------

with st.container():
    st.markdown(
        '<div class="rai-card">'
        '<div class="rai-section-label">Tools &amp; AI Disclosure</div>'
        "<p>Built during RescueHacks using: <strong>Gemini</strong> "
        "for natural-language incident extraction, "
        "<strong>Claude</strong> as an AI coding assistant during "
        "development, <strong>Streamlit</strong> for the interface, "
        "and <strong>Pydantic</strong> for structured data "
        "modeling. The deterministic safety-evaluation logic is "
        "hand-written and does not depend on any AI model.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="rai-disclaimer">RescueAI is a prototype and does '
    "not diagnose medical conditions or replace emergency "
    "services or qualified healthcare professionals.</div>",
    unsafe_allow_html=True,
)
