Communication Contract (for partner microserevice)

Overview: A random function generator using basic operators (no logarithmic or trig functions) and return the functions after html encoding. 

Tips:
Data can be requested and received using the Flask API for the server.py. Included in the server.py file is are two example html files for rendering, and to help model implementation after. 
Make sure you run pip install -r requirements.txt to make sure you have all the necessary packages and files in your environment

REQUESTING
- use method 'POST'
- for example, when implementing it with your UI, <form method="POST" action ="#"> is sufficient if the service is ran locally (http://127.0.0.1:5000)
- ex)
    - method: 'POST'
    - url: http://127.0.0.1:5000


RECEIVING
- use method 'GET'
- this is the default behavior
- ex)
    - method: 'GET'
    - url: http://127.0.0.1:5000


UML Sequence Diagram
- https://lucid.app/lucidchart/ed6c93ce-7282-44d3-a91c-07c89192f32f/edit?viewport_loc=752%2C-255%2C2889%2C1165%2C0_0&invitationId=inv_bdecaae6-18b6-4f30-8b1f-edb37effa076

:)


