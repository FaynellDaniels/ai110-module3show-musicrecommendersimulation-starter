# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works

The recommender compares each song with the user's favorite genre, favorite
mood, target energy level, and acoustic preference. It awards 2 points for a
genre match and 1 point for a mood match. Energy receives up to 2 points:
the closer a song's energy is to the user's target, the more points it earns.
If the user likes acoustic music, songs with high acousticness receive an
additional 0.5 points.

The program repeats this scoring process for every song in the CSV file. It
then sorts the songs from the highest score to the lowest score and returns the
top recommendations. Each result includes an explanation listing the matches
and points that produced its score, making the CLI-first simulation easy to
understand.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

My recommendation system has several limitations that could affect the quality and fairness of its recommendations. It does not consider important features such as song lyrics, artist popularity, language, cultural influences, or detailed listening history. The music catalog is also limited, with some genres being underrepresented. For example, lofi has three songs, pop has two, and most other genres only have one, making it difficult to provide variety for users with different musical preferences. The scoring system can also overfit to one preference, especially energy level, which can contribute up to four points and potentially outweigh genre or mood matches. This means users whose preferences closely match the available catalog may receive better recommendations than those with less common tastes. To improve the system, I would expand the music catalog, allow partial matches for similar genres and moods, balance the scoring weights, and introduce an exploration feature that helps users discover new music instead of repeatedly receiving similar recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the three profiles defined in `src/main.py`: High-Energy Pop,
Chill Lofi, and Deep Intense Rock. High-Energy Pop ranked *Sunrise City*
first, followed by *Rooftop Lights* and *Gym Hero*; this makes sense because
the profile combines pop, happy mood, and a high target energy. Chill Lofi
ranked *Midnight Coding*, *Library Rain*, and *Focus Flow* highest, which
matches the lofi/chill preferences and the acoustic bonus. Deep Intense Rock
ranked *Storm Runner* first, followed by *Gym Hero* and *Iron Eclipse*, which
fits the intense, high-energy target.

- **High-Energy Pop vs. Chill Lofi:** Pop recommends upbeat pop or
  pop-adjacent songs, while Lofi shifts to lower-energy lofi songs. This
  difference is expected because the target energy changes from `0.80` to
  `0.40`, the genre and mood labels change, and Chill Lofi receives acoustic
  bonuses.
- **High-Energy Pop vs. Deep Intense Rock:** Both profiles favor energetic
  music, but Pop puts *Sunrise City* first while Rock puts *Storm Runner*
  first. The genre and mood matches explain the different leaders, while
  *Gym Hero* appears in both lists because its `0.93` energy is close to both
  high-energy targets.
- **Chill Lofi vs. Deep Intense Rock:** These profiles produce the clearest
  contrast: Chill Lofi favors calm, acoustic-leaning songs, whereas Deep
  Intense Rock favors loud, intense songs. Their different energy targets and
  categorical preferences make the non-overlapping top recommendations
  reasonable.

The most surprising result was that *Gym Hero* reached the top three for both
High-Energy Pop and Deep Intense Rock even though its mood is `intense` rather
than `happy` and its genre is not rock. This demonstrates the effect of the
weight-shift experiment: energy similarity can contribute up to four points
and sometimes outweighs an unmatched genre or mood.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
