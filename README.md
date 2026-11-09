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

### Data Flow Plan

1. **Input — User Preferences:** Read the user's favorite genre, favorite mood,
   target energy, and acoustic preference.
2. **Process — The Recommendation Loop:** Read each individual song from
   `songs.csv`, compare its features with the user preferences, apply the
   Algorithm Recipe, and store its total score and explanation.
3. **Output — The Ranking:** Sort every scored song from highest to lowest and
   return the top `k` recommendations.

The flow for one song is:

```text
User preferences + one CSV song
              |
              v
       Calculate each point value
              |
              v
       Save total score and reasons
              |
              v
      Rank with all other songs
              |
              v
       Return the top K songs
```

### Potential Biases and Limitations

The system might over-prioritize genre and energy, causing a song with the
right mood but a different genre to rank lower than it deserves. The acoustic
bonus may also favor songs with higher acousticness when the user has not
provided enough information about that preference. Finally, the small CSV
catalog and its fixed genre and mood labels may underrepresent some musical
styles, so the recommendations cannot reflect tastes missing from the data.

### How Songs Are Recommended

The system will:
1. Compare each song with the user's profile.
2. Calculate a compatibility score for each song.
3. Rank songs from highest to lowest score.
4. Recommend the songs with the highest scores.

Input: User Preferences
  genre, mood, target energy, acoustic preference
          |
          v
Process: Evaluate Every Song in songs.csv
  For each song:
    - genre match?       +2.0
    - mood match?        +1.0
    - energy similarity? up to +2.0
    - acoustic match?    +0.5
    - calculate total score
          |
          v
Ranking:
  Sort all songs by score, highest first
          |
          v
Output:
  Return the top K recommendations
  with each song's score and explanation

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
Loaded songs: 18

Top recommendations for genre='pop', mood='happy', energy=0.80:

1. Sunrise City by Neon Echo
   Score: 4.96
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+1.96)

2. Gym Hero by Max Pulse
   Score: 3.74
   Reasons: genre match (+2.0); energy similarity (+1.74)

3. Rooftop Lights by Indigo Parade
   Score: 2.92
   Reasons: mood match (+1.0); energy similarity (+1.92)

4. Night Drive Loop by Neon Echo
   Score: 1.90
   Reasons: energy similarity (+1.90)

5. City Cipher by Northside Verse
   Score: 1.86
   Reasons: energy similarity (+1.86)

```


---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

## System Evaluation

The reusable user preference dictionaries are defined in
[`src/main.py`](src/main.py), and the scoring and ranking logic is implemented
in [`src/recommender.py`](src/recommender.py). Three baseline profiles cover
different parts of the catalog:

| Profile | Preferences | Expected behavior |
| --- | --- | --- |
| **High-Energy Pop** | `genre="pop"`, `mood="happy"`, `energy=0.80` | Prefer *Sunrise City* and other upbeat pop or close-energy songs. |
| **Chill Lofi** | `genre="lofi"`, `mood="chill"`, `energy=0.40`, `likes_acoustic=True` | Prefer *Midnight Coding* and *Library Rain*, with an additional acoustic bonus. |
| **Deep Intense Rock** | `genre="rock"`, `mood="intense"`, `energy=0.95` | Prefer *Storm Runner* because it matches the genre and mood and is close to the target energy. |

### Adversarial and Edge-Case Profiles

These profiles can be passed to `score_song` or `recommend_songs` to test
whether the scoring logic behaves predictably:

1. **Conflicting signals:** `{"genre": "pop", "mood": "sad", "energy": 0.90}`.
   The system should not invent a mood match; it should rank high-energy pop
   songs using the genre and energy points only.
2. **Exact opposite energy:** `{"genre": "rock", "mood": "intense", "energy": 0.0}`.
   This checks that the energy score falls to zero for a song at energy `1.0`
   while genre and mood points still apply.
3. **Unknown categorical values:** `{"genre": "unknown", "mood": "unknown", "energy": 0.5}`.
   No genre or mood matches should be reported, but every song should still
   receive a bounded energy-similarity score.
4. **Boundary energy values:** test `energy=0.0` and `energy=1.0` to verify
   that the similarity formula remains within its intended `0.0` to `2.0`
   range.
5. **Acoustic tie-breaker:** compare the same categorical and energy
   preferences with `likes_acoustic=False` and `likes_acoustic=True`. Only
   songs with `acousticness >= 0.60` should gain the `+0.5` bonus.

These cases probe conflicting preferences, missing matches, numeric
boundaries, and the optional acoustic signal. They also expose a limitation:
the current scorer adds independent points rather than modeling trade-offs, so
a strong genre match can still outrank a song with the preferred mood but a
different genre.

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
