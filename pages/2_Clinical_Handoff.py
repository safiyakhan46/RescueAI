import streamlit as st

from theme import apply_theme
from services.response import generate_handoff_summary, get_first_aid_guidance
from services.conversation import ConversationEngine


st.set_page_config(
    page_title="RescueAI — Clinical Handoff",
    page_icon="📋",
    layout="wide",
)

apply_theme()


# ---------------------------------------------------------
# Session state (shared with the main assessment page)
# ---------------------------------------------------------

if "engine" not in st.session_state:
    st.session_state.engine = ConversationEngine()


engine = st.session_state.engine
incident = engine.incident
triage = engine.triage


st.markdown('<div class="rai-header-card">', unsafe_allow_html=True)
st.markdown(
    '<div class="rai-title">📋 Clinical Handoff</div>'
    '<div class="rai-subtitle">A structured summary ready to '
    "read to a dispatcher or hand to arriving responders</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

if incident is None:

    st.info(
        "No assessment has been started yet. Go to the main "
        "**RescueAI** page and describe what happened to begin "
        "building an incident summary."
    )

else:

    summary_text = generate_handoff_summary(incident, triage)

    left, right = st.columns([3, 2])

    with left:

        st.markdown(
            '<div class="rai-section-label">Handoff Summary</div>',
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.text(summary_text)

        st.download_button(
            "⬇ Download as .txt",
            data=summary_text,
            file_name="rescueai_handoff_summary.txt",
            mime="text/plain",
            use_container_width=True,
        )

        st.caption(
            "Copy this summary aloud to a 911/emergency "
            "dispatcher, or hand it to paramedics on arrival."
        )

    with right:

        st.markdown(
            '<div class="rai-section-label">Triage Status</div>',
            unsafe_allow_html=True,
        )

        if triage is not None:

            urgency_colors = {
                "EMERGENCY": ("🔴", "status-emergency"),
                "URGENT": ("🟠", "status-urgent"),
                "NON_URGENT": ("🟢", "status-nonurgent"),
                "INSUFFICIENT_INFORMATION": ("🔵", "status-pending"),
            }

            emoji, css_class = urgency_colors.get(
                triage.urgency, ("⚪", "status-pending")
            )

            st.markdown(
                f'<span class="rai-status-pill {css_class}">'
                f"{emoji} {triage.urgency.replace('_', ' ')}</span>",
                unsafe_allow_html=True,
            )

            st.write("")

            if triage.red_flags:
                st.markdown("**⚠ Warning signs detected:**")
                for flag in triage.red_flags:
                    st.markdown(f"- {flag}")

            if triage.missing_information:
                st.markdown("**Still needed:**")
                for item in triage.missing_information:
                    st.markdown(f"- {item}")

            st.markdown("**Recommended action:**")
            st.info(triage.recommended_action)

        st.markdown(
            '<div class="rai-section-label" style="margin-top:18px;">'
            "General First-Aid Guidance</div>",
            unsafe_allow_html=True,
        )

        guidance = get_first_aid_guidance(incident)

        if not guidance:
            st.caption("No active red flags requiring first-aid guidance.")
        else:
            st.caption(
                "General guidance only — not a diagnosis. Always "
                "follow instructions from emergency dispatchers "
                "if available."
            )
            for label, text in guidance:
                st.markdown(
                    f'<div class="rai-firstaid-card">'
                    f'<div class="rai-firstaid-title">{label}</div>'
                    f'<div class="rai-firstaid-text">{text}</div>'
                    f"</div>",
                    unsafe_allow_html=True,
                )

st.markdown(
    '<div class="rai-disclaimer">RescueAI is a prototype and does '
    "not diagnose medical conditions or replace emergency "
    "services or qualified healthcare professionals.</div>",
    unsafe_allow_html=True,
)
