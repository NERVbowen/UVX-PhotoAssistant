import streamlit as st

st.set_page_config(
    page_title="UVX Photochemistry",
    page_icon="🧪",
    layout="wide"
)

home, tab_db, tab_similarity, tab_el = st.tabs([
    "🏠 Home",
    "📚 Photoinitiator Database",
    "🔍 Similarity Search",
    "🧪 E/L Screening"
])

with home:
    st.title("🧪 UVX Photochemistry Database")

    st.caption(
        "Free tools and curated data for photochemistry, photoinitiators, "
        "UV/LED curing, photopolymerization, and photoactive materials."
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Photoinitiators", "47")

    with col2:
        st.metric("UV Spectra", "47")

    with col3:
        st.metric("Chemical Structures", "In progress")

    with col4:
        st.metric("AI Tools", "Beta")

    st.markdown("---")

    st.subheader("🔬 What is UVX Photochemistry?")

    st.write(
        "UVX Photochemistry is an open-access platform for researchers and engineers "
        "working with photoinitiators, photopolymerization, UV/LED curing, "
        "photoactive materials, polymers, medical devices, pharmaceutical packaging, "
        "and extractables/leachables (E/L)."
    )

    st.write(
        "The goal is to provide practical, searchable, and AI-assisted tools for "
        "photochemistry and materials research."
    )

    st.subheader("🚀 Available and Planned Tools")

    tools = [
        {
            "Tool": "📚 Photoinitiator Database",
            "Description": "Search common photoinitiators and view UV absorption spectra.",
            "Status": "Available"
        },
        {
            "Tool": "🔍 Similar Structure Search",
            "Description": "Draw or enter a molecule and compare it with known photoinitiators.",
            "Status": "Planned"
        },
        {
            "Tool": "🧪 E/L Screening",
            "Description": "Preliminary screening of molecular properties relevant to extractables and leachables.",
            "Status": "Planned"
        },
        {
            "Tool": "🌈 UV Spectrum Explorer",
            "Description": "View and compare absorption spectra for photoinitiators.",
            "Status": "In progress"
        },
        {
            "Tool": "💡 LED Compatibility Selector",
            "Description": "Match photoinitiators with common LED wavelengths such as 365, 385, 395, and 405 nm.",
            "Status": "Planned"
        },
    ]

    st.dataframe(tools, use_container_width=True, hide_index=True)

    st.subheader("⭐ Key Features")

    colA, colB = st.columns(2)

    with colA:
        st.markdown(
            """
            - Curated photoinitiator database  
            - UV absorption spectra  
            - Type I / Type II classification  
            - Application-focused search  
            - Structure-based comparison  
            """
        )

    with colB:
        st.markdown(
            """
            - RDKit-based molecular analysis  
            - Future similarity search  
            - Future E/L screening  
            - Public research reference  
            - Continuously updated database  
            """
        )

    st.subheader("⚠️ Disclaimer")

    st.info(
        "This platform is intended for research, education, and preliminary screening only. "
        "Results should not replace experimental validation, toxicological review, "
        "or regulatory assessment."
    )

    st.subheader("💬 Feedback")

    st.write(
        "Suggestions, bug reports, and collaboration ideas are welcome. "
        "Please leave feedback through [UVX Chem](https://uvxchem.com)."
    )


with tab_db:
    st.header("📚 Photoinitiator Database")
    st.info("Database tab will be added next.")

with tab_similarity:
    st.header("🔍 Similar Structure Search")
    st.info("Similarity search will be added after the database is stable.")

with tab_el:
    st.header("🧪 E/L Screening")
    st.info("E/L screening module will be added later.")