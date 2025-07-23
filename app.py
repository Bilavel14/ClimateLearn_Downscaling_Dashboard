# ============================
# Climate Dashboard App (Phase 1)
# Filename: app.py or main.py
# ============================

# ---------- 1. LIBRARIES ----------
import streamlit as st                           # 1 - For dashboard UI

# ---------- 2. PAGE SETUP ----------
st.set_page_config(                              # 6
    page_title="ClimateLearn | Downscaling Dashboard",  # 7
    layout="wide"                                # 8
)                                                # 9

# ---------- 3. SIDEBAR NAVIGATION ----------
st.sidebar.title("🌐 ClimateLearn Navigation")                 # 10
page = st.sidebar.radio("Go to:", [                            # 11
    "About This Tool",                                         # 12
    "What is Downscaling?",                                    # 13
    "ERA5 and Data Sources",                                   # 14
    "Vulnerable Districts",                                    # 15
    "Climate Modeling Basics",                                 # 16
    "NetCDF Explained",                                        # 17
    "Coming Soon"                                              # 18
])                                                             # 19

# ---------- 4. PAGE ROUTING ----------
if page == "About This Tool":                                  # 20
    st.title("🌍 Welcome to ClimateLearn")                     # 21
    st.markdown("""
    This dashboard is designed for MSc/PhD students and educators to understand climate data downscaling
    with ERA5 precipitation data from 2010–2020. It provides interactive learning sections and maps that will be
    enhanced with analysis modules in future phases.
    """)

elif page == "What is Downscaling?":                           # 22
    st.header("📏 What is Downscaling?")                       # 23
    st.markdown("""
    Downscaling refers to methods used to refine climate data from coarse global or reanalysis scales down to
    regional or local scales. It can be statistical or dynamical. Key reasons include:
    - Improving local weather and climate predictions
    - Supporting disaster planning and policy
    - Making maps and models more relevant to specific regions
    """)

elif page == "ERA5 and Data Sources":                          # 24
    st.header("📡 ERA5 and Climate Data")                      # 25
    st.markdown("""
    ERA5 is the fifth-generation reanalysis dataset from ECMWF. It offers global hourly data at 31 km resolution.
    For this dashboard, we use **monthly total precipitation** (variable: `tp`) over **Northern Pakistan (2010–2020)**.

    The data is freely available through the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/).
    """)

elif page == "Vulnerable Districts":                           # 26
    st.header("⚠️ Vulnerable Districts of Northern Pakistan")  # 27
    st.markdown("""
    We focus on 5 high-risk districts due to tourism and exposure to floods, snowmelt, and heavy rainfall:

    1. **Gilgit** – Glacial lake outburst floods
    2. **Skardu** – High snowfall and weather variability
    3. **Hunza** – Landslides and narrow valleys
    4. **Chitral** – Cloudbursts and flash floods
    5. **Neelum Valley** – Monsoon impact and isolation

    Each will be studied further in future analysis modules.
    """)

elif page == "Climate Modeling Basics":                        # 28
    st.header("📘 Basics of Climate Modeling")                 # 29
    st.markdown("""
    Climate models simulate the Earth’s atmosphere, land, ocean, and ice systems. They help in:
    - Forecasting future weather and climate
    - Understanding interactions between systems
    - Evaluating mitigation strategies

    Models are either **global** (GCMs) or **regional** (RCMs). Downscaling helps refine outputs from GCMs.
    """)

elif page == "NetCDF Explained":                               # 30
    st.header("📦 Understanding NetCDF Files")                 # 31
    st.markdown("""
    NetCDF (Network Common Data Form) is a format for storing multi-dimensional climate and geospatial data.
    A typical NetCDF file contains:
    - Variables (e.g., temperature, precipitation)
    - Dimensions (time, latitude, longitude)
    - Metadata (units, source, time range)

    Python libraries like `xarray` and `netCDF4` allow easy reading and visualization.
    """)

elif page == "Coming Soon":                                    # 32
    st.header("🚧 Coming Soon")                                # 33
    st.markdown("""
    This section will include:
    - Interactive analysis of ERA5 data
    - District-level rainfall maps
    - Time series visualizations
    - Exportable charts

    All features will be part of **Phase 2**, once data processing is integrated.
    """)
