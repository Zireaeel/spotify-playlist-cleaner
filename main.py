import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Enter your Spotify app details here
CLIENT_ID = '...' # you should add your CLIENT_ID
CLIENT_SECRET = '...' # you should add your CLIENT_SECRET code
REDIRECT_URI = 'http://localhost:8888/callback'  # Specify this URL in Spotify app settings

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-public playlist-modify-private"))

# Add your playlist ID here (Link)
playlist_id = "https://open.spotify.com/playlist/..."

def get_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def remove_duplicates_from_playlist(playlist_id):
    tracks = get_playlist_tracks(playlist_id)
    seen_tracks = {}
    to_remove = []
    track_ids = []

    for index, item in enumerate(tracks):
        track = item['track']

        if track is None:
            continue

        track_id = track['id']
        
        if track_id not in seen_tracks:
            seen_tracks[track_id] = index
        else:
            to_remove.append(item)
            track_ids.append(track_id)

    if to_remove:
        track_ids_to_remove = [item['track']['id'] for item in to_remove]
        
        sp.playlist_remove_all_occurrences_of_items(playlist_id, track_ids_to_remove)
        print(f"{len(track_ids_to_remove)} adet tekrar eden şarkı kaldırıldı.\n")

        print("Kaldırılan Şarkılar:")
        for track_id in track_ids_to_remove:
            track_info = next(item for item in tracks if item['track']['id'] == track_id)
            print(f"- {track_info['track']['name']} - {track_info['track']['artists'][0]['name']}")

        print("\nYeniden Eklenen Şarkılar:")
        for track_id in track_ids_to_remove:
            sp.playlist_add_items(playlist_id, [track_id])
            track_info = next(item for item in tracks if item['track']['id'] == track_id)
            print(f"- {track_info['track']['name']} - {track_info['track']['artists'][0]['name']}")
    else:
        print("Tekrar eden şarkı bulunamadı.")

remove_duplicates_from_playlist(playlist_id)
