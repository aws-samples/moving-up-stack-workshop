db = {
    "users": [
        {
            "id": 2,
            "username": "marceline",
            "name": "Marceline Abadeer",
            "bio": "1000 year old vampire queen, musician"
        }
    ],

    "threads": [
        {
            "id": 2,
            "title": "What's up with the Lich?",
            "createdBy": 2
        }
    ],

    "posts": [
        {
            "thread": 2,
            "text": "Has anyone checked on the lich recently?",
            "user": 2
        }
    ]
}


db_more = {
    "users": [
        {
            "id": 1,
            "username": "marceline",
            "name": "Marceline Abadeer",
            "bio": "1000 year old vampire queen, musician"
        },
        {
            "id": 2,
            "username": "finn",
            "name": "Finn 'the Human' Mertens",
            "bio": "Adventurer and hero, last human, defender of good"
        },
        {
            "id": 3,
            "username": "pb",
            "name": "Bonnibel Bubblegum",
            "bio": "Scientist, bearer of candy power, ruler of the candy kingdom"
        }
    ],

    "threads": [
        {
            "id": 1,
            "title": "What's up with the Lich?",
            "createdBy": 4
        },
        {
            "id": 2,
            "title": "Party at the candy kingdom tomorrow",
            "createdBy": 3
        },
        {
            "id": 3,
            "title": "In search of a new guitar",
            "createdBy": 1
        }
    ],

    "posts": [
        {
            "thread": 1,
            "text": "Has anyone checked on the lich recently?",
            "user": 4
        },
        {
            "thread": 1,
            "text": "I'll stop by and see how he's doing tomorrow!",
            "user": 2
        },
        {
            "thread": 2,
            "text": "Come party with the candy people tomorrow!",
            "user": 3
        }
    ]
}
