from firebase import firebase

firebase = firebase.FirebaseApplication('https://safesuit-a3fbf.firebaseio.com/')

firebase.put('',"blinked", True)
