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
    # ACQUISITION
    # Args:
        # host (str, optional): hostname or IP for the utopiahub. Defaults to None.
        # board_id (int, optional): brainflow board id, see <https://brainflow.readthedocs.io/en/stable/SupportedBoards.html> 0=cyton, 1=ganglyon. Defaults to 1.
        # ip_port (int, optional): brainflow ip-port. Defaults to 0.
        # serial_port (str, optional): brainflow serial-port for the board. Defaults to ''.
        # mac_address (str, optional): brainflow mac-address. Defaults to ''.
        # other_info (str, optional): other info to send to brainflow. Defaults to ''.
        # serial_number (str, optional): board serial number. Optional. Defaults to ''.
        # ip_address (str, optional): brainflow ip_address. Defaults to ''.
        # ip_protocol (int, optional): brainflow ip protocol. Defaults to 0.
        # timeout (float, optional): brainflow timeout. Defaults to 0.
        # streamer_params (str, optional): brainflow streamer params. Defaults to ''.
        # log (int, optional): brainflow log level. Defaults to 1.
        # config_params (list, optional): additional configuration parameters to send to the board after startup. Defaults to None.
        # trigger_check (bool, optional): flag to configure channel-8 on cyton as trigger input, e.g. for timing tests. Defaults to 0.
        # samplingFrequency (float, optional): desired sampling rate to set the board to. Defaults to 0.
    # "acquisition": "fakedata",
    "acquisition": "brainflow",
    "acq_args": {
        "board_id": 1,
        "mac_address": "f8:06:40:fe:0f:14",
        # On Linux
        "serial_port": "/dev/ttyACM0",
        # On MacOS
        # "serial_port": "/dev/cu.usbmodem11",
    },
    # DECODER
    # Args:
        # ui (UtopiaDataInterface, optional): The utopia data interface class. Defaults to None.
        # clsfr (BaseSequence2Sequence, optional): the classifer to use when model fitting. Defaults to None.
        # msg_timeout_ms (float, optional): timeout for getting new messages from the data-interface. Defaults to 100.
        # host (str, optional): hostname for the utopia hub. Defaults to None.
        # tau_ms (float, optional): length of the stimulus response. Defaults to 400.
        # offset_ms (float, optiona): offset in ms to shift the analysis window. Use to compensate for response lag.  Defaults to 0.
        # stopband (tuple, optional): temporal filter specification for `UtopiaDataInterface.butterfilt_and_downsample`. Defaults to ((45,65),(5.5,25,'bandpass'))
        # ftype (str, optional): type of temporal filter to use.  Defaults to 'butter'.
        # logdir (str, optional): location to save output files.  Defaults to None.
        # order (int, optional): order of temporal filter to use.  Defaults to 6.
        # out_fs (float, optional): sample rate after the pre-processor. Defaults to 100.
        # evtlabs (tuple, optional): the brain event coding to use.  Defaults to None.
        # calplots (bool, optional): flag if we make plots after calibration. Defaults to False.
        # predplots (bool, optional): flag if we make plots after each prediction trial. Defaults to False.
        # prior_dataset ([str,(dataset)]): calibration data from a previous run of the system.  Used to pre-seed the model.  Defaults to None.
        # prediction_offsets ([ListInt], optional): a list of stimulus offsets to try at prediction time to cope with stimulus timing jitter.  Defaults to None.

    "decoder": "decoder",
    "decoder_args":{
        "stopband" : [[45,65],[0,3],[25,-1]],
        "out_fs" : 100,
        "evtlabs" : ["re","fe"],
        "tau_ms" : 300,
        "calplots" : False,
        "predplots" : False,
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
    "presentation_args": {
        "ncal": 10,
        "npred": 10,
        "selectionThreshold": 0.2,
        "symbols": [['H', 'C', 'O'], ['A', 'S', 'N']],
        "stimfile": "ssvep.png",
        "framesperbit": 2,
        "fullscreen": False,
        "calibration_trialduration": 10,
    },
}

mindaffectBCI.online_bci.run(**config)
