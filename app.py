"""
TRIP.SA - Smart Tourism Recommendation System for Saudi Arabia
Premium Redesign - Modern Dark Theme with Gold Accents
Master's Thesis Project
"""
import streamlit as st
import pandas as pd
import math
import os
from datetime import datetime, timedelta
import random
from PIL import Image
from restaurants_data import CITY_RESTAURANTS, get_restaurant_for_meal

try:
    from fpdf import FPDF
    import arabic_reshaper
    from bidi.algorithm import get_display
except ImportError:
    FPDF = None
    arabic_reshaper = None
    get_display = None

try:
    import folium
    from streamlit_folium import st_folium
    HAS_FOLIUM = True
except ImportError:
    HAS_FOLIUM = False

try:
    import pydeck as pdk
    HAS_PYDECK = True
except ImportError:
    HAS_PYDECK = False

# ============================================================
# Page Configuration
# ============================================================
_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon-192.png")
if os.path.exists(_icon_path):
    _app_icon = Image.open(_icon_path)
else:
    _app_icon = "🌍"

st.set_page_config(
    page_title="TRIP.SA - Smart Trip Planner",
    page_icon=_app_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PWA Support - Progressive Web App
# ============================================================
PWA_ICON_192 = "https://files.manuscdn.com/user_upload_by_module/session_file/310519663217221142/SscCIPVpbcKDJXBE.png"
PWA_ICON_512 = "https://files.manuscdn.com/user_upload_by_module/session_file/310519663217221142/ScMomDSukNazOkpe.png"
APPLE_ICON = "https://files.manuscdn.com/user_upload_by_module/session_file/310519663217221142/AWoGEWKckRMAgOrj.png"

st.markdown(f"""
<script>
    (function() {{
        function setFavicon() {{
            var links = document.querySelectorAll("link[rel*='icon']");
            links.forEach(function(link) {{ link.remove(); }});
            var link32 = document.createElement('link');
            link32.rel = 'icon'; link32.type = 'image/png'; link32.sizes = '32x32';
            link32.href = '{PWA_ICON_192}'; document.head.appendChild(link32);
            var link192 = document.createElement('link');
            link192.rel = 'icon'; link192.type = 'image/png'; link192.sizes = '192x192';
            link192.href = '{PWA_ICON_192}'; document.head.appendChild(link192);
            var appleLink = document.createElement('link');
            appleLink.rel = 'apple-touch-icon'; appleLink.href = '{APPLE_ICON}';
            document.head.appendChild(appleLink);
            var manifestData = {{
                name: 'TRIP.SA - Smart Trip Planner', short_name: 'TRIP.SA',
                description: 'Smart Tourism Recommendation System for Saudi Arabia',
                start_url: '.', display: 'standalone',
                background_color: '#0B1A0F', theme_color: '#0B1A0F',
                orientation: 'portrait',
                icons: [
                    {{ src: '{PWA_ICON_192}', sizes: '192x192', type: 'image/png' }},
                    {{ src: '{PWA_ICON_512}', sizes: '512x512', type: 'image/png' }}
                ]
            }};
            var manifestBlob = new Blob([JSON.stringify(manifestData)], {{type: 'application/json'}});
            var manifestUrl = URL.createObjectURL(manifestBlob);
            var manifestLink = document.createElement('link');
            manifestLink.rel = 'manifest'; manifestLink.href = manifestUrl;
            document.head.appendChild(manifestLink);
            var themeColor = document.createElement('meta');
            themeColor.name = 'theme-color'; themeColor.content = '#0B1A0F';
            document.head.appendChild(themeColor);
            var appleMeta1 = document.createElement('meta');
            appleMeta1.name = 'apple-mobile-web-app-capable'; appleMeta1.content = 'yes';
            document.head.appendChild(appleMeta1);
            var appleMeta2 = document.createElement('meta');
            appleMeta2.name = 'apple-mobile-web-app-status-bar-style'; appleMeta2.content = 'black-translucent';
            document.head.appendChild(appleMeta2);
        }}
        setFavicon();
        setTimeout(setFavicon, 500);
        setTimeout(setFavicon, 2000);
        setTimeout(setFavicon, 5000);
        var observer = new MutationObserver(function(mutations) {{
            var needsUpdate = mutations.some(function(m) {{
                return Array.from(m.addedNodes).some(function(n) {{
                    return n.tagName === 'LINK' && n.rel && n.rel.includes('icon') && !n.href.includes('manuscdn');
                }});
            }});
            if (needsUpdate) setFavicon();
        }});
        observer.observe(document.head, {{ childList: true }});
    }})();
</script>
""", unsafe_allow_html=True)

# ============================================================
# Premium CSS Design - TRIP.SA Dark Luxury Theme
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

    * { font-family: 'Inter', sans-serif; }

    /* ---- Global Dark Theme ---- */
    html, body, [class*="css"] { background: #0B1A0F !important; color: #E8E8E8 !important; }
    .main .block-container { background: #0B1A0F !important; }
    .stApp { background: #0B1A0F !important; }

    /* ---- Hide Streamlit defaults ---- */
    #MainMenu, footer, header { visibility: hidden; }

    /* ---- Scrollbar ---- */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0B1A0F; }
    ::-webkit-scrollbar-thumb { background: #C5A43B; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #D4AF37; }

    /* ---- Sidebar - Deep Forest ---- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #071208 0%, #0D2818 40%, #14532D 100%) !important;
        border-right: 1px solid rgba(197, 164, 59, 0.2) !important;
    }
    section[data-testid="stSidebar"] * { color: #D1D5DB !important; }
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stMultiSelect label,
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] .stSlider label {
        color: #C5A43B !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
    }

    /* ---- Sidebar Dropdowns ---- */
    section[data-testid="stSidebar"] .stSelectbox > div > div,
    section[data-testid="stSidebar"] .stMultiSelect > div > div {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(197, 164, 59, 0.3) !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px) !important;
    }
    section[data-testid="stSidebar"] .stSelectbox > div > div *,
    section[data-testid="stSidebar"] .stMultiSelect > div > div > div {
        color: #E8E8E8 !important;
    }
    section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] span,
    section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] div {
        color: #C5A43B !important;
        font-weight: 500 !important;
    }
    section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {
        background-color: rgba(197, 164, 59, 0.15) !important;
        border: 1px solid #C5A43B !important;
        border-radius: 20px !important;
    }
    section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] span {
        color: #C5A43B !important;
        font-weight: 600 !important;
    }
    [data-baseweb="popover"] li,
    [data-baseweb="popover"] div[role="option"] {
        color: #E8E8E8 !important;
        background-color: #162B1E !important;
    }
    [data-baseweb="popover"] li:hover,
    [data-baseweb="popover"] div[role="option"]:hover {
        background-color: #1E3A2A !important;
    }
    [data-baseweb="popover"] { background-color: #162B1E !important; border: 1px solid rgba(197,164,59,0.3) !important; }
    section[data-testid="stSidebar"] hr {
        border-color: rgba(197, 164, 59, 0.15) !important;
    }

    /* ---- Hero Header - Glassmorphism Card ---- */
    .hero-card {
        background: linear-gradient(145deg, #0D2818 0%, #14532D 50%, #1B6B3A 100%);
        padding: 3rem 2.5rem;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 2.5rem;
        border: 1px solid rgba(197, 164, 59, 0.25);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255,255,255,0.05);
        position: relative;
        overflow: hidden;
    }
    .hero-card::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: radial-gradient(circle at 30% 30%, rgba(197,164,59,0.06) 0%, transparent 50%),
                    radial-gradient(circle at 70% 70%, rgba(34,197,94,0.04) 0%, transparent 50%);
        pointer-events: none;
        animation: shimmer 8s ease-in-out infinite alternate;
    }
    @keyframes shimmer {
        0% { transform: translate(0, 0); }
        100% { transform: translate(5%, 5%); }
    }
    .hero-card .logo-text {
        font-family: 'Playfair Display', serif;
        color: #C5A43B;
        font-size: 3.8rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 6px;
        text-shadow: 0 2px 20px rgba(197, 164, 59, 0.3);
        position: relative;
    }
    .hero-card .logo-dot {
        color: #22C55E;
        font-size: 4.2rem;
    }
    .hero-card .tagline {
        color: #A7F3D0;
        font-size: 1.1rem;
        font-weight: 400;
        margin-top: 0.8rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .hero-card .sub {
        color: rgba(255,255,255,0.4);
        font-size: 0.8rem;
        margin-top: 0.5rem;
        letter-spacing: 1px;
    }
    .hero-card .compass-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        display: block;
    }

    /* ---- Overview Grid (KPI Cards) ---- */
    .overview-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
        margin: 1.5rem 0 2rem;
    }
    .overview-card {
        background: linear-gradient(145deg, #111F16 0%, #162B1E 100%);
        border: 1px solid rgba(197, 164, 59, 0.15);
        border-radius: 16px;
        padding: 1.5rem 1rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .overview-card::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #C5A43B, #22C55E);
    }
    .overview-card:hover {
        transform: translateY(-4px);
        border-color: rgba(197, 164, 59, 0.4);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }
    .overview-card .icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
    .overview-card .value {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        font-weight: 700;
        color: #C5A43B;
        margin: 0.3rem 0;
    }
    .overview-card .label {
        font-size: 0.72rem;
        color: #9CA3AF;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* ---- Section Title ---- */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #C5A43B;
        padding-bottom: 0.8rem;
        margin: 2.5rem 0 1.5rem;
        position: relative;
        display: inline-block;
    }
    .section-title::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 60px; height: 3px;
        background: linear-gradient(90deg, #C5A43B, transparent);
        border-radius: 2px;
    }

    /* ---- Day Header ---- */
    .day-header {
        background: linear-gradient(90deg, #14532D 0%, #1B6B3A 60%, #22C55E 100%);
        color: white;
        padding: 1.1rem 1.8rem;
        border-radius: 16px 16px 0 0;
        font-size: 1.1rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        letter-spacing: 0.5px;
        border-bottom: 2px solid #C5A43B;
    }
    .day-body {
        background: #111F16;
        border-radius: 0 0 16px 16px;
        padding: 1.5rem;
        border: 1px solid rgba(197, 164, 59, 0.1);
        border-top: none;
        margin-bottom: 1.5rem;
    }

    /* ---- Activity Row ---- */
    .act-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem 1.2rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        background: rgba(255,255,255,0.03);
        border-left: 3px solid #22C55E;
        transition: all 0.3s ease;
    }
    .act-row:hover {
        background: rgba(34, 197, 94, 0.08);
        transform: translateX(6px);
        border-left-color: #C5A43B;
    }
    .act-time {
        min-width: 130px;
        font-weight: 700;
        color: #22C55E;
        font-size: 0.88rem;
        font-variant-numeric: tabular-nums;
    }
    .act-info { flex: 1; }
    .act-name { font-weight: 600; color: #E8E8E8; font-size: 0.95rem; }
    .act-cat { font-size: 0.76rem; color: #9CA3AF; margin-top: 3px; }
    .act-dur {
        font-size: 0.78rem;
        font-weight: 600;
        color: #C5A43B;
        background: rgba(197, 164, 59, 0.1);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        white-space: nowrap;
        border: 1px solid rgba(197, 164, 59, 0.25);
    }

    /* ---- Hotel Card ---- */
    .hotel-box {
        background: linear-gradient(135deg, rgba(197,164,59,0.08) 0%, rgba(197,164,59,0.03) 100%);
        border: 1px solid rgba(197, 164, 59, 0.25);
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin-top: 1rem;
        display: flex;
        align-items: center;
        gap: 1.2rem;
    }
    .hotel-icon { font-size: 2rem; }
    .hotel-info { flex: 1; }
    .hotel-name { font-weight: 700; color: #C5A43B; font-size: 1rem; }
    .hotel-meta { font-size: 0.83rem; color: #9CA3AF; margin-top: 0.2rem; }
    .hotel-badge {
        background: linear-gradient(135deg, #C5A43B, #A08930);
        color: #0B1A0F;
        font-weight: 700;
        padding: 0.4rem 0.9rem;
        border-radius: 10px;
        font-size: 0.9rem;
    }

    /* ---- Transport Banner ---- */
    .transport {
        background: linear-gradient(90deg, #071208 0%, #0D2818 100%);
        color: #D1D5DB;
        padding: 0.9rem 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        font-size: 0.88rem;
        font-weight: 500;
        border-left: 3px solid #C5A43B;
        border: 1px solid rgba(197, 164, 59, 0.15);
    }

    /* ---- Meal Break ---- */
    .meal-card {
        text-align: center;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border: 1px solid rgba(197, 164, 59, 0.2);
        border-radius: 12px;
        background: rgba(197, 164, 59, 0.05);
        color: #C5A43B;
        font-weight: 600;
        font-size: 0.88rem;
    }

    /* ---- Buttons ---- */
    .stButton > button {
        background: linear-gradient(135deg, #C5A43B 0%, #A08930 100%) !important;
        color: #0B1A0F !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 0.8rem 2rem !important;
        font-size: 1rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(197, 164, 59, 0.3) !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(197, 164, 59, 0.4) !important;
        background: linear-gradient(135deg, #D4B84A 0%, #B09A40 100%) !important;
    }

    /* ---- Map Section ---- */
    .map-section {
        background: #111F16;
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(197, 164, 59, 0.1);
        margin: 1.5rem 0;
    }

    /* ---- Expander ---- */
    .streamlit-expanderHeader {
        background: #111F16 !important;
        color: #C5A43B !important;
        border: 1px solid rgba(197, 164, 59, 0.15) !important;
        border-radius: 10px !important;
    }
    .streamlit-expanderContent {
        background: #0B1A0F !important;
        border: 1px solid rgba(197, 164, 59, 0.1) !important;
    }

    /* ---- Dataframe ---- */
    .stDataFrame { background: #111F16 !important; border-radius: 12px !important; }

    /* ---- Success/Info/Warning messages ---- */
    .stAlert { background: #111F16 !important; border-radius: 12px !important; }

    /* ---- Mobile Sidebar Hint Bar ---- */
    .mobile-sidebar-hint {
        display: flex; align-items: center; justify-content: center;
        background: linear-gradient(135deg, #14532D 0%, #1B6B3A 100%);
        border: 1px solid rgba(197, 164, 59, 0.4);
        border-radius: 12px;
        padding: 0.7rem 1.2rem;
        margin-bottom: 1rem;
        cursor: pointer;
        text-align: center;
        animation: pulse-hint 2s ease-in-out infinite;
        transition: all 0.3s ease;
    }
    .mobile-sidebar-hint:hover {
        background: linear-gradient(135deg, #1B6B3A 0%, #22C55E 100%);
        border-color: #C5A43B;
    }
    .mobile-sidebar-hint .hint-icon {
        font-size: 1.3rem;
        margin-right: 0.5rem;
    }
    .mobile-sidebar-hint .hint-text {
        color: #C5A43B;
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 0.5px;
    }
    .mobile-sidebar-hint .hint-arrow {
        color: #22C55E;
        font-size: 1.2rem;
        margin-left: 0.5rem;
        display: inline-block;
        animation: bounce-arrow 1.5s ease-in-out infinite;
    }
    @keyframes pulse-hint {
        0%, 100% { box-shadow: 0 0 5px rgba(197, 164, 59, 0.2); }
        50% { box-shadow: 0 0 15px rgba(197, 164, 59, 0.4); }
    }
    @keyframes bounce-arrow {
        0%, 100% { transform: translateX(0); }
        50% { transform: translateX(-5px); }
    }

    /* ---- PWA / Mobile Responsive ---- */
    @media (max-width: 768px) {
        .mobile-sidebar-hint { }
        .hero-card { padding: 2rem 1.2rem; border-radius: 16px; }
        .hero-card .logo-text { font-size: 2.5rem !important; letter-spacing: 3px; }
        .hero-card .tagline { font-size: 0.85rem !important; }
        .overview-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 0.8rem !important; }
        .overview-card { padding: 1rem !important; }
        .overview-card .value { font-size: 1.3rem !important; }
        .act-row { flex-wrap: wrap; gap: 0.5rem; padding: 0.8rem; }
        .act-time { min-width: 100%; font-size: 0.82rem; }
        .act-dur { margin-left: auto; }
        .hotel-box { flex-wrap: wrap; padding: 1rem; }
        .transport { flex-wrap: wrap; font-size: 0.82rem; padding: 0.7rem 1rem; }
        .section-title { font-size: 1.2rem; }
        .day-header { font-size: 1rem; padding: 0.8rem 1.2rem; }
        .day-body { padding: 1rem; }
        .meal-card { font-size: 0.82rem; padding: 0.6rem; }
    }

    @media (max-width: 480px) {
        .overview-grid { grid-template-columns: repeat(2, 1fr) !important; }
        .hero-card .logo-text { font-size: 2rem !important; }
        .act-row { padding: 0.6rem; }
    }

    @media (display-mode: standalone) {
        body { padding-top: env(safe-area-inset-top); }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# Data Constants - Matched to Survey Exactly
# ============================================================

ACTIVITY_DURATION = {
    'Restaurants': 120, 'Food & Beverages': 120, 'Restaurant': 120,
    'International Kitchen': 120, 'Italian Kitchen': 120, 'Asian Kitchen': 120,
    'Shopping': 180, 'Traditional Market': 180,
    'Entertainment': 300, 'Amusement parks': 300, 'Adventure': 300,
    'Public Park': 300, 'Cinema': 180,
    'Museum': 150, 'Historic site': 120, 'Culture & History': 120,
    'Cultural': 120, 'Art Gallery': 120, 'Libraries': 90,
    'Religious Site': 90, 'Mosques': 90, 'Architectural sites': 120,
    'Nature': 180, 'Natural site': 180, 'Mountains': 180, 'Farm': 120,
    'Beach': 180, 'Water sports': 180, 'Sports': 150,
    'Families': 180, 'Classes and Training': 120,
    'Accommodations': 0, 'General': 90,
}

CITY_TO_ATTR = {
    'Riyadh': ['Riyadh', 'Diriyah'],
    'Jeddah': ['Jeddah'],
    'Makkah': ['Makkah'],
    'Madinah': ['Madinah'],
    'AlUla': ['AlUla'],
    'Al Ahsa': ['Al Ahsa'],
    'Eastern Province': ['Eastern Province'],
    'Aseer': ['Aseer'],
    'Taif': ['Taif'],
    'Tabuk': ['Tabuk'],
    'The Red Sea': ['The Red Sea'],
    'Hail': ['Hail ', 'Hail'],
    'Qassim': ['Qassim'],
    'Al Baha': ['Al Baha'],
    'Najran': ['Najran'],
    'Yanbu': ['Yanbu'],
    'Al Jubail': ['Al Jubail ', 'Al Jubail'],
    'Jazan': ['Jazan ', 'Jazan'],
    'KAEC': ['KAEC'],
}

CITY_EN_TO_AR_HOTELS = {
    'Riyadh': ['الرياض', 'الدرعية'],
    'Diriyah': ['الدرعية', 'الرياض'],
    'Jeddah': ['جدة'],
    'Makkah': ['مكة المكرمة'],
    'Madinah': ['المدينة المنورة'],
    'AlUla': ['العلا'],
    'Eastern Province': ['الخبر', 'الدمام', 'الظهران'],
    'Aseer': ['أبها', 'خميس مشيط'],
    'Taif': ['الطائف', 'الهدا', 'الشفا الطائف'],
    'Tabuk': ['تبوك'],
    'Al Ahsa': ['الأحساء', 'الهفوف', 'المبرز'],
    'The Red Sea': ['أملج', 'الوجه', 'ينبع'],
    'Hail': ['حائل'],
    'Qassim': ['بريدة', 'القصيم', 'عنيزة'],
    'Al Baha': ['الباحة'],
    'Najran': ['نجران'],
    'Yanbu': ['ينبع'],
    'Al Jubail': ['الجبيل'],
    'Jazan': ['جازان', 'جيزان'],
    'KAEC': ['مدينة الملك عبدالله الاقتصادية', 'رابغ'],
}

CITY_COORDS = {
    'Riyadh': (24.7136, 46.6753),
    'Jeddah': (21.4858, 39.1925),
    'Makkah': (21.3891, 39.8579),
    'Madinah': (24.4672, 39.6024),
    'Tabuk': (28.3896, 36.5624),
    'AlUla': (26.5408, 37.8733),
    'Aseer': (18.2164, 42.5053),
    'Taif': (21.2716, 40.4158),
    'Eastern Province': (26.2172, 50.1971),
    'Al Ahsa': (25.3548, 49.5832),
    'The Red Sea': (25.0, 37.0),
    'Hail': (27.5114, 41.7208),
    'Qassim': (26.3260, 43.9750),
    'Al Baha': (20.0000, 41.4667),
    'Najran': (17.4917, 44.1322),
    'Yanbu': (24.0895, 38.0618),
    'Al Jubail': (27.0046, 49.6225),
    'Jazan': (16.8892, 42.5611),
    'KAEC': (22.4539, 39.1282),
}

AVAILABLE_CITIES = list(CITY_TO_ATTR.keys())

TRIP_DURATION_OPTIONS = ['1-3 Days', '4-7 Days', '8-14 Days', 'More than 14 Days']
TRAVELER_OPTIONS = ['Solo Traveler', 'With a Partner', 'With Family', 'With Friends']
INTEREST_OPTIONS = [
    'History & Culture', 'Nature & Adventure', 'Entertainment & Events',
    'Shopping & Luxury', 'Relaxation & Wellness', 'Religious Tourism',
]
PACE_OPTIONS = [
    'Relaxed - One main activity per day with plenty of free time',
    'Balanced - Two to three activities per day with a balance between exploration and rest',
    'Action-Packed - A packed schedule to explore as many sites as possible',
]
CUISINE_OPTIONS = [
    'Traditional Saudi', 'Middle Eastern',
    'Asian (Japanese, Chinese, etc.)', 'European (Italian, French, etc.)',
    'International / Fusion', 'Fast Food / Burgers',
]
BUDGET_OPTIONS = {
    'Budget-Friendly - Less than 300 SAR': (0, 300),
    'Mid-Range - 300 - 800 SAR': (300, 800),
    'Luxury - More than 800 SAR': (800, 99999),
}
ACCOMMODATION_OPTIONS = {
    'Budget Hotel / Hostel': ['فندق', 'نزل'],
    'Mid-Range Hotel (3-4 Stars)': ['فندق'],
    'Luxury Hotel / Resort (5 Stars)': ['فندق', 'منتجع'],
    'Serviced Apartment': ['شقة فندقية', 'شقة مفروشة', 'شقة مخدومة', 'شقق مفروشة'],
    'Traditional Stay (Heritage Lodging)': ['بيت ضيافة', 'نزل'],
}
INTEREST_TO_CATS = {
    'History & Culture': ['Culture & History', 'Historic site', 'Museum', 'Art Gallery', 'Architectural sites', 'Libraries'],
    'Nature & Adventure': ['Nature', 'Natural site', 'Mountains', 'Farm', 'Adventure', 'Sports', 'Water sports'],
    'Entertainment & Events': ['Entertainment', 'Amusement parks', 'Cinema', 'Public Park', 'Families'],
    'Shopping & Luxury': ['Shopping', 'Traditional Market'],
    'Relaxation & Wellness': ['Beach', 'Nature', 'Natural site', 'Public Park'],
    'Religious Tourism': ['Religious Site', 'Mosques'],
}

# ============================================================
# Helper Functions (Unchanged - Same ML Logic)
# ============================================================

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates using Haversine formula."""
    R = 6371
    lat1_r, lat2_r = math.radians(lat1), math.radians(lat2)
    d_lat, d_lon = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(d_lon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))


def get_transport_mode(distance_km):
    """Determine transport mode and estimated time based on distance."""
    if distance_km < 50:
        return 'Car', f'{int(distance_km / 60 * 60)} min', distance_km
    elif distance_km < 400:
        hours = distance_km / 100
        return 'Car', f'{int(hours)}h {int((hours % 1) * 60)}m', distance_km
    else:
        hours = distance_km / 800
        return 'Plane', f'{int(hours)}h {int((hours % 1) * 60)}m', distance_km


def find_hotels(df_hotels, city, budget_range, acc_type):
    """Find hotels matching city, budget, and accommodation type."""
    ar_cities = CITY_EN_TO_AR_HOTELS.get(city, [])
    if not ar_cities:
        return pd.DataFrame()
    mask = df_hotels['المدينة / المنطقة'].isin(ar_cities)
    hotels = df_hotels[mask].copy()
    if city in ['Riyadh', 'Jeddah', 'Makkah', 'Madinah']:
        hotels = hotels[~hotels['نوع الإقامة'].isin(['شاليه', 'فيلا'])]
    if acc_type in ACCOMMODATION_OPTIONS:
        type_list = ACCOMMODATION_OPTIONS[acc_type]
        if type_list:
            type_filtered = hotels[hotels['نوع الإقامة'].isin(type_list)]
            if len(type_filtered) > 0:
                hotels = type_filtered
    if budget_range:
        low, high = budget_range
        price_col = 'السعر لليلة الواحدة (SAR)'
        hotels = hotels[hotels[price_col].notna()]
        budget_filtered = hotels[(hotels[price_col] >= low) & (hotels[price_col] <= high)]
        if len(budget_filtered) > 0:
            hotels = budget_filtered
    return hotels


def find_activities(df_activities, city, preferred_categories):
    """Find activities matching city and preferred categories."""
    city_list = CITY_TO_ATTR.get(city, [city])
    mask = df_activities['City'].isin(city_list)
    acts = df_activities[mask].copy()
    acts = acts[acts['Category'] != 'Accommodations']
    acts = acts.dropna(subset=['Attraction Name'])
    if preferred_categories:
        cat_acts = acts[acts['Category'].isin(preferred_categories)]
        if len(cat_acts) >= 1:
            acts = cat_acts
        else:
            religious_cats = {'Religious Site', 'Mosques'}
            if not religious_cats.intersection(set(preferred_categories)):
                acts = acts[~acts['Category'].isin(religious_cats)]
    return acts


def get_pace_key(pace_full):
    """Extract pace key from full survey text."""
    if pace_full.startswith('Relaxed'):
        return 'Relaxed'
    elif pace_full.startswith('Action-Packed'):
        return 'Action-Packed'
    return 'Balanced'


def schedule_day(activities_df, pace_key, city, num_activities=5, budget_level='mid-range', used_restaurants=None):
    """Schedule activities for one day with realistic timing and real restaurant names."""
    if used_restaurants is None:
        used_restaurants = set()
    if city in ['Riyadh', 'Jeddah']:
        day_start = 10 * 60
    else:
        day_start = 9 * 60 if pace_key == 'Relaxed' else 8 * 60
    if pace_key == 'Relaxed':
        day_end = 21 * 60
    elif pace_key == 'Action-Packed':
        day_end = 23 * 60
    else:
        day_end = 22 * 60
    lunch_time = 13 * 60
    dinner_time = 19 * 60
    travel_gap = 30
    scheduled = []
    current_time = day_start
    lunch_added = False
    dinner_added = False
    if len(activities_df) > num_activities:
        sampled = activities_df.sample(num_activities)
    else:
        sampled = activities_df
    evening_cats = {'Entertainment', 'Amusement parks', 'Adventure', 'Public Park', 'Cinema'}
    records = sampled.to_dict('records')
    records.sort(key=lambda a: 1 if str(a.get('Category', '')) in evening_cats else 0)

    def _add_meal(meal_type, duration_min):
        nonlocal current_time
        rest = get_restaurant_for_meal(city, meal_type, budget_level, used_restaurants)
        rest_name = rest['name_en'] if rest else 'Local Restaurant'
        rest_cuisine = rest['cuisine'] if rest else ''
        rest_name_ar = rest['name_ar'] if rest else ''
        if rest:
            used_restaurants.add(rest['name_en'])
        scheduled.append({
            'type': meal_type,
            'time': f'{current_time // 60:02d}:{current_time % 60:02d}',
            'end_time': f'{(current_time + duration_min) // 60:02d}:{(current_time + duration_min) % 60:02d}',
            'restaurant_name': rest_name,
            'restaurant_name_ar': rest_name_ar,
            'restaurant_cuisine': rest_cuisine,
            'duration_min': duration_min,
        })
        current_time += duration_min + travel_gap

    for act in records:
        cat = str(act.get('Category', 'General'))
        duration = ACTIVITY_DURATION.get(cat, 90)
        if pace_key == 'Relaxed':
            duration = int(duration * 1.2)
        elif pace_key == 'Action-Packed':
            duration = int(duration * 0.85)
        if city in ['Riyadh', 'Jeddah'] and cat in evening_cats:
            current_time = max(current_time, 16 * 60)
        if not lunch_added and current_time >= lunch_time - 30 and current_time <= lunch_time + 60:
            lunch_added = True
            _add_meal('lunch', 60)
        if current_time + duration > day_end:
            break
        t_start = f'{current_time // 60:02d}:{current_time % 60:02d}'
        t_end_val = current_time + duration
        t_end = f'{t_end_val // 60:02d}:{t_end_val % 60:02d}'
        scheduled.append({
            'type': 'activity',
            'name': act.get('Attraction Name', 'Activity'),
            'category': cat,
            'time': t_start,
            'end_time': t_end,
            'duration_min': duration,
            'lat': act.get('Latitude', None),
            'lon': act.get('Longitude', None),
        })
        current_time = t_end_val + travel_gap
        if not lunch_added and current_time >= lunch_time:
            lunch_added = True
            _add_meal('lunch', 60)
        if not dinner_added and current_time >= dinner_time - 30 and current_time <= dinner_time + 60:
            dinner_added = True
            _add_meal('dinner', 90)
    return scheduled


def build_map(selected_cities, all_day_activities, hotel_locations=None):
    """Build an interactive Folium map with dark theme."""
    if not HAS_FOLIUM:
        return None
    m = folium.Map(location=[24.0, 44.0], zoom_start=5, tiles='cartodbdark_matter')
    colors = ['#14532D', '#D4AF37', '#22C55E', '#166534', '#0A2E14',
              '#15803D', '#B8860B', '#2D6A4F', '#40916C', '#52B788', '#74C69D']
    for day_idx, city in enumerate(selected_cities):
        coords = CITY_COORDS.get(city, None)
        if coords:
            color = colors[day_idx % len(colors)]
            folium.Marker(
                location=coords,
                popup=f"<b>Day {day_idx+1}: {city}</b>",
                tooltip=f"Day {day_idx+1} - {city}",
                icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(m)
            if day_idx < len(all_day_activities):
                act_num = 0
                for act in all_day_activities[day_idx]:
                    if act['type'] == 'activity' and act.get('lat') and act.get('lon'):
                        try:
                            lat = float(act['lat'])
                            lon = float(act['lon'])
                            if not math.isnan(lat) and not math.isnan(lon):
                                act_num += 1
                                folium.Marker(
                                    location=[lat, lon],
                                    popup=f"<b>Day {day_idx+1} - Activity {act_num}</b><br>"
                                           f"<b>{act['name']}</b><br>"
                                           f"Category: {act['category']}<br>"
                                           f"Time: {act['time']} - {act['end_time']}<br>"
                                           f"Duration: {act['duration_min']} min",
                                    tooltip=f"Day {day_idx+1}: {act['name']}",
                                    icon=folium.Icon(color='lightgreen', icon='star', prefix='fa')
                                ).add_to(m)
                        except (ValueError, TypeError):
                            pass
            if hotel_locations and day_idx < len(hotel_locations) and hotel_locations[day_idx]:
                h_info = hotel_locations[day_idx]
                h_coords = h_info.get('coords', coords)
                folium.Marker(
                    location=h_coords,
                    popup=f"<b>Day {day_idx+1} Hotel</b><br>"
                           f"<b>{h_info.get('name', 'Hotel')}</b><br>"
                           f"Rating: {h_info.get('rating', 'N/A')}<br>"
                           f"Price: {h_info.get('price', 'N/A')}",
                    tooltip=f"{h_info.get('name', 'Hotel')}",
                    icon=folium.Icon(color='orange', icon='bed', prefix='fa')
                ).add_to(m)
    route_coords = []
    for city in selected_cities:
        coords = CITY_COORDS.get(city, None)
        if coords:
            route_coords.append(coords)
    if len(route_coords) > 1:
        folium.PolyLine(
            route_coords, weight=3, color='#C5A43B', opacity=0.8, dash_array='10'
        ).add_to(m)
    legend_html = '''
    <div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
                background: #111F16; padding: 14px 18px; border-radius: 12px;
                border: 1px solid rgba(197,164,59,0.3); box-shadow: 0 4px 20px rgba(0,0,0,0.5);
                font-family: Inter, sans-serif; font-size: 13px; color: #D1D5DB;">
        <div style="font-weight: 700; color: #C5A43B; margin-bottom: 8px; letter-spacing: 1px;">MAP LEGEND</div>
        <div style="margin: 5px 0;"><span style="color: #22C55E;">&#9679;</span> City Center</div>
        <div style="margin: 5px 0;"><span style="color: #22C55E;">&#9733;</span> Activity / Attraction</div>
        <div style="margin: 5px 0;"><span style="color: #D4AF37;">&#9679;</span> Hotel / Accommodation</div>
        <div style="margin: 5px 0;"><span style="color: #C5A43B;">- - -</span> Travel Route</div>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    return m


# ============================================================
# Data Loading
# ============================================================

@st.cache_resource
def load_data():
    """Load hotel and activity data from Excel files."""
    df_hotels, df_activities = None, None
    search_dirs = ['.', '/mount/src/tripsa-app', '/mount/src/trip-sa', os.path.dirname(__file__)]
    for d in search_dirs:
        try:
            for f in os.listdir(d):
                if f.endswith('.xlsx'):
                    path = os.path.join(d, f)
                    if 'hotel' in f.lower() or 'accommodation' in f.lower():
                        df_hotels = pd.read_excel(path)
                    elif 'attraction' in f.lower() or 'demo' in f.lower():
                        df_activities = pd.read_excel(path)
        except:
            continue
    return df_hotels, df_activities


# ============================================================
# Main Application
# ============================================================

def main():
    # Sidebar Hint Bar - Using Streamlit native components
    hint_cols = st.columns([1, 6, 1])
    with hint_cols[1]:
        sidebar_btn = st.button(
            "◀ 🧭  Tap here to open Trip Planner  🧭 ▶",
            key="open_sidebar_hint",
            use_container_width=True
        )
    
    # Inject CSS to style the hint button + auto-open sidebar script
    st.markdown("""
    <style>
    /* Style the hint button */
    button[kind="secondary"][data-testid="stBaseButton-secondary"] {
        background: linear-gradient(135deg, #14532D 0%, #1B6B3A 100%) !important;
        border: 1px solid rgba(197, 164, 59, 0.4) !important;
        border-radius: 12px !important;
        color: #C5A43B !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.5px !important;
        padding: 0.8rem 1.5rem !important;
        animation: pulse-hint 2s ease-in-out infinite !important;
        transition: all 0.3s ease !important;
    }
    button[kind="secondary"][data-testid="stBaseButton-secondary"]:hover {
        background: linear-gradient(135deg, #1B6B3A 0%, #22C55E 100%) !important;
        border-color: #C5A43B !important;
        color: #FFD700 !important;
    }
    </style>
    <script>
    // Auto-inject sidebar opener into parent
    (function() {
        function tryOpenSidebar() {
            try {
                var doc = window.parent.document;
                // Find the collapsed sidebar control
                var ctrl = doc.querySelector('[data-testid="collapsedControl"]') ||
                           doc.querySelector('[data-testid="stSidebarCollapsedControl"]') ||
                           doc.querySelector('button[aria-label="Open sidebar"]');
                if (ctrl) { ctrl.click(); }
            } catch(e) {}
        }
        // Listen for clicks on hint buttons in parent
        setTimeout(function() {
            try {
                var doc = window.parent.document;
                var btns = doc.querySelectorAll('button');
                btns.forEach(function(b) {
                    if (b.textContent && b.textContent.includes('Trip Planner')) {
                        b.addEventListener('click', function() {
                            setTimeout(tryOpenSidebar, 100);
                        });
                    }
                });
            } catch(e) {}
        }, 1000);
    })();
    </script>
    """, unsafe_allow_html=True)
    
    if sidebar_btn:
        st.sidebar.markdown("""<div style='text-align:center; padding:1rem; color:#C5A43B; font-size:1.2rem;'>✅ Trip Planner is open! Scroll down to fill your preferences.</div>""", unsafe_allow_html=True)

    # Hero Header - Premium Dark Card
    st.markdown("""
    <div class="hero-card">
        <span class="compass-icon">🧭</span>
        <div class="logo-text">TRIP<span class="logo-dot">.</span>SA</div>
        <div class="tagline">Smart Tourism Recommendation System</div>
        <div class="sub">Powered by Machine Learning &amp; Data Analytics &nbsp;|&nbsp; Kingdom of Saudi Arabia</div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # Sidebar - Premium Dark Survey
    # ============================================================
    st.sidebar.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem;">
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #C5A43B; font-weight: 700; letter-spacing: 3px;">TRIP<span style="color:#22C55E;">.</span>SA</div>
        <div style="font-size: 0.7rem; color: #9CA3AF; letter-spacing: 2px; text-transform: uppercase; margin-top: 0.3rem;">Plan Your Journey</div>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("---")

    trip_duration = st.sidebar.selectbox(
        "How long is your stay in the Kingdom?",
        options=TRIP_DURATION_OPTIONS, index=1
    )
    st.sidebar.markdown("---")

    traveler_type = st.sidebar.selectbox(
        "How many people are traveling?",
        options=TRAVELER_OPTIONS, index=0
    )
    st.sidebar.markdown("---")

    interests = st.sidebar.multiselect(
        "What are your main interests? (Select up to 3)",
        options=INTEREST_OPTIONS,
        default=['History & Culture'],
        max_selections=3
    )
    preferred_cats = []
    for interest in interests:
        preferred_cats.extend(INTEREST_TO_CATS.get(interest, []))
    preferred_cats = list(set(preferred_cats))
    st.sidebar.markdown("---")

    pace = st.sidebar.selectbox(
        "What is your preferred travel pace?",
        options=PACE_OPTIONS, index=1
    )
    pace_key = get_pace_key(pace)
    st.sidebar.markdown("---")

    cuisines = st.sidebar.multiselect(
        "What cuisines would you like to try?",
        options=CUISINE_OPTIONS,
        default=['Traditional Saudi']
    )
    st.sidebar.markdown("---")

    daily_budget = st.sidebar.selectbox(
        "What is your approximate daily budget for activities & food?",
        options=list(BUDGET_OPTIONS.keys()), index=1
    )
    st.sidebar.markdown("---")

    has_religious = 'Religious Tourism' in interests
    city_options = AVAILABLE_CITIES.copy()
    if not has_religious:
        city_options = [c for c in city_options if c not in ['Makkah', 'Madinah']]

    selected_cities = st.sidebar.multiselect(
        "Which cities would you like to visit?",
        options=city_options,
        default=['Riyadh'] if 'Riyadh' in city_options else [city_options[0]],
        help="Makkah & Madinah are available only when 'Religious Tourism' is selected."
    )
    st.sidebar.markdown("---")

    accommodation_type = st.sidebar.selectbox(
        "What type of accommodation do you prefer?",
        options=list(ACCOMMODATION_OPTIONS.keys()), index=2
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("")
    generate = st.sidebar.button("Generate Trip Plan", use_container_width=True)

    # ============================================================
    # Generate Trip Plan
    # ============================================================

    if generate:
        if not selected_cities:
            st.error("Please select at least one city to visit.")
            return

        df_hotels, df_activities = load_data()
        if df_hotels is None or df_activities is None:
            st.error("Could not load data files. Please ensure the Excel files are in the project directory.")
            return

        budget_range = BUDGET_OPTIONS.get(daily_budget, (0, 99999))
        dur_total = {'1-3 Days': 3, '4-7 Days': 5, '8-14 Days': 10, 'More than 14 Days': 16}
        total_trip_days = dur_total.get(trip_duration, 5)
        num_cities = len(selected_cities)
        if num_cities > 0:
            base_days = max(2, total_trip_days // num_cities)
            remainder = total_trip_days - (base_days * num_cities)
        else:
            base_days = 2
            remainder = 0

        itinerary_cities = []
        for i, city in enumerate(selected_cities):
            city_days = base_days + (1 if i < remainder else 0)
            for _ in range(city_days):
                itinerary_cities.append(city)

        total_distance = 0
        for i in range(len(selected_cities) - 1):
            c1 = CITY_COORDS.get(selected_cities[i], (24.7, 46.7))
            c2 = CITY_COORDS.get(selected_cities[i + 1], (24.7, 46.7))
            total_distance += calculate_distance(c1[0], c1[1], c2[0], c2[1])

        budget_key = daily_budget.split(' - ')[0].lower() if daily_budget else 'mid-range'
        if 'budget' in budget_key:
            rest_budget = 'budget'
        elif 'luxury' in budget_key:
            rest_budget = 'luxury'
        else:
            rest_budget = 'mid-range'

        all_day_activities = []
        hotel_data_list = []
        used_activities = set()
        used_restaurants = set()
        random.seed(42)

        for day_idx, city in enumerate(itinerary_cities):
            city_acts = find_activities(df_activities, city, preferred_cats)
            if len(used_activities) > 0:
                city_acts = city_acts[~city_acts['Attraction Name'].isin(used_activities)]
            if len(city_acts) > 0:
                num_acts = 3 if pace_key == 'Relaxed' else 5 if pace_key == 'Action-Packed' else 4
                scheduled = schedule_day(city_acts, pace_key, city, num_acts, rest_budget, used_restaurants)
                all_day_activities.append(scheduled)
                for item in scheduled:
                    if item['type'] == 'activity':
                        used_activities.add(item['name'])
            else:
                all_day_activities.append([])

            hotels = find_hotels(df_hotels, city, budget_range, accommodation_type)
            if len(hotels) > 0:
                best = hotels.sort_values('درجة التقييم (من 10)', ascending=False, na_position='last').iloc[0]
                h_name = best['اسم مكان الإقامة']
                h_rating = best.get('درجة التقييم (من 10)', None)
                h_price = best.get('السعر لليلة الواحدة (SAR)', None)
                h_type = best.get('نوع الإقامة', '')
                h_city_ar = best.get('المدينة / المنطقة', '')
                rating_display = f"{h_rating}/10" if pd.notna(h_rating) else "N/A"
                price_display = f"{h_price:,.0f} SAR/night" if pd.notna(h_price) else "N/A"
                hotel_coords = CITY_COORDS.get(city, [24.0, 44.0])
                hotel_data_list.append({
                    'name': str(h_name), 'rating': rating_display,
                    'price': price_display, 'type': str(h_type),
                    'city_ar': str(h_city_ar), 'coords': hotel_coords,
                })
            else:
                hotel_data_list.append(None)

        st.session_state['trip_result'] = {
            'selected_cities': list(selected_cities),
            'itinerary_cities': itinerary_cities,
            'total_distance': total_distance,
            'traveler_type': traveler_type,
            'daily_budget': daily_budget,
            'trip_duration': trip_duration,
            'pace_key': pace_key,
            'all_day_activities': all_day_activities,
            'hotel_data_list': hotel_data_list,
        }

    # ============================================================
    # Display Trip Plan
    # ============================================================

    if 'trip_result' not in st.session_state:
        return

    result = st.session_state['trip_result']
    selected_cities = result['selected_cities']
    itinerary_cities = result['itinerary_cities']
    total_distance = result['total_distance']
    traveler_type = result['traveler_type']
    daily_budget = result['daily_budget']
    trip_duration = result['trip_duration']
    pace_key = result['pace_key']
    all_day_activities = result['all_day_activities']
    hotel_data_list = result['hotel_data_list']
    budget_range = BUDGET_OPTIONS.get(daily_budget, (0, 99999))
    total_days = len(itinerary_cities)

    # ---- Overview Cards ----
    st.markdown('<div class="section-title">Trip Overview</div>', unsafe_allow_html=True)

    total_activities = sum(1 for day in all_day_activities for act in day if act.get('type') == 'activity')

    st.markdown(f"""
    <div class="overview-grid">
        <div class="overview-card">
            <div class="icon">📅</div>
            <div class="value">{total_days}</div>
            <div class="label">Total Days</div>
        </div>
        <div class="overview-card">
            <div class="icon">🏙️</div>
            <div class="value">{len(selected_cities)}</div>
            <div class="label">Cities</div>
        </div>
        <div class="overview-card">
            <div class="icon">📍</div>
            <div class="value">{total_activities}</div>
            <div class="label">Activities</div>
        </div>
        <div class="overview-card">
            <div class="icon">🛣️</div>
            <div class="value">{total_distance:,.0f} km</div>
            <div class="label">Distance</div>
        </div>
        <div class="overview-card">
            <div class="icon">👤</div>
            <div class="value">{traveler_type.split(' ')[0]}</div>
            <div class="label">Traveler</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- Day-by-Day Itinerary ----
    st.markdown('<div class="section-title">Day-by-Day Itinerary</div>', unsafe_allow_html=True)

    hotel_locations = []

    for day_idx, city in enumerate(itinerary_cities):
        day_num = day_idx + 1

        if day_idx > 0 and itinerary_cities[day_idx] != itinerary_cities[day_idx - 1]:
            prev_city = itinerary_cities[day_idx - 1]
            c1 = CITY_COORDS.get(prev_city, (24.7, 46.7))
            c2 = CITY_COORDS.get(city, (24.7, 46.7))
            dist = calculate_distance(c1[0], c1[1], c2[0], c2[1])
            mode, duration, _ = get_transport_mode(dist)
            icon = '✈️' if mode == 'Plane' else '🚗'
            st.markdown(f"""
            <div class="transport">
                <span style="font-size:1.3rem">{icon}</span>
                <span>Travel: {prev_city} → {city} &nbsp;|&nbsp; {mode} &nbsp;|&nbsp; {duration} &nbsp;|&nbsp; {dist:,.0f} km</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="day-header">
            <span style="font-size:1.3rem">📍</span>
            Day {day_num} — {city}
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="day-body">', unsafe_allow_html=True)

        scheduled = all_day_activities[day_idx] if day_idx < len(all_day_activities) else []

        if len(scheduled) > 0:
            for item in scheduled:
                if item['type'] in ('lunch', 'dinner'):
                    meal_icon = '🍽️' if item['type'] == 'lunch' else '🌙'
                    meal_label = 'Lunch' if item['type'] == 'lunch' else 'Dinner'
                    rest_name = item.get('restaurant_name', 'Local Restaurant')
                    rest_cuisine = item.get('restaurant_cuisine', '')
                    cuisine_text = f' &nbsp;•&nbsp; {rest_cuisine}' if rest_cuisine else ''
                    st.markdown(f"""
                    <div class="meal-card">{meal_icon} {meal_label} at <b>{rest_name}</b>{cuisine_text} &nbsp;|&nbsp; {item['time']} - {item['end_time']}</div>
                    """, unsafe_allow_html=True)
                else:
                    dur_h = item['duration_min'] // 60
                    dur_m = item['duration_min'] % 60
                    dur_str = f"{dur_h}h {dur_m}m" if dur_h > 0 else f"{dur_m} min"
                    st.markdown(f"""
                    <div class="act-row">
                        <div class="act-time">{item['time']} - {item['end_time']}</div>
                        <div class="act-info">
                            <div class="act-name">{item['name']}</div>
                            <div class="act-cat">{item['category']}</div>
                        </div>
                        <div class="act-dur">{dur_str}</div>
                    </div>
                    """, unsafe_allow_html=True)

            table_data = []
            for s in scheduled:
                if s['type'] in ('lunch', 'dinner'):
                    meal_label = 'Lunch' if s['type'] == 'lunch' else 'Dinner'
                    rest_name = s.get('restaurant_name', 'Local Restaurant')
                    row = {
                        'Time': f"{s['time']} - {s['end_time']}",
                        'Duration': f"{s.get('duration_min', 60)} min",
                        'Attraction': f"{meal_label} at {rest_name}",
                        'Category': s.get('restaurant_cuisine', 'Restaurant'),
                    }
                else:
                    row = {
                        'Time': f"{s['time']} - {s['end_time']}",
                        'Duration': f"{s['duration_min']} min",
                        'Attraction': s.get('name', 'Activity'),
                        'Category': s.get('category', 'General'),
                    }
                if s['type'] == 'activity' and s.get('lat') and s.get('lon'):
                    try:
                        lat_v = float(s['lat'])
                        lon_v = float(s['lon'])
                        if not math.isnan(lat_v) and not math.isnan(lon_v):
                            row['Location'] = f"{lat_v:.4f}, {lon_v:.4f}"
                        else:
                            row['Location'] = city
                    except (ValueError, TypeError):
                        row['Location'] = city
                else:
                    row['Location'] = city
                table_data.append(row)
            with st.expander("View Schedule Table"):
                st.dataframe(pd.DataFrame(table_data), use_container_width=True, hide_index=True)
        else:
            st.info(f"No activities found for {city}. Try adjusting your interests.")

        h_data = hotel_data_list[day_idx] if day_idx < len(hotel_data_list) else None
        if h_data:
            hotel_locations.append(h_data)
            st.markdown(f"""
            <div class="hotel-box">
                <div class="hotel-icon">🏨</div>
                <div class="hotel-info">
                    <div class="hotel-name">{h_data['name']}</div>
                    <div class="hotel-meta">{h_data['type']} &nbsp;•&nbsp; {h_data['city_ar']} &nbsp;•&nbsp; {h_data['price']}</div>
                </div>
                <div class="hotel-badge">⭐ {h_data['rating']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            hotel_locations.append(None)
            st.warning(f"No accommodations found matching your criteria in {city}. Try adjusting budget or type.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ---- Interactive Map ----
    st.markdown('<div class="section-title">Trip Route Map</div>', unsafe_allow_html=True)

    city_points = []
    activity_points = []
    hotel_points = []
    route_path = []

    for day_idx, city in enumerate(itinerary_cities):
        coords = CITY_COORDS.get(city, None)
        if coords:
            city_points.append({
                'lat': coords[0], 'lon': coords[1],
                'name': f"Day {day_idx+1}: {city}", 'type': 'city'
            })
            route_path.append(coords)
        if day_idx < len(all_day_activities):
            for act in all_day_activities[day_idx]:
                if act.get('type') == 'activity' and act.get('lat') and act.get('lon'):
                    try:
                        lat_v = float(act['lat'])
                        lon_v = float(act['lon'])
                        if not math.isnan(lat_v) and not math.isnan(lon_v):
                            activity_points.append({
                                'lat': lat_v, 'lon': lon_v,
                                'name': act['name'],
                                'category': act.get('category', ''),
                                'time': f"{act['time']} - {act['end_time']}",
                                'day': day_idx + 1
                            })
                    except (ValueError, TypeError):
                        pass
        if day_idx < len(hotel_locations) and hotel_locations[day_idx]:
            h_info = hotel_locations[day_idx]
            h_coords = h_info.get('coords')
            if h_coords:
                hotel_points.append({
                    'lat': h_coords[0], 'lon': h_coords[1],
                    'name': h_info.get('name', 'Hotel'),
                    'rating': h_info.get('rating', 'N/A'),
                    'price': h_info.get('price', 'N/A'),
                    'day': day_idx + 1
                })

    if HAS_FOLIUM:
        trip_map = build_map(itinerary_cities, all_day_activities, hotel_locations)
        if trip_map:
            st_folium(trip_map, width=None, height=500)
    elif HAS_PYDECK and (city_points or activity_points):
        layers = []
        if city_points:
            city_df = pd.DataFrame(city_points)
            layers.append(pdk.Layer(
                'ScatterplotLayer', data=city_df,
                get_position='[lon, lat]', get_color='[20, 83, 45, 220]',
                get_radius=15000, pickable=True, auto_highlight=True,
            ))
            layers.append(pdk.Layer(
                'TextLayer', data=city_df,
                get_position='[lon, lat]', get_text='name',
                get_size=14, get_color='[197, 164, 59, 255]',
                get_alignment_baseline="'bottom'",
                font_family='"Inter", sans-serif',
            ))
        if activity_points:
            act_df = pd.DataFrame(activity_points)
            layers.append(pdk.Layer(
                'ScatterplotLayer', data=act_df,
                get_position='[lon, lat]', get_color='[34, 197, 94, 200]',
                get_radius=5000, pickable=True, auto_highlight=True,
            ))
        if hotel_points:
            hotel_df = pd.DataFrame(hotel_points)
            layers.append(pdk.Layer(
                'ScatterplotLayer', data=hotel_df,
                get_position='[lon, lat]', get_color='[212, 175, 55, 230]',
                get_radius=8000, pickable=True, auto_highlight=True,
            ))
        if len(route_path) > 1:
            path_data = [{'path': [[c[1], c[0]] for c in route_path]}]
            layers.append(pdk.Layer(
                'PathLayer', data=path_data,
                get_path='path', get_color='[197, 164, 59, 180]',
                width_min_pixels=3, get_width=5,
            ))
        all_lats = [p['lat'] for p in city_points + activity_points + hotel_points]
        all_lons = [p['lon'] for p in city_points + activity_points + hotel_points]
        center_lat = sum(all_lats) / len(all_lats) if all_lats else 24.0
        center_lon = sum(all_lons) / len(all_lons) if all_lons else 44.0
        lat_range = max(all_lats) - min(all_lats) if len(all_lats) > 1 else 2
        zoom = max(4, min(11, int(12 - lat_range * 1.5)))
        view_state = pdk.ViewState(
            latitude=center_lat, longitude=center_lon, zoom=zoom, pitch=0,
        )
        deck = pdk.Deck(
            layers=layers, initial_view_state=view_state,
            map_style='mapbox://styles/mapbox/dark-v10',
            tooltip={
                'html': '<b>{name}</b><br/>{category}{time}{rating}{price}',
                'style': {
                    'backgroundColor': '#111F16', 'color': '#C5A43B',
                    'fontSize': '13px', 'padding': '8px 12px',
                    'borderRadius': '8px', 'border': '1px solid rgba(197,164,59,0.3)',
                }
            }
        )
        st.pydeck_chart(deck, use_container_width=True)

        st.markdown("""
        <div style="display: flex; gap: 2rem; padding: 0.8rem 1rem; background: #111F16;
                    border-radius: 10px; border: 1px solid rgba(197,164,59,0.15); margin-top: 0.5rem;
                    flex-wrap: wrap; font-size: 0.85rem; color: #D1D5DB;">
            <span><span style="display:inline-block; width:14px; height:14px; border-radius:50%;
                   background:#14532D; vertical-align:middle; margin-right:6px;"></span>City Center</span>
            <span><span style="display:inline-block; width:14px; height:14px; border-radius:50%;
                   background:#22C55E; vertical-align:middle; margin-right:6px;"></span>Activity</span>
            <span><span style="display:inline-block; width:14px; height:14px; border-radius:50%;
                   background:#C5A43B; vertical-align:middle; margin-right:6px;"></span>Hotel</span>
            <span><span style="display:inline-block; width:14px; height:4px;
                   background:#C5A43B; vertical-align:middle; margin-right:6px;"></span>Route</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        map_data = []
        for city in itinerary_cities:
            coords = CITY_COORDS.get(city, None)
            if coords:
                map_data.append({'lat': coords[0], 'lon': coords[1]})
        for day_acts in all_day_activities:
            for act in day_acts:
                if act.get('type') == 'activity' and act.get('lat') and act.get('lon'):
                    try:
                        lat_v = float(act['lat'])
                        lon_v = float(act['lon'])
                        if not math.isnan(lat_v) and not math.isnan(lon_v):
                            map_data.append({'lat': lat_v, 'lon': lon_v})
                    except (ValueError, TypeError):
                        pass
        if map_data:
            st.map(pd.DataFrame(map_data))

    # ---- Footer ----
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0; color: #6B7280; font-size: 0.8rem;">
        <div style="font-family: 'Playfair Display', serif; font-size: 1.2rem; color: #C5A43B; margin-bottom: 0.5rem; letter-spacing: 3px;">TRIP<span style="color:#22C55E;">.</span>SA</div>
        <div>Smart Tourism Recommendation System for Saudi Arabia</div>
        <div style="margin-top: 0.3rem;">Master's Thesis Project &nbsp;|&nbsp; King Saud University &nbsp;|&nbsp; 2026</div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
