# Jesus-Saves-HackNCAT-7.0
During the 2023 North Carolina A&amp;T Hackathon (HackNCAT 7.0), the team I was a part of, Jesus Saves, created a prototype of an interface that allows the user to interact with a refrigerator and monitor the logs. This problem was given to us by ThermoFisher. The problems we had to solve include: 

- Creating a log file to show temperature over time
- Locating fridge location and contents
- Identifying potential weaknesses and implementing solutions

Our team used Python to create a working program with the following functionality:

- Allows the user to change the temperature, close the door, and check the temperature, remotely.
- Creates a log entry when the door is opened or closed (remotely or physically), temperature changes, successful user log-ins, and unsuccessful user log-ins.
- Prototype of an application users could interact with instead of the Python Console.

Future functions/implementations that we would include if we had more time would be:

Utilizing Secure Habits
- Implementing two-factor authentication by sending the user an email with a randomly generated code.
- Implementing a fingerprint reader and/or face and iris scanner.
- Requiring password complexity and expiration.
- Storing password hashes instead of plaintext.

Alerting the User
- One problem that we encountered was that the door to the fridge was denoted as closed when it was really open due to the magnet. We would utilize a sensor that must be pressed in order for the door to be recognized as closed. 
- If the temperature is set to or reaches a value outside of the specified range, a designated user will be alerted via email or phone call, depending on the severity.


Overall, it was a very fun and engaging learning experience! I thank Thermo Fisher for the opportunity to compete and the gracious prize I received.

Jesus Saves Team Members:
Andre Harris
Bernard Bridges III
Eden Rhodes
Indya Griffin

