# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# - intent: properties_entities
#   examples: |
#     - movies [Rowan Atkinson]{"entity": "Name"} acted in
#     - in which movie did [Rowan Atkinson]{"entity":"Name"} act
#     - movies directed by [Christopher Nolan]{"entity": "Name"}.
#     - movies directed by [christopher nolan]{"entity": "Name"}.
#     - [Angela hope]{"entity": "Name"} is followed by
#     - [Tatman]{"entity": "Name"} is followed by
#     - movies produced by [Joel Silver]{"entity": "Name"}.
#     - what are the movies that are produced by [Joel Silver]{"entity": "Name"}
#     - movies reviewed by [James Thompson]{"entity": "Name"}
#     - movies written by [Andy Wachowski]{"entity": "Name"}
#     - movies written by [Tatman]{"entity": "Name"}
#     - who follows [Angela Hope]{"entity":"Name"}
#     - who follows [Tatman]{"entity":"Name"}

#     - Actors born in [1980]{"entity": "Born"}
#     - Actors whose date of birth is [1980]{"entity": "Born"}
    
#     - movies with rating [45]{"entity": "Rating"}
#     - movies whose rating is greater than [45]{"entity": "Rating"}
#     - movies which contains rating below [45]{"entity": "Rating"}
    
#     - movies released before [1980]{"entity": "Released"}
#     - movies released after [1980]{"entity": "Released"}
#     - movies released in [1980]{"entity": "Released"}
#     - movies before [1980]{"entity": "Released"}
#     - movies after [1980]{"entity": "Released"}
#     - movies in [1980]{"entity": "Released"}

#     - director of [Avengers]{"entity":"Movie"}
#     - who is the director of [Notebook]{"entity":"Movie"}
#     - who is the director of [notebook]{"entity":"Movie"}
#     - who acted in the movie [Avengers]{"entity":"Movie"}.
#     - who acted in the movie [avengers]{"entity":"Movie"}.
#     - writer of movie [Avengers]{"entity": "Movie"}
#     - writer of movie [avengers]{"entity": "Movie"}
#     - who produced [avengers]{"entity": "Movie"} movie
#     - who produced [Avengers]{"entity": "Movie"} movie
#     - who produced [Notebook]{"entity": "Movie"} movie
#     - who produced [notebook]{"entity": "Movie"} movie
#     - who is the producer of the movie [Avengers]{"entity": "Movie"}
#     - who is the producer of the movie [avengers]{"entity": "Movie"}
#     - who is the writer of the movie [Avengers]{"entity": "Movie"}
#     - who is the writer of the movie [avengers]{"entity": "Movie"}
#     - who reviewed the movie [Avengers]{"entity": "Movie"}
#     - who is the reviewer of the movie [Avengers]{"entity": "Movie"}
#     - who reviewed the movie [avengers]{"entity": "Movie"}