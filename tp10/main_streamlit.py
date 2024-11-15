import streamlit as st
from CustomerDAO import CustomerDAO

# streamlit run .\main_streamlit.py
def main():
    st.set_page_config(layout='wide')
    with CustomerDAO(r"..\customers_db.db") as dao:
        customers = list(dao.find_all())
    
    st.write('# Le titre')
    st.write('Hello World')
    name = st.text_input("FirstName", "")
    if st.button("Say hello"):
        st.write("Hello", name)
    
    st.dataframe(customers,hide_index=True,use_container_width=True)

if __name__=='__main__':
    main()
