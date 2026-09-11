
import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="OrgPulse, AI-Powered Org. Intelligence",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

data = pd.read_csv("orgpulse_processed_data.csv")
risk = pd.read_csv("orgpulse_risk_analysis.csv")
weekly = pd.read_csv("orgpulse_weekly_trends.csv")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("OrgPulse")
st.subheader("Organizational Intelligence System")

st.markdown(
    """
    **OrgPulse** uses semantic AI, semantic embeddings and unsupervised
    learning to identify organizational problems, discover problem
    categories, analyze trends and calculate organizational risk.
    """
)

st.divider()

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Reports",
    len(data)
)

col2.metric(
    "Problem Categories",
    10
)

critical_count = len(
    risk[
        risk["Risk Level"]
        .astype(str)
        .str.contains("CRITICAL")
    ]
)

col3.metric(
    "Critical Problems",
    critical_count
)

highest_risk = risk["Risk Score"].max()

col4.metric(
    "Highest Risk Score",
    f"{highest_risk:.2f}"
)

st.divider()

# --------------------------------------------------
# RISK ANALYSIS
# --------------------------------------------------

st.header("Organizational Risk Analysis")

risk_display = risk.sort_values(
    by="Risk Score",
    ascending=False
)

st.dataframe(
    risk_display,
    width="stretch",
    hide_index=True
)

# --------------------------------------------------
# TOP RISKS
# --------------------------------------------------

st.subheader("Highest Priority Problems")

top_risks = risk_display.head(3)

for _, row in top_risks.iterrows():

    category = row["problem_category"]
    score = row["Risk Score"]
    level = row["Risk Level"]

    if "CRITICAL" in str(level):

        st.error(
            f"CRITICAL: {category} — Risk Score: {score:.2f}"
        )

    elif "MODERATE" in str(level):

        st.warning(
            f"MODERATE: {category} — Risk Score: {score:.2f}"
        )

    else:

        st.success(
            f"LOW: {category} — Risk Score: {score:.2f}"
        )

st.divider()

# --------------------------------------------------
# WEEKLY TRENDS
# --------------------------------------------------

st.header("Weekly Organizational Problem Trends")

weekly["week"] = pd.to_datetime(weekly["week"])

weekly_pivot = weekly.pivot(
    index="week",
    columns="problem_category",
    values="reports"
)

st.line_chart(
    weekly_pivot,
    width="stretch"
)

st.divider()

# --------------------------------------------------
# CURRENT PROBLEM DISTRIBUTION
# --------------------------------------------------

st.header("Current Problem Distribution")

latest_week = weekly["week"].max()

latest_data = weekly[
    weekly["week"] == latest_week
].sort_values(
    by="reports",
    ascending=False
)

st.bar_chart(
    latest_data.set_index("problem_category")["reports"],
    width="stretch"
)

st.divider()

# --------------------------------------------------
# EMERGING PROBLEMS
# --------------------------------------------------

st.header("Emerging Organizational Problems")

emerging = risk.sort_values(
    by="Growth (%)",
    ascending=False
)

st.dataframe(
    emerging[
        [
            "problem_category",
            "Previous Week",
            "Latest Week",
            "Growth (%)"
        ]
    ],
    width="stretch",
    hide_index=True
)

st.divider()

# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------

with st.expander("View Processed Company Reports"):

    st.dataframe(
        data.head(100),
        width="stretch",
        hide_index=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "OrgPulse | AI-powered Organizational Intelligence System"
)
