import streamlit as st
import pandas as pd

@st.dialog("Project Full Details")
def show_project_popup(project):
    st.markdown(f"<h3 style='text-align: center; color: #000000; margin-top:0px;'>{project['Project Name']}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"**Project Category:**<br>{project['Project Category']}", unsafe_allow_html=True)
    st.markdown(f"**Start Date:**<br>{project['Start Date'].strftime('%d:%m:%Y')}", unsafe_allow_html=True)
    st.markdown(f"**Description:**<br>{project['Description']}", unsafe_allow_html=True)
    st.markdown(f"**Client Name:**<br>{project['Client Name']}", unsafe_allow_html=True)
    st.markdown(f"**Tools and Language:**<br>{project['Tools and Language']}", unsafe_allow_html=True)
    st.markdown(f"**Assigned Employee:**<br>{project['Assigned Employee']}", unsafe_allow_html=True)
    st.markdown(f"**End Date:**<br>{project['Deadline Date'].strftime('%d:%m:%Y')}", unsafe_allow_html=True)
    st.markdown(f"**Current Progress:**<br>{project['Progress of Project']}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Close Details", use_container_width=True):
        if "proj_id" in st.query_params:
            del st.query_params["proj_id"]
        st.rerun()

def create_table(df, columns_to_show):
    html_table = "<table class='project-table'><thead><tr>"
    for col in columns_to_show:
        html_table += f"<th>{col}</th>"
    html_table += "</tr></thead><tbody>"
    
    for _, row in df.iterrows():
        html_table += "<tr>"
        for col in columns_to_show:
            if col == "Project Name":
                name_link = f"<a href='?page=Project%20Detail&proj_id={row['Project ID']}' target='_self'>{row['Project Name']}</a>"
                html_table += f"<td>{name_link}</td>"
            elif col in ["Start Date", "Deadline Date"]:
                html_table += f"<td>{row[col].strftime('%d:%m:%Y')}</td>"
            else:
                html_table += f"<td>{row[col]}</td>"
        html_table += "</tr>"
    html_table += "</tbody></table>"
    return html_table

def show_project_page():
    st.markdown("""
    <style>
    .project-table { width: 100%; border-collapse: collapse; background-color: #FFFFFF; color: #000000; margin-top: 15px; }
    .project-table th, .project-table td { border: 2px solid #000000; padding: 12px; text-align: left; }
    .project-table th { font-weight: bold; font-size: 16px; background-color: #F8F9FA; }
    .project-table a { color: #0000EE; text-decoration: underline; font-weight: bold; cursor: pointer; }
    
    div[data-testid="stTabs"] button[data-baseweb="tab"] { background-color: #f1f1f1; border: 1px solid #cccccc; padding: 10px 24px; }
    div[data-testid="stTabs"] button[aria-selected="true"] { background-color: #cccccc; font-weight: bold; }
    .unpaid { color: #ff0000; font-weight: bold; }
    .paid { color: #00b300; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #000000;'>📂 Project Detail</h1>", unsafe_allow_html=True)
    st.markdown("---")

    data = {
        "Project ID": ["PRJ001", "PRJ002", "PRJ003", "PRJ004", "PRJ005", "PRJ006", "PRJ007", "PRJ008", "PRJ009", "PRJ010"],
        "Project Name": ["AscendHub", "Aquatic Camouflage AI", "Bruno Chatbot", "Resume Parser Analyzer", "AWS Cloud Migration", "Advanced CRM Tracker", "Global SEO Campaign", "Secure Host Deployment", "E-commerce Web Portal", "ERP System Sync"],
        "Project Category": ["Mobile App", "Custom Software", "Custom Software", "Web App", "System Integration", "CRM", "Digital Marketing", "Domain and Hosting", "Web App", "System Integration"],
        "Revenue": [12500, 8200, 5000, 15000, 20000, 18000, 4500, 3000, 25000, 12000],
        "Paid": [10000, 2000, 5000, 0, 0, 0, 2000, 1500, 25000, 0],
        "Unpaid": [2500, 6200, 0, 15000, 20000, 18000, 2500, 1500, 0, 12000],
        "Progress of Project": ["75%", "90%", "85%", "40%", "10%", "5%", "60%", "15%", "100%", "0%"],
        "Deadline Date": ["2026-07-15", "2026-06-20", "2026-06-30", "2026-08-15", "2026-11-20", "2026-12-10", "2026-09-01", "2026-07-01", "2026-05-15", "2027-01-15"],
        "Start Date": ["10-Jan-2026", "05-Feb-2026", "12-Dec-2025", "01-Mar-2026", "15-Sep-2026", "01-Oct-2026", "01-Jun-2026", "01-May-2026", "01-Jan-2026", "10-Nov-2026"],
        "Description": ["Mobile app dev.", "AI Camouflage.", "NLP Chatbot.", "Deep learning parser.", "Migrating local servers to AWS Cloud.", "Setting up advanced CRM tracking.", "SEO and digital marketing strategy.", "Domain setup and cloud hosting.", "Full-stack e-commerce site.", "Syncing legacy ERP with modern APIs."],
        "Client Name": ["Internal", "Marine Research", "Empoweryou", "AB Infotech", "TechCorp Global", "RetailPro Inc.", "GrowthStart", "NetWeb LLC", "ShopEase", "Manufac Inc."],
        "Tools and Language": ["Flutter", "YOLOv8", "Gemini", "Python", "AWS, Docker", "React, Node.js", "Google Analytics, SEO Tools", "AWS Route 53, Nginx", "MERN Stack", "Python, REST APIs"],
        "Assigned Employee": ["Parth Tanve", "Parth Tanve", "Parth Tanve", "Afatab Khan", "TBD", "TBD", "Neha Gupta", "Vikram Verma", "Arya sir", "TBD"],
        "Status": ["Active", "Completed", "Completed", "Active", "Onboard", "Onboard", "Active", "Onboard", "Completed", "Pipeline"]
    }
    df = pd.DataFrame(data)
    
    df["Deadline Date"] = pd.to_datetime(df["Deadline Date"])
    df["Start Date"] = pd.to_datetime(df["Start Date"])

    if "proj_id" in st.query_params:
        p = df[df["Project ID"] == st.query_params["proj_id"]].iloc[0]
        show_project_popup(p)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["project active", "project deadline", "project complete", "project pipeline", "project category"])

    with tab1:
        st.markdown(create_table(df[df["Status"]=="Active"], ["Project Name", "Project Category", "Revenue", "Progress of Project", "Deadline Date"]), unsafe_allow_html=True)
        
    with tab2:
        df_sorted = df.sort_values(by=["Deadline Date", "Revenue"], ascending=[True, False])
        st.markdown(create_table(df_sorted, ["Project Name", "Project Category", "Deadline Date", "Revenue"]), unsafe_allow_html=True)
        
    with tab3:
        comp_df = df[df["Status"] == "Completed"].sort_values(by="Unpaid", ascending=False)
        html_table = "<table class='project-table'><thead><tr><th>Project Name</th><th>Project Category</th><th>Submission Date</th><th>Total Revenue</th><th>Paid</th><th>Unpaid</th></tr></thead><tbody>"
        for _, row in comp_df.iterrows():
            link = f"<a href='?page=Project%20Detail&proj_id={row['Project ID']}' target='_self'>{row['Project Name']}</a>"
            html_table += f"<tr><td>{link}</td><td>{row['Project Category']}</td><td>{row['Deadline Date'].strftime('%d:%m:%Y')}</td><td>${row['Revenue']}</td><td class='paid'>${row['Paid']}</td><td class='unpaid'>${row['Unpaid']}</td></tr>"
        html_table += "</tbody></table>"
        st.markdown(html_table, unsafe_allow_html=True)
        
    with tab4:
        pipe_df = df[df["Status"].isin(["Pipeline", "Onboard"])]
        html_table = "<table class='project-table'><thead><tr><th>Client Name</th><th>Project Name</th><th>Project Category</th><th>Description</th><th>Estimated Revenue</th><th>Estimated Start Date</th></tr></thead><tbody>"
        for _, row in pipe_df.iterrows():
            html_table += f"<tr><td>{row['Client Name']}</td><td>{row['Project Name']}</td><td>{row['Project Category']}</td><td>{row['Description']}</td><td class='paid'>${row['Revenue']}</td><td>{row['Start Date'].strftime('%d:%m:%Y')}</td></tr>"
        html_table += "</tbody></table>"
        st.markdown(html_table, unsafe_allow_html=True)
        
    with tab5:
        # 2 Columns for Side-by-Side Dropdowns
        col1, col2 = st.columns(2)
        
        with col1:
            category_options = ["All", "Digital Marketing", "Web App", "Mobile App", "CRM", "Custom Software", "System Integration", "Domain and Hosting"]
            selected_category = st.selectbox("Select Project Category", category_options)
            
        with col2:
            status_options = ["All", "Active", "Onboard", "Completed", "Pipeline"]
            selected_status = st.selectbox("Select Status", status_options)
        
        filtered_df = df.copy()
        
        # Apply Filters based on selections
        if selected_category != "All":
            filtered_df = filtered_df[filtered_df["Project Category"] == selected_category]
            
        if selected_status != "All":
            filtered_df = filtered_df[filtered_df["Status"] == selected_status]
        
        filtered_df = filtered_df.sort_values(by="Deadline Date", ascending=True)
        
        # Display the table or "no data" message
        if len(filtered_df) > 0:
            st.markdown(create_table(filtered_df, ["Project Name", "Project Category", "Status", "Start Date", "Deadline Date"]), unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: #888; font-size: 16px; padding: 10px; background: #eee; border-radius: 5px;'>No projects available for the selected filters.</p>", unsafe_allow_html=True)