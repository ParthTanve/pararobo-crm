import streamlit as st
import sqlite3
import base64

def init_db():
    conn = sqlite3.connect("proposals.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            proposal_name TEXT PRIMARY KEY,
            file_data BLOB,
            file_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_file_to_db(proposal_name, file_data, file_name):
    conn = sqlite3.connect("proposals.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO documents (proposal_name, file_data, file_name)
        VALUES (?, ?, ?)
    ''', (proposal_name, file_data, file_name))
    conn.commit()
    conn.close()

def get_file_from_db(proposal_name):
    conn = sqlite3.connect("proposals.db")
    cursor = conn.cursor()
    cursor.execute('SELECT file_data, file_name FROM documents WHERE proposal_name = ?', (proposal_name,))
    row = cursor.fetchone()
    conn.close()
    return row

@st.dialog("View Document", width="large")
def view_pdf_dialog(proposal_name):
    row = get_file_from_db(proposal_name)
    if row:
        file_data, file_name = row
        base64_pdf = base64.b64encode(file_data).decode('utf-8')
        
        
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf">'
        
        st.markdown(f"<h4 style='color: #333;'>{file_name}</h4>", unsafe_allow_html=True)
        st.markdown(pdf_display, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(label="📥 Download File", data=file_data, file_name=file_name, mime="application/pdf", use_container_width=True)
    else:
        st.error("No document found in database for this proposal. Please upload and submit first.")

def show_proposal_page():
    init_db()

    st.markdown("""
    <style>
    div[data-testid="stFileUploader"] {
        padding: 0px;
    }
    div[data-testid="stFileUploader"] > div {
        padding: 0px;
        min-height: 40px;
    }
    div[data-testid="stFileUploader"] > div > div > div {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #000000;'>📄 Quotation & Proposal</h1>", unsafe_allow_html=True)
    st.markdown("---")

    proposals = [
        "Real Estate", "FMCG", "Political", "Software", "AI Automation", 
        "Website", "Salons", "Cafes", "Resorts", "School and Colleges", 
        "MSEB", "Banks", "Hospitals and clinic", "Insurance"
    ]

    st.markdown("""
    <div style="display: flex; font-weight: bold; font-size: 18px; background-color: #F8F9FA; padding: 15px; border: 2px solid #000000; color: #000000;">
        <div style="flex: 2;">Proposal Name</div>
        <div style="flex: 2;">Upload Document</div>
        <div style="flex: 1; text-align: center;">Save Data</div>
        <div style="flex: 1; text-align: center;">View Document</div>
    </div>
    """, unsafe_allow_html=True)

    for idx, p in enumerate(proposals):
        col1, col2, col3, col4 = st.columns([2, 2, 1, 1], vertical_alignment="center")
        
        with col1:
            st.markdown(f"<p style='font-size: 16px; font-weight: 600; color: #000000; margin: 10px 0px 10px 15px;'>{p}</p>", unsafe_allow_html=True)
            
        with col2:
            uploaded_file = st.file_uploader("Upload", type=['pdf'], key=f"up_{idx}", label_visibility="collapsed")
            
        with col3:
            if st.button(" Submit", key=f"sub_{idx}", use_container_width=True):
                if uploaded_file is not None:
                    file_data = uploaded_file.getvalue()
                    save_file_to_db(p, file_data, uploaded_file.name)
                    st.success("Saved!")
                else:
                    st.warning("Upload First!")
                    
        with col4:
            if st.button(" View", key=f"view_{idx}", use_container_width=True):
                view_pdf_dialog(p)
                    
        st.markdown("<hr style='margin: 0px; border-color: #cccccc;'>", unsafe_allow_html=True)