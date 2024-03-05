import streamlit as st
from PIL import Image
from classification import classify, rice_quality_check

st.set_page_config(page_title='Rice Sure', page_icon='fav.jpeg', layout="centered", initial_sidebar_state="auto", menu_items=None)


st.image('ricesurelogo.jpeg', width=200)
tab1, tab2, tab3 = st.tabs(["Prediction and Quality Check", "Rice Information", "Group Members"])

with tab1:
        #st.title("Rice Sure")
        #st.divider()
        st.subheader("RiceSure app fights fraudulent in the rice industry by using Convolutional Neural Network with Transfer Learning and Fine Tuning to identify rice grain types and ensure consistent quality control.")
        st.subheader("Some of the rice varieties including Basmati Rice, Jasmine Rice, Karacadag Rice, Arborio Rice, and Ipsala have different features and structure. Let's predict the type of the rice below. ")
        #st.divider()
        #st.subheader("Upload rice grain image.")
        uploaded_file = st.file_uploader("Choose an image of a rice grain. (Kindly attach only rice grain images)")
        if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image')
                image.save('up.jpg')
                #st.divider()
                
                if st.button('Click to process'):
                        st.spinner(text="Predicting...")
                        #st.balloons()
                        st.success('The image was uploaded successfully and below are the rice type and rice quality check')
                        label = classify(uploaded_file)
                        quality = rice_quality_check('up.jpg')
                        
                        #res = sign_names.get(label)
                        st.markdown(label)
                        st.markdown(quality)
with tab2:
        st.subheader("Basmati Rice")
        st.image("Basmati.jpg", width=200)
        st.write("Basmati rice is a long-grain rice variety grown primarily in India and Pakistan. It has a distinctive nutty flavor and aroma, and the cooked grains are fluffy and separate, making it a popular choice for biryanis, pilafs, and other Indian and Middle Eastern dishes.")
        #st.divider()
        
        st.subheader("Jasmine Rice")
        st.image("Jasmine.jpg", width=200)
        st.write("Jasmine rice is a long-grain rice variety grown in Thailand, Cambodia, and Vietnam. It has a fragrant aroma and a slightly sweet flavor, making it popular in Asian cuisine. Jasmine rice is fluffy and soft when cooked and is often served alongside curries, stir-fries, and other spicy dishes.")
        #st.divider()
        
        st.subheader("Karacadag Rice")
        st.image("Karacadag.jpg", width=200)
        st.write("Karacadag rice is a type of aromatic, medium-grain rice grown in southeastern Turkey. It has a nutty flavor and slightly sticky texture, making it suitable for pilafs, stews, and other savory dishes.")
        #st.divider()
        
        st.subheader("Arborio Rice")
        st.image("Arborio.jpg", width=200)
        st.write("Arborio rice is a short-grain rice variety grown in Italy. It has a high starch content and a creamy texture, making it ideal for making risotto, a classic Italian rice dish.")
        #st.divider()
        
        st.subheader("Ipsala Rice")
        st.image("Ipsala.jpg", width=200)
        st.write("Ipsala rice is a type of rice grown in the Ipsala district of Edirne Province, Turkey. It is a long-grain rice with a white color and a slightly nutty flavor. Ipsala rice is known for its high quality and is often used in pilafs, soups, and desserts.")

with tab3:
        st.write("Rajasegaran a/l M Sivaanandan (22052733)")
        st.write("Basubeit, Omar Gumaan Saleh (22054606)")
        st.write("Safwan bin Shamsir (S2195293)")
        st.write("Azle Abd Ghalim (S2036517)")
        st.write("Intan Nor Qamarina Binti Yunus (S2180929)")
        
       
         
         
