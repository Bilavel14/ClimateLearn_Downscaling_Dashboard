# ============================
# Climate Dashboard App (Phase 1)
# Filename: app.py or main.py
# ============================

# ---------- 1. LIBRARIES ----------
import streamlit as st                           # For dashboard UI
import random                                    # For background image switching
import base64                                    # For embedding images in CSS
import os                                        # For file path management

# ---------- 2. PAGE SETUP ----------
st.set_page_config(
    page_title="ClimateLearn | Downscaling Dashboard",
    layout="wide"
)

# ---------- 3. BACKGROUND IMAGE LOGIC ----------
image_folder = "C:/City Survey/images"            # <- CHANGE IF MOVED
image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]
selected_image = random.choice(image_files)
image_path = os.path.join(image_folder, selected_image)

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

base64_image = get_base64_of_image(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- 4. SIDEBAR NAVIGATION ----------
st.sidebar.title("🌐 ClimateLearn Navigation")
page = st.sidebar.radio("Go to:", [
    "About This Tool",
    "What is Downscaling?",
    "ERA5 and Data Sources",
    "Vulnerable Districts",
    "Climate Modeling Basics",
    "NetCDF Explained",
    "Coming Soon"
])

# ---------- 5. PAGE ROUTING ----------
if page == "About This Tool":
    st.title("🌍 Welcome to ClimateLearn")
    st.markdown("""
    This dashboard is designed for MSc/PhD students and educators to understand climate data downscaling
    with ERA5 precipitation data from 2010–2020. It provides interactive learning sections and maps that will be
    enhanced with analysis modules in future phases.
    """)

elif page == "What is Downscaling?":
    st.header("📏 What is Downscaling?")
    st.markdown("""
    Downscaling refers to methods used to refine climate data from coarse global or reanalysis scales down to
    regional or local scales. It can be statistical or dynamical. Key reasons include:
    - Improving local weather and climate predictions
    - Supporting disaster planning and policy
    - Making maps and models more relevant to specific regions
    """)

elif page == "ERA5 and Data Sources":
    st.header("📡 ERA5 and Climate Data")
    st.markdown("""
    ERA5 is the fifth-generation reanalysis dataset from ECMWF. It offers global hourly data at 31 km resolution.
    For this dashboard, we use **monthly total precipitation** (variable: `tp`) over **Northern Pakistan (2010–2020)**.
    
    The data is freely available through the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/).
    """)

elif page == "Vulnerable Districts":
    st.header("⚠️ Vulnerable Districts of Northern Pakistan")
    st.markdown("""
    We focus on 5 high-risk districts due to tourism and exposure to floods, snowmelt, and heavy rainfall:

    1. **Gilgit** – Glacial lake outburst floods
    2. **Skardu** – High snowfall and weather variability
    3. **Hunza** – Landslides and narrow valleys
    4. **Chitral** – Cloudbursts and flash floods
    5. **Neelum Valley** – Monsoon impact and isolation
    
    Each will be studied further in future analysis modules.
    """)

elif page == "Climate Modeling Basics":
    st.header("📘 Basics of Climate Modeling")
    st.markdown("""
    Climate models simulate the Earth’s atmosphere, land, ocean, and ice systems. They help in:
    - Forecasting future weather and climate
    - Understanding interactions between systems
    - Evaluating mitigation strategies

    Models are either **global** (GCMs) or **regional** (RCMs). Downscaling helps refine outputs from GCMs.
    """)

elif page == "NetCDF Explained":
    st.header("📦 Understanding NetCDF Files")
    st.markdown("""
    NetCDF (Network Common Data Form) is a format for storing multi-dimensional climate and geospatial data.
    A typical NetCDF file contains:
    - Variables (e.g., temperature, precipitation)
    - Dimensions (time, latitude, longitude)
    - Metadata (units, source, time range)

    Python libraries like `xarray` and `netCDF4` allow easy reading and visualization.
    """)

elif page == "Coming Soon":
    st.header("🚧 Coming Soon")
    st.markdown("""
    This section will include:
    - Interactive analysis of ERA5 data
    - District-level rainfall maps
    - Time series visualizations
    - Exportable charts

    All features will be part of **Phase 2**, once data processing is integrated.
    """)
