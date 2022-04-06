from flask import Flask, request
import os

app = Flask( __name__ )

@app.route( '/' )
def extract_data() :
    """Driver code for the HouseCallPro required redirect url.
    """

    print( 'Redirect the user' )
    
    return 'Base application - REDIRECT', 200

if __name__ == "__main__" :

    app.run( host='0.0.0.0', port=int( os.getenv( 'PORT', 8080 )))