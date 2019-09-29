# alphabet-recognition
This is our submission for the ImplementAI 2019 hackathon

## Requirements
Our project uses `pygame` and `pytesseract`

## Instructions
Install the required packages, then run the `game.py` file from the command line. 
* The blue dot is controlled with the W/S/A/D keys (for up/down/left/right respectively). 
* The red dot is controlled with the arrow keys. 
* Touch the dots together to turn on/off tracing. The tracing is done by the red dot.
* Whenever tracing is turned off, a screenshot of the game is saved 
and the optical character recognition module is used to make a prediction.
  * If the prediction is correct, press 'Return' to save the character and start writing the next character. 
    The stored word word will be printed to the terminal.
  * If the prediction is incorrect, press the spacebar to clear the screen without saving the character.
  * If you haven't finished writing the character, continue writing without pressing any key.
