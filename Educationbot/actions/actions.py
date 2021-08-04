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
import json
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    knowledge = Path("data/data_set.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            for blob in tracker.latest_message['entities']:
                print(tracker.latest_message)
                print(blob['entity'])
              #  print("%s" %datatable)
            if blob['entity'] == 'datatable':
                name = blob['value']
               # print("root part of '%s':" %self.knowledge)
                if name in self.knowledge:
                    dispatcher.utter_message(text=f"Yes, {name} is a student.")
                else:
                    dispatcher.utter_message(text=f"I do not recognize {name}, are you sure it is correctly spelled?")
            return []


#class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
 #   def __init__(self):
  #      knowledge_base = InMemoryKnowledgeBase("data/pokemondb.json")
   #     super().__init__(knowledge_base)
