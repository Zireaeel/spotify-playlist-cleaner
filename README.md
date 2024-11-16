# Spotify-Playlist-Cleaner
with Spotify-Playlist-Cleaner, you can remove duplicate songs from your Spotify playlist (if the same song appears more than once). The removed song will be brought back into the playlist only once, so it won't be doubled anymore. __Be careful__ when using the code, as it changes the added date of the songs. If you care about the added dates in your playlist, avoid using it.
It is written with the help of the spotipy module, that helps you to connect your device to your spotify account.
#
"Spotipy" supports all of the features of the Spotify Web API including access to all end points, and support for user authorization. For details on the capabilities you are encouraged to review the Spotify Web API documentation.
## Installation
* <tab><tab>pip install spotipy
* <tab><tab>py -m pip install spotipy (for windows users)
* <tab><tab>pip install spotipy --upgrade (to upgrade the library)
## How does it work?
* First, you will need to install Spotipy and get the Spotify API keys.
* You must register in the Spotify developer dashboard and create an app.
* ### User Information:
* __Spotify API Information:__ You can get client_id, client_secret, and redirect_uri information from the Spotify Developer Dashboard.
* __Playlist ID:__ You can copy the link by right-clicking on the playlist you want in your Spotify application, clicking "Share" and "Copy Playlist Link". You can get the ID in the link that you copied.
* ### Attention!:
* __Spotify API Limits:__ The Spotify API may limit the number of requests you can make in a given time period, so it may be worth paying attention to the number of requests when handling very large playlists.
* __*Spotify Permissions:*__ You will need Spotify API permissions for the code to work. These permissions are required for playlist reading and editing (removing songs).
### Why is it not working?
* Ensure that spotipy is installed on your computer. If not, you can install it by typing "pip install spotipy" in the command prompt or terminal in VSCode!
* Make sure you approve spotify permissions!
* Make sure the IDs are correct!
* Make sure you register and create an app in the Spotify developer dashboard!
