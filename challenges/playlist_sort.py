"""
Implement a solution to re-arrange a list of N tracks on a playlist.
The position field of each track must reflect the order. If a position
is given out of range the list should be returned in the current order.

The list data will be in the format displayed in the examples below.

Ex. Move the track data in index 0 to index 2 and update the positions.

initial:

[
    {
        'playlist_id': 1,
        'track_id': 3212,
        'position': 1,
    },
    {
        'playlist_id': 1,
        'track_id': 3213,
        'position': 2,
    },
    {
        'playlist_id': 1,
        'track_id': 3214,
        'position': 3,
    },
    {
        'playlist_id': 1,
        'track_id': 3216,
        'position': 4,
    },
    {
        'playlist_id': 1,
        'track_id': 3217,
        'position': 5,
    },
]

result:

[
    {
        'playlist_id': 1,
        'track_id': 3213,
        'position': 1,
    },
    {
        'playlist_id': 1,
        'track_id': 3214,
        'position': 2,
    },
    {
        'playlist_id': 1,
        'track_id': 3212,
        'position': 3,
    },
    {
        'playlist_id': 1,
        'track_id': 3216,
        'position': 4,
    },
    {
        'playlist_id': 1,
        'track_id': 3217,
        'position': 5,
    },
]

"""


def playlist_sort(playlist_tracks, track_id, position):
    
    # Check the position count, if position is out of range, return list as is
    if position <= len(playlist_tracks):
        
        # Find track entry with given track_id
        # found_track = False
        found_track_position = 0
        
        for track in playlist_tracks:
            if track['track_id'] == track_id:
                # Find position of track to move
                found_track_position = track['position']
            elif found_track_position:
                if position > found_track_position:
                    # Update all track entries between with new positions
                    current_position = track['position']
                    playlist_tracks[current_position-1]['position'] =  current_position - 1
                    if current_position == (position + 1):
                        # Update position of track now that previous one has moved
                        playlist_tracks[found_track_position-1]['position'] = position + 1
                        break
        if found_track_position != 0 and ((position + 1) < (found_track_position)):
            for track in playlist_tracks:
                current_position = track['position']
                if current_position < found_track_position and current_position >= (position + 1):
                    # Update all track entries between position and track to move with new positions
                    playlist_tracks[current_position-1]['position'] =  current_position + 1
                    if current_position == found_track_position - 1:
                        # Stop once we've reached the track before the given track_id
                        break
                    elif current_position == (position + 1):
                        # Update position of track now that previous one has moved
                        playlist_tracks[found_track_position-1]['position'] = position + 1
                    
        playlist_tracks = sorted(playlist_tracks, key=lambda x: x['position'])
    return playlist_tracks
