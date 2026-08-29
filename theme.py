import streamlit as st


def apply_theme():
    """
    Shared soft-gradient, card-based styling inspired by modern
    health-tech dashboards. Call once near the top of every page
    (app.py and each file under pages/) so the look stays
    consistent across the app.
    """

    st.markdown(
        """
        <style>

        /* ---- Overall canvas ---- */

        .stApp {
            background: linear-gradient(
                160deg, #EAF1FF 0%, #F3F8FF 50%, #FFFFFF 100%
            );
        }

        .block-container {
            padding-top: 1.6rem;
            max-width: 1200px;
        }

        /* ---- Typography ---- */

        .rai-title {
            font-size: 30px;
            font-weight: 800;
            letter-spacing: -0.3px;
            margin-bottom: 0;
            color: #1B2B4B;
        }

        .rai-subtitle {
            font-size: 14px;
            color: #6B7A8D;
            margin-top: 2px;
            margin-bottom: 0;
        }

        .rai-section-label {
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #1E5FE0;
            margin-bottom: 10px;
            margin-top: 4px;
        }

        /* ---- Top header card ---- */

        .rai-header-card {
            background: #FFFFFF;
            border-radius: 22px;
            padding: 18px 26px;
            box-shadow: 0 8px 24px rgba(70, 90, 160, 0.10);
            margin-bottom: 18px;
        }

        /* ---- Status pill ---- */

        .rai-status-pill {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 8px 18px;
            border-radius: 24px;
            font-weight: 700;
            font-size: 12.5px;
            letter-spacing: 0.3px;
            white-space: nowrap;
        }

        .status-emergency {
            background: linear-gradient(135deg, #FF6B6B, #E63946);
            color: #FFFFFF;
        }

        .status-urgent {
            background: linear-gradient(135deg, #FFB86B, #F0932B);
            color: #FFFFFF;
        }

        .status-nonurgent {
            background: linear-gradient(135deg, #4EDCA0, #1E9E6B);
            color: #FFFFFF;
        }

        .status-pending {
            background: linear-gradient(135deg, #4E86F5, #1E5FE0);
            color: #FFFFFF;
        }

        /* ---- Disclaimer ---- */

        .rai-disclaimer {
            font-size: 12px;
            color: #8A97A6;
            line-height: 1.5;
            margin-top: 4px;
        }

        /* ---- Cards ---- */

        .rai-card {
            border-radius: 20px;
            padding: 18px 20px;
            margin-bottom: 16px;
            background-color: #FFFFFF;
            box-shadow: 0 6px 18px rgba(70, 90, 160, 0.08);
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 20px !important;
            border: none !important;
            box-shadow: 0 6px 18px rgba(70, 90, 160, 0.08);
        }

        /* ---- Colorful stat tiles ---- */

        .rai-tile {
            border-radius: 18px;
            padding: 16px 18px;
            color: #FFFFFF;
            min-height: 92px;
            box-shadow: 0 6px 16px rgba(70, 90, 160, 0.14);
        }

        .rai-tile-label {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            opacity: 0.85;
            margin-bottom: 6px;
        }

        .rai-tile-value {
            font-size: 16px;
            font-weight: 700;
            line-height: 1.35;
        }

        .rai-tile-blue {
            background: linear-gradient(135deg, #6E8BFF, #4A5CF0);
        }

        .rai-tile-cyan {
            background: linear-gradient(135deg, #4FA6F0, #1E82D6);
        }

        .rai-tile-purple {
            background: linear-gradient(135deg, #2E4FCC, #16327A);
        }

        /* ---- Progress ring ---- */

        .rai-ring-wrap {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .rai-ring-label {
            font-size: 12.5px;
            color: #6B7A8D;
            font-weight: 600;
        }

        /* ---- Safety checklist ---- */

        .rai-safety-item {
            font-size: 14px;
            padding: 9px 0;
            border-bottom: 1px solid #F0F1FA;
        }

        .safety-ok {
            color: #1E9E6B;
        }

        .safety-warn {
            color: #E63946;
            font-weight: 700;
        }

        .safety-unknown {
            color: #ABB4C4;
        }

        /* ---- First aid card ---- */

        .rai-firstaid-card {
            border-radius: 16px;
            background: linear-gradient(135deg, #FFF3E0, #FFE8CC);
            padding: 14px 16px;
            margin-bottom: 10px;
        }

        .rai-firstaid-title {
            font-weight: 700;
            font-size: 13px;
            color: #C1660A;
            margin-bottom: 4px;
        }

        .rai-firstaid-text {
            font-size: 13px;
            line-height: 1.55;
            color: #5A4630;
        }

        /* ---- Chat bubbles ---- */

        div[data-testid="stChatMessage"] {
            border-radius: 18px;
            padding: 4px 6px;
        }

        div[data-testid="stChatInput"] textarea {
            border-radius: 24px !important;
        }

        /* ---- Buttons ---- */

        .stButton button {
            border-radius: 14px !important;
            font-weight: 600 !important;
        }

        .rai-scenario-caption {
            font-size: 12px;
            color: #8A97A6;
            margin-bottom: 6px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
