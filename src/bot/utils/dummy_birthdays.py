from datetime import date, timedelta

# Small set of dummy birthdays for testing.
# The event dates are set relative to today so they follow each day:
# first entry = today + 1 day, next = today + 2 days, ... up to 7 entries.
_today = date.today()

DUMMY_BIRTHDAYS = {
    "Ada Lovelace": {
        "person_name": "Ada Lovelace",
        "event_date": _today + timedelta(days=1),
        "born_on": f"{(_today + timedelta(days=1)).day:02}.{(_today + timedelta(days=1)).month:02}.1900",
        "email": "ada@example.com",
        "relation": "hero",
        "hobbies": "math, poetry",
        "greeting_style": "with admiration",
    },
    "Alan Turing": {
        "person_name": "Alan Turing",
        "event_date": _today + timedelta(days=2),
        "born_on": f"{(_today + timedelta(days=2)).day:02}.{(_today + timedelta(days=2)).month:02}.1900",
        "email": "alan@example.com",
        "relation": "mentor",
        "hobbies": "puzzles",
        "greeting_style": "with deep respect",
    },
    "Grace Hopper": {
        "person_name": "Grace Hopper",
        "event_date": _today + timedelta(days=3),
        "born_on": f"{(_today + timedelta(days=3)).day:02}.{(_today + timedelta(days=3)).month:02}.1900",
        "email": "grace@example.com",
        "relation": "inspiration",
        "hobbies": "navy, compilers",
        "greeting_style": "with gratitude",
    },
    "Katherine Johnson": {
        "person_name": "Katherine Johnson",
        "event_date": _today + timedelta(days=4),
        "born_on": f"{(_today + timedelta(days=4)).day:02}.{(_today + timedelta(days=4)).month:02}.1900",
        "email": "katherine@example.com",
        "relation": "colleague",
        "hobbies": "astronomy",
        "greeting_style": "with pride",
    },
    "Tim Berners-Lee": {
        "person_name": "Tim Berners-Lee",
        "event_date": _today + timedelta(days=5),
        "born_on": f"{(_today + timedelta(days=5)).day:02}.{(_today + timedelta(days=5)).month:02}.1900",
        "email": "tim@example.com",
        "relation": "friend",
        "hobbies": "web",
        "greeting_style": "cheerfully",
    },
    "Linus Torvalds": {
        "person_name": "Linus Torvalds",
        "event_date": _today + timedelta(days=6),
        "born_on": f"{(_today + timedelta(days=6)).day:02}.{(_today + timedelta(days=6)).month:02}.1900",
        "email": "linus@example.com",
        "relation": "peer",
        "hobbies": "linux",
        "greeting_style": "with a wink",
    },
    "Margaret Hamilton": {
        "person_name": "Margaret Hamilton",
        "event_date": _today + timedelta(days=7),
        "born_on": f"{(_today + timedelta(days=7)).day:02}.{(_today + timedelta(days=7)).month:02}.1900",
        "email": "margaret@example.com",
        "relation": "advisor",
        "hobbies": "software",
        "greeting_style": "with admiration",
    },
}

__all__ = ["DUMMY_BIRTHDAYS"]
