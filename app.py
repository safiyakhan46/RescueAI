import streamlit as st

from services.conversation import ConversationEngine
from services.response import (
    generate_response,
    generate_handoff_summary,
    get_first_aid_guidance,
)
from theme import apply_theme
from sidebar import render_sidebar


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="RescueAI",
    page_icon="🩺",
    layout="wide",
)

apply_theme()


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------

if "engine" not in st.session_state:
    st.session_state.engine = ConversationEngine()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pending_message" not in st.session_state:
    st.session_state.pending_message = None


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

URGENCY_DISPLAY = {
    "EMERGENCY": ("●", "EMERGENCY", "status-emergency"),
    "URGENT": ("●", "URGENT", "status-urgent"),
    "NON_URGENT": ("●", "NON-URGENT", "status-nonurgent"),
    "INSUFFICIENT_INFORMATION": (
        "●",
        "ASSESSING",
        "status-pending",
    ),
}


def status_pill_html(triage):

    if triage is None:
        dot, label, css_class = "●", "NOT STARTED", "status-pending"
    else:
        dot, label, css_class = URGENCY_DISPLAY.get(
            triage.urgency,
            ("●", triage.urgency, "status-pending"),
        )

    return f'<span class="rai-status-pill {css_class}">{dot} {label}</span>'


def safety_row(label, value):

    if value is True:
        return (
            f'<div class="rai-safety-item safety-warn">'
            f'⚠ {label} — confirmed</div>'
        )

    if value is False:
        return (
            f'<div class="rai-safety-item safety-ok">'
            f'✓ {label} — ruled out</div>'
        )

    return (
        f'<div class="rai-safety-item safety-unknown">'
        f'· {label} — not yet reported</div>'
    )


def render_assessment_panel(incident, triage):

    st.markdown(
        '<div class="rai-section-label">Current Assessment</div>',
        unsafe_allow_html=True,
    )

    if incident is None:
        st.caption("No information gathered yet.")
        return

    situation = (
        incident.situation_type
        if incident.situation_type
        and incident.situation_type.strip().lower()
        not in {"unspecified", "unknown"}
        else "Not yet determined"
    )

    symptoms_text = (
        ", ".join(incident.symptoms)
        if incident.symptoms
        else "None reported"
    )

    safety_fields = [
        incident.loss_of_consciousness,
        incident.breathing_difficulty,
        incident.severe_bleeding,
        incident.severe_head_neck_back_pain,
        incident.confusion,
        incident.vomiting,
        incident.seizure,
    ]

    resolved_count = sum(1 for v in safety_fields if v is not None)
    total_count = len(safety_fields)
    completeness_pct = round(100 * resolved_count / total_count)

    tile1, tile2, tile3 = st.columns(3)

    with tile1:
        st.markdown(
            f'<div class="rai-tile rai-tile-blue">'
            f'<div class="rai-tile-label">Situation</div>'
            f'<div class="rai-tile-value">{situation}</div>'
            f"</div>",
            unsafe_allow_html=True,
        )

    with tile2:
        st.markdown(
            f'<div class="rai-tile rai-tile-cyan">'
            f'<div class="rai-tile-label">Symptoms</div>'
            f'<div class="rai-tile-value">{symptoms_text}</div>'
            f"</div>",
            unsafe_allow_html=True,
        )

    with tile3:
        st.markdown(
            f'<div class="rai-tile rai-tile-purple">'
            f'<div class="rai-tile-label">Completeness</div>'
            f'<div class="rai-tile-value">{completeness_pct}% '
            f"({resolved_count}/{total_count})</div>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown(
        '<div class="rai-section-label" style="margin-top:14px;">'
        "Safety Checklist</div>",
        unsafe_allow_html=True,
    )

    fields = [
        ("Loss of consciousness", incident.loss_of_consciousness),
        ("Difficulty breathing", incident.breathing_difficulty),
        ("Severe bleeding", incident.severe_bleeding),
        ("Severe head/neck/back pain", incident.severe_head_neck_back_pain),
        ("Confusion", incident.confusion),
        ("Vomiting", incident.vomiting),
        ("Seizure", incident.seizure),
    ]

    rows_html = "".join(
        safety_row(label, value) for label, value in fields
    )

    st.markdown(rows_html, unsafe_allow_html=True)

    if triage is not None:

        st.markdown(
            '<div class="rai-section-label" style="margin-top:14px;">'
            "Triage Detail</div>",
            unsafe_allow_html=True,
        )

        if triage.missing_information:
            st.markdown("**Information still needed:**")
            for item in triage.missing_information:
                st.markdown(f"- {item}")

        if triage.recommended_action:
            st.markdown("**Recommended action:**")
            st.info(triage.recommended_action)


def render_first_aid_guidance(incident):

    guidance = get_first_aid_guidance(incident)

    if not guidance:
        return

    st.markdown(
        '<div class="rai-section-label" style="margin-top:6px;">'
        "General First-Aid Guidance</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "General guidance only — not a diagnosis. Always follow "
        "instructions from emergency dispatchers if available."
    )

    for label, text in guidance:
        st.markdown(
            f'<div class="rai-firstaid-card">'
            f'<div class="rai-firstaid-title">{label}</div>'
            f'<div class="rai-firstaid-text">{text}</div>'
            f"</div>",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown('<div class="rai-header-card">', unsafe_allow_html=True)

header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown(
        '<div class="rai-title">🩺 RescueAI</div>'
        '<div class="rai-subtitle">Emergency navigation &amp; '
        "clinical handoff assistant</div>",
        unsafe_allow_html=True,
    )

with header_right:
    st.markdown(
        f'<div style="text-align:right; padding-top: 10px;">'
        f'{status_pill_html(st.session_state.engine.triage)}</div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="rai-disclaimer">RescueAI is a prototype and does '
    "not diagnose medical conditions or replace emergency "
    "services or qualified healthcare professionals. If someone "
    "is experiencing a life-threatening emergency, contact your "
    "local emergency services immediately.</div>",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Layout: conversation (left) + assessment panel (right)
# ---------------------------------------------------------

conversation_col, assessment_col = st.columns([2, 1])

with conversation_col:

    st.markdown(
        '<div class="rai-section-label">Conversation</div>',
        unsafe_allow_html=True,
    )

    chat_container = st.container(height=380)

    with chat_container:
        for message in st.session_state.chat_history:
            avatar = "🧑" if message["role"] == "user" else "🩺"
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

    if not st.session_state.chat_history:

        st.markdown(
            '<div class="rai-scenario-caption">Try a demo '
            "scenario:</div>",
            unsafe_allow_html=True,
        )

        demo_col1, demo_col2, demo_col3 = st.columns(3)

        DEMO_SCENARIOS = [
            (
                "🩹 Minor fall",
                "My friend tripped and scraped her knee, "
                "she's fine and talking normally",
            ),
            (
                "❓ Needs follow-up",
                "My brother fell down the stairs and he's "
                "dizzy",
            ),
            (
                "🚨 Emergency",
                "My dad collapsed and he's bleeding a lot "
                "from his head, he won't wake up",
            ),
        ]

        for col, (label, scenario_text) in zip(
            [demo_col1, demo_col2, demo_col3], DEMO_SCENARIOS
        ):
            with col:
                if st.button(
                    label,
                    use_container_width=True,
                    key=f"demo_{label}",
                ):
                    st.session_state.pending_message = scenario_text
                    st.rerun()

    user_message = st.chat_input("Tell me what happened...")

    if not user_message and st.session_state.get("pending_message"):
        user_message = st.session_state.pending_message
        st.session_state.pending_message = None

    if user_message:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        with st.spinner("RescueAI is reviewing what you shared..."):

            try:
                result = st.session_state.engine.process_message(
                    user_message
                )

                triage = result["triage"]
                incident = result["incident"]
                gemini_degraded = result.get(
                    "gemini_degraded", False
                )
                new_incident_detected = result.get(
                    "new_incident_detected", False
                )

                degraded_notice = ""

                if gemini_degraded:
                    degraded_notice = (
                        "\n\n---\n"
                        "⚠️ *AI extraction is temporarily "
                        "unavailable (the language model is "
                        "unreachable or rate-limited). RescueAI "
                        "is continuing to evaluate safety using "
                        "the most recent known information.*"
                    )

                new_incident_notice = ""

                if new_incident_detected:
                    new_incident_notice = (
                        "\n\n_Note: this looks like a different "
                        "situation than what we were discussing "
                        "— starting a fresh assessment for it._"
                    )

                if triage.urgency == "EMERGENCY":

                    assistant_response = (
                        "🚨 **EMERGENCY — Please contact "
                        "emergency services immediately.**\n\n"
                        f"{triage.recommended_action}\n\n"
                        f"**Why:** {triage.reasoning}\n\n"
                        "**RescueAI has identified:**\n"
                    )

                    for flag in triage.red_flags:
                        assistant_response += f"- {flag}\n"

                    assistant_response += (
                        "\n**Do not delay contacting emergency "
                        "services to continue this "
                        "conversation.** Follow the instructions "
                        "provided by the emergency dispatcher."
                    )

                    assistant_response += degraded_notice

                else:

                    assistant_response = generate_response(
                        incident=incident,
                        triage=triage,
                        user_message=user_message,
                    )

                    assistant_response += degraded_notice
                    assistant_response += new_incident_notice

            except Exception:

                assistant_response = (
                    "I ran into a problem processing that "
                    "message. Please try again — if this keeps "
                    "happening, the AI service may be "
                    "temporarily unavailable."
                )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": assistant_response,
            }
        )

        st.rerun()

with assessment_col:

    with st.container(border=True):
        render_assessment_panel(
            st.session_state.engine.incident,
            st.session_state.engine.triage,
        )

    if st.session_state.engine.incident is not None:

        render_first_aid_guidance(st.session_state.engine.incident)

        with st.expander("📋 Clinical handoff summary"):

            summary_text = generate_handoff_summary(
                st.session_state.engine.incident,
                st.session_state.engine.triage,
            )

            st.text(summary_text)

            st.caption(
                "Read this aloud to a dispatcher or share it "
                "with arriving responders."
            )


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

render_sidebar(active_page="Assessment")
