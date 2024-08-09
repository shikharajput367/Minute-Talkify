import os
import json
from  fpdf import FPDF # pip install fpdf python-docx
from  docx import Document
from scripts.utils import read_contents,split
from prompts import minutes_prompt
from chat_prompt_new import create_llm
from talking_point import talking_point_generator
from generator import predict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st
import uuid  # Import uuid module for generating unique keys
import time 
from dataclasses import dataclass
from talking_context import talking_prompt
import plotly.graph_objects as go #pip install streamlit plotly transformers
import streamlit.components.v1 as components
from streamlit.components.v1 import html,components


def open_pdf_file(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
    st.write(pdf_bytes)
def submit(prompt):
        if uploaded_file is not None:
            #file_path = os.path.join('C:\\Users\\ajain2\\Downloads\\minutes_generator\\minutes_generator\\', uploaded_file.name)
        
            file_path = os.path.join('C:\\Users\\ssingh4\\Desktop\\minutes_generator\\', uploaded_file.name)
            file_content = read_contents(file_path)
        
        #user_input = st.session_state.user_message
        chunks = json.dumps(split(file_content))
        prompt1 = talking_prompt(chunks,prompt) #user_input
        response_path=predict(prompt1)
        #message=st.session_state.message
        #print(response_path)
        #type(response_path)
        #response_file_path='C:\\Users\\ajain2\\Downloads\\minutes_generator\\minutes_generator\\customer_conversation_input.txt'
        #create_text_file(response_path,response_file_path) 
        #bot_response = create_llm(prompt,response_file_path) 
        #if  message  :
        
        return response_path
def create_text_file(output,txt_file_path):
      with open(txt_file_path,'w') as f:
            f.write(output)

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
      

def create_pdf(output,pdf_file_path):
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)
        pdf.multi_cell(0,10,output)
        pdf.output(pdf_file_path)
    
def create_doc(output,doc_file_path):
        doc=Document()
        doc.add_paragraph(output)
        doc.save(doc_file_path)

def generate_mom(file_content,format_components):
        global output
        chunks = json.dumps(split(file_content))
        prompt = minutes_prompt(chunks,format_components)
        output1=predict(prompt)
        #print(prompt)
        #print(output1)
        return output1
        #output=st.text_area(label='MoM',value=predict(prompt),value=st.session_state.text,height=250) 
        #return output    
        #st.session_state.text=output
        # output=st.text_area(label='MoM',value=predict(prompt),height=250)

# Function to send email
def send_email(subject, body, recipients):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Example port, adjust as necessary
    smtp_username = 'guidelocal849@gmail.com'
    smtp_password = 'lfba kcfw zjky hkvp'

    # Create message
    
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipients, msg.as_string())

def page1():
    #background-color:purple;
    
    st.markdown("""
        <style>
        
        
        .stButton>button {
            width:100%;
            
            color:black;
        }   
        
        .title1 {
            
            color: black;
            font-weight: bold;
            font-size:40px;
        }  
        </style>
        """, unsafe_allow_html=True
        )

    st.markdown(f'<p class="title1">Minutes Generator</p>', unsafe_allow_html=True)
    #st.title("Minutes MasterMind")
    #st.markdown("Upload transcript file", unsafe_allow_html=True)
    #st.write('Upload transcript file')

    uploaded_file = st.sidebar.file_uploader("Upload transcript file", type="txt")

    col1,col2=st.sidebar.columns(2) 
    with col1:
          upload=st.button("Upload")
    with col2:
          clear=st.button('Clear')
    if upload:
          st.sidebar.success(f'file Uploaded: {uploaded_file.name}')
    if uploaded_file is not None:
        
        #string_data=uploaded_file.getvalue().decode("utf-8")
        #save_directory=tempfile.gettempdir()
        file_path = os.path.join('C:\\Users\\ssingh4\\Desktop\\minutes_generator\\', uploaded_file.name)
        file_content = read_contents(file_path)

        #st.text_area(label=file_path,value=file_content,height=250)
    options_for_first_dropdown = ['all', 'custom']

    # Define options for the second dropdown based on the first dropdown's selection
    options_for_second_dropdown = {
        'all': [],
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


    

    if 'text' not in st.session_state:
        st.session_state.text=""

    Generate_button=st.button(label='Generate minutes')    

    if Generate_button: 
            #with st.spinner(text="In progress"):
                        #time.sleep(3)
            if selection=='all':
                #a= st.write('this is the generated transcript..')
                    a=['Meeting Name', 'Date','Time', 'Attendees','Agenda','Important Discussion Details', 'Adjournment', 'Future Plans','Timelines']
                    st.session_state.text= generate_mom(file_content,a)
                    
                        

                
            if selection=='custom':
                    a=list(second_selection)
                    st.session_state.text= generate_mom(file_content,a)
                    
    text=st.text_area(label='MoM',value=st.session_state.text,height=350)
            
    # if selection=='custom':
            
        #    st.session_state.text= generate_mom(file_content)
            #st.text_area(label='MoM',value=output1,height=250)

    st.session_state.text=text
    #list1=['Download PDF','Download DOCX']
    #st.selectbox('Select an operation', list1)
    #st.button('Get file')
    #btn = st.button(label='generate minutes')
    

    
    
    if clear:
        st.session_state.text=""
        text=""
        st.rerun()
        

    list1=['Download PDF','Download DOCX']
    operation = st.sidebar.selectbox('Select an operation', list1)
    if st.sidebar.button('Submit'):
                if operation=='Download PDF':
                    pdf_file_path = os.path.join('C:\\Users\\ssingh4\\Desktop\\minutes_generator\\test_output.pdf')
                    #output='xyasad'
                    create_pdf(text,pdf_file_path)
                    ss=st.sidebar.success(f'PDF file created: {pdf_file_path}')
                    #link1='file:///C:/Users/ajain2/Downloads/minutes_generator/minutes_generator/test_output.pdf'
                    #st.markdown(f'<a href="{link1}" target="_blank">click me</a>',unsafe_allow_html=True)
                    #components.iframe(pdf_file_path,width=700,height=1000)
                if operation=='Download DOCX':
                    doc_file_path = os.path.join('C:\\Users\\ssingh4\\Desktop\\minutes_generator\\test_output.docx')
                    #output='xyasad'
                    create_doc(text,doc_file_path)
                    st.sidebar.success(f'Doc file created: {doc_file_path}')
                
    
    st.sidebar.write('Send Email')
    email_list=['aasthajain971@gmail.com','ajain2@automotivemastermind.com']
    recipients = st.sidebar.multiselect('Select Recipient email(s)', email_list)
                    #recipients=st.text_area(label='Recipient email(s)',value=st.session_state.text,height=250)
                    #recipients = st.text_input("Recipient email(s) (comma-separated)", "")
    greeting = "Hello Masterminds,\n\nPFB Minutes of Meeting: \n\n"
    closing = '\n\nBest regards,\nAastha Jain'

    

    body = greeting + text + closing
    #st.text_area(label='body_text',value=body)
    
    sendb=st.sidebar.button('Send')

    if sendb:
                        
                        subject = 'Meeting Minutes'
                        
                        #recipient_emails = [email.strip() for email in recipients.split(',')]
                        try:
                            send_email(subject, body,  recipients)
                            st.sidebar.success('Email sent successfully!')  # Show success message
                        except Exception as e:
                            st.error(f"Failed to send email: {str(e)}")  # Show error message               

    
    
@dataclass
class Message:
    actor: str
    payload: str 

def page2():
    
    st.markdown("""
        <style>
        .body{
                background-color:purple !important;
        }       
        .stButton>button {
            width:100%;
        }   
        .userMsg {
            color: #800080;
            font-style: italic;
            font-weight: bold;
            font-size:20px    
                
        }
        .botMsg {
                
            color: orange;     
            font-style: italic;
            font-weight: bold;
        }
        .title2 {
            color: black;
            font-weight: bold;
            
        }
        .title1 {
            color: black;
            font-weight: bold;
            font-size:40px
        }  
        </style>
        """, unsafe_allow_html=True)
    
    
    st.markdown('<script>document.getElementById("Message").scrollIntoView();</script>', unsafe_allow_html=True)

    global uploaded_file
    uploaded_file=st.sidebar.file_uploader("Upload Recording", type="txt")

    
    col1,col2=st.sidebar.columns(2)   
    with col1:
              
        Upload=st.button('  Upload  '+' '*20)
    with col2:
        clear=st.button('  clear  '+' '*20)
    
    
    

    if uploaded_file is not None:
            #file_path = os.path.join('C:\\Users\\ajain2\\Downloads\\minutes_generator\\minutes_generator\\', uploaded_file.name)
        
            file_path = os.path.join('C:\\Users\\ssingh4\\Desktop\\minutes_generator\\', uploaded_file.name)
            file_content = read_contents(file_path)
            if Upload : 
                #st.sidebar.write('You have uploaded:',uploaded_file.name)
                st.sidebar.success(f'file Uploaded: {uploaded_file.name}')
    #st.title("Generate Talking points and BPS")
    # Function to get response from your chatbot model
    st.markdown(f'<p class="title1">Talkify</p>', unsafe_allow_html=True)
    
    st.write('Hi! Please upload customer recording(txt) to generate talking points and behaviour prediction based on previous customer Interaction!')
    #st.write("Hello Mastermind. How can I assist you today?")
    #st.markdown(f'<p class="title2">Hello Mastermind. How can I assist you today?</p>', unsafe_allow_html=True)
    USER = "user"
    ASSISTANT = "ai"
    MESSAGES = "messages"
    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hello Mastermind. How can I assist you today?")]

    msg: Message
    for msg in st.session_state[MESSAGES]:
        st.chat_message(msg.actor).write(msg.payload)

    prompt: str = st.chat_input("Enter a prompt here")
    
    if prompt:
        st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
        st.chat_message(USER).write(prompt)
        response: str = submit(prompt)
        st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
        st.chat_message(ASSISTANT).write(response)
    
    
    
    if clear:
          st.session_state[MESSAGES]=[]
          st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hello Mastermind. How can I assist you today?")]
          st.rerun()
    
    st.sidebar.write("")
    st.sidebar.write("Redirect to Customer Dashboard")
    dashboard= st.sidebar.button(label="Customer Dashboard")
    if dashboard:
          open_page('http://localhost:3000/')
          #my_component = components.declare_component("my_component", path="frontend/build")
          #my_component = components.declare_component("my_component",  url='http://localhost:3000')
          #my_component(greeting="Hello", name="World")
          #link='check out this [link](http://localhost:3000/)'
          #st.markdown(link,unsafe_allow_html=True)
          
    
if __name__ == "__main__":
    
    
    st.set_page_config(layout="wide",page_title="Minute Generator", page_icon=":brain:",
    initial_sidebar_state="expanded")
    
    
    


    st.image("logo.png", width=300)
    st.sidebar.title("Navigation")
    page=st.sidebar.radio("Go to",('MoM Generator','Customer Insight'))

    if page=='MoM Generator':
        
        
        page1()
        #tab2.page2()
        
    if page=='Customer Insight':
        
             page2()
    
    
        