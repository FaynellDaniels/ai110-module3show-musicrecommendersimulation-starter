from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the user's top k songs ranked by compatibility score."""
        ranked_songs = sorted(
            self.songs,
            key=lambda song: score_song(
                {
                    "genre": user.favorite_genre,
                    "mood": user.favorite_mood,
                    "energy": user.target_energy,
                    "likes_acoustic": user.likes_acoustic,
                },
                song.__dict__,
            )[0],
            reverse=True,
        )
        return ranked_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return the scoring reasons for a song recommendation."""
        _, reasons = score_song(
            {
                "genre": user.favorite_genre,
                "mood": user.favorite_mood,
                "energy": user.target_energy,
                "likes_acoustic": user.likes_acoustic,
            },
            song.__dict__,
        )
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file with numeric fields converted to numbers."""
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        songs = []
        for row in reader:
            songs.append(
                {
                    **row,
                    "id": int(row["id"]),
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
        return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's compatibility score and readable scoring reasons."""
    score = 0.0
    reasons = []

    if user_prefs.get("genre", "").strip().lower() == song["genre"].strip().lower():
        score += 1.0
        reasons.append("genre match (+1.0)")

    if user_prefs.get("mood", "").strip().lower() == song["mood"].strip().lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = float(user_prefs.get("energy", 0.5))
    energy_similarity = max(0.0, 1.0 - abs(float(song["energy"]) - target_energy))
    energy_points = 4.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    if user_prefs.get("likes_acoustic", False) and float(song["acousticness"]) >= 0.6:
        score += 0.5
        reasons.append("acoustic preference (+0.5)")

    if not reasons:
        reasons.append("no matching preferences")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by their compatibility scores."""
    ranked = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        ranked.append((song, score, "; ".join(reasons)))
    ranked.sort(key=lambda recommendation: recommendation[1], reverse=True)
    return ranked[:k]
