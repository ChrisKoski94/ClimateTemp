# streamlit_app.py
import streamlit as st

def main():
    st.title("Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections")

    # Displaying the image from the data folder
    image_path = "data/_a12672b9-08f6-45e7-99f5-dad7c20210aa.jpg"
    st.image(image_path, caption="Caption for the image", use_column_width=True)

if __name__ == "__main__":
    main()


