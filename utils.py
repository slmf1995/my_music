import requests
import urllib.parse


def request_an_access_token(client_id: str, client_secret: str) -> str:
    # https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
    """
    Requests an access token from the Spotify Web API by making a POST request to the
    Spotify Accounts service with the specified client ID and client secret.

    Args:
        client_id (str): The client ID provided by Spotify for API authentication.
        client_secret (str): The client secret provided by Spotify for API authentication.

    Returns:
        str: The access token returned by the Spotify Accounts service.

    Raises:
        requests.exceptions.RequestException: If the request fails for any reason.
        KeyError: If the access token is not found in the response JSON object.
    """
    url = 'https://accounts.spotify.com/api/token'

    response = requests.post(url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }).json()

    return response['access_token']


def get_playlist(user_id: str, access_token: str) -> dict:
    # https://developer.spotify.com/documentation/web-api/reference/get-playlist
    """
    Gets a list of playlists owned or followed by a Spotify user.

    Args:
        user_id (str): The Spotify user ID of the user whose playlists are being retrieved.
        access_token (str): The access token for the Spotify Web API.

    Returns:
        dict: A dictionary representing the JSON response returned by the Spotify Web API.

    Raises:
        requests.exceptions.RequestException: If the request fails for any reason.
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'

    response = requests.get(url, headers=headers).json()

    return response


def get_playlist_tracks(playlist_id: str, access_token: str, offset: int) -> dict:
    # https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
    """
    Gets a list of tracks in a Spotify playlist.

    Args:
        playlist_id (str): The ID of the Spotify playlist whose items are being retrieved.
        access_token (str): The access token for the Spotify Web API.
        offset (int): The index of the first item to be retrieved.

    Returns:
        dict: A dictionary representing the JSON response returned by the Spotify Web API.

    Raises:
        requests.exceptions.RequestException: If the request fails for any reason.
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    url = 'https://api.spotify.com/v1/playlists/' + \
        playlist_id + '/tracks?offset=' + str(offset)

    response = requests.get(url, headers=headers).json()

    return response


def get_audio_features(track_id: str, access_token: str) -> dict:
    # https://developer.spotify.com/documentation/web-api/reference/get-audio-features
    """
    Gets audio features for a given track in the Spotify catalog.

    Args:
        track_id (str): The Spotify ID for the track.
        access_token (str): The access token for the Spotify Web API.

    Returns:
        dict: A dictionary representing the JSON response returned by the Spotify Web API.

    Raises:
        requests.exceptions.RequestException: If the request fails for any reason.
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    url = 'https://api.spotify.com/v1/audio-features/' + track_id

    response = requests.get(url, headers=headers).json()

    return response


def get_audio_analysis(track_id: str, access_token: str) -> dict:
    # https://developer.spotify.com/documentation/web-api/reference/get-audio-analysis
    """
    Gets audio analysis for a given track in the Spotify catalog.

    Args:
        track_id (str): The Spotify ID for the track.
        access_token (str): The access token for the Spotify Web API.

    Returns:
        dict: A dictionary representing the JSON response returned by the Spotify Web API.

    Raises:
        requests.exceptions.RequestException: If the request fails for any reason.
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    url = 'https://api.spotify.com/v1/audio-analysis/' + track_id

    response = requests.get(url, headers=headers).json()

    return response


def add_playlists_tracks(track_id: str, playlist_id: str, access_token: str) -> dict:
    # https://developer.spotify.com/documentation/web-api/reference/reorder-or-replace-playlists-tracks
    """
    Add tracks in a playlist.

    Args:
        track_id (str): The Spotify ID for the new track to add to the playlist.
        playlist_id (str): The Spotify ID for the playlist to modify.
        access_token (str): The access token for the Spotify Web API.

    Returns:
        dict: A dictionary representing the JSON response returned by the Spotify Web API.

    Raises:
        requests.exceptions.RequestException: If the request fails for any reason.
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + \
        '/tracks?uris=' + urllib.parse.quote('spotify:track:' + track_id)

    response = requests.post(url, headers=headers).json()

    return response
