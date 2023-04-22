#this notebook comes from tutorial https://mindaffect-bci.readthedocs.io/en/latest/simple_output_tutorial.html

#creating a simple output module


# Import the utopia2output module
from mindaffectBCI.utopia2output import Utopia2Output

u2o=Utopia2Output()

def helloworld(objID):
   print("hello world")


#And connect it so it is run when the object with ID=1 is selected. You can create as many output functions as needed,
#and connect them to different object ID’s by simply adding them to the dictionary as key-value pairs.

# set the objectID2Action dictionary to use our helloworld function if 1 is selected
u2o.objectID2Action={ 1:helloworld }


#To successfully test your presentation module it is important to have the other components of the BCI running.
#As explained in the quickstart tutorial, additionally to the presentation we build here, we need the Hub, Decoder, and
#Acquisition components for a functioning BCI.
#For a quick test (with fake data) of this presentation module you can run all these components with a given configuration
#file using.
import mindaffectBCI.online_bci
config = mindaffectBCI.online_bci.load_config('fake_recogniser.json')
mindaffectBCI.online_bci.run(**config)

#We now connect our output module to a running decoder and run the main loop. Selection of ID=1 will result in printing
#“Hello World” to this prompt.

# connect
u2o.connect()

# run the main loop
u2o.run()
