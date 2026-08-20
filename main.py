# 🎬 Movie Recommendation System by Category


# IMPORT LIBRARIES


import pandas as pd
import matplotlib.pyplot as plt


# LOAD DATASET


try:
    movies = pd.read_csv("movies.csv")
    print("✅ Dataset Loaded Successfully!\n")

except FileNotFoundError:
    print("❌ movies.csv file not found!")
    exit()


# DISPLAY FIRST 5 MOVIES


print("📂 First 5 Movies:\n")
print(movies.head(), "\n")


# USER INPUT


category = input("🎥 Enter Movie Category: ")

# Convert input to lowercase
category = category.lower()


# FILTER MOVIES


recommended = movies[
    movies['genres'].str.lower().str.contains(category)
]


# SHOW RESULTS


if recommended.empty:

    print("\n❌ No movies found in this category!")

else:

    print(f"\n🎬 Movies in '{category}' category:\n")

    for i, movie in enumerate(recommended['title'].head(10), start=1):

        print(f"{i}. {movie}")


# 📊 GRAPH 1: TOP CATEGORIES


genre_counts = movies['genres'].value_counts().head(10)

plt.figure(figsize=(10,5))

genre_counts.plot(kind='bar')

plt.title("Top Movie Categories")

plt.xlabel("Genres")

plt.ylabel("Number of Movies")

plt.show()


# 📊 GRAPH 2: TOTAL MOVIES


plt.figure(figsize=(5,5))

movie_count = len(movies)

plt.bar(["Movies"], [movie_count])

plt.title("Total Movies in Dataset")

plt.ylabel("Count")

plt.show()


# 📊 GRAPH 3: Category Distribution


categories = ["Action", "Comedy", "Horror", "Romance", "Animation"]

counts = []

for cat in categories:

    count = movies['genres'].str.contains(cat, case=False).sum()

    counts.append(count)

plt.figure(figsize=(8,5))

plt.plot(categories, counts, marker='o')

plt.title("Movie Category Distribution")

plt.xlabel("Category")

plt.ylabel("Number of Movies")

plt.show()
