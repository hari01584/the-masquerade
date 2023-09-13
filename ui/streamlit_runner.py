import sys,os
sys.path.append(os.getcwd())

import streamlit as st
from connector.base import Connector

# -------- Helper functions -------- #
def is_empty(text):
    return text.strip() == ""

class StreamRunner():
    def __init__(self):
        st.set_page_config(page_title="TheMasquerade", page_icon=":woozy_face:")
        st.title("TheMasquerade - A mask, behind every face")
        st.subheader("Generate a persona")

        # init nones
        self.company_profile = None
        self.projects = None
        self.experience = None
        self.extra_misc = None

    def build(self):
        self.company_profile = st.text_area("Company profile", height=400)
        self.projects = st.text_area("My projects", height=200)
        self.experience = st.text_area("Experiences", height=200)
        self.extra_misc = st.text_area("Extra (or Misc)", height=200)
        self.contact_details = st.text_area("Contact details", height=100)

        if st.button("Submit", use_container_width=True):
            self.submit()

    def submit(self):
        if is_empty(self.company_profile):
            st.error("Please enter the company profile")
            return

        # Get connector for inference engine
        connector = get_llm_connector()
        # Get output
        output = connector.evaluate({
            "company_profile": self.company_profile,
            "projects": self.projects,
            "experience": self.experience,
            "extra_misc": self.extra_misc,
            "contact": self.contact_details
        })

        headline = "Regarding intern/full"
        # Show output
        st.write(output)

@st.cache_resource
def get_llm_connector():
    return Connector()

runner = StreamRunner()
runner.build()

# Also init connector!
get_llm_connector()