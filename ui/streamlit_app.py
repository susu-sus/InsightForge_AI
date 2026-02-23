import sys
import os
import re
from datetime import datetime
from io import BytesIO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.workflow.graph import ResearchWorkflow

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(page_title="InsightForge AI", layout="wide")


# ==========================================
# CUSTOM UI STYLE
# ==========================================
st.markdown("""
<style>
.stApp {
    background-color: #0d0d0d;
    color: white;
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 60px;
}

.brand {
    font-size: 20px;
    font-weight: 600;
}

.hero {
    text-align: center;
    margin-top: 120px;
}

.hero-title {
    font-size: 52px;
    font-weight: 700;
    margin-bottom: 12px;
}

.highlight {
    color: #4da3ff;
}

.hero-subtitle {
    color: #aaaaaa;
    font-size: 18px;
    margin-bottom: 40px;
}

/* INPUT */
.stTextInput input {
    background-color: #1a1a1a;
    color: white;
    border: 1px solid #333;
    border-radius: 12px;
    padding: 14px;
    text-align: center;
}

/* GREEN BUTTON */
.stButton button {
    background: linear-gradient(90deg, #00c853, #00e676);
    color: black;
    border-radius: 12px;
    padding: 10px 28px;
    font-weight: 600;
    border: none;
}

.stButton button:hover {
    background: linear-gradient(90deg, #00e676, #00c853);
}

.section-card {
    max-width: 1000px;
    margin: 60px auto;
    padding: 40px;
}

.footer {
    text-align: center;
    margin-top: 60px;
    font-size: 13px;
    color: #777;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "main"

if "result_state" not in st.session_state:
    st.session_state.result_state = None


# ==========================================
# NAVBAR
# ==========================================
col1, col2 = st.columns([8,1])

with col1:
    st.markdown(
        "<div class='brand'>🧠 InsightForge AI</div>",
        unsafe_allow_html=True
    )

with col2:
    if st.button("About"):
        st.session_state.page = "about"
        st.rerun()


# ==========================================
# MAIN PAGE
# ==========================================
if st.session_state.page == "main":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
            Just ask for it, <span class="highlight">it gets structured.</span>
        </div>
        <div class="hero-subtitle">
            InsightForge AI is a research intelligence platform that enables users to explore global knowledge and generate structured, professional reports with precision.
        </div>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input("")

    if st.button("Generate Report"):
        if query.strip():
            workflow = ResearchWorkflow()
            state = workflow.run(query)
            st.session_state.result_state = state
            st.session_state.page = "results"
            st.rerun()


# ==========================================
# RESULTS PAGE
# ==========================================
elif st.session_state.page == "results":

    state = st.session_state.result_state

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)

    st.header("Research Output")

    if st.button("Back to Home"):
        st.session_state.page = "main"
        st.rerun()

    st.subheader("Research Topic")
    st.write(state.query)

    st.subheader("Research Plan")
    for step in state.plan:
        clean_step = re.sub(r"[*#]", "", step)
        st.write(f"• {clean_step}")

    st.subheader("Final Report")
    clean_display = re.sub(r"\*\*(.*?)\*\*", r"\1", state.final_report)
    st.write(clean_display)

    # ==========================================
    # PROFESSIONAL PDF GENERATION
    # ==========================================
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    title_style = ParagraphStyle(
        name="Title",
        fontSize=20,
        spaceAfter=20,
        textColor=colors.black
    )

    heading_style = ParagraphStyle(
        name="Heading",
        fontSize=16,
        spaceAfter=12,
        textColor=colors.black
    )

    normal_style = ParagraphStyle(
        name="Normal",
        fontSize=11,
        spaceAfter=6,
        textColor=colors.black
    )

    bullet_style = ParagraphStyle(
        name="Bullet",
        fontSize=11,
        leftIndent=15,
        spaceAfter=4,
        textColor=colors.black
    )

    code_style = ParagraphStyle(
        name="Code",
        fontSize=9,
        leftIndent=20,
        spaceAfter=4,
        textColor=colors.black
    )

    elements = []

    elements.append(Paragraph("INSIGHTFORGE AI RESEARCH REPORT", title_style))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Research Topic", heading_style))
    elements.append(Paragraph(state.query, normal_style))
    elements.append(Spacer(1, 15))

    elements.append(Paragraph("Research Plan", heading_style))
    for step in state.plan:
        clean_step = re.sub(r"[*#]", "", step)
        elements.append(Paragraph(f"• {clean_step}", bullet_style))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Final Report", heading_style))
    elements.append(Spacer(1, 10))

    lines = state.final_report.split("\n")
    inside_code = False

    for line in lines:
        line = line.strip()

        if line.startswith("```"):
            inside_code = not inside_code
            continue

        if inside_code:
            elements.append(Paragraph(line, code_style))
            continue

        # Remove bold
        line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)

        # Detect headings
        if line.startswith("###"):
            clean = line.replace("###", "").strip()
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(clean, heading_style))

        elif line.startswith("##"):
            clean = line.replace("##", "").strip()
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(clean, heading_style))

        elif line.startswith("* ") or line.startswith("- "):
            clean = line[2:].strip()
            elements.append(Paragraph(f"• {clean}", bullet_style))

        elif re.match(r"\d+\.", line):
            elements.append(Paragraph(line, bullet_style))

        elif line != "":
            elements.append(Paragraph(line, normal_style))
            elements.append(Spacer(1, 6))

    doc.build(elements)

    st.download_button(
        "Download PDF",
        buffer.getvalue(),
        file_name="InsightForge_Professional_Report.pdf",
        mime="application/pdf"
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# ABOUT PAGE
# ==========================================
elif st.session_state.page == "about":

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)

    st.header("About InsightForge AI")

    st.write("""
    InsightForge AI is a modular multi-agent research intelligence system 
    designed to transform natural language queries into structured analytical outputs.

    The system integrates large language models, vector-based retrieval systems, 
    and agent-driven workflows to generate professional, export-ready reports.
    """)

    if st.button("Back to Home"):
        st.session_state.page = "main"
        st.rerun()

    st.markdown(
        f"<div class='footer'>© {datetime.now().year} InsightForge AI • Intelligent Research Simplified</div>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)