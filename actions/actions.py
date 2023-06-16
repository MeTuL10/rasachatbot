# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime
import requests

class Actiontime(Action):

    def name(self) -> Text:
        return "action_get_time"
    def run(self, dispatcher,tracker,domain):
        ct=datetime.datetime.now()
        s="the time is "+str(ct)
        dispatcher.utter_message(s)
        return []
    

class Actionadd(Action):

    def name(self) -> Text:
        return "action_add"
    def run(self, dispatcher,tracker,domain):
        a = tracker.get_slot('num1')
        a=int(a)
        b= tracker.get_slot('num2')
        b=int(b)
        s="the sum of the numbers: "+str(a+b)
        dispatcher.utter_message(s)
        return []
    
class Actionsub(Action):

    def name(self) -> Text:
        return "action_sub"
    def run(self, dispatcher,tracker,domain):
        a = tracker.get_slot('num1')
        a=int(a)
        b= tracker.get_slot('num2')
        b=int(b)
        s="the difference of the numbers: "+str(a-b)
        dispatcher.utter_message(s)
        return []
    
class Actionmul(Action):

    def name(self) -> Text:
        return "action_mul"
    def run(self, dispatcher,tracker,domain):
        a = tracker.get_slot('num1')
        a=int(a)
        b= tracker.get_slot('num2')
        b=int(b)
        s="the product of the numbers: "+str(a*b)
        dispatcher.utter_message(s)
        return []
    
class Actiondiv(Action):

    def name(self) -> Text:
        return "action_div"
    def run(self, dispatcher,tracker,domain):
        a = tracker.get_slot('num1')
        a=int(a)
        b= tracker.get_slot('num2')
        b=int(b)
        s="the quotient of the numbers: "+str(a/b)
        dispatcher.utter_message(s)
        return []
    
class Actionage(Action):
    def name(self) -> Text:
        return "action_age"
    def run(self, dispatcher,tracker,domain):
        a = tracker.get_slot('age')        
        s="your age is: "+str(a)
        dispatcher.utter_message(s)
        return []
