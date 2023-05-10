import mindaffectBCI.online_bci
import signal

# Custom SIGINT when CTRL + C is pressed to close everything properly
def SignalHandler_SIGINT(SignalNumber, Frame):
    mindaffectBCI.online_bci.shutdown()
    print("Application closed")
    exit()

# Register the signal with SignalHandler
signal.signal(signal.SIGINT, SignalHandler_SIGINT)

config = {
    # "logdir": "./logs",
    # ACQUISITION
    "acquisition": "brainflow",
    "acq_args": {
        "board_id": 1,
        "mac_address": "f8:06:40:fe:0f:14",
        # Christophe Linux
        # https://mindaffect-bci.readthedocs.io/en/latest/amp_config.html#ampref
        "serial_port": "/dev/ttyACM0",
        # Emmanuel MacOS
        # "serial_port": "/dev/cu.usbmodem11",
    },
    # DECODER
    "decoder": "decoder",
    "decoder_args": {
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
        "calplots": False,
        # Prediction plots
        "predplots": False,
    },
    # PRESENTATION
    # Args:
    #     nCal (int, optional): number of calibration trials. Defaults to 10.
    #     nPred (int, optional): number of prediction trials at a time. Defaults to 10.
    #     selectionThreshold: target error threshold for selection to occur. Defaults to 0.1
    #     simple_calibration (bool, optional): flag if we show only a single target during calibration, Defaults to False.
    #     stimFile ([type], optional): the stimulus file to use for the codes. Defaults to None.
    #     framesperbit (int, optional): number of video frames per stimulus codebit. Defaults to 1.
    #     fullscreen (bool, optional): flag if should runn full-screen. Defaults to False.
    #     fullscreen_stimulus (bool, optional): flag if should run the stimulus (i.e. flicker) in fullscreen mode. Defaults to True.
    #     simple_calibration (bool, optional): flag if we only show the *target* during calibration.  Defaults to False
    #     calibration_trialduration (float, optional): flicker duration for the calibration trials. Defaults to 4.2.
    #     prediction_trialduration (float, optional): flicker duration for the prediction trials.  Defaults to 10.
    #     calibration_args (dict, optional): additional keyword arguments to pass to `noisetag.startCalibration`. Defaults to None.
    #     prediction_args (dict, optional): additional keyword arguments to pass to `noisetag.startPrediction`. Defaults to None.

    "presentation": "selectionMatrix",
    # "presentation": "smart_keyboard.bci_keyboard",
    "presentation_args": {
        "ncal": 1,
        "npred": 3,
        # "selectionThreshold": 0.1,
        "symbols": [['F', 'R']],
        "stimfile": "ssvep.png",
        # "framesperbit": 1,
        # "fullscreen": false,
        # "fullscreen_stimulus": true,
        # "simple_calibration": true,
        # "host": "-",
    }
}

mindaffectBCI.online_bci.run(**config)
