🎬 Movie Recommendation System

📌 Overview

This project is a Content-Based Movie Recommendation System built using Natural Language Processing (NLP) techniques. It recommends the top 5 movies based on the movie selected by the user.

The system analyzes movie-related information and calculates similarities between movies to identify and recommend movies with similar content.

The project also includes an interactive web interface developed using Streamlit, allowing users to select a movie and instantly receive recommendations along with their movie posters.

🚀 Features

Movie Recommendations: Recommends the top 5 similar movies based on the user's selected movie.
NLP-Based Recommendation: Uses Natural Language Processing techniques to process movie information and identify similarities.
Interactive User Interface: Built with Streamlit for a simple and user-friendly experience.
Movie Posters: Fetches and displays movie posters dynamically using the TMDB API.
TMDB Dataset: Uses movie information from The Movie Database (TMDB).

🛠️ Technologies Used

Python – Core programming language.
Pandas – Data manipulation and preprocessing.
NumPy – Numerical operations.
NLTK / Porter Stemmer – Text preprocessing and stemming.
Scikit-learn – Feature extraction and similarity calculations.
Stealit – Frontend and web application development.
TMDB API – Fetching movie posters and movie-related information.
Pickle – Saving and loading the trained recommendation data.

⚙️ How It Works

The recommendation system follows these steps:

Data Collection: Uses the TMDB movie dataset containing movie-related information.

Data Preprocessing: Cleans and processes relevant movie features such as genres, keywords, overview, cast, and crew.

Feature Engineering: Combines the selected movie attributes into a single text-based feature representation.

Text Preprocessing: Applies NLP techniques such as stemming and text normalization.

Vectorization: Converts textual data into numerical vectors using CountVectorizer.

Similarity Calculation: Uses cosine similarity to calculate similarity scores between movies.

Recommendation: Identifies and returns the top 5 most similar movies based on the selected movie.

Poster Fetching: Uses the TMDB API to retrieve and display the posters of recommended movies.

🖥️ Application Interface

The application is developed using Streamlit.

Users can:

Select a movie from the dropdown menu.

Click the recommendation button.

View the top 5 recommended movies.

Explore the movie posters displayed alongside the recommendations.