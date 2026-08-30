import streamlit as st
from datetime import date, time
import pandas as pd

from sunflow_engine import analyze_destination


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SunFlow AI",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# REAL TRAVEL PHOTO
# ============================================================

HERO_IMAGE = (
    "https://images.unsplash.com/"
    "photo-1500534623283-312aade485b7"
    "?auto=format&fit=crop&w=1800&q=85"
)


# ============================================================
# CSS
# ============================================================

st.html("""
<style>

html, body, [class*="css"] {
    font-family: Inter, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top right, #123d32 0%, transparent 30%),
        #061612;
    color: white;
}

.block-container {
    max-width: 1450px;
    padding-top: 1rem;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #04110d;
    border-right: 1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] * {
    color: #dcefe7;
}


/* HERO */

.hero {
    min-height: 480px;
    border-radius: 28px;
    overflow: hidden;
    position: relative;

    background-image:
        linear-gradient(
            90deg,
            rgba(2,15,11,.92) 0%,
            rgba(2,15,11,.70) 38%,
            rgba(2,15,11,.18) 100%
        ),
        url("HERO_IMAGE");

    background-size: cover;
    background-position: center;

    padding: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;

    box-shadow: 0 20px 60px rgba(0,0,0,.35);
}

.brand {
    font-size: 48px;
    font-weight: 900;
    letter-spacing: -2px;
}

.green {
    color: #54e38e;
}

.tagline {
    font-size: 20px;
    color: #d5e9df;
    margin-top: 8px;
}

.hero-small {
    margin-top: 25px;
    color: #a9c8ba;
    font-size: 14px;
}

.connected {
    display: inline-block;
    margin-top: 20px;
    padding: 8px 14px;
    border-radius: 30px;
    background: rgba(42,211,112,.15);
    border: 1px solid rgba(42,211,112,.35);
    color: #6af29b;
    font-weight: 700;
}


/* GLASS CARDS */

.glass {
    background: rgba(10,32,26,.82);
    border: 1px solid rgba(255,255,255,.09);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 12px 35px rgba(0,0,0,.20);
    backdrop-filter: blur(12px);
}

.metric-label {
    color: #9ebbb0;
    font-size: 13px;
    font-weight: 600;
}

.metric-value {
    color: white;
    font-size: 28px;
    font-weight: 800;
    margin-top: 7px;
}

.section {
    font-size: 25px;
    font-weight: 800;
    margin: 28px 0 14px 0;
}


/* RISK */

.risk-high {
    background: linear-gradient(
        135deg,
        rgba(127,29,29,.45),
        rgba(10,32,26,.9)
    );

    border: 1px solid rgba(248,113,113,.25);
    border-radius: 20px;
    padding: 24px;
}

.risk-value {
    font-size: 38px;
    font-weight: 900;
    color: #fb7185;
}


/* SOLAR */

.solar-card {
    background: linear-gradient(
        135deg,
        rgba(120,90,0,.30),
        rgba(10,32,26,.9)
    );

    border: 1px solid rgba(250,204,21,.22);
    border-radius: 20px;
    padding: 24px;
}


/* WATER */

.water-card {
    background: linear-gradient(
        135deg,
        rgba(3,105,161,.25),
        rgba(10,32,26,.9)
    );

    border: 1px solid rgba(56,189,248,.20);
    border-radius: 20px;
    padding: 24px;
}


/* AI */

.ai-card {
    background: linear-gradient(
        135deg,
        rgba(91,33,182,.25),
        rgba(10,32,26,.9)
    );

    border: 1px solid rgba(167,139,250,.20);
    border-radius: 20px;
    padding: 24px;
}


/* FOOTER */

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 25px;
    color: #6f8d80;
    border-top: 1px solid rgba(255,255,255,.08);
}

</style>
""")


# Replace placeholder inside CSS with image URL
st.html(
    f"""
    <style>
    .hero {{
        background-image:
        linear-gradient(
            90deg,
            rgba(2,15,11,.92) 0%,
            rgba(2,15,11,.70) 38%,
            rgba(2,15,11,.18) 100%
        ),
        url("{HERO_IMAGE}");
    }}
    </style>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div style="
        font-size:25px;
        font-weight:900;
        margin:15px 0 30px 5px;
    ">
        ☀️ SunFlow <span style="color:#54e38e;">AI</span>
    </div>
    """)

    st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🗺️ Map Explorer",
            "🌡️ Climate Analysis",
            "💧 Water Planner",
            "🤖 AI Insights",
            "🕘 History"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.html("""
    <div class="glass">

        <div style="font-weight:800;">
            FortyGuard
        </div>

        <div style="
            color:#54e38e;
            margin-top:7px;
            font-size:13px;
            font-weight:700;
        ">
            ● CONNECTED
        </div>

    </div>
    """)


# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div style="
        font-size:14px;
        color:#68e69b;
        font-weight:800;
        letter-spacing:2px;
    ">
        CLIMATE INTELLIGENCE PLATFORM
    </div>

    <div class="brand">
        SunFlow <span class="green">AI</span>
    </div>

    <div class="tagline">
        Climate-Aware Travel & Clean Water Intelligence
    </div>

    <div class="hero-small">
        Transforming environmental data into smarter,
        safer and more sustainable travel decisions.
    </div>

    <div>
        <span class="connected">
            ● FortyGuard API Connected
        </span>
    </div>

</div>
""")


# ============================================================
# SEARCH
# ============================================================

st.html("""
<div class="section">
    🌍 Explore a Destination
</div>
""")

search_col, button_col = st.columns([5, 1])

with search_col:

    destination = st.text_input(
        "Destination",
        placeholder="Search any destination — e.g. New York, California, Switzerland",
        label_visibility="collapsed"
    )

with button_col:

    analyze = st.button(
        "✨ ANALYZE",
        type="primary",
        use_container_width=True
    )


# ============================================================
# PARAMETERS
# ============================================================

with st.expander("⚙️ Advanced Environmental Parameters"):

    p1, p2, p3 = st.columns(3)

    with p1:

        temperature = st.number_input(
            "Temperature (°C)",
            value=32.5,
            step=0.1
        )

    with p2:

        selected_date = st.date_input(
            "Analysis Date",
            value=date(2026, 8, 19)
        )

    with p3:

        selected_time = st.time_input(
            "Analysis Time",
            value=time(14, 0)
        )


# ============================================================
# RUN ENGINE
# ============================================================

if analyze:

    if not destination.strip():

        st.warning("Enter a destination first.")

    else:

        with st.status(
            "Running SunFlow climate intelligence...",
            expanded=True
        ):

            st.write("📍 Locating destination...")

            try:

                st.write("🌡️ Requesting FortyGuard environmental data...")

                result = analyze_destination(
                    destination,
                    temperature,
                    selected_date.strftime("%Y-%m-%d"),
                    selected_time.strftime("%H:%M")
                )

                st.write("🤖 Processing SunFlow analysis...")

                st.session_state["result"] = result
                st.session_state["destination"] = destination

                st.write("✅ Analysis completed.")

            except Exception as e:

                st.error("Analysis failed.")
                st.exception(e)


# ============================================================
# RESULTS
# ============================================================

if "result" in st.session_state:

    result = st.session_state["result"]

    environment = result["environment"]
    analysis = result["analysis"]

    destination_name = st.session_state["destination"]


    # ========================================================
    # LOCATION
    # ========================================================

    st.html("""
    <div class="section">
        📍 Destination Intelligence
    </div>
    """)

    st.html(
        f"""
        <div class="glass">

            <div style="
                color:#8ba89c;
                font-size:12px;
                font-weight:800;
            ">
                CURRENT DESTINATION
            </div>

            <div style="
                font-size:30px;
                font-weight:900;
                margin-top:5px;
            ">
                📍 {destination_name}
            </div>

            <div style="
                color:#8ba89c;
                margin-top:8px;
            ">
                Latitude: {environment["latitude"]:.5f}
                &nbsp; • &nbsp;
                Longitude: {environment["longitude"]:.5f}
                &nbsp; • &nbsp;
                Elevation: {environment["elevation"]:.1f} m
            </div>

        </div>
        """
    )


    # ========================================================
    # METRICS
    # ========================================================

    st.html("""
    <div class="section">
        🌡️ Environmental Conditions
    </div>
    """)

    m1, m2, m3, m4 = st.columns(4)

    metrics = [
        ("🌡️", "Temperature",
         f'{environment["temperature"]:.1f}°C'),

        ("🔥", "Heat Index",
         f'{environment["heat_index"]:.1f}°C'),

        ("💧", "Humidity",
         f'{environment["humidity"]:.1f}%'),

        ("🌧️", "Precipitation",
         f'{environment["precipitation"]:.1f} mm')
    ]

    for column, (icon, label, value) in zip(
        [m1, m2, m3, m4],
        metrics
    ):

        with column:

            st.html(
                f"""
                <div class="glass">

                    <div class="metric-label">
                        {icon} {label}
                    </div>

                    <div class="metric-value">
                        {value}
                    </div>

                </div>
                """
            )


    # ========================================================
    # ANALYSIS
    # ========================================================

    st.html("""
    <div class="section">
        🧠 SunFlow Intelligence
    </div>
    """)

    r1, r2 = st.columns(2)

    with r1:

        st.html(
            f"""
            <div class="risk-high">

                <div style="
                    color:#fda4af;
                    font-weight:800;
                ">
                    🔥 HEAT RISK
                </div>

                <div class="risk-value">
                    {analysis["heat_risk"]}
                </div>

                <div style="
                    color:#aebfb8;
                    margin-top:7px;
                ">
                    Environmental heat assessment
                </div>

            </div>
            """
        )

    with r2:

        st.html(
            f"""
            <div class="solar-card">

                <div style="
                    color:#fde68a;
                    font-weight:800;
                ">
                    ☀️ SOLAR AVAILABILITY
                </div>

                <div style="
                    color:#facc15;
                    font-size:38px;
                    font-weight:900;
                    margin-top:5px;
                ">
                    {analysis["solar_availability"]}
                </div>

                <div style="
                    color:#aebfb8;
                    margin-top:7px;
                ">
                    Derived from FortyGuard irradiance data
                </div>

            </div>
            """
        )


    # ========================================================
    # MAP
    # ========================================================

    st.html("""
    <div class="section">
        🗺️ Live Destination Map
    </div>
    """)

    map_df = pd.DataFrame(
        {
            "latitude": [environment["latitude"]],
            "longitude": [environment["longitude"]]
        }
    )

    st.map(map_df)


    # ========================================================
    # SOLAR
    # ========================================================

    st.html("""
    <div class="section">
        ☀️ Solar Intelligence
    </div>
    """)

    solar_df = pd.DataFrame(
        {
            "Irradiance": [
                environment["ghi"],
                environment["dni"],
                environment["dhi"]
            ]
        },
        index=["GHI", "DNI", "DHI"]
    )

    st.bar_chart(solar_df)

    s1, s2, s3 = st.columns(3)

    for col, label, value in [
        (s1, "GHI", environment["ghi"]),
        (s2, "DNI", environment["dni"]),
        (s3, "DHI", environment["dhi"])
    ]:

        with col:

            st.html(
                f"""
                <div class="glass">

                    <div class="metric-label">
                        ☀️ {label}
                    </div>

                    <div class="metric-value">
                        {value:.1f}
                    </div>

                    <div style="
                        color:#8ba89c;
                        font-size:12px;
                    ">
                        W/m²
                    </div>

                </div>
                """
            )


    # ========================================================
    # WATER + AI
    # ========================================================

    st.html("""
    <div class="section">
        💧 Water Planning & AI Recommendations
    </div>
    """)

    w1, w2 = st.columns(2)


    with w1:

        if analysis["heat_risk"] in [
            "High",
            "Very High"
        ]:

            priority = "HIGH"

            message = (
                "Elevated heat conditions increase the "
                "importance of hydration and clean-water planning."
            )

        else:

            priority = "NORMAL"

            message = (
                "Current conditions indicate a comparatively "
                "manageable heat environment."
            )

        st.html(
            f"""
            <div class="water-card">

                <h3>💧 Water Planning Assistant</h3>

                <p style="color:#b5d7e8;">
                    {message}
                </p>

                <div style="
                    color:#7dd3fc;
                    font-size:12px;
                    font-weight:800;
                    margin-top:20px;
                ">
                    WATER PLANNING PRIORITY
                </div>

                <div style="
                    font-size:34px;
                    font-weight:900;
                    color:#38bdf8;
                ">
                    {priority}
                </div>

                <div style="
                    margin-top:15px;
                    color:#9cc6d8;
                ">
                    💧 Stay hydrated<br>
                    🧴 Carry safe drinking water<br>
                    🌱 Prefer sustainable water sources
                </div>

            </div>
            """
        )


    with w2:

        if analysis["heat_risk"] in [
            "High",
            "Very High"
        ]:

            advice = (
                "Heat conditions are elevated. "
                "Plan outdoor activities carefully and "
                "maintain adequate hydration."
            )

        else:

            advice = (
                "Current conditions are suitable for "
                "outdoor exploration with normal precautions."
            )

        if analysis["solar_availability"] == "Strong":

            solar_advice = (
                "Strong solar availability also creates "
                "potential for solar-powered activities "
                "and clean-water systems."
            )

        else:

            solar_advice = (
                "Solar availability should be considered "
                "when planning solar-dependent activities."
            )

        st.html(
            f"""
            <div class="ai-card">

                <h3>🤖 SunFlow AI Insight</h3>

                <p style="color:#c7b9e8;">
                    {advice}
                </p>

                <p style="color:#c7b9e8;">
                    {solar_advice}
                </p>

                <div style="
                    margin-top:20px;
                    color:#a78bfa;
                    font-weight:800;
                ">
                    FortyGuard Data
                    →
                    SunFlow Intelligence
                    →
                    Actionable Recommendation
                </div>

            </div>
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    ☀️ <b>SunFlow AI</b>

    <br><br>

    Climate Intelligence • Clean Water • Sustainable Travel

    <br>

    Powered by FortyGuard Environmental Intelligence

</div>
""")