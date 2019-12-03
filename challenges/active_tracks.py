"""
Given a list of track data, return the IDs of active tracks.
The list may contain duplicate tracks.

    [
        {
            'id': 1,
            'name': 'In Arms',
            'active': True,
        },
        {
            'id': 2,
            'name': 'Deep Dip',
            'active': False,
        },
        {
            'id': 3,
            'name': 'Panic Room',
            'active': True,
        },
        {
            'id': 1,
            'name': 'In Arms',
            'active': True,
        },
    ]  # should return [1, 3]

"""


def active_tracks(tracks):
    active_tracks = []
    
    # iterate tracks 
    for track in tracks:
        # if the track is already in the track list, skip
        if not track['id'] in active_tracks:
            # if the unique track is active, add it to list
            if track['active'] == True:
                active_tracks.append(track['id'])
            
    return active_tracks
