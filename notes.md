# Notes on the BCI project
## Administrative stuff and general info
- Our validation will be done between two parts:
  1. Mesure time and opinion of the user when remaining still after typing a key (dwell time), and make a face movement to UNDO (i.e. clear) the letter he has typed
  2. Same but with a specific validation after each letter, and use a clear button?
  3. Could make the same experiment but with another layout (QWERTY vs alphabetical?)
  4. User evaluation will be done with 5 to 10 people


## Brainwaves and EEG stuff
### BCI and Cyton board
- To **place the electrodes** we can use the 10-20 system (EGG). This shows where to place the electrodes depending on the part of the brain we want to measure.
- With our Cyton board, we have 4 channels. These channels measure the **difference of potential** of the given electrodes with the electrode we place to the lobe of the ear (the REF pin).
- The other pin (D_G) is to make some noise cancelling, it makes a common ground between the body and the Cyton board

### Brainwaves
Different type of brainwaves depending on the frequency:
1. Delta waves (0.5 to 4 Hz), they help to characterize the depth of sleep (stage 3 of NREM, non-rapid eye movement)
2. Theta waves (4 to 7 Hz), they are used to measure things like learning, the memory or spatial navigation (e.g. walking), emitted by the hippocampus
3. Alpha waves (8 to 12 Hz), emitted by the occipital lobe (behind the head), it is the activity of the brain when we relaxe for example with closed eyes, and are at their highest peak during drowsiness (i.e. just before falling asleep). It seems that alphawave spike before a mistake, so it can be meaused in mistake prediction
4. Mu waves (7.5 to 12.5 Hz), emitted by the part of the brain that controls the voluntary movement, spike when body is physically at rest. Wikipedia is talking about BCI for this wave, because it seems that measuring these waves could help people with physical problems to communicate and navigate.
5. SMR waves (12.5 to 15.5 Hz), or sensorimotor rhythm, not fully understand by now. Spikes when snsorimotor parts of the brain are at rest
6. Beta waves (15 to 30 Hz), split into three groups (low betawaves/beta 1, betawaves/beta 2 and high betawaves/beta3 depending on the frequency), it seems to be associated with waking consciousness or active concentration/thinking
7. Gamma wave (> 30 Hz), correlated with working memory, attention. They are increased via meditation or neurostimulation. It seems that people with Alzheimer or epilepsy or schizophrenia have an altered gamma activity.

### Event-related potentials (ERP)
1. P300 is an event-related potential, an appeares when the human has a surprise. P stands for positive amplitude and 300 because the spike (i.e. difference of potential measured)  appears around 300 ms after the "surprise"/stimulus. I am not really sure about the amplitude but it seems it has an increasing of the amplitude of around 10 microvolts.
2. N170, N stands for negative amplitude, and is observed when the human recognize a face, and so the spike is meaured (negatively) 170 ms after seeing the face (so that is very quick!)

### Evoked potentials
These are similar than event-related potentials but with a lower latency. While ERP are associated with higher cognitive process, EP are a response with a quick stimulus (with a visual feature, or some audio trigger)
1. P300 could also have a spike related to a evoked potential
1. Steady-state (visual) evoked potential (SSvEP) can be used with repeated visual stimulus (like a blinking effect in our case) and this will then be activated at the same frequency than the blinking. That is what our BCI is used to work 


## Code and implementation
- Indices of the landmarks of FaceMesh https://github.com/Unity-Technologies/arfoundation-samples/issues/754
- We are implementing an evoked-response BCI https://mindaffect-bci.readthedocs.io/en/latest/how_an_evoked_bci_works.html that is at each blink/flash a spike is measures. By knowing the frequence, we can compare the frequence with the sequence of spikes measured: https://sapienlabs.org/lab-talk/bci-using-steady-state-visual-evoked-potentials/
