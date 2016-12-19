# webcam-xylophone
An augemented reality xylophone that lights up and plays notes when you move your finger over them. This is a Max patch, which will run in [Max](https://cycling74.com/products/max/). If a Google Cloud Vision API key is specified in `generatejson.py`, emotion recognition is enabled, and while playing the xylophone, the set of notes will change based on happy, sad, angry, etc. emotions that Google is able to detect from your face.

## Requirements
  1. Download `cv.jit` package from the Max package manager
  2. Download the `shell` package from https://cycling74.com/toolbox/bernstein-shell/
  3. Download the `requests` package for python (2.7) like ```sudo -H pip2.7 install requests``` or ```sudo -H pip install requests``` If you can't manage to get this to work, use the patch without the Google API: ar_xylophone_sans_google

## Instructions for use
1. Find the absolute working directory where this max patch (and accompanying files) are located and write it (copy/paste it) into the above message, then bang the message. Make sure to include the trailing slash. On my computer, it looks like /Users/jakobkarstens/Desktop/maxpats/final/ -- This allows the `shell` object to access the files here.
2. Click `open` at the top left to open the webcam, then turn the toggle on to start the entire program.
3. Move your fingers and hit the notes in quick, motions! They will light up and play notes.
4. Try smiling at the camera for a few seconds straight (3 to be exact) - Google should be able to recognize the emotion as happy, and the
notes will be happy notes. Try contorting your face into sad or angry faces and if Google is able to recognize the emotion,
the notes will change to sad or angry notes. 
5. Adjust the slider labeled `MOTION SENSITIVITY` as necessary to make the xylophone notes more or less sensitive to movement.

## Notes (pun intended)
 - This works best in a will-let room, finger contrasting against the background, computer on table steady, nothing else moving in the background.
 - Google seems best at detecting "joy" as opposed to other emotions. "anger" seems to come up more often than it shoud...
 - If the `shell` object stops working (it is known to be buggy) or you just want to try it without the emotion recognition, just the xylophone notes, play with the ar_xylophone_sans_google max patch
