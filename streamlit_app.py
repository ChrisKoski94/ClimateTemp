# streamlit_app.py
import streamlit as st

def main():
    st.title("Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections")

    # Displaying the image from the data folder
    image_path = "data/_a12672b9-08f6-45e7-99f5-dad7c20210aa.jpg"
    st.image(image_path, use_column_width=True)

    # Add a link to the Project Breakdown page
    st.sidebar.markdown("[Project Breakdown](#project-breakdown)")

def project_breakdown():
    st.title("Project Breakdown")

    # Text for the breakdown
    breakdown_text = """
    **Chris Kowalski**
    Report 1 - Exploration, data visualization, and data pre-processing report

    **Betsi Flores**
    Report 2 – Modeling Report

    **Maroun Hleihel**
    Report 3 - Challenges and Insights in Climate Modeling
    """

    st.markdown(breakdown_text)

if __name__ == "__main__":
    # Check for page selection
    pages = {"Home": main, "Project Breakdown": project_breakdown}
    selection = st.sidebar.radio("Navigate", list(pages.keys()))

    # Run the selected page
    pages[selection]()



