🎬 Movie Recommendation System

This project is a movie recommendation system built with **Streamlit** and powered by a **machine learning model**. It recommends movies based on a selected title using **cosine similarity** and displays movie posters fetched from the **TMDB API**.

> Dataset used: [Kaggle - TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  


---

## 📚 Table of Contents

- [Overview](#overview)
- [Theory of Recommendation Systems](#theory-of-recommendation-systems)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [Usage Restriction](#usage-restriction)

---

## 🧠 Overview

The movie recommendation system helps users discover movies similar to their favorites. By selecting a movie from the list, users receive a list of the **top 10 recommended movies**, along with their posters.

The system uses a **content-based recommendation algorithm** with **cosine similarity** to calculate how similar movies are based on features like genres, keywords, and more. Posters are retrieved in real-time using the **TMDB API**, and the entire interface is powered by **Streamlit** for ease of use.

---

## 📊 Theory of Recommendation Systems

### What is a Recommendation System?

A recommendation system is a type of information filtering system that predicts user preferences for items, like movies or products.

### Types of Recommendation Systems

1. **Content-Based Filtering**: Recommends items similar to those the user has liked, based on item features.
2. **Collaborative Filtering**: Recommends items based on preferences of similar users.
3. **Hybrid Models**: Combine content-based and collaborative filtering for improved accuracy.

### Cosine Similarity

This system uses **cosine similarity** to compute how close two movies are in feature space. A higher cosine similarity means a stronger match.

---

## 💻 Tech Stack

- **Python 3.8+**
- **Pandas** – for data manipulation
- **Scikit-learn** – for similarity calculations
- **Pickle** – for loading preprocessed data
- **Requests** – to call the TMDB API
- **Streamlit** – to build the web app UI
- **TMDB API** – to fetch movie posters

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
Run the app:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to http://localhost:8501

Select a movie and click "Recommend" to get top 10 movie suggestions with posters.

📁 Dataset
The dataset includes metadata like movie titles, genres, keywords, and more. It is preprocessed and stored in a movie_data.pkl file for efficient loading and similarity computation.

🧠 Model
The recommendation model is based on cosine similarity of feature vectors extracted from the movie dataset. No deep learning is used — this is a classic content-based filtering approach using feature engineering and similarity scoring.

✅ Results
The system returns:

A list of 10 similar movies to the selected title

Each movie's poster fetched using the TMDB API

Results displayed instantly via a Streamlit web UI

🤝 Contributing
Contributions are welcome!
If you’d like to improve the recommendation logic, UI, or performance, feel free to open an issue or submit a pull request.

❗ Usage Restriction
This project is shared for educational and personal learning purposes only.
