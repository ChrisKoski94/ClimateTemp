# streamlit_app.py
import streamlit as st

try:
    from pages.home import home_page
    from pages.project_breakdown import project_breakdown_page
    from pages.other_page import other_page
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")

def main():
    st.title("Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections")

    # Displaying the image from the data folder
    image_path = "data/_a12672b9-08f6-45e7-99f5-dad7c20210aa.jpg"
    st.image(image_path, use_column_width=True)

    # Add a link to different pages in the sidebar
    page = st.sidebar.radio("Navigate", ["Home", "Project Breakdown", "Other Page"])

    if page == "Home":
        home_page()
    elif page == "Project Breakdown":
        project_breakdown_page()
    elif page == "Other Page":
        other_page()

if __name__ == "__main__":
    main()

