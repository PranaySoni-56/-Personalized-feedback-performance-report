import streamlit as st
import time

# --- Setup & Configuration ---
st.set_page_config(page_title="AI Performance Feedback", page_icon="📈", layout="centered")

st.title("📈 AI Performance Feedback Generator")
st.markdown("Transform raw metrics and bullet points into professional, constructive performance reviews instantly.")

# --- Input Form ---
with st.form("feedback_form"):
    st.subheader("Employee Data Input")
    
    col1, col2 = st.columns(2)
    with col1:
        emp_name = st.text_input("Employee Name", "Sarah Jenkins")
        role = st.text_input("Role/Title", "Data Scientist")
    with col2:
        manager_name = st.text_input("Manager Name", "Pranay Soni")
        review_period = st.selectbox("Review Period", ["Q1 2026", "Q2 2026", "Mid-Year 2026", "Annual 2026"])
    
    st.divider()
    
    # Performance Metrics
    score = st.slider("Overall KPI Achievement (%)", 0, 100, 88)
    
    strengths = st.multiselect(
        "Key Strengths (Select up to 3)", 
        ["Python Programming", "Model Deployment", "Team Communication", "Problem Solving", "Meeting Deadlines", "Client Presentations"],
        default=["Python Programming", "Problem Solving"]
    )
    
    improvements = st.multiselect(
        "Areas for Improvement", 
        ["Code Documentation", "Public Speaking", "Time Management", "Cross-team Collaboration"],
        default=["Code Documentation"]
    )
    
    custom_notes = st.text_area("Additional Manager Notes", "Sarah did a great job migrating the legacy database, but she needs to make sure her code is commented so the junior devs can understand it.")

    submit_button = st.form_submit_button("Generate Personalized Report", type="primary")

# --- AI Generation Logic ---
if submit_button:
    st.divider()
    st.subheader("⚙️ System Output")
    
    # CTO Flex: Show the prompt that WOULD be sent to the LLM
    with st.expander("View Backend LLM Prompt (For CTO Architecture Review)"):
        st.code(f"""
        System: You are an expert HR professional. Write a constructive, empathetic performance review.
        Data Context:
        - Employee: {emp_name} ({role})
        - Reviewer: {manager_name}
        - KPI Score: {score}%
        - Strengths: {', '.join(strengths)}
        - Areas to Improve: {', '.join(improvements)}
        - Context: {custom_notes}
        
        Task: Generate a 3-paragraph professional review structured as: 1) Achievements, 2) Growth Areas, 3) Looking Forward.
        """, language="text")

    with st.spinner("Synthesizing data and drafting review..."):
        time.sleep(2) # Simulate API latency
        
        # Simulated LLM Output
        st.success(f"✅ Official {review_period} Feedback Report Generated")
        
        st.markdown(f"""
        ### **Performance Review: {emp_name}**
        **Role:** {role} | **Period:** {review_period} | **Reviewer:** {manager_name}
        **Overall KPI Score:** {score}/100
        
        ---
        
        #### **1. Achievements & Strengths**
        {emp_name} has shown strong performance during this review cycle, achieving an impressive {score}% on core KPIs. Notably, {emp_name}'s expertise in {strengths[0]} and {strengths[1] if len(strengths) > 1 else 'general technical execution'} has been a massive asset to the team. A specific highlight was the successful migration of the legacy database, which was executed flawlessly and showcased excellent problem-solving capabilities.
        
        #### **2. Areas for Growth & Development**
        While technical execution is a clear strength, the primary focus for the next quarter should be on {improvements[0]}. As we scale the engineering team, it is crucial that all complex codebases are thoroughly commented. Ensuring that junior developers can easily read and adapt the work will amplify {emp_name}'s impact and establish them as a technical leader on the team.
        
        #### **3. Looking Forward**
        Overall, {emp_name} is a highly valued member of the organization. By maintaining their current momentum and dedicating time to improve documentation practices, I am confident we will see even greater leadership and impact in the upcoming quarter. 
        """)
