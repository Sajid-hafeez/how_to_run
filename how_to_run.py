import base64
import streamlit as st
def image_to_base64(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()

video_file = open(
    'demo.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.markdown(
    "<h2 style='font-family:Times New Roman, Times, serif; font-style:italic;'>Data Scientist behind the app</h2>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='font-family:Times New Roman, Times, serif; font-style:italic;'>"
    "Hello mate, I hope everything works well on your end as well, for any kinding of questions feel free to reach out to me.<br>"
    "I offer services related to Data science and statistical analysis using R, Python, Stata, SPSS, Weka and Power BI. Feel free to contact me on the following."
    "</div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

email_logo_base64 = image_to_base64("email.png")
linkedin_logo_base64 = image_to_base64("whats.png")
website_logo_base64 = image_to_base64("web.png")

col1.markdown(
    f"""
    <div style='font-family:Times New Roman, Times, serif; font-style:italic;'>
        <p><img src='data:image/png;base64,{email_logo_base64}' style='width:20px; vertical-align:middle;'/> Email: <a href='mailto:Sajidhafeex@gmail.com'>Sajidhafeex@gmail.com</a></p>
        <p><img src='data:image/png;base64,{linkedin_logo_base64}' style='width:20px; vertical-align:middle;'/> LinkedIn: <a href='https://www.linkedin.com/in/sajid-hafeex'>https://www.linkedin.com/in/sajid-hafeex</a></p>
        <p><img src='data:image/png;base64,{website_logo_base64}' style='width:20px; vertical-align:middle;'/> Website: <a href='https://Rprogrammers.com'>https://Rprogrammers.com</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)

col2.image("giphy.gif")
