import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="MapTech Survey Solutions - Working Model", layout="wide", page_icon="🚁")

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/color/96/000000/drone.png", width=100)
st.sidebar.title("MapTech Solutions")
st.sidebar.subheader("Digital Survey Portal")

page = st.sidebar.radio("Navigate", ["📊 executive Dashboard", "🧮 ROI Calculator", "🚀 Survey Simulator", "📋 Project Tracker"])

st.sidebar.divider()
st.sidebar.info("This is an interactive model based on Case Study 156: Mapping and Surveying Drones.")

# Common constants
DRONE_SPEED_MULTIPLIER = 5      # Drones are ~5x faster
DRONE_COST_REDUCTION = 0.45     # 45% cost reduction
MANUAL_ACCURACY_BASE = 88
DRONE_ACCURACY_BASE = 98

if page == "📊 executive Dashboard":
    st.title("🚁 MapTech Executive Dashboard")
    st.markdown("### Accelerating Surveying with AI & Drones")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg. Manual Survey Time", "21 Days", delta="Current", delta_color="off")
    col2.metric("Projected Drone Time", "4 Days", delta="-80% Time", delta_color="normal")
    col3.metric("Projected Cost Savings", "45%", delta="₹18L Annual", delta_color="normal")
    
    st.divider()
    
    st.subheader("Why Transition to Drones?")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Current Challenges (Manual):**
        * ⏳ **Slow Turnaround:** 2-4 weeks per project.
        * 💸 **High OPEX:** ₹40 Lakhs annually on labor & transit.
        * 📉 **Errors & Delays:** Affecting project timelines.
        * 😡 **Customer Churn:** 17% increase in client complaints.
        """)
    with c2:
        st.markdown("""
        **Drone Solutions (Proposed):**
        * ⚡ **Rapid Surveying:** Days instead of weeks.
        * 🎯 **High Accuracy:** AI-processed geospatial data.
        * 🏗️ **Deliverables:** Accurate 3D models and terrain maps.
        * 🤝 **Client Retention:** Faster delivery improves satisfaction and CLV.
        """)

elif page == "🧮 ROI Calculator":
    st.title("🧮 Interactive ROI Calculator")
    st.markdown("Calculate the projected savings and Net Benefit of investing in the Drone System.")
    
    st.sidebar.header("Calculator Inputs")
    current_opex = st.sidebar.number_input("Current Annual OPEX (₹)", value=4000000, step=100000)
    investment = st.sidebar.number_input("Drone Investment (₹)", value=7000000, step=100000)
    expected_reduction = st.sidebar.slider("Expected Cost Reduction (%)", min_value=10, max_value=80, value=45) / 100.0
    
    annual_savings = current_opex * expected_reduction
    net_benefit_yr1 = annual_savings - investment
    payback_period = investment / annual_savings if annual_savings > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Annual Savings", f"₹{annual_savings:,.0f}", f"{expected_reduction*100}% reduction")
    col2.metric("Year 1 Net Benefit", f"₹{net_benefit_yr1:,.0f}", "CapEx Impact", delta_color="inverse")
    col3.metric("Estimated Payback Period", f"{payback_period:.1f} Years", "ROI Timeframe")
    
    st.divider()
    st.subheader("10-Year Financial Projection")
    
    years = np.arange(1, 11)
    # Manual cumulated cost
    manual_cumulative = current_opex * years
    # Drone cumulated cost: Investment + (Reduced OPEX * years)
    drone_opex = current_opex * (1 - expected_reduction)
    drone_cumulative = investment + (drone_opex * years)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(years, manual_cumulative, label="Manual Surveying (Cumulative Cost)", color='red', marker='o')
    ax.plot(years, drone_cumulative, label="Drone Surveying (Cumulative Cost)", color='green', marker='o')
    ax.fill_between(years, manual_cumulative, drone_cumulative, where=(manual_cumulative > drone_cumulative), interpolate=True, color='green', alpha=0.1, label="Net Cash Savings")
    
    ax.set_xlabel("Years")
    ax.set_ylabel("Cumulative Cost (₹)")
    ax.set_title("Long-Term Financial Benefit of Drone Investment")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig)

elif page == "🚀 Survey Simulator":
    st.title("🚀 Live Survey Simulation Model")
    st.markdown("Simulate a surveying project to see the operational difference between Manual and Drone methods.")
    
    with st.form("survey_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            project_name = st.text_input("Project Name", "Highway expansion Sector 4")
        with col2:
            area_size = st.number_input("Survey Area (Hectares)", min_value=10, max_value=500, value=50)
        with col3:
            complexity = st.selectbox("Terrain Complexity", ["Low", "Medium", "High"])
            
        method = st.radio("Select Surveying Method", ["Traditional Manual (Total Station/GPS)", "AI-Enabled Drone Mapping"], horizontal=True)
        
        submitted = st.form_submit_button("Start Survey Project")
        
    if submitted:
        st.divider()
        st.subheader(f"Processing Project: {project_name}")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        if "Manual" in method:
            # Simulate slow manual process
            total_days = int(area_size * 0.4)
            if complexity == "Medium": total_days = int(total_days * 1.5)
            if complexity == "High": total_days = int(total_days * 2.0)
            
            for i in range(100):
                time.sleep(0.02) # Slower simulation
                progress_bar.progress(i + 1)
                if i == 20: status_text.text("Status: Mobilizing field engineers...")
                elif i == 40: status_text.text("Status: Facing weather delays in field...")
                elif i == 70: status_text.text("Status: Manually recording waypoints...")
                elif i == 90: status_text.text("Status: Entering data into CAD software...")
            
            accuracy = max(70, MANUAL_ACCURACY_BASE - (area_size * 0.05))
            satisfaction = max(2, 10 - (total_days / 10))
            
        else:
            # Simulate fast drone process
            total_days = int(max(1, (area_size * 0.4) / DRONE_SPEED_MULTIPLIER))
            if complexity == "High": total_days += 1
            
            for i in range(100):
                time.sleep(0.005) # Much faster simulation
                progress_bar.progress(i + 1)
                if i == 20: status_text.text("Status: Programming autonomous flight path...")
                elif i == 50: status_text.text("Status: Drone capturing high-res aerial imagery...")
                elif i == 80: status_text.text("Status: AI processing geospatial & 3D models...")
            
            accuracy = DRONE_ACCURACY_BASE
            satisfaction = min(10, 10 - (total_days / 10))
            
        status_text.text("✅ Survey Complete!")
        
        # Display Results
        st.success("Project Successfully Mapped & Surveyed.")
        
        rc1, rc2, rc3 = st.columns(3)
        rc1.metric("Time Taken", f"{total_days} Days")
        rc2.metric("Mapping Accuracy", f"{accuracy:.1f} %")
        rc3.metric("Client Satisfaction Score", f"{satisfaction:.1f} / 10")
        
        if "Drone" in method:
            st.info("💡 **AI Data Generated:** Point Cloud Data, Orthomosaic Map, 3D Terrain Model.")

elif page == "📋 Project Tracker":
    st.title("📋 CRM & Project Tracker")
    st.markdown("Track how surveying methods impact client deliverables and overall satisfaction.")
    
    # Mock database
    data = {
        "Project ID": ["PRJ-101", "PRJ-102", "PRJ-103", "PRJ-104", "PRJ-105"],
        "Client": ["Apex Builders", "Govt. Infra Dept", "Skyline Developers", "Metro Rail Corp", "Green Energy Ltd"],
        "Method": ["Manual", "Manual", "Drone AI", "Drone AI", "Manual"],
        "Area (ha)": [120, 300, 150, 80, 200],
        "Est. Delivery": ["Delayed (3 Weeks)", "Delayed (4 Weeks)", "On Time (3 Days)", "On Time (2 Days)", "Delayed (5 Weeks)"],
        "Client Status": ["Frustrated ⚠️", "Escalated ⛔", "Highly Satisfied ⭐", "Repeat Customer 🌟", "Churn Risk 🔴"]
    }
    
    df_projects = pd.DataFrame(data)
    
    # Styled dataframe
    def color_status(val):
        color = 'white'
        if 'Delayed' in val: color = '#ffcccc'
        elif 'On Time' in val: color = '#ccffcc'
        if 'Frustrated' in val or 'Escalated' in val or 'Churn' in val: color = '#ffcccc'
        elif 'Satisfied' in val or 'Repeat' in val: color = '#ccffcc'
        return f'background-color: {color}; color: black'

    st.dataframe(df_projects.style.map(color_status, subset=['Est. Delivery', 'Client Status']), use_container_width=True)
    
    st.warning("**CRM Alert:** 17% increase in client complaints directly linked to manual survey delays. Transitioning to digital deliverables (Drone AI) has shown a 100% on-time delivery rate in pilot projects.")
