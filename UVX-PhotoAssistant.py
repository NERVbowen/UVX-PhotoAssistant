import streamlit as st
import pandas as pd
import os

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
        st.metric("Photoinitiators", "68")

    with col2:
        st.metric("UV Spectra", "47")

    with col3:
        st.metric("Chemical Structures", "In progress")

    # with col4:
    #     st.metric("AI Tools", "Beta")

    st.markdown("---")

    st.subheader("🔬 What is UVX Photochemistry?")

    st.write(
        "UVX Photochemistry is an open-access platform for researchers and engineers "
        "working with photoinitiators, photopolymerization, UV/LED curing, "
        "photoactive materials."
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
    import os

    st.header("📚 Photoinitiator Database")
    st.markdown("---")

    st.subheader("📖 Data Sources & Disclaimer")

    st.info("""
    UVX PhotoAssistant is an independent open-source research project created to support the photochemistry community.

    This database compiles and summarizes publicly available information from multiple sources, including supplier technical literature, PubChem (NCBI), EuPIA guidance documents, manufacturer technical data sheets, and peer-reviewed scientific literature.

    Chemical identifiers and molecular properties are verified whenever possible using multiple public sources.

    Original UV absorption spectra, product literature, trademarks, product names, and other copyrighted materials remain the property of their respective copyright holders. No affiliation with or endorsement by any manufacturer, supplier, or organization is implied.

    This database is intended for research and educational purposes only. Users should consult the original literature and manufacturer documentation for authoritative chemical, regulatory, and safety information.
    """)

    st.subheader("📚 References")

    st.markdown("""
    1. **Sigma-Aldrich.** *Photoinitiators Selection Guide.* Sigma-Aldrich / Merck technical literature.

    2. **EuPIA.** *EuPIA Suitability List of Photoinitiators and Photosynergists for Food Contact Materials.* Update January 2026.

    3. **PubChem.** National Center for Biotechnology Information (NCBI).  
       https://pubchem.ncbi.nlm.nih.gov/

    4. Manufacturer technical data sheets and publicly available scientific literature.
    """)

    df = pd.read_csv("data/photoinitiators.csv")

    st.caption(f"{len(df)} compounds loaded from the UVX photoinitiator database.")

    col1, col2 = st.columns([1, 2])

    with col1:
        keyword = st.text_input("Search", placeholder="Name, CAS, formula, SMILES")

        type_filter = st.multiselect(
            "Type",
            sorted(df["photoinitiator_type"].dropna().unique())
            if "photoinitiator_type" in df.columns else []
        )

        class_filter = st.multiselect(
            "Class",
            sorted(df["chemical_class"].dropna().unique())
            if "chemical_class" in df.columns else []
        )

    df_show = df.copy()

    if keyword:
        mask = False
        for col in ["name", "cas", "formula", "smiles"]:
            if col in df_show.columns:
                mask = mask | df_show[col].astype(str).str.contains(
                    keyword, case=False, na=False
                )
        df_show = df_show[mask]

    if type_filter and "photoinitiator_type" in df_show.columns:
        df_show = df_show[df_show["photoinitiator_type"].isin(type_filter)]

    if class_filter and "chemical_class" in df_show.columns:
        df_show = df_show[df_show["chemical_class"].isin(class_filter)]

    with col2:
        st.write(f"**Results: {len(df_show)} compounds**")

        show_cols = [
            c for c in [
                "name",
                "cas",
                "formula",
                "molecular_weight",
                "photoinitiator_type",
                "chemical_class"
            ]
            if c in df_show.columns
        ]

        st.dataframe(
            df_show[show_cols],
            use_container_width=True,
            hide_index=True
        )

    if len(df_show) > 0:
        st.markdown("---")

        selected_name = st.selectbox(
            "Select a photoinitiator",
            df_show["name"].astype(str).tolist()
        )

        row = df_show[df_show["name"].astype(str) == selected_name].iloc[0]

        st.subheader(f"🔬 {row['name']}")

        c1, c2 = st.columns([1, 2])

        with c1:
            st.markdown("### Basic Information")
            st.write(f"**Product No:** {row.get('product_no', '')}")
            st.write(f"**Purity:** {row.get('purity', '')}")
            st.write(f"**CAS:** {row.get('cas', '')}")
            st.write(f"**CAS Status:** {row.get('cas_status', '')}")
            st.write(f"**Formula:** {row.get('formula', '')}")
            st.write(f"**Molecular Weight:** {row.get('molecular_weight', '')}")
            st.write(f"**Exact Mass:** {row.get('exact_mass', '')}")
            st.write(f"**Type:** {row.get('photoinitiator_type', '')}")
            st.write(f"**Class:** {row.get('chemical_class', '')}")
            st.write(f"**Source PDF Page:** {row.get('source_pdf_page', '')}")

        with c2:
            st.markdown("### SMILES")
            smiles = str(row.get("smiles", "")).strip()
            if smiles and smiles.lower() != "nan":
                st.code(smiles)
            else:
                st.info("SMILES not available or needs verification.")

        st.markdown("### 🌈 UV Absorption Spectrum")

        image_file = str(row.get("spectrum_image", "")).strip()
        image_path = os.path.join("spectra_images_full", image_file)

        if image_path and image_path.lower() != "nan":
            if os.path.exists(image_path):
                st.image(
                    image_path,
                    caption="UV Absorption Spectrum",
                    use_container_width=True
                )
            else:
                st.warning("No experimental UV absorption spectrum is currently available for this compound. "
                           "The database is continuously being updated.")

                st.markdown("""
                **You can estimate the UV absorption using the UV Predictor in LCMS Assistant.**

                1. Copy the SMILES shown above.
                2. Open **LCMS Assistant → 🌈 UV Predictor**.
                3. Paste the SMILES to predict:
                """)

                st.link_button(
                    "Visit UVX Chem",
                    "https://www.uvxchem.com/"
                )
        else:
            st.warning(    "No experimental UV absorption spectrum is currently available for this compound. "
                            "The database is continuously being updated.")

            st.markdown("""
            **You can estimate the UV absorption using the UV Predictor in LCMS Assistant.**

            1. Copy the SMILES shown above.
            2. Open **LCMS Assistant → 🌈 UV Predictor**.
            3. Paste the SMILES to predict:
            """)

            st.link_button(
                "Visit UVX Chem",
                "https://www.uvxchem.com/"
            )

with tab_similarity:
    st.header("🔍 Similar Structure Search")
    st.info("Similarity search will be added after the database is stable.")

with tab_el:
    st.header("🧪 E/L Screening")
    st.info("E/L screening module will be added later.")

st.caption("UVX PhotoAssistant v0.1 | Developed by Bowen Wang")