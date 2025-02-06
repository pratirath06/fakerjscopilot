def load_faker_music_docs():
    docs = {
        "music": {
            "album": {
                "description": "Returns a random album name",
                "patterns": [
                    "album name", "record name",
                    "music album", "generate album"
                ],
                "examples": [
                    "faker.music.album() // '1989'"
                ],
                "notes": [
                    "Returns localized album names if available",
                    "Pulls from a curated list of popular albums"
                ]
            },
            "artist": {
                "description": "Returns a random artist name",
                "patterns": [
                    "artist name", "band name",
                    "musician name", "generate artist"
                ],
                "examples": [
                    "faker.music.artist() // 'The Beatles'"
                ],
                "notes": [
                    "Returns localized artist names if available",
                    "Includes both bands and solo artists",
                    "Pulls from a curated list of notable musicians"
                ]
            },
            "genre": {
                "description": "Returns a random music genre",
                "patterns": [
                    "music genre", "musical style",
                    "type of music", "generate genre"
                ],
                "examples": [
                    "faker.music.genre() // 'Reggae'"
                ],
                "notes": [
                    "Returns localized genre names if available",
                    "Includes both broad and specific genres",
                    "Coverage of popular music categories"
                ]
            },
            "songName": {
                "description": "Returns a random song name",
                "patterns": [
                    "song name", "track name",
                    "music title", "generate song"
                ],
                "examples": [
                    "faker.music.songName() // 'White Christmas'"
                ],
                "notes": [
                    "Returns localized song names if available",
                    "Pulls from a curated list of popular songs",
                    "Includes songs from various genres and eras"
                ]
            }
        },
        "usage_examples": {
            "album_catalog": {
                "description": "Generate a complete album entry",
                "code": [
                    "const album = {",
                    "  name: faker.music.album(),",
                    "  artist: faker.music.artist(),",
                    "  genre: faker.music.genre()",
                    "}"
                ]
            },
            "song_catalog": {
                "description": "Generate a complete song entry",
                "code": [
                    "const song = {",
                    "  name: faker.music.songName(),",
                    "  artist: faker.music.artist(),",
                    "  genre: faker.music.genre()",
                    "}"
                ]
            }
        }
    }
    return docs