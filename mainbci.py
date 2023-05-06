import mindaffectBCI.online_bci
# from mindaffectBCI.utopia2output import Utopia2Output
import signal

# Custom SIGINT when CTRL + C is pressed to close everything properly
def SignalHandler_SIGINT(SignalNumber,Frame):
    if "hub_process" in locals():
        mindaffectBCI.online_bci.shutdown(hub_process)
    if "acq_process" in locals():
        mindaffectBCI.online_bci.shutdown(acq_process)
    if "decoder_process" in locals():
        mindaffectBCI.online_bci.shutdown(decoder_process)
    print()
    exit()

# Register the signal with SignalHandler
signal.signal(signal.SIGINT, SignalHandler_SIGINT)


# def testoutput(objID):
#     print(f"\nPrediction {objID}\n")
#
#

# Start the utopia-hub process
hub_process = mindaffectBCI.online_bci.startHubProcess()


# u2o = Utopia2Output()
# # Set the objectID2Action dictionary to use our helloworld function if 1 is selected
# u2o.objectID2Action = {
#     -1: testoutput,
#     0: testoutput,
#     1: testoutput,
#     2: testoutput,
#     3: testoutput,
#     4: testoutput,
#     5: testoutput,
#     6: testoutput,
#     7: testoutput,
# }

# Start the ganglion acquisition process
# Using brainflow for the acquisition driver
acq_args = {
    "board_id": 1,
    # "mac_address": "F8:28:19:EB:CB:0A",
    "mac_address": "f8:06:40:fe:0f:14",
    # Christophe Linux
    # https://mindaffect-bci.readthedocs.io/en/latest/amp_config.html#ampref
    "serial_port": "/dev/ttyACM0",
    # Emmanuel MacOS
    # "serial_port": "com4",
}
acq_process = mindaffectBCI.online_bci.startacquisitionProcess('brainflow', acq_args)


# Start the decoder process, with default args for noise-tagging
decoder_args = {
    # Filter frequencies
    "stopband": ((3, 90, "bandpass"), (47, 53), (57, 63)),
    # Post-filtering sampling rate of the data, should be greater than twice the maximum frequency
    "out_fs": 100,
    # 're', 'fe', 'flash', what is the brain response trigger
    # 're' is rising-edge and 'fe' is falling-edge
    "evtlabs": ("re", "fe"),
    # Expected brain response after x ms
    "tau_ms": 300,
    # End-of-calibration plots
    "calplots": True,
    # Prediction plots
    "predplots": True,
}
decoder_process = mindaffectBCI.online_bci.startDecoderProcess('decoder', decoder_args)

# If there is a problem show where it is a stop everything
if not mindaffectBCI.online_bci.check_is_running(hub_process, acq_process, decoder_process):
    print(f"Hub was running: {hub_process.poll() is None}")
    print(f"Acquisition was running: {acq_process.is_alive()}")
    print(f"Decoder was running: {decoder_process.is_alive()}")
    mindaffectBCI.online_bci.shutdown(hub_process, acq_process, decoder_process)
    exit()

# u2o.connect()
# u2o.run()


# Here is an example presentation, to remove when our interface/presentation is done
# symbols could be a 2D list with strings that are display on the screen
# symbols = [["I'm happy","I'm sad"], ["I want to play","I want to sleep"]]
symbols = [['F', 'R'], ['I', 'B'], ['O', 'U', 'G']]

# Run the presentation, with our matrix and default parameters for a noise tag
from mindaffectBCI.examples.presentation import selectionMatrix
selectionMatrix.run(symbols=symbols, stimfile="ssvep.png")
# selectionMatrix.run(symbols=symbols, stimfile="mgold_65_6532_psk_60hz.png")

# shutdown the background processes
# N.B. only needed if something went wrong..
mindaffectBCI.online_bci.shutdown(hub_process, acq_process, decoder_process)
exit()

# config = mindaffectBCI.online_bci.load_config('noisetag_bci')
# uncomment this line to use fakedata
#config['acquisition']='fakedata'
# mindaffectBCI.online_bci.run(**config)
