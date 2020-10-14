from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from firebase import firebase
import time
import json

firebase = firebase.FirebaseApplication('enter your firebase link here', None)  
data =  { 
    'Message': 'mess',  
          'Phone NO':   '7587780420' 
          }  
result = firebase.post('/Notifications/', data)
result = firebase.post('/Notifications/', data)
result = firebase.post('/Notifications/', data)

