import streamlit as st
from PIL import Image


st.set_page_config(page_title="portfolia", page_icon="wave", layout="wide")

profile_pic = Image.open("Emily.jpg")
#Header section 

with st.container():
    st.subheader("Hi, l'm Emily :wave: :smile:")
    st.title("l'm a data analyst| data scientist | ML enthuastist")
    st.write("""Highly skilled and motivated data scientist  seeking to contribute my  problem skills in a data science position.
              Currently am pursing a degree in computer science with a strong foundation in mathematics and analytical skills.
             Eager to contribute my skills in a real world problem.""")
    st.write("[Email](kemuntoemily515@gmail.com) | [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)")

#About me
st.markdown("""
            <style>
            .custom-container{
            background-color: grey;}
            </style>
            """,unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    col1,col2=st.columns(2)
    with col1:
       st.image(profile_pic, width=150)
      #st.markdown( <img src='Emily.jpg', width='100' style='display: rouded; margin: auto;'/>
                 # ",unsafe_allow_html=True)

    with col2:
        st.write("About me")
        st.write("""l'm a passionate data scientist with a strong background in mathematics,databases,python and machine learning.
                 l love building machine learning models and web application for data using streamlit python framework.
                 l love problem solving and driving out insights for better decision_making out from large amounts of data.
                 Also coming up with unique visualisation for easier understanding by non tech people in the industries.
                 """)
        st.markdown('/div', unsafe_allow_html=True)
#My skills
with st.container():
    st.divider()
    st.header("My skills")

    st.write(
        """
        - 👨‍💻 Programming: Python,SQL
        - 🧠 Machine Learning: scikit-learn, TensorFlow, PyTorch
        - 🌐 Web Dev: Streamlit, FastAPI, HTML/CSS, Flask
        - ☁ Cloud: AWS, Docker, GitHub Actions
        """
         )
    st.write("Data visualisation: matplotlib,seaborn,tableau,powerbi :barchart:")

#my projects
with st.container():
    st.divider()
    st.header("My projects")
    
    project_cols=st.columns(2)
    with project_cols[0]:
        st.subheader("🔍 ML Laptop prices App")
        st.write("Built a Streamlit app to predict laptop prices")
        st.write("[Github repo](https://github.com/emily2004-rty/laptop-price-prediction.git)")

    with project_cols[1]:
        st.subheader("Healthcare powerbi analysis")
        st.write("Created an interactive healthcare dashboard using powerbi.")
        st.write("[Github repo](https://github.com/emily2004-rty/power-bi/tree/main/healthcare)")

#my contacts
with st.container():
    st.write("---")
    st.header("📬 Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kemuntoemily515@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("Alternatively, reach me at [my email](mailto:kemuntoemily515@gmail.com)")

    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)