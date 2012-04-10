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
         {'objType':'overlay', 'mViewImage':'latOverlay.png', 'itemName': 'latLongOverlay'},
         {'objType':'overlay', 'mViewImage':'legendOverlay.png', 'itemName': 'legendOverlay'},
         
         
         #cities/trees and others
         {'pos':(-350, 100),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city0'},
         {'pos':(-450, 910),'objType':'landmark','pViewImage':'city2.png','mViewImage':'capital.png', 'itemName':'city1'},
         {'pos':(450, -700),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city2'},

         {'pos':(-1700, -600),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city3'},
         {'pos':(-1800, 1000),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city4'},
         {'pos':(800, 1200),'objType':'landmark','pViewImage':'city2.png','mViewImage':'capital.png', 'itemName':'city5'},

         {'pos':(-1400, -1000),'objType':'landmark','pViewImage':'city2.png','mViewImage':'capital.png', 'itemName':'city6'},
         {'pos':(300, -1900),'objType':'landmark','pViewImage':'city2.png','mViewImage':'city.png', 'itemName':'city7'},
         {'pos':(0, -1300),'objType':'landmark','pViewImage':'city2.png','mViewImage':'capital.png', 'itemName':'city8'},
         {'pos':(0, -1800),'objType':'landmark','pViewImage':'Forest3.png','mViewImage':'tree.png', 'itemName':'forest0'},
         {'pos':(-500, 1700),'objType':'landmark','pViewImage':'Forest3.png','mViewImage':'tree.png', 'itemName':'forest1'},

         {'pos':(200,158),'objType':'tree'},
         {'pos':(-800,45),'objType':'tree'},
         {'pos':(120,80),'objType':'tree'},
         {'pos':(310,470),'objType':'tree'},
         {'pos':(220, -400),'objType':'tree'},
         {'pos':(100,500),'objType':'tree'},

         {'pos':(-1800, 1600),'objType':'tree'},
         {'pos':(-1600,1600),'objType':'tree'},
         {'pos':(500,1100),'objType':'tree'},
         {'pos':(550,1100),'objType':'tree'},
         {'pos':(-450, -400),'objType':'tree'},
         {'pos':(100,1300),'objType':'tree'},    
                 
        ],
    
    'addClue':
        [
         {'landmark': 'forest0','text': "For this final clue\n search the coldest forest"},
         {'landmark':'city0',  'text': "Find the next clue\n in a city known for its timber"},
         {'landmark': 'city5', 'text':  "Search for the next clue \n in the smallest nation's capital"},
         
         {'landmark': 'forest1','text': "Find the next clue in the\n most tropical forest"},
         {'landmark':'city2',  'text': "Check the city that is \n closest to 39 deg latitude"},
         {'landmark': 'city3', 'text':  "Find the next clue \n in a city close to its capital"},

         {'landmark': 'city4','text': "The next clue lies within the \n same nation\n "},
         {'landmark':'city1',  'text': "Search the nearest capital\n for the next clue"},
         {'landmark': 'city5', 'text':  "Search for the second clue \n at 120 deg longitude"},
         
        ],
    
    

}
