import os

import streamlit as st

from services.conversation import ConversationEngine


def render_sidebar(active_page: str = "Assessment"):
    """
    Shared sidebar shown on every page, so navigation feels
    consistent whether you're on the main assessment tool,
    About page, or Clinical Handoff page.
    """

    with st.sidebar:

        st.header("🩺 RescueAI")

        st.caption(f"You're viewing: **{active_page}**")

        st.write(
            "RescueAI combines conversational AI with a "
            "deterministic safety layer to help organize "
            "information during potentially urgent situations."
        )

        st.divider()

        st.subheader("Current capabilities")

        st.write("✓ Natural-language incident extraction")
        st.write("✓ Structured incident data")
        st.write("✓ Safety-rule evaluation")
        st.write("✓ Conversational history")
        st.write("✓ Deterministic emergency escalation")
        st.write("✓ General first-aid guidance")

        st.divider()

        if os.getenv("MOCK_MODE", "false").strip().lower() == "true":
            st.info("🧪 Demo mode active — offline extraction.")
            st.divider()

        if st.button(
            "🔄 Start new assessment",
            use_container_width=True,
            key=f"reset_{active_page}",
        ):
            st.session_state.engine = ConversationEngine()
            st.session_state.chat_history = []
            st.session_state.pending_message = None
            st.rerun()
