# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
MoodMuse 1.0 💗

MoodMuse is a personalized music recommendation system that finds songs based on a user's musical taste, mood, and energy preferences.

---

## 2. Intended Use  

MoodMuse is designed to recommend songs that match a user's musical taste. It uses preferences such as genre, mood, energy, and acoustic preference. It assumes users can describe the type of music they enjoy. This project is a classroom simulation that demonstrates how recommendation systems work. It is not intended to replace real-world music platforms.

---

## 3. How the Model Works

The recommender compares each song with the user's favorite genre, favorite mood, target energy level, and acoustic preference. It awards 2 points for a genre match and 1 point for a mood match. Energy receives up to 2 points based on how close the song is to the user's target. If the user likes acoustic music, songs with high acoustics receive an additional 0.5 points.

The program repeats this process for every song in the CSV file. It then sorts the songs from highest to lowest score and returns the top recommendations. Each recommendation includes an explanation of why the song received its score.



---

## 4. Data  

The model uses a small music catalog stored in a CSV file. The catalog includes songs from genres such as lofi, pop, rock, and other styles. Each song includes features such as genre, mood, energy, tempo, and acousticness.

The dataset has some limitations. Lofi has three songs, pop has two, and most other genres only have one. It does not include enough songs to represent every type of musical preference. It also does not consider lyrics, language, artist popularity, or cultural influences.

---

## 5. Strengths  

MoodMuse works well when users have clear music preferences that match the available songs. It successfully recommends upbeat pop songs for users who prefer high-energy music and calmer lofi songs for users who enjoy relaxed music. It also recognizes when songs have similar energy levels. The recommendations generally matched my expectations when I tested the three different user profiles.

---

## 6. Limitations and Bias 

MoodMuse has several limitations that could affect the quality and fairness of its recommendations. It does not consider important features such as song lyrics, artist popularity, language, cultural influences, or detailed listening history. The music catalog is also limited, with some genres being underrepresented. For example, lofi has three songs, pop has two, and most other genres only have one. This makes it difficult to provide variety for users with different musical preferences. The scoring system can also overfit to one preference, especially energy level, which can sometimes outweigh genre or mood matches. Users whose preferences closely match the available catalog may receive better recommendations than users with less common tastes. To improve the system, I would expand the music catalog, allow partial matches for similar genres and moods, balance the scoring weights, and introduce an exploration feature.



---

## 7. Evaluation  

I tested the three user profiles defined in src/main.py: High-Energy Pop, Chill Lofi, and Deep Intense Rock to see whether the recommendations matched their different musical preferences. I looked at the highest-ranked songs for each profile and compared how the genre, mood, and energy preferences affected the results. High-Energy Pop ranked Sunrise City first, Chill Lofi ranked Midnight Coding first, and Deep Intense Rock ranked Storm Runner first, which matched what I expected based on each profile. I also compared the recommendations across profiles to see how much they differed. The most surprising result was that Gym Hero appeared in the top three for both High-Energy Pop and Deep Intense Rock, even though its genre and mood did not perfectly match both profiles. This showed me that energy similarity can sometimes have a stronger influence on the final score than genre or mood. Overall, the tests showed that the recommender generally behaves as expected, but they also revealed how adjusting scoring weights can change which songs are prioritized.

---

## 8. Future Work  

If I continued developing MoodMuse, I would make a few improvements:

- Expand the music catalog to include more songs and genres.

- Add features such as artist popularity, lyrics, and listening history.

- Improve the scoring system to give users more variety and introduce them to new music.

---

## 9. Personal Reflection  

One of my biggest learning moments was realizing how different preferences can change the recommendations a system produces. I learned that even a simple scoring algorithm can create recommendations that feel personalized. AI tools helped me understand coding concepts, troubleshoot errors, and organize my ideas. However, I still had to test the code and double-check suggestions because not every solution worked with my program. I was surprised by how a few features and scoring rules could make recommendations feel similar to what real music platforms provide. This project helped me understand that recommendation systems are not just about finding matches but also about balancing user preferences and music discovery. If I continued this project, I would expand the dataset and experiment with more advanced recommendation methods.
