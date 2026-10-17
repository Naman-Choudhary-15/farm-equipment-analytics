import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# Set page configuration for modern clean SaaS look
st.set_page_config(
    page_title="AgriFlow • Farm Equipment Utilization",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ENSURE DATA EXISTS (Auto-generator for seamless cloud deploy) ---
def ensure_dataset():
    if not os.path.exists('telemetry_data.csv'):
        np.random.seed(42)
        machine_types = ['Tractor', 'Harvester', 'Irrigation Pump']
        seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
        data = []
        start_date = datetime(2026, 1, 1)
        for _ in range(500):
            m_type = np.random.choice(machine_types)
            season = np.random.choice(seasons)
            planned = np.random.uniform(6, 12)
            actual = planned * np.random.uniform(0.7, 1.1)
            idle = actual * np.random.uniform(0.1, 0.4)
            fuel = (actual * 15) + (idle * 5) + np.random.normal(0, 5)
            engine_load = np.clip(np.random.normal(65, 15), 10, 100)
            maint = 'Yes' if (engine_load > 85 or idle > 3) and np.random.random() > 0.5 else 'No'
            data.append({
                'Date': (start_date + pd.Timedelta(days=int(np.random.randint(0, 180)))).strftime('%Y-%m-%d'),
                'Machine_ID': f"{m_type[:3].upper()}-{np.random.randint(100, 999)}",
                'Machine_Type': m_type,
                'Season': season,
                'Operating_Hours_Planned': round(planned, 1),
                'Operating_Hours_Actual': round(actual, 1),
                'Idle_Hours': round(idle, 1),
                'Fuel_Consumption_Liters': round(max(0, fuel), 1),
                'Engine_Load_Percent': round(engine_load, 1),
                'Maintenance_Required': maint
            })
        df_gen = pd.DataFrame(data)
        df_gen.to_csv('telemetry_data.csv', index=False)

ensure_dataset()

# --- CUSTOM CSS: LEAVEFLOW-INSPIRED MODERN SAAS DESIGN ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Clean light background */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }
    
    /* Hide Streamlit default header, deploy button, footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar Styling - Clean Light Minimalist */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
        box-shadow: 2px 0 6px rgba(0,0,0,0.02);
    }
    
    /* Top Navbar header container */
    .nav-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 0px 20px 0px;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .brand-container {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .brand-logo {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        font-weight: 800;
        font-size: 1.25rem;
        width: 38px;
        height: 38px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
    }
    .brand-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0f172a;
        letter-spacing: -0.5px;
    }
    .user-pill {
        display: flex;
        align-items: center;
        gap: 10px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #334155;
    }
    .user-avatar {
        background: #eff6ff;
        color: #2563eb;
        width: 26px;
        height: 26px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.75rem;
    }
    
    /* Breadcrumbs */
    .breadcrumbs {
        font-size: 0.75rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 4px;
    }
    
    /* Hero Welcome Banner */
    .hero-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #2563eb;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 24px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .hero-tag {
        font-size: 0.75rem;
        font-weight: 700;
        color: #2563eb;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .hero-title {
        font-size: 1.75rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0 0 6px 0;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 0.95rem;
        color: #64748b;
        margin: 0;
    }
    
    /* LeaveFlow Metric Cards */
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px 20px;
        display: flex;
        align-items: center;
        gap: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
    }
    .metric-icon-box {
        width: 44px;
        height: 44px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        flex-shrink: 0;
    }
    .metric-details {
        flex-grow: 1;
    }
    .metric-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #64748b;
        margin-bottom: 2px;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.2;
    }
    .metric-subtext {
        font-size: 0.75rem;
        color: #94a3b8;
        font-weight: 500;
        margin-top: 2px;
    }
    
    /* Content Card wrapper */
    .content-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        height: 100%;
    }
    .card-header-tag {
        font-size: 0.7rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0f172a;
        margin: 2px 0 16px 0;
    }
    
    /* Status Badge Pills */
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .status-pill-green {
        background-color: #ecfdf5;
        color: #059669;
    }
    .status-pill-amber {
        background-color: #fffbeb;
        color: #d97706;
    }
    .status-pill-red {
        background-color: #fef2f2;
        color: #dc2626;
    }
    
    /* Custom Streamlit Tab bar */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f1f5f9;
        padding: 4px;
        border-radius: 10px;
        border-bottom: none;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
        color: #64748b;
        background-color: transparent;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #2563eb !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv('telemetry_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    df['Fuel_Consumption_Liters'].fillna(df['Fuel_Consumption_Liters'].median(), inplace=True)
    return df

df = load_data()

# --- TOP NAVBAR ---
st.markdown("""
<div class="nav-bar">
    <div class="brand-container">
        <div class="brand-logo">A</div>
        <div>
            <div class="brand-title">AgriFlow</div>
        </div>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
        <div class="user-pill">
            <span style="color:#64748b; font-weight:500;">STUDENT</span>
            <div class="user-avatar">N</div>
            <span>Naman Choudhary</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.markdown("### 🎛️ Workspace Filters")
    st.caption("Filter equipment telemetry records dynamically.")
    
    selected_machine = st.multiselect(
        "Equipment Category",
        options=sorted(df['Machine_Type'].unique()),
        default=sorted(df['Machine_Type'].unique())
    )
    
    selected_season = st.multiselect(
        "Operating Season",
        options=sorted(df['Season'].unique()),
        default=sorted(df['Season'].unique())
    )
    
    st.markdown("---")
    min_load, max_load = st.slider("Engine Load Range (%)", 0, 100, (0, 100))
    
    st.markdown("---")
    st.markdown("""
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; font-size:0.8rem; color:#475569;">
        <strong>Project Context:</strong><br>
        • Course: Foundation of Data Science<br>
        • Institute: NIET Greater Noida<br>
        • SDG 2: Zero Hunger
    </div>
    """, unsafe_allow_html=True)

# Apply filters
filtered_df = df[
    (df['Machine_Type'].isin(selected_machine)) &
    (df['Season'].isin(selected_season)) &
    (df['Engine_Load_Percent'] >= min_load) &
    (df['Engine_Load_Percent'] <= max_load)
]

if filtered_df.empty:
    st.warning("No records match your selected filter criteria. Adjust the sidebar filters.")
    st.stop()

# --- BREADCRUMBS & HERO WELCOME CARD ---
st.markdown("""
<div class="breadcrumbs">WORKSPACE / OVERVIEW</div>
<div class="hero-card">
    <div>
        <div class="hero-tag">PBL • FOUNDATION OF DATA SCIENCE</div>
        <h1 class="hero-title">Welcome back, Naman</h1>
        <p class="hero-subtitle">Farm equipment telemetry at a glance. Track operational efficiency, fuel metrics, and machine health alerts.</p>
    </div>
    <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
        <span style="background: #eff6ff; color: #2563eb; border: 1px solid #bfdbfe; font-size: 0.8rem; font-weight: 700; padding: 6px 14px; border-radius: 9999px;">
            ● Telemetry Stream Active
        </span>
        <span style="font-size: 0.75rem; color: #94a3b8;">500 In-field Machine Sensors</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4 METRIC CARDS ROW (LEAVEFLOW STYLE) ---
total_actual = filtered_df['Operating_Hours_Actual'].sum()
total_idle = filtered_df['Idle_Hours'].sum()
total_fuel = filtered_df['Fuel_Consumption_Liters'].sum()
alert_count = int((filtered_df['Maintenance_Required'] == 'Yes').sum())

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon-box" style="background:#eff6ff; color:#2563eb;">🚜</div>
        <div class="metric-details">
            <div class="metric-label">Active Hours</div>
            <div class="metric-value">{total_actual:,.0f}</div>
            <div class="metric-subtext">Total operating time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    idle_pct = (total_idle / total_actual * 100) if total_actual > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon-box" style="background:#fef3c7; color:#d97706;">⏱️</div>
        <div class="metric-details">
            <div class="metric-label">Idle Time</div>
            <div class="metric-value">{total_idle:,.0f} <span style="font-size:1rem; font-weight:600; color:#d97706;">hrs</span></div>
            <div class="metric-subtext">{idle_pct:.1f}% idle loss ratio</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon-box" style="background:#ecfdf5; color:#059669;">⛽</div>
        <div class="metric-details">
            <div class="metric-label">Fuel Usage</div>
            <div class="metric-value">{total_fuel:,.0f} <span style="font-size:1rem; font-weight:600; color:#059669;">L</span></div>
            <div class="metric-subtext">Cumulative consumption</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    alert_color = "#dc2626" if alert_count > 0 else "#059669"
    alert_bg = "#fef2f2" if alert_count > 0 else "#ecfdf5"
    alert_sub = "Inspection required" if alert_count > 0 else "All systems nominal"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon-box" style="background:{alert_bg}; color:{alert_color};">🚨</div>
        <div class="metric-details">
            <div class="metric-label">Maintenance Alerts</div>
            <div class="metric-value" style="color:{alert_color};">{alert_count}</div>
            <div class="metric-subtext">{alert_sub}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# --- MODERN NAVIGATION TABS ---
tab_overview, tab_charts, tab_alerts = st.tabs([
    "📊 Activity & Fleet Overview",
    "📈 Analytics & 3D Telemetry",
    "🚨 Predictive Maintenance Queue"
])

# --- TAB 1: ACTIVITY & BREAKDOWN (LEAVEFLOW LAYOUT) ---
with tab_overview:
    col_left, col_right = st.columns([1.7, 1])
    
    with col_left:
        st.markdown("""
        <div class="content-card">
            <div class="card-header-tag">EQUIPMENT TELEMETRY</div>
            <div class="card-title">Recent Equipment Activity</div>
        """, unsafe_allow_html=True)
        
        # Display clean formatted table matching the reference card style
        recent_df = filtered_df.sort_values('Date', ascending=False).head(7).copy()
        
        # Create friendly formatted rows
        display_rows = []
        for _, row in recent_df.iterrows():
            maint_status = row['Maintenance_Required']
            if maint_status == 'Yes':
                badge = '<span class="status-pill status-pill-red">● Maintenance Alert</span>'
            elif row['Engine_Load_Percent'] > 75:
                badge = '<span class="status-pill status-pill-amber">● High Load</span>'
            else:
                badge = '<span class="status-pill status-pill-green">● Operational</span>'
                
            display_rows.append(f"""
            <div style="display:flex; justify-content:space-between; align-items:center; padding:12px 6px; border-bottom:1px solid #f1f5f9;">
                <div style="display:flex; align-items:center; gap:14px;">
                    <span style="font-size:0.8rem; font-weight:700; color:#2563eb; background:#eff6ff; padding:4px 8px; border-radius:6px;">#{row['Machine_ID']}</span>
                    <div>
                        <div style="font-weight:700; color:#0f172a; font-size:0.9rem;">{row['Machine_Type']}</div>
                        <div style="font-size:0.75rem; color:#94a3b8;">{row['Date'].strftime('%d %b %Y')} • {row['Season']}</div>
                    </div>
                </div>
                <div style="display:flex; align-items:center; gap:20px;">
                    <div style="text-align:right;">
                        <span style="font-size:0.85rem; font-weight:700; color:#0f172a;">{row['Fuel_Consumption_Liters']:.1f} L</span>
                        <div style="font-size:0.7rem; color:#64748b;">Load: {row['Engine_Load_Percent']:.0f}%</div>
                    </div>
                    {badge}
                </div>
            </div>
            """)
        
        st.markdown("".join(display_rows), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_right:
        st.markdown("""
        <div class="content-card">
            <div class="card-header-tag">FLEET HEALTH BREAKDOWN</div>
            <div class="card-title">Machine Condition Share</div>
        """, unsafe_allow_html=True)
        
        # Donut Chart exactly matching the LeaveFlow bottom right ring chart!
        cond_counts = filtered_df['Maintenance_Required'].value_counts()
        labels = ['Optimal Condition', 'Maintenance Needed']
        values = [cond_counts.get('No', 0), cond_counts.get('Yes', 0)]
        colors = ['#10b981', '#ef4444']
        
        fig_donut = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.72,
            marker_colors=colors,
            textinfo='none',
            hoverinfo='label+value+percent'
        )])
        
        fig_donut.update_layout(
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
            margin=dict(t=10, b=30, l=10, r=10),
            height=260,
            annotations=[dict(
                text=f"<b>{len(filtered_df)}</b><br><span style='font-size:12px;color:#64748b'>assets</span>",
                x=0.5, y=0.5, font_size=20, showarrow=False
            )]
        )
        st.plotly_chart(fig_donut, use_container_width=True)
        
        st.markdown(f"""
        <div style="margin-top:14px; padding-top:12px; border-top:1px solid #f1f5f9; font-size:0.75rem; color:#64748b;">
            Summary of {len(filtered_df)} filtered machinery units across operational zones.
        </div>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: DETAILED ANALYTICS & 3D ---
with tab_charts:
    c_chart1, c_chart2 = st.columns(2)
    
    with c_chart1:
        st.markdown("""
        <div class="content-card">
            <div class="card-header-tag">PERFORMANCE METRICS</div>
            <div class="card-title">Planned vs Actual Operating Hours</div>
        """, unsafe_allow_html=True)
        
        avg_hours = filtered_df.groupby('Machine_Type')[['Operating_Hours_Planned', 'Operating_Hours_Actual']].mean().reset_index()
        fig_bar = px.bar(
            avg_hours,
            x='Machine_Type',
            y=['Operating_Hours_Planned', 'Operating_Hours_Actual'],
            barmode='group',
            color_discrete_sequence=['#93c5fd', '#2563eb'],
            template='plotly_white'
        )
        fig_bar.update_layout(
            margin=dict(t=10, b=20, l=10, r=10),
            legend_title_text="",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            height=300
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c_chart2:
        st.markdown("""
        <div class="content-card">
            <div class="card-header-tag">RESOURCE CONSUMPTION</div>
            <div class="card-title">Idle Hours vs Fuel Loss</div>
        """, unsafe_allow_html=True)
        
        fig_scatter = px.scatter(
            filtered_df,
            x='Idle_Hours',
            y='Fuel_Consumption_Liters',
            color='Machine_Type',
            color_discrete_sequence=['#2563eb', '#10b981', '#f59e0b'],
            template='plotly_white',
            hover_name='Machine_ID'
        )
        fig_scatter.update_layout(
            margin=dict(t=10, b=20, l=10, r=10),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            height=300
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    
    # 3D Telemetry Matrix
    st.markdown("""
    <div class="content-card">
        <div class="card-header-tag">INTERACTIVE MULTIDIMENSIONAL SENSORS</div>
        <div class="card-title">3D Telemetry Spatial Matrix (Idle vs Load vs Fuel)</div>
        <p style="font-size:0.85rem; color:#64748b; margin-top:-10px;">Click and drag to rotate, pinch to zoom. Visualizes multi-sensor telematics correlation.</p>
    """, unsafe_allow_html=True)
    
    fig_3d = px.scatter_3d(
        filtered_df,
        x='Idle_Hours',
        y='Engine_Load_Percent',
        z='Fuel_Consumption_Liters',
        color='Machine_Type',
        size='Operating_Hours_Actual',
        hover_name='Machine_ID',
        color_discrete_sequence=['#2563eb', '#10b981', '#f59e0b'],
        template='plotly_white'
    )
    fig_3d.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        height=480
    )
    st.plotly_chart(fig_3d, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: PREDICTIVE MAINTENANCE QUEUE ---
with tab_alerts:
    st.markdown("""
    <div class="content-card">
        <div class="card-header-tag">SYSTEM ALERTS</div>
        <div class="card-title">Predictive Maintenance Queue</div>
        <p style="font-size:0.85rem; color:#64748b; margin-top:-10px;">
            Telemetry algorithms flag units exceeding 85% engine load thresholds or having abnormal idle fuel dissipation.
        </p>
    """, unsafe_allow_html=True)
    
    alerts_df = filtered_df[filtered_df['Maintenance_Required'] == 'Yes'].sort_values('Engine_Load_Percent', ascending=False)
    
    if not alerts_df.empty:
        st.dataframe(
            alerts_df[['Machine_ID', 'Machine_Type', 'Date', 'Season', 'Engine_Load_Percent', 'Idle_Hours', 'Fuel_Consumption_Liters']],
            column_config={
                "Machine_ID": "Asset ID",
                "Machine_Type": "Category",
                "Engine_Load_Percent": st.column_config.ProgressColumn("Engine Load", format="%.1f%%", min_value=0, max_value=100),
                "Idle_Hours": st.column_config.NumberColumn("Idle Time (h)", format="%.1f"),
                "Fuel_Consumption_Liters": st.column_config.NumberColumn("Fuel (L)", format="%.1f"),
            },
            hide_index=True,
            use_container_width=True
        )
    else:
        st.success("🎉 All equipment units are operating under safe temperature and load thresholds.")
        
    st.markdown("</div>", unsafe_allow_html=True)
