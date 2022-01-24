import streamlit as st
import webbrowser
from datetime import time as timeline
import pywhatkit as kit
gcolor="#112233"
pcolor="#52BD78"

st.markdown("""<style> 
                [data-testid="stToolbar"] > div:first-child{display:None; }
                div.element-container{margin: 0px 0px 1rem;}
                div.stSlider > div{width: 580px; margin-left:auto;margin-right:auto; max-width:85vw;}
                div.block-container{padding: 1rem 1rem 10rem;}
            </style>""", unsafe_allow_html=True)

st.markdown('<h1 style="color:{};text-align: center;font-size: 42px;">Send Custom WhatsApp Messages</h1>'.format(pcolor),unsafe_allow_html=True)
st.markdown('<ul><li>Make Sure Your Computer and Network is On for Scheduled Time.</li><li>Ensure that You have logged in to Whatsapp Web in Your Browser. (No need to keep Tab Open)</li></ul>',unsafe_allow_html=True)
st.write('<style>div.row-widget.stTextInput > div{flex-direction:row;justify-content:space-around;}div.row-widget.stTextInput > label{font-size: 20px !important;margin-bottom: 0px; text-align:center; color:{pcolor};}</style>', unsafe_allow_html=True)
if(st.button("Log in to WhatsApp Web")):
    webbrowser.open("https://web.whatsapp.com/")

n=(st.text_input("Enter Contact (Mobile Number) Here",0))
n.replace(" ","")
n=n.lstrip('0')
if(len(n)!=10):
    st.warning("Enter a Valid 10 Digit Mobile No. to Continue")
    st.stop()
n="+91"+n
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content:space-around;}div.row-widget.stRadio > label{font-size: 20px !important;margin-bottom: 0px;text-align:center; color:pcolor;}</style>', unsafe_allow_html=True)
genre = st.radio("Type Of Message : ",('BirthDay Wish', 'Marriage Anniversary Wish', 'General Message'))
st.write('<style>div.stSlider > div{flex-direction:row;justify-content:space-around;text-align:left;}div.stSlider > label{font-size: 20px !important;margin-bottom: 0px;text-align:center; color:pcolor;}</style>', unsafe_allow_html=True)
Time = st.slider("Time of Message:",value=(timeline(0, 0)))
element = st.empty()
message='Hi!'
if genre == 'BirthDay Wish':
        cust_bday = element.checkbox("Custom Bday Message")
        if(cust_bday):
            message='Wishing You a Very Happy Birthday!🎂\nMay You Have a Happy Year Ahead. Wishing You Health and Prosperity!💞\nCelebrate the Day 🥂'
elif genre == 'Marriage Anniversary Wish':
        cust_anniversary = element.checkbox("Custom Anniversary Message")
        if(cust_anniversary):
            message='Wishing You a Very Happy Marriage Anniversary!💑\nMay You Have a Happy Married Life Ahead.Wishing You and Your Soulmate Health and Prosperity!💞\nCelebrate the Day 🥂'
else:
    element.text("Please Write Your Message Below!")
message=st.text_area("Message to Deliver",message)   

c1,c2=st.columns(2)
with c1:
    details=(st.button("Show Message Details "))
with c2:
       submitted = st.button("Submit")
if(details):
    st.markdown('Message to : {}'.format(n,Time),unsafe_allow_html=True)
    st.markdown(' Time Of Message : {}'.format(Time),unsafe_allow_html=True)
    st.markdown('Message Text : {}'.format(message),unsafe_allow_html=True)
if(submitted):
    try:
        st.markdown('<h6 style="text-align: left; margin-bottom:0;">Your Message will be sent </h6> ',unsafe_allow_html=True)
        # with st.spinner('Please Wait for a While'):
        #     time.sleep(5)
        st.info('You may Close the Application in a minute! Message will be sent at its Time')
        st.balloons()
        st.text(kit.sendwhatmsg(n,message,Time.hour,Time.minute))
        st.text("SENT!")  
    except:
        st.error('Sorry! This is an error')
    
    
    
    
# c1,c2=st.columns(2)  
    # with c1:
    #    hr = st.slider("Choose Hours",max_value=23)
    # with c2:
    #     min = st.slider("Choose Minutes",max_value=59)