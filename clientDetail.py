import streamlit as st
import pandas as pd
import datetime

@st.dialog("Client Full Details")
def show_client_popup(client):
    st.markdown(f"<h3 style='text-align: center; color: #000000; margin-top:0px;'>{client['Client Name']}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"**🏢 Company Information:**<br>{client['Company Information']}", unsafe_allow_html=True)
    st.markdown(f"**📞 Contacts:**<br>{client['Contacts']}", unsafe_allow_html=True)
    st.markdown(f"**🧾 GST Details:**<br>{client['GST Details']}", unsafe_allow_html=True)
    st.markdown(f"**📍 Billing Address:**<br>{client['Billing Address']}", unsafe_allow_html=True)
    st.markdown(f"**🤝 Agreements:**<br>{client['Agreements']}", unsafe_allow_html=True)
    st.markdown(f"**📄 Documents:**<br>{client['Documents']}", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Close Details", use_container_width=True):
        if "client_id" in st.query_params:
            del st.query_params["client_id"]
        st.rerun()

def create_info_table(df):
    html_table = """
    <style>
    .client-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #FFFFFF;
        color: #000000;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .client-table th, .client-table td {
        border: 2px solid #000000;
        padding: 12px;
        text-align: left;
    }
    .client-table th {
        font-weight: bold;
        font-size: 16px;
        background-color: #F8F9FA;
    }
    .client-table a {
        color: #0000EE;
        text-decoration: underline;
        font-weight: bold;
        cursor: pointer;
    }
    </style>
    <table class="client-table">
        <thead>
            <tr>
                <th>Client Name</th>
                <th>Project Name</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in df.iterrows():
        status_color = "#00b300" if row['Status'] == 'Active' else "#ff9900"
        link = f"<a href='?page=Client%20Detail&client_id={row['Client ID']}' target='_self'>{row['Client Name']}</a>"
        html_table += "<tr>"
        html_table += f"<td>{link}</td>"
        html_table += f"<td>{row['Project Name']}</td>"
        html_table += f"<td style='color: {status_color}; font-weight: bold;'>{row['Status']}</td>"
        html_table += "</tr>"
    html_table += "</tbody></table>"
    return html_table

def create_team_table(df):
    html_table = """
    <table class="client-table">
        <thead>
            <tr>
                <th>Project Name</th>
                <th>Status</th>
                <th>Start Date</th>
                <th>End Date</th>
                <th>Team Lead</th>
                <th>Team Members</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in df.iterrows():
        if row['Status'] == 'Completed':
            status_color = "#888888"
        elif row['Status'] == 'Onboard':
            status_color = "#ff9900"
        else:
            status_color = "#00b300"
            
        html_table += "<tr>"
        html_table += f"<td><strong>{row['Project Name']}</strong></td>"
        html_table += f"<td style='color: {status_color}; font-weight: bold;'>{row['Status']}</td>"
        html_table += f"<td>{row['Start Date']}</td>"
        html_table += f"<td>{row['End Date']}</td>"
        html_table += f"<td style='color: #0000EE; font-weight: bold;'>{row['Team Lead']}</td>"
        html_table += f"<td>{row['Team Members']}</td>"
        html_table += "</tr>"
    html_table += "</tbody></table>"
    return html_table

def show_client_page():
    st.markdown("""
    <style>
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        font-size: 20px !important;
        padding: 15px 40px !important;
        background-color: #f1f1f1 !important;
        border: 2px solid #cccccc !important;
        border-bottom: none !important;
        border-radius: 8px 8px 0px 0px !important;
        color: #000000 !important;
        margin-right: 5px !important;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #cccccc !important;
        font-weight: bold !important;
        border-color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #000000;'>🤝 Client Management</h1>", unsafe_allow_html=True)
    st.markdown("---")

    info_data = {
        "Client ID": ["CL001", "CL002", "CL003", "CL004"],
        "Client Name": [
            "Dr. Ananya Sharma (Marine Research Inst.)", 
            "Rahul Verma (Empoweryou Tech)", 
            "Sneha Patil (Global AI)", 
            "John Doe (RetailPro Inc.)"
        ],
        "Project Name": ["Aquatic Camouflage AI", "Bruno Chatbot", "Resume Parser Analyzer", "CRM Integration Setup"],
        "Status": ["Active", "Active", "Active", "Onboarding"],
        "Company Information": [
            "Leading research institute focusing on marine biology and oceanography.",
            "EdTech startup focusing on student skill empowerment.",
            "IT services company specializing in enterprise software.",
            "Global retail chain upgrading their internal CRM."
        ],
        "Contacts": [
            "Dr. Ananya Sharma (+91 9876543210)<br>Rajiv Menon (+91 9988776655)",
            "Rahul Verma (+91 8877665544)",
            "Sneha Patil (+91 7766554433)",
            "John Doe (+1 415-555-0198)"
        ],
        "GST Details": ["27AAACM1234N1Z5", "27BBBCM5678P1Z2", "27CCDDM9012Q1Z8", "International (N/A)"],
        "Billing Address": [
            "12/A, Ocean View Tech Park, Mumbai, 400001",
            "3rd Floor, Innovation Hub, Pune, 411001",
            "Sector 15, IT City, Bangalore, 560100",
            "450 Retail Avenue, San Francisco, CA 94105"
        ],
        "Agreements": ["NDA Signed, SLA Active", "Service Contract Signed", "MOU Signed", "Contract Pending Approval"],
        "Documents": ["Company_Reg.pdf, Tax_Cert.pdf", "GST_Certificate.pdf", "Vendor_Form_Signed.pdf", "Requirements_Doc.pdf"]
    }
    df_info = pd.DataFrame(info_data)

    if "client_id" in st.query_params:
        client_id = st.query_params["client_id"]
        if client_id in df_info["Client ID"].values:
            selected_client = df_info[df_info["Client ID"] == client_id].iloc[0]
            show_client_popup(selected_client)

    tab1, tab2 = st.tabs(["Client Information", "Client Timeline"])

    with tab1:
        st.markdown(create_info_table(df_info), unsafe_allow_html=True)

    with tab2:
        st.markdown("<h3 style='color: #333;'>📅 Filter Projects by Date</h3>", unsafe_allow_html=True)
        
        col_date1, col_date2 = st.columns(2)
        with col_date1:
            filter_start = st.date_input("Select Start Date", datetime.date(2025, 11, 1))
        with col_date2:
            filter_end = st.date_input("Select End Date", datetime.date(2026, 12, 31))

        team_data = {
            "Project Name": ["Legacy Data Migration", "Aquatic Camouflage AI", "Bruno Chatbot", "Resume Parser Analyzer", "CRM Integration Setup"],
            "Status": ["Completed", "Active", "Active", "Active", "Onboard"],
            "Start Date": ["01-Nov-2025", "05-Jan-2026", "12-Dec-2025", "01-Mar-2026", "01-Jun-2026"],
            "End Date": ["15-Jan-2026", "20-Feb-2026", "30-Jun-2026", "15-Aug-2026", "10-Dec-2026"],
            "Team Lead": ["Arya sir", "Parth Tanve", "Parth Tanve", "Parth Tanve", "Afatab Khan"],
            "Team Members": ["Vikram Verma", "Vikram Verma, Arya sir", "Neha Gupta, Anjali Desai", "Rohan Mehta, Sonal Jain", "Karan Patel, Pooja Reddy"]
        }
        df_team = pd.DataFrame(team_data)
        
        df_team['Start_DT'] = pd.to_datetime(df_team['Start Date']).dt.date
        df_team['End_DT'] = pd.to_datetime(df_team['End Date']).dt.date
        
        mask = (df_team['Start_DT'] <= filter_end) & (df_team['End_DT'] >= filter_start)
        filtered_df = df_team[mask].copy()
        
        comp_count = len(filtered_df[filtered_df['Status'] == 'Completed'])
        act_count = len(filtered_df[filtered_df['Status'] == 'Active'])
        onb_count = len(filtered_df[filtered_df['Status'] == 'Onboard'])
        
        if "status_filter" not in st.session_state:
            st.session_state.status_filter = "All"
            
        status_filter = st.session_state.status_filter

        act_bg = "#e3f2fd" if status_filter == "Active" else "#ffffff"
        onb_bg = "#fff3e0" if status_filter == "Onboard" else "#ffffff"
        comp_bg = "#f5f5f5" if status_filter == "Completed" else "#ffffff"

        css = f"""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
            border-left: 6px solid #3498db !important;
            background-color: {act_bg} !important;
            height: 85px !important;
            border-radius: 8px !important;
            border: 1px solid #ddd !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05) !important;
            transition: all 0.3s ease !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) button p {{
            font-size: 20px !important;
            font-weight: bold !important;
            color: #3498db !important;
        }}
        
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{
            border-left: 6px solid #ff9900 !important;
            background-color: {onb_bg} !important;
            height: 85px !important;
            border-radius: 8px !important;
            border: 1px solid #ddd !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05) !important;
            transition: all 0.3s ease !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) button p {{
            font-size: 20px !important;
            font-weight: bold !important;
            color: #ff9900 !important;
        }}
        
        div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {{
            border-left: 6px solid #888888 !important;
            background-color: {comp_bg} !important;
            height: 85px !important;
            border-radius: 8px !important;
            border: 1px solid #ddd !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05) !important;
            transition: all 0.3s ease !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:nth-child(3) button p {{
            font-size: 20px !important;
            font-weight: bold !important;
            color: #888888 !important;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"Active Projects: {act_count}", use_container_width=True):
                st.session_state.status_filter = "Active" if status_filter != "Active" else "All"
                st.rerun()

        with col2:
            if st.button(f"Onboard Projects: {onb_count}", use_container_width=True):
                st.session_state.status_filter = "Onboard" if status_filter != "Onboard" else "All"
                st.rerun()

        with col3:
            if st.button(f"Completed Projects: {comp_count}", use_container_width=True):
                st.session_state.status_filter = "Completed" if status_filter != "Completed" else "All"
                st.rerun()

        st.markdown("<h4 style='color: #333; margin-top: 25px; margin-bottom: 10px;'>📌 Client Projects</h4>", unsafe_allow_html=True)
        
        if status_filter != "All":
            bars_df = filtered_df[filtered_df['Status'] == status_filter]
            
        else:
            bars_df = filtered_df
        
        active_colors = ["#3498db", "#2ecc71", "#9b59b6", "#e84393", "#00cec9"]
        onboard_colors = ["#ff9900", "#e67e22", "#d35400", "#f39c12"]
        
        act_idx = 0
        onb_idx = 0
        
        bars_html = '<div style="margin-bottom: 30px;">'
        if len(bars_df) == 0:
            bars_html += f'<p style="color: #888; font-size: 16px; padding: 10px; background: #eee; border-radius: 5px;">No {status_filter if status_filter != "All" else ""} projects available in this date range.</p>'
        else:
            for _, row in bars_df.iterrows():
                status = row['Status']
                if status == 'Completed':
                    bg_color = "#888888"
                elif status == 'Active':
                    bg_color = active_colors[act_idx % len(active_colors)]
                    act_idx += 1
                else:
                    bg_color = onboard_colors[onb_idx % len(onboard_colors)]
                    onb_idx += 1
                
                bars_html += f'<div style="background-color: {bg_color}; color: #ffffff; padding: 14px 18px; margin-bottom: 12px; border-radius: 6px; box-shadow: 2px 2px 5px rgba(0,0,0,0.15); display: flex; justify-content: space-between; align-items: center;">'
                bars_html += f'<div style="font-size: 16px; font-weight: bold;">{row["Project Name"]} <span style="font-size: 12px; font-weight: normal; background: rgba(255,255,255,0.25); padding: 3px 8px; border-radius: 4px; margin-left: 10px;">{status}</span></div>'
                bars_html += f'<div style="font-size: 15px; font-weight: 500; background: rgba(0,0,0,0.15); padding: 4px 10px; border-radius: 4px;">📅 {row["Start Date"]} &nbsp;➔&nbsp; {row["End Date"]}</div>'
                bars_html += '</div>'
                
        bars_html += "</div>"
        st.markdown(bars_html, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #333;'>👥 Project Teams & Deadlines</h3>", unsafe_allow_html=True)
        st.markdown(create_team_table(filtered_df), unsafe_allow_html=True)