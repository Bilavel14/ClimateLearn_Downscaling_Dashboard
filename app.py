# ============================
# Climate Dashboard App (Phase 1)
# Filename: app.py or main.py
# ============================

# ---------- 1. LIBRARIES ----------
import streamlit as st                           # 1 - For dashboard UI
import random                                    # 2 - For background image switching
import base64                                    # 3 - For embedding images in CSS
import os                                        # 4 - For file path management

# ---------- 2. PAGE SETUP ----------
st.set_page_config(                              # 6
    page_title="ClimateLearn | Downscaling Dashboard",  # 7
    layout="wide"                                # 8
)                                                # 9

# ---------- 3. BACKGROUND IMAGE LOGIC ----------
current_dir = os.path.dirname(os.path.abspath(__file__))       # 11
image_folder = os.path.join(current_dir, "images")             # 12

if os.path.exists(image_folder):                               # 14
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]  # 15
    if image_files:                                            # 16
        selected_image = random.choice(image_files)            # 17
        image_path = os.path.join(image_folder, selected_image)  # 18

        def get_base64_of_image(image_path):                   # 20
            with open(image_path, "rb") as img_file:           # 21
                return base64.b64encode(img_file.read()).decode()  # 22

        base64_image = get_base64_of_image(image_path)         # 24
    else:                                                      # 25
        st.warning("No PNG images found in the 'images' folder.")  # 26
        base64_image = None                                    # 27
else:                                                          # 28
    st.error("The 'images' folder was not found.")             # 29
    base64_image = None                                        # 30

st.markdown(                                                   # 32
    f"""                                                       # 33
    <style>                                                    # 34
    .stApp {{                                                  # 35
        background-image: url("data:image/png;base64,{base64_image}");  # 36
        background-size: cover;                                # 37
        background-position: center;                           # 38
        background-attachment: fixed;                          # 39
    }}                                                         # 40
    </style>                                                   # 41
    """,                                                       # 42
    unsafe_allow_html=True                                     # 43
)                                                              # 44

# ---------- 4. SIDEBAR NAVIGATION ----------
st.sidebar.title("🌐 ClimateLearn Navigation")                 # 46
page = st.sidebar.radio("Go to:", [                            # 47
    "About This Tool",                                         # 48
    "What is Downscaling?",                                    # 49
    "ERA5 and Data Sources",                                   # 50
    "Vulnerable Districts",                                    # 51
    "Climate Modeling Basics",                                 # 52
    "NetCDF Explained",                                        # 53
    "Coming Soon"                                              # 54
])                                                             # 55

# ---------- 5. PAGE ROUTING ----------
if page == "About This Tool":                                  # 57
    st.title("🌍 Welcome to ClimateLearn")                     # 58
    st.markdown("""                                            # 59
    This dashboard is designed for MSc/PhD students and educators to understand climate data downscaling
    with ERA5 precipitation data from 2010–2020. It provides interactive learning sections and maps that will be
    enhanced with analysis modules in future phases.
    """)                                                       # 63

elif page == "What is Downscaling?":                           # 65
    st.header("📏 What is Downscaling?")                       # 66
    st.markdown("""                                            # 67
    Downscaling refers to methods used to refine climate data from coarse global or reanalysis scales down to
    regional or local scales. It can be statistical or dynamical. Key reasons include:
    - Improving local weather and climate predictions
    - Supporting disaster planning and policy
    - Making maps and models more relevant to specific regions
    """)                                                       # 73

elif page == "ERA5 and Data Sources":                          # 75
    st.header("📡 ERA5 and Climate Data")                      # 76
    st.markdown("""                                            # 77
    ERA5 is the fifth-generation reanalysis dataset from ECMWF. It offers global hourly data at 31 km resolution.
    For this dashboard, we use **monthly total precipitation** (variable: `tp`) over **Northern Pakistan (2010–2020)**.
    
    The data is freely available through the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/).
    """)                                                       # 83

elif page == "Vulnerable Districts":                           # 85
    st.header("⚠️ Vulnerable Districts of Northern Pakistan")  # 86
    st.markdown("""                                            # 87
    We focus on 5 high-risk districts due to tourism and exposure to floods, snowmelt, and heavy rainfall:

    1. **Gilgit** – Glacial lake outburst floods
    2. **Skardu** – High snowfall and weather variability
    3. **Hunza** – Landslides and narrow valleys
    4. **Chitral** – Cloudbursts and flash floods
    5. **Neelum Valley** – Monsoon impact and isolation
    
    Each will be studied further in future analysis modules.
    """)                                                       # 95

elif page == "Climate Modeling Basics":                        # 97
    st.header("📘 Basics of Climate Modeling")                 # 98
    st.markdown("""                                            # 99
    Climate models simulate the Earth’s atmosphere, land, ocean, and ice systems. They help in:
    - Forecasting future weather and climate
    - Understanding interactions between systems
    - Evaluating mitigation strategies

    Models are either **global** (GCMs) or **regional** (RCMs). Downscaling helps refine outputs from GCMs.
    """)                                                       # 106

elif page == "NetCDF Explained":                               # 108
    st.header("📦 Understanding NetCDF Files")                 # 109
    st.markdown("""                                            # 110
    NetCDF (Network Common Data Form) is a format for storing multi-dimensional climate and geospatial data.
    A typical NetCDF file contains:
    - Variables (e.g., temperature, precipitation)
    - Dimensions (time, latitude, longitude)
    - Metadata (units, source, time range)

    Python libraries like `xarray` and `netCDF4` allow easy reading and visualization.
    """)                                                       # 118

elif page == "Coming Soon":                                    # 120
    st.header("🚧 Coming Soon")                                # 121
    st.markdown("""                                            # 122
    This section will include:
    - Interactive analysis of ERA5 data
    - District-level rainfall maps
    - Time series visualizations
    - Exportable charts

    All features will be part of **Phase 2**, once data processing is integrated.
    """)                                                       # 129
