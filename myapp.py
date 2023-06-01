import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    # Create a title for your app
    st.title("Pixabay Web Scraper")

    # Add an input field to enter the search term
    search_term = st.text_input("Enter search term", "nature")

    # Create a button to initiate the scraping process
    if st.button("Scrape"):
        # Make a GET request to Pixabay website
        response = requests.get(f"https://pixabay.com/images/search/{search_term}/")
        soup = BeautifulSoup(response.content, "html.parser")

        # Find and display the images on the page
        images = soup.find_all("img", {"src": True})
        for image in images:
            st.image(image["src"])

    # Add a footer or any additional information
    st.text("Web Scraper by Your Name")

# Call the main function directly
main()