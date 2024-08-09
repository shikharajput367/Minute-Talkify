import streamlit as st

# Title of the page

st.set_page_config(page_title="Minute MasterMind", page_icon=":brain:")

# Display a logo at the top (make sure to replace 'logo.png' with the path to your actual logo file)
st.image("logo.png", width=300)

# Display the title
st.title("Minutes MasterMind")

def page1():
    st.markdown("Upload transcript file", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type="txt")

    options_for_first_dropdown = ['all', 'custom']

    # Define options for the second dropdown based on the first dropdown's selection
    options_for_second_dropdown = {
        'all': ['all'],
        'custom': ['Meeting Name', 'Date','Time', 'Attendees','Agenda','Important Discussion Details', 'Adjournment', 'Future Plans','Timelines']
    }

    # First dropdown
    selection = st.selectbox('Select Entities', options_for_first_dropdown)

    # Second dropdown whose options depend on the first dropdown's selection
    if selection:
        # Get the corresponding options for the second dropdown
        options = options_for_second_dropdown[selection]
        # Display the second dropdown
        second_selection = st.multiselect('Select values to be inferred', options)


    st.markdown("""
    <style>
    .stMarkdown { margin-bottom: -20px; }
    .stFileUploader { margin-top: -20px; }
    button {
        font-size: 20px !important;
        height: 3em !important;
        width: 100% !important;
    }
    .stFileUploader button {
                padding: 0.25rem 0.5rem; /* Smaller padding */
                font-size: 12px; /* Smaller font size */
            }
    </style>
    """, unsafe_allow_html=True)



    # Two buttons side by side with increased size
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Generate'):
            a= st.write('this is the generated transcript..')
            
            

    with col2:
        if st.button('Clear'):
            st.write('Clearing..')

    list1=['View','Download PDF','Download DOCX']
    st.selectbox('Select an operation', list1)
    st.button('Get file')

def page2():
    st.write('new page 2')

st.slidebar.title("Navigation")
page=st.slidebar.radio("Go to",('Page 1','Page 2'))

if page=='Page 1':
    page1()
if page=='Page 2':
    page2()