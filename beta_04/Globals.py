

#Not really global, but that is how we are going to use it.
DEBUG = True

def debug( *args ):
    if DEBUG:
        for message in args:
            print message,
        print
