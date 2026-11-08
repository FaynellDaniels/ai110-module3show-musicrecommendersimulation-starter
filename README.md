# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project recommends songs from [`data/songs.csv`](data/songs.csv) by scoring
each song against a user's preferred genre, mood, energy level, and acoustic
preference. It ranks the catalog from the highest score to the lowest score
and explains the points earned by each recommendation.

---

## How The System Works

- Real-world music recommendation systems analyze a user's listening habits, preferences, and interests to suggest songs they are likely to enjoy. My recommendation system will use information such as genre, mood, energy, and tempo to compare songs with a user's preferences. Each song will receive a compatibility score based on how closely its features match the user's profile. The system will prioritize recommending songs that match the user's musical taste while also introducing some variety so they can discover new music.

1. Song Object

Each Song object will store the following features:
- Title: Name of the song.
- Artist: Name of the artist.
- Genre: Musical category (pop, R&B, hip-hop, rock, etc.).
- Mood: Overall feeling of the song (happy, sad, relaxed, energetic).
- Energy: How calm or upbeat the song is.
- Tempo: How fast or slow the song is.

2. UserProfile Object

Each UserProfile object will store the user's music preferences:
- Favorite Genres: Genres the user enjoys listening to.
- Preferred Moods: Types of moods they enjoy in music.
- Preferred Energy Level: Whether they prefer low, medium, or high-energy songs.
- Preferred Tempo: Whether they prefer slow, moderate, or fast-paced songs.
- Listening History: Songs the user has previously listened to or enjoyed.

3. Recommender Object

-The Recommender will calculate a compatibility score for each song by comparing its features against the user's preferences.

### Algorithm Recipe: Scoring Logic Design

The supplied [`data/songs.csv`](data/songs.csv) has 18 songs with genre, mood,
energy, and acousticness values. I chose weights that balance exact preference
matches with a gradual energy similarity score:

1. **Genre match: +2.0 points.** Genre is the strongest categorical signal
   because it represents the user's broad musical style.
2. **Mood match: +1.0 point.** Mood matters, but it should not overpower genre.
3. **Energy similarity: up to +2.0 points.** The score is
   `2.0 * (1 - abs(song_energy - target_energy))`. An exact match earns 2.0
   points, while a song one full energy unit away earns 0 points.
4. **Acoustic preference: +0.5 points.** If the user likes acoustic music, a
   song with `acousticness >= 0.60` receives a small bonus. This is a tie-breaker
   rather than a dominant preference.

The maximum score is 5.5 points. Songs are sorted by score in descending order,
and the top `k` songs are recommended. The same recipe is used by both the
object-oriented and functional recommender interfaces.

4. How Songs Are Recommended

The system will:
1. Compare each song with the user's profile.
2. Calculate a compatibility score for each song.
3. Rank songs from highest to lowest score.
4. Recommend the songs with the highest scores.



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


