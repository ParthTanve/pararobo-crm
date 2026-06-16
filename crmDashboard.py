import streamlit as st
import urllib.parse
import employeeDetail
import internDetail
import projectDetail
import taskDetail
import leadDetail
import clientDetail
import quotationAndProposal

current_page = st.query_params.get("page", "Dashboard")

def navigate(page_name):
    st.query_params.clear()
    st.query_params.page = page_name

st.set_page_config(page_title="CRM Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3, h4, h5, h6, p, span, div, label { color: #000000 !important; }
    hr { border-color: #000000 !important; }
    
    header[data-testid="stHeader"] {
        background-color: #FFFFFF !important;
    }
    header[data-testid="stHeader"] * {
        color: #000000 !important;
    }
    
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 3px solid #000000 !important; }
    [data-testid="stSidebar"] * { color: #000000 !important; }
    div[data-testid="stExpander"] { border: 2px solid #000000 !important; border-radius: 8px !important; background-color: #FFFFFF !important; }
    
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CCCCCC !important;
        border-radius: 6px !important;
        font-weight: 500 !important;
    }
    div.stButton > button:hover {
        border-color: #000000 !important;
        background-color: #F8F9FA !important;
    }
    
    .kpi-card {
        border: 3px solid #000000;
        border-radius: 8px; 
        padding: 20px; 
        background-color: #FFFFFF;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        height: 160px; 
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .kpi-card:hover {
        transform: scale(1.03);
        box-shadow: 8px 8px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

def create_clickable_kpi_card(title, value, delta, is_negative=False):
    delta_color = "#ff0000" if is_negative else "#00b300" 
    safe_title = urllib.parse.quote(title)
    
    html_code = f"""
    <a href="?page={safe_title}" target="_self" style="text-decoration: none; color: inherit; display: block;">
        <div class="kpi-card">
            <p style="margin: 0; font-size: 16px; font-weight: bold; color: #555555;">{title}</p>
            <h2 style="margin: 5px 0; font-size: 32px; color: #000000;">{value}</h2>
            <p style="margin: 0; font-size: 16px; font-weight: bold; color: {delta_color};">{delta}</p>
        </div>
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2>Menu</h2>", unsafe_allow_html=True)
    
    if st.button("📊 Dashboard", use_container_width=True):
        navigate("Dashboard")
        st.rerun()
        
    with st.expander("🧑‍💼 Employees Detail"):
        if st.button("View Employees", use_container_width=True):
            navigate("Employees Detail")
            st.rerun()
       
    with st.expander("🧑‍🎓 Interns Detail"):
        if st.button("View Intern", use_container_width=True):
            navigate("Intern Detail")
            st.rerun()
                    
    with st.expander("📂 Project Detail"):
        if st.button("View Projects", use_container_width=True):
            navigate("Project Detail")
            st.rerun()
            
    with st.expander("📝 Task"):
        if st.button("View Tasks", use_container_width=True):
            navigate("Task")
            st.rerun()
            
    with st.expander("🎯 Leads"):
        if st.button("View Leads", use_container_width=True):
            navigate("Lead Detail")
            st.rerun()
            
    with st.expander("🤝 Client Management"):
        if st.button("View Clients", use_container_width=True):
            navigate("Client Detail")
            st.rerun()

    with st.expander("📄 Quotation & Proposal"):
        if st.button("View Proposals", use_container_width=True):
            navigate("Quotation and Proposal")
            st.rerun()

kpi_pages = [
    "Total Leads", "Qualified Leads", "Active Clients", 
    "Revenue This Month", "Pending Payments", "Ongoing Projects", 
    "Team Utilization %", "Open Support Tickets", "Interns Active", 
    "Proposal Conversion Rate"
]

if current_page == "Dashboard":
    spacer_left, logo_col, text_col, spacer_right = st.columns([2.5, 1, 4, 2.5], vertical_alignment="center")
    
    with logo_col:
        st.image("companybwedit.png", width=120)
    with text_col:
        st.image("company text .png", width=500)

    st.markdown("<h3 style='text-align: left; color: #555555; margin-top: 15px;'>📊 CRM Dashboard</h3>", unsafe_allow_html=True)
    st.markdown("---")

    row1_cols = st.columns(5)
    with row1_cols[0]:
        create_clickable_kpi_card("Total Leads", "1,245", "↑ 12%")
    with row1_cols[1]:
        create_clickable_kpi_card("Qualified Leads", "842", "↑ 5%")
    with row1_cols[2]:
        create_clickable_kpi_card("Active Clients", "150", "↑ 3")
    with row1_cols[3]:
        create_clickable_kpi_card("Revenue This Month", "$45,200", "↑ $2,400")
    with row1_cols[4]:
        create_clickable_kpi_card("Pending Payments", "$8,400", "↓ -$400")

    row2_cols = st.columns(5)
    with row2_cols[0]:
        create_clickable_kpi_card("Ongoing Projects", "24", "↑ 2")
    with row2_cols[1]:
        create_clickable_kpi_card("Team Utilization %", "85%", "↑ 4%")
    with row2_cols[2]:
        create_clickable_kpi_card("Open Support Tickets", "12", "↓ -3", is_negative=True)
    with row2_cols[3]:
        create_clickable_kpi_card("Interns Active", "5", "↑ 1")
    with row2_cols[4]:
        create_clickable_kpi_card("Proposal Conversion Rate", "68%", "↑ 2.5%")

elif current_page == "Employees Detail":
    employeeDetail.show_employee_page()

elif current_page == "Intern Detail":
    internDetail.show_intern_page()

elif current_page == "Task":
    taskDetail.show_task_page()

elif current_page == "Project Detail":
    projectDetail.show_project_page()

elif current_page == "Lead Detail":
    leadDetail.show_lead_page()

elif current_page == "Client Detail":
    clientDetail.show_client_page()

elif current_page == "Quotation and Proposal":
    quotationAndProposal.show_proposal_page()

elif current_page in kpi_pages:
    st.markdown(f"<h1>Welcome to {current_page}</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"<h3>Detailed view and analytics for {current_page} will be displayed here.</h3>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("⬅ Back to Dashboard", use_container_width=False):
        navigate("Dashboard")
        st.rerun()