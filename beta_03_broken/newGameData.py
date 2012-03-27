# File that store data
commands = {
    'addloc':
        [
         # character
         {'pos':(0,0),'objType':'char','pViewImage':'circle.png', 'mViewImage': 'circle.png'},
         
         #background
         {'objType':'bg','mViewImage':'mapBackground.png'},
         
         #overlay
         {'objType':'overlay', 'mViewImage':'colorOverlay.png', 'itemName': 'colorOverlay'},
         {'objType':'overlay', 'mViewImage':'latLongOverlay.png', 'itemName': 'latLongOverlay'},
         {'objType':'overlay', 'mViewImage':'legendOverlay.png', 'itemName': 'legendOverlay'},
         
         
         #cities/trees and others
         {'pos':(-350, 100),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city0'},
         {'pos':(-450, 910),'objType':'landmark','pViewImage':'city2.png','mViewImage':'capital.png', 'itemName':'city1'},
         {'pos':(450, -700),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city2'},
         {'pos':(200,158),'objType':'tree'},
         {'pos':(-800,45),'objType':'tree'},
         {'pos':(120,80),'objType':'tree'},
         {'pos':(310,470),'objType':'tree'},
         {'pos':(220, -400),'objType':'tree'},
         {'pos':(100,500),'objType':'tree'},         
        ],
    
    'addClue':
        [
         {'landmark': 'city1','text': "For this final clue\n Look to the city most southernly"},
         {'landmark':'city0',  'text': "Check 37.8 deg latitude\n (Distance from Equator)"},
         {'landmark': 'city2', 'text':  "Search for the second clue \n in the northernmost city"},
         
        ],
    
    

}
