# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on user preferences using machine learning and natural language processing techniques.

## 🎯 Project Description

**Movie Recommender System | Machine Learning & NLP**

- Developed a content-based movie recommendation engine analyzing 4,800+ movies using cosine similarity and text vectorization. Implemented NLP preprocessing with Porter Stemming and CountVectorizer to extract features from movie metadata including genres, keywords, cast, and crew. Built an interactive Streamlit web interface integrated with TMDB API for real-time movie poster fetching and personalized recommendations.

## ✨ Features

- Content-based filtering using movie metadata (genres, keywords, cast, crew, plot)
- NLP text preprocessing with Porter Stemming
- Interactive Streamlit web interface
- Real-time movie poster fetching via TMDB API
- Cosine similarity-based recommendations
- 5000+ feature analysis using CountVectorizer

## 🛠️ Technologies Used

- Python 3.7+
- scikit-learn (CountVectorizer, Cosine Similarity)
- NLTK (Porter Stemmer)
- Pandas, NumPy
- Streamlit
- TMDB API
- Pickle

## 🚀 Installation
```bash
# Clone the repository
git clone <repository-url>
cd Movie-Recommender-ML

# Install dependencies
pip install -r requirement.txt

# Run the application
streamlit run app.py
```

## 📊 Dataset

TMDB 5000 Movies dataset containing 4,803 movies with metadata including genres, keywords, cast, crew, and overviews.

## 👨‍💻 Author

**Benrabah Seif Islem**
- Email: islamsseeiiff@gmail.com

## 📄 License

This project is open source and available under the MIT License.
