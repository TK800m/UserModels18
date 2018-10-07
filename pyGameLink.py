import pylink as pl
from pylink import getEYELINK
import re
import psychopy
import pygame
import os

screenx = 1600
screeny = 1200
cd = 32   #color depth
screen_dims = (screenx, screeny)
filename = 'mysample.edf'

#el = pl.EyeLink(None)
pygame.init()
pygame.display.init()
#pygame.display.set_mode((800, 600), pygame.FULLSCREEN |pygame.DOUBLEBUF |pygame.RLEACCEL|pygame.HWSURFACE ,32)
#use getModeData() later to get eye_information and sampling_rate


#INITIATE EYETRACKER
def eyeTrkInit (sp):
        #el = pl.EyeLink()      #default - 100.1.1.1
        el = pl.EyeLink(None)
        el.sendCommand("screen_pixel_coords = 0 0 %d %d" %sp)
        el.sendMessage("DISPLAY_COORDS  0 0 %d %d" %sp)
        el.sendCommand("select_parser_configuration 0")
        el.sendCommand("scene_camera_gazemap = NO")
        el.sendCommand("pupil_size_diameter = %s"%("YES"))

        return(el)


el = eyeTrkInit(screen_dims)

#CALLIBRATE EYETRACKER
def eyeTrkCalib (el,sp,cd):
     pl.openGraphics(sp,cd)
     pl.setCalibrationColors((255,255,255),(0,0,0))
     pl.setTargetSize(int(sp[0]/70), int(sp[1]/300))
     pl.setCalibrationSounds("","","")
     pl.setDriftCorrectSounds("","off","off")
     el.doTrackerSetup()
     pl.closeGraphics()
     #el.setOfflineMode()

eyeTrkCalib(el,screen_dims,cd)

edfFileName = filename
pl.getEYELINK().openDataFile(edfFileName)
pl.flushGetkeyQueue();          #gets rid of old keys from the tracker key queue
#pl.getEYELINK().setOfflineMode();


def set_file_contents():
    # set EDF file contents
    pl.getEYELINK().sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
    pl.getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS, PUPILSIZE")

    # set link data (used for gaze cursor)
    pl.getEYELINK().sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON")
    pl.getEYELINK().sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS, PUPILSIZE")

    #button to accept fixation during drift
    #pl.getEYELINK().sendCommand("button_function %d 'accept_target_fixation'"%(5));
    #pl.getEYELINK().sendCommand("button_function %d 'accept_target_fixation'"%(pl.ENTER_KEY));

    return edfFileName

def end_recording():
    pl.getEYELINK().sendMessage("REC_STOP");
    pl.endRealTimeMode();  #set system priority back to normal (still slightly higher though)
    pl.pumpDelay(100);
    pl.getEYELINK().stopRecording();
    #process and dispatch any waiting messages:
    while pl.getEYELINK().getkey() : #0 if no key pressed
        pass;

def end_eyelink():
    '''
    Cleanup and close tracker.
    '''
    if pl.getEYELINK() != None:
        # File transfer and cleanup!
        pl.getEYELINK().setOfflineMode();
        pl.msecDelay(500);

        #Close the file and transfer it to Display PC
        pl.getEYELINK().closeDataFile()
        pl.getEYELINK().receiveDataFile(edfFileName, edfFileName)
        pl.getEYELINK().close()
        pl.closeGraphics()

set_file_contents()

#for each new person, do the following:
getEYELINK().startRecording(1, 1, 1, 1)           #0 if successful. Takes 10-30ms for recording to begin
pl.beginRealTimeMode(100)               #sets highest system priority and waits 100ms

#wait for sample data via link for max 1000 ms
if not getEYELINK().waitForBlockStart(1000,1,0): #returns true if data available
    end_recording()
    print ("ERROR: No link samples received!")
    getEYELINK().sendMessage("TRIAL ERROR")
    end_eyelink()





#Run LineReader
os.system('source activate UMpy27')
os.system('python /Users/apple/Documents/GitHub/UserModels18-mine/lineReader_plus_Q.py')


'''
#Get eye used
eye_used = pl.getEYELINK().eyeAvailable(); #determine which eye(s) are available 0:left, 1:right
if eye_used == pl.RIGHT_EYE:
  	pl.getEYELINK().sendMessage("EYE_USED 1 RIGHT");
elif eye_used == pl.LEFT_EYE or eye_used == pl.BINOCULAR:
  	pl.getEYELINK().sendMessage("EYE_USED 0 LEFT");
  	eye_used = pl.LEFT_EYE;
else:
  	print "Error in getting the eye information!";

eventblock = pl.getEYELINK().getEventsInBlock()

a=0
all_event_json = {}
while a<=100:
    this_data = {}
    dt = pl.getEYELINK().getNewestSample() # check for new sample update
    if(dt != None):
		# Gets the gaze position of the latest sample,
		if eye_used == pl.RIGHT_EYE and dt.isRightSample():
			gaze_position = dt.getRightEye().getGaze()
		elif eye_used == pl.LEFT_EYE and dt.isLeftSample():
			gaze_position = dt.getLeftEye().getGaze()

    this_data.update({'gaze_position':gaze_position})

    dt = pl.getEYELINK().getEventDataFlags()   # get new eventdataflags for pupilsize, gaze and velocity
    if eye_used == pl.RIGHT_EYE and dt.isRightSample:
        pupil_size = dt.getRightEye().getPupilSize()
    elif eye_used == pl.LEFT_EYE and dt.isLeftSample():
        pupil_size = dt.getLeftEye().getPupilSize()

    this_data.update({'pupil_size':pupil_size})
    all_event_json.update({a:this_data})
    a= a+1
'''

