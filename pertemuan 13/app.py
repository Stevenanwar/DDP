import streamlit as st
 


st.write('hello')

dashboard = st.Page("./page/dashboard.py", title="Dashboard")
nabung = st.Page("./page/nabung.py", title="nabung")

pg = st.navigation({
    "Dashboard": [dashboard],
    "Nabung": [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []
pg.run()
