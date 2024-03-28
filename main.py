import streamlit as st
class XRayAnalyzer:
    def __init__(self):
        st.set_page_config(
            page_title="X-ray Analyzer",
            page_icon="./app/static/logo.jpg",
            layout="wide",
            menu_items={}
        )
        st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

    def load_base_html(self, path="static/base.html"):
        with open(path) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    def load_description_html(self, path="static/discpreption.html"):
        with open(path) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    def run(self):
        # Center the title of the page
        self.load_base_html()
        st.markdown("""
            <h1 style='text-align: center;
                        font-family: "Black Han Sans", sans-serif;
                        margin-top: 10px;'>
                Welcome to X-ray Image Analysis
            </h1>
            """, unsafe_allow_html=True)
        self.load_description_html()

if __name__ == "__main__":
    analyzer = XRayAnalyzer()
    analyzer.run()