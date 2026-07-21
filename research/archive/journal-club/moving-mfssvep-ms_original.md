# Novel Moving Steady-State Visual Evoked Potential Stimulus to Assess Afferent and Efferent Dysfunction in Multiple Sclerosis

- DOI: https://doi.org/10.1109/TNSRE.2023.3243554
- Source PDF: `research/paper_candidates/papers/Novel_Moving_Steady-State_Visual_Evoked_Potential_Stimulus_to_Assess_Afferent_and_Efferent_Dysfunction_in_Multiple_Sclerosis.pdf`
- Extraction: `pdftotext` reading-order text

---

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 31, 2023

1297

Novel Moving Steady-State Visual Evoked
Potential Stimulus to Assess Afferent and
Efferent Dysfunction in Multiple Sclerosis
Masaki Nakanishi , Senior Member, IEEE, Annalise Miner,
Tzyy-Ping Jung , Fellow, IEEE, and Jennifer Graves
Abstract— Afferent and efferent visual dysfunction are
prominent features of multiple sclerosis (MS). Visual outcomes have been shown to be robust biomarkers of the
overall disease state. Unfortunately, precise measurement
of afferent and efferent function is typically limited to tertiary care facilities, which have the equipment and analytical capacity to make these measurements, and even then,
only a few centers can accurately quantify both afferent and
efferent dysfunction. These measurements are currently
unavailable in acute care facilities (ER, hospital floors).
We aimed to develop a moving multifocal steady-state
visual evoked potential (mfSSVEP) stimulus to simultaneously assess afferent and efferent dysfunction in MS
for application on a mobile platform. The brain-computer
interface (BCI) platform consists of a head-mounted virtualreality headset with electroencephalogram (EEG) and electrooculogram (EOG) sensors. To evaluate the platform,
we recruited consecutive patients who met the 2017 MS
McDonald diagnostic criteria and healthy controls for a
pilot cross-sectional study. Nine MS patients (mean age
32.7 years, SD 4.33) and ten healthy controls (24.9 years,
SD 7.2) completed the research protocol. The afferent measures based on mfSSVEPs showed a significant difference
between the groups (signal-to-noise ratio of mfSSVEPs for
controls: 2.50 ± 0.72 vs. MS: 2.04 ± 0.47) after controlling
for age (p = 0.049). In addition, the moving stimulus successfully induced smooth pursuit movement that can be
measured by the EOG signals. There was a trend for worse
smooth pursuit tracking in cases vs. controls, but this did
not reach nominal statistical significance in this small pilot
sample. This study introduces a novel moving mfSSVEP
stimulus for a BCI platform to evaluate neurologic visual
function. The moving stimulus showed a reliable capability to assess both afferent and efferent visual functions
simultaneously.
Manuscript received 11 July 2022; revised 14 October 2022 and
12 December 2022; accepted 27 December 2022. Date of publication 8 February 2023; date of current version 16 February 2023.
This work was supported by the University of California San Diego
Galvanizing Engineering in Medicine Program. (Corresponding author:
Masaki Nakanishi.)
This work involved human subjects or animals in its research. Approval
of all ethical and experimental procedures and protocols was granted
by the University of California San Diego Human Research Protections
Program.
Masaki Nakanishi and Tzyy-Ping Jung are with the Swartz Center for Computational Neuroscience, Institute for Neural Computation,
University of California San Diego, La Jolla, CA 92093 USA (e-mail:
masaki@sccn.ucsd.edu; jung@sccn.ucsd.edu).
Annalise Miner and Jennifer Graves are with the Department of Neuroscience, University of California San Diego, La Jolla, CA 92093 USA
(e-mail: aeminer@health.ucsd.edu; jgraves@health.ucsd.edu).
Digital Object Identifier 10.1109/TNSRE.2023.3243554

Index Terms— Afferent and efferent visual pathway,
electroencephalogram (EEG), electrooculogram (EOG),
multifocal steady-state visual evoked potential (mfSSVEP),
multiple sclerosis (MS), virtual reality headset.

I. I NTRODUCTION
NE of the greatest unmet needs in multiple sclerosis
(MS) research and clinical care is the ability to quantify
disease burden with highly reproducible and rater-independent
methods. Significant advancements have been made in measuring visual dysfunction through the use of low-contrast letter
acuity measures, visual evoked potentials (VEP), optical coherence tomography (OCT), and efferent oculometrics, but these
tools are not in widespread use in most MS clinics and often
require support from those with subspecialty training in neuroophthalmology [1]. Most of the equipment is cumbersome
and immovable. The functional vision measures also typically
require performing a correction of refractive error, which most
neurologists are not equipped to provide in their offices.
Despite the difficulty of conducting extensive, systematic
visual testing in neurology clinics or acute care settings, the
visual system has demonstrated an exceptional ability to detect
demyelinating injury even in those who have no clinical symptoms. Standard full-field VEP has been used to support the
diagnosis of MS for over 50 years [2], [3]. In young patients
with MS, without any detectable exam finding abnormalities,
latency delays can be seen for saccadic (fast) eye movements
that distinguish these patients from healthy controls [4]. Disruption of smooth pursuit eye movements also distinguishes
MS eyes from controls [5]. The current understanding of the
quantitative relationships between structure and function in the
visual system far surpasses that of other central nervous system
pathways. Thus, the afferent and efferent visual pathways are
well poised to serve as a model system of injury and repair for
therapeutic investigations and clinical monitoring in MS [6].
The majority of MS patients are not diagnosed or cared
for in clinic settings with advanced visual function testing
facilities. A mobile platform that does not require dedicated
room space or a trained technician, such as the one proposed here, would enable more widespread use of quantitative afferent/efferent vision testing in acute care settings and
non-tertiary care centers.
Efferent visual function testing is currently only used in
observational research settings. Despite its proven ability to

O

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

1298

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 31, 2023

detect dysfunction, quantification of dysfunction has not been
brought to the clinic or trial setting. This situation is largely
due to the lack of technical expertise and immovable equipment needed to perform these measurements. As an example,
one of the most commonly used platforms for MS studies
requires the clinician, technician or researcher to write their
own software, which is not practical for neurologists in private
practice. By developing commercial-grade algorithms, we will
remove the need for signal-processing expertise. The use of
a headset platform will allow the testing to be brought to
the patient rather than having to burden the patient with a
trip to an offsite research lab. Removing these critical barriers
will facilitate the use of efferent visual outcome measures in
clinical trials and clinic settings.
Recently, brain-computer interfaces based on multi-focal
steady-state VEP (mfSSVEP) have been used to objectively
assess visual-field deficits in glaucoma patients [7]. In contrast
to transient (i.e., standard) VEPs, steady-state VEPs (SSVEPs)
are elicited by rapid flickering stimulation, producing a
brain response characterized by a quasi-sinusoidal waveform
that has frequency components with constant amplitude and
phase [8]. The technique is faster than standard VEPs and
less susceptible to artifacts produced by blinking and eye
movements as well as electromyographic noise contamination,
and it may present a better signal-to-noise ratio [9], [10],
[11], [12], [13], [14]. The current study builds on the prior
work in glaucoma by adding a moving multi-focal SSVEP
(mfSSVEP) stimulus for assessing both afferent and efferent
visual function simultaneously. The MSight BCI platform
piloted in this study will greatly facilitate research on the
correlations between the afferent and efferent measures in
neurological disease and support the development of new and
novel indices of MS-related visual dysfunction. We hypothesized that SSVEP amplitudes across the frequencies assessed
would be lower compared to control subjects given the high
prevalence of both clinical and subclinical afferent injury
in MS. We also hypothesized reduced fidelity of stimulus
tracking in the efferent measure based on high rates of efferent
visual dysfunction even in those with mild disease course.
II. M ETHODS
A. Participants
We offered enrollment to consecutive patients who attended
the University of California San Diego (UCSD) MS Center.
Participants with MS had to meet the updated 2017 McDonald
criteria for MS [15]. The included participants were exposed
to a variety of MS disease modifying medications including
oral (e.g., dimethyl fumarate, fingolimod) and infusion (e.g.,
ocrelizumab) medications. Age similar healthy controls had no
history of neurological or ophthalmological disease. The study
was approved by UCSD Human Research Protections Program
and all participants provided informed written consent.
B. Visual Stimulus
Multi-focal visual stimuli consisting of two patterns of
20 sectors in three concentric rings (subtending 8.4◦ , 21◦ ,
and 35◦ of the visual field) and moving in 15◦ -wide 2-D

Fig. 1. A moving multi-focal stimulus. (Top) The stimulus was presented
at the center of a screen and started to move at a constant speed
with an angle θ assigned randomly in a 15◦ -wide 2-D space. To avoid
visually-crowded illustration, the fixation point was depicted rather than
the multi-focal stimulus in the figure. (Bottom) Participants fixed their
gaze at the center of the stimulus so that it simultaneously elicits multifocal steady-state visual evoked potentials (mfSSVEPs) and smooth eye
movements.

space at a constant speed [8] were implemented and presented on a Samsung Odyssey + head-mounted display
(HMD). Different frequencies were assigned to each sector,
ranging from 8 to 11.8 Hz with a frequency interval of
0.2 Hz. To enhance the signal-to-noise ratio (SNR) in eliciting mfSSVEPs, the platform uses a frequency-approximation
approach to render flexible frequencies with a variable number
of frames in a stimulating period [16], [17]. Two patterns
(A and B) of visual stimuli, each with 10 of 20 sectors
flickered concurrently, were presented separately, to facilitate
the calculation of the SNR (see II-D Data Analysis). For
example, the stimulus pattern A contained 8 to 11.6 Hz with
a 0.4 Hz interval and the stimulus pattern B contained 8.2 to
11.8 Hz with a 0.4 Hz interval. The fixation target moves in
2-D space at v = 60◦ /s rendered randomly and smoothly on
the screen of the HMD (Fig. 1). At the beginning of each
trial, a 2-D moving angle θ was assigned, and the horizontal
and the vertical moving speeds were determined based on
the angle. For example, horizontal and vertical speeds can
be determined as vcos(θ ) and vsin(θ ), respectively. Once the
stimulus reached to one of the 15◦ -wide boundaries in four
directions, the moving direction was flipped as shown in Fig.1.
C. Data Acquisition
EEG and electrooculogram (EOG) data were measured
using a BioSemi ActiveTwo EEG system (BioSemi, Inc.). EEG
data were recorded with nine Ag/AgCl Electrodes covering the
occipital area and an additional one at Cz. EOG electrodes
were placed above the superior orbit and below the inferior

NAKANISHI et al.: NOVEL MOVING STEADY-STATE VISUAL EVOKED POTENTIAL STIMULUS

Fig. 2.
Experimental environment. Participants fixed their gaze at
the center of the stimulus so that it simultaneously elicits multi-focal
steady-state visual evoked potentials (mfSSVEPs) and saccadic eye
movements.

orbit for vertical eye movement and to the left of the left and
right of each eye for horizontal eye movement. The HMD
was placed on top of the electrode cap (Fig. 2). The data
were digitized with common mode sense (CMS) and driven
right leg (DRL) electrodes at a sampling rate of 2,048 Hz.
Event triggers that indicated the onsets of visual stimulation
and horizontal and vertical stimulus position were sent through
the LabStreamingLayer (LSL) [18] to the EEG system. The
participants were asked to sit in a comfortable chair and gaze
at a red dot located in the center of the moving visual stimuli.
They were also instructed to avoid eye blinking during the
5-second visual stimulation. The experiment consisted of three
sessions with stimulus A-pattern and three sessions with stimulus B-pattern for each eye. Each session per eye contained
30 6-second trials, including 5 seconds of visual stimulation
followed by a 1-second short break, totaling 3 minutes. In sum,
each participant performed 360 trials (i.e., 2 eyes × 2 stimulus
patterns × 3 sessions × 30 trials/session) of the gazing task.
D. Data Analysis
EEG data were first resampled to 256 Hz and re-referenced
to the Cz channel. Then, data epochs composed of 9-channel
5-second mfSSVEPs were extracted from the continuous EEG
data according to the event markers. Considering a latency
delay in the visual system [19], the data epochs were extracted
in [0.14 5.14] s, where the time zero indicated stimulus
onsets. Each EEG epoch was band-pass filtered using a
Chebyshev Type I filter created with MATLAB’s cheb1ord()
and cheby() functions. The filter has less than 3 dB of
ripple in the passband between 6 and 90 Hz, a stopband
that attenuated by 35 dB below 4 Hz and above 100 Hz to
preserve the components at the frequencies of interest (i.e.,
8, 8.2, . . . , 11.8 Hz with an interval of 0.2 Hz) and their harmonic components [20]. Zero-phase forward and reverse filtering was implemented using the filtfilt() function in Matlab.
As an afferent measure, we employed the SNR of mfSSVEPs
which was defined as the ratio of the signal power induced by
the stimuli to that of spontaneous activity [17], [21]. Having
the two stimulus patterns (i.e., A and B), the signals and
noises can be defined as the components corresponding to the
frequencies that flickered in a pattern and that did not flicker in
the other pattern, respectively. Therefore, it can be computed
as follows:
P
f ∈ f t F( f )
,
(1)
SNR = P
f ∈ f nt F( f )

1299

where F( f ) indicates the amplitude spectrum at a frequency
of f Hz computed by discrete Fourier transform (DFT), and
f t and f nt are subsets of stimulus frequencies ranging from
8.0 to 11.8 Hz containing target and non-target frequencies
that are contained in each pattern of visual stimulus (e.g.,
8.0, 8.4, . . . , 11.6 Hz are target and 8.2, 8.6, . . . , 11.8 Hz are
non-target frequencies for pattern A). The SNR was quantified
for each eye on each participant. To compute an SNR, we first
took an average of 90 5-s data epochs on each condition
(i.e., eye and stimulus pattern), obtained amplitude spectra by
applying DFT to the averaged waveforms, and then computed
the eq (1) using the spectra corresponding to the stimulus
patterns A and B. The SNR defined here indicates the changes
of frequency components in EEG due to the visual stimulation,
which is suitable to measure the abnormality in afferent visual
pathway [17].
EOG data were also resampled to 256 Hz and converted to
vertical and horizontal EOG (vEOG and hEOG) by subtracting
the signal obtained from the electrodes placed above superior
orbit and below inferior orbit and right and left of each eye,
respectively. However, the electrode placed above the superior
orbit interfered with the HMD, contaminating the EOG data
with interference noises. As a result, vEOG measurements
were excluded from the following analysis. The data were
then epoched according to the event triggers. To quantify the
participants’ efferent tracking function, correlation coefficients
between the amplitude of hEOG data and the horizontal trajectory of the visual stimulus were computed as eye-tracking
performance.
One-way analysis of covariances (ANCOVAs) were conducted to determine statistically significant differences
between the MS participants and the healthy controls on
the SNR of mfSSVEPs and the eye-tracking performance
controlling for age. In other words, the participants’ age was
the covariate in the ANCOVA.
III. R ESULTS
We recruited nine MS participants (mean age: 32.7 ±
4.33 yrs., 66.6 % female) and ten healthy controls (mean age:
24.9 ± 7.2 yrs., 80 % female). The MS patients exhibited
a wide range of disability accumulation, as measured by the
Expanded Disability Status Scale (EDSS) scores. MS subjects
had EDSS scores from 0 (no disability) to 6.5 (needing a
walker for ambulation). The averaged disease duration was
8.8 years ranging from 0.9 to 24.6 years. Eight MS participants
had a history of clinical optic neuritis and no patients had
history of an overt clinical efferent abnormality on a bedside
exam.
Fig. 3 illustrates examples of the amplitude spectra of
mfSSVEPs and EOG-based horizontal eye-tracking data collected from a healthy control and an MS participant. Each
amplitude spectrum was obtained by combining the spectra corresponding to the two visual stimulus patterns (i.e.,
(a) and (b)). More specifically, the maximum values at each
frequency bins between the two spectra were obtained
and used to draw the final spectrum shown in Fig. 3(a).
As shown in the figure, the MS patient clearly showed
degraded mfSSVEP amplitude across the frequency spectrum

1300

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 31, 2023

Fig. 3. Examples of (a) the time-series and amplitude spectra of mfSSVEPs and (b) EOG-based eye tracking data collected from a healthy
participant and a MS participant. The frequency range highlighted in gray indicates the frequency range of stimulus frequencies (i.e., 8 - 11.8 Hz).

Fig. 4. Averaged mfSSVEP SNR (left) and eye-tracking performance
(right) across participants in each group. The error bars indicate standard errors.

and weakly-correlated eye trajectory with the moving stimulus
compared with the healthy control. In Fig. 3(b), the stimulus
position and EOG-based eye trajectory were plotted in 2-D
spaces. The control eye was able to closely track the stimulus
while the MS eye had evident departures from the stimulus
position.
Fig. 4 shows the averaged mfSSVEP signal-to-noise ratio
(SNR) and eye-tracking performance across eyes in each
group. The mean SNR of mfSSVEPs in the control and MS
groups were 2.54 ± 0.76 and 2.19 ± 0.47, respectively. The
one-way ANCOVA showed that the SNRs of the mfSSVEP in
the control group were significantly higher than those in the
MS group after controlling for participants’ age (F(1,34) =
4.18, p = 0.049). The mean eye-tracking performance in the
control and MS groups were 68.71 ± 14.16 and 68.33 ± 11.75,
respectively. Across the MS and controls groups, there was
no statistically significant difference in the mean eye-tracking
performance after controlling for participants’ age (F(1,34) =
0.01, p = 0.753) in this pilot sample size, despite some
extreme differences for some MS participants (Figure 3).
IV. D ISCUSSION
This study provides preliminary validation of this VR
BCI-based assessment of MS-related visual dysfunction and
introduced a novel moving evoked potential stimulus. While
afferent and efferent measures have independently shown
validity as disease burden outcomes in MS and other neurological diseases, this is the first use of a moving evoked

potential stimulus to simultaneously stimulate both visual
systems [22], [23], [24]. This pilot paradigm integrated an
EEG headset with an HMD to create a portable data collection
method and applied a moving mfSSVEP stimulus to concurrently assess both afferent and efferent visual pathways in MS
patients. Our results demonstrated that mfSSVEP SNR was
significantly lower in MS patients than in healthy control eyes,
suggesting that this approach can be used to assess afferent
visual dysfunction in MS eyes.
These measures provide valuable insight and potential
biomarkers for sub-clinical disease activity in the MS population. Additionally, this integrated headset’s ability to collect multiple measures of visual function underlines its use
as an efficient and transportable tool for tracking disease
progression.
The efferent measures based on the hEOG-based eyetracking performance showed a trend between the two experimental groups, but not a nominally statistically significant
difference. The small sample size of this pilot study may be
one factor contributing to this. A few participants had apparent
subclinical abnormalities on this efferent testing and this pilot
test demonstrated the ability to elicit eye movement responses
with the novel stimulus. Participants recruited did not have
overt clinical efferent dysfunction on bedside exam, which
may have impacted the lack of nominal statistical significance
in this small sample size. It could also reflect the fact that
EOG data were largely contaminated by the interferences from
the head-mounted display because it was placed on top of the
electrodes. Removal of the vEOG data due to technical artifact
may have obscured the ability to measure the differences in
efferent features between MS participants and healthy controls.
Newer VR headset models include a built-in video-based eyetracker (e.g. HTC Vive Pro Eye); in the future, using such
devices to precisely assess the efferent visual pathway would
be preferable and will be pursued for the advancement of this
platform. The overall results of this study demonstrate the
importance of re-examining these findings with a larger sample
size and updated technology in order to establish validity and
revisit the significance of efferent visual pathway measures.
It will also be imperative to address potential longitudinal
changes in these measures in both MS patients and healthy
controls, to evaluate the device’s applicability as a reliable
marker of MS disease progression.

NAKANISHI et al.: NOVEL MOVING STEADY-STATE VISUAL EVOKED POTENTIAL STIMULUS

V. C ONCLUSION
This study uses a virtual reality headset with a moving
visual flicker stimulus to simultaneously assess afferent and
efferent visual functions. The results showed that the proposed
mobile platform could induce and measure both mfSSVEPs
and smooth pursuit behavior in healthy controls and MS
patients. In particular, the SNR of mfSSVEPs in the MS
patients was significantly lower than that in the healthy controls, indicating a degraded afferent visual function in the
MS patients. The proposed protocol has a great potential to
facilitate research and the development of a novel diagnostic
tool for MS-related visual dysfunction.
ACKNOWLEDGMENT
The authors would like to thank the generous participants
who donated their time for this study.
R EFERENCES
[1] J. S. Graves et al., “Leveraging visual outcome measures to advance
therapy development in neuroimmunologic disorders,” Neurol. Neuroimmunology Neuroinflammation, vol. 9, no. 2, p. e1126, Mar. 2022.
[2] L. Leocani, S. Guerrieri, and G. Comi, “Visual evoked potentials as a
biomarker in multiple sclerosis and associated optic neuritis,” J. NeuroOphthalmology, vol. 38, no. 3, pp. 350–357, Sep. 2018.
[3] J. L. Barton, J. Y. Garber, A. Klistorner, and M. H. Barnett, “The electrophysiological assessment of visual function in multiple sclerosis,” Clin.
Neurophysiol. Pract., vol. 4, pp. 90–96, May 2019.
[4] A. Yousef et al., “Subclinical saccadic eye movement dysfunction in
pediatric multiple sclerosis,” J. Child Neurol., vol. 34, no. 1, pp. 38–43,
Jan. 2019.
[5] T. Rempe et al., “Quantification of smooth pursuit dysfunction in
multiple sclerosis,” Multiple Sclerosis Rel. Disorders, vol. 54, Sep. 2021,
Art. no. 103073.
[6] J. Graves and L. J. Balcer, “Eye disorders in patients with multiple
sclerosis: Natural history and management,” Clin. Ophthalmol., vol. 4,
pp. 1409–1422, Dec. 2010.
[7] M. Nakanishi et al., “Detecting glaucoma with a portable brain-computer
interface for objective assessment of visual function loss,” JAMA Ophthalmol., vol. 135, no. 6, pp. 550–557, Jun. 2017.
[8] F. B. Vialatte, M. Maurice, J. Dauwels, and A. Cichocki, “Steady-state
visually evoked potentials: Focus on essential paradigms and future
perspectives,” Prog. Neurobiol., vol. 90, pp. 418–438, Apr. 2010.
[9] A. M. Norcia, L. G. Appelbaum, J. M. Ales, B. R. Cottereau, and
B. Rossion, “The steady-state visual evoked potential in vision research:
A review,” J. Vis., vol. 15, no. 6, p. 4, May 2015.

1301

[10] S. N. Abdullah, N. Aldahlawi, Y. Rosli, Vaegan, M. Y. Boon, and
T. Maddess, “Effect of contrast, stimulus density, and viewing distance on multifocal steady-state visual evoked potentials (MSVs),”
Investigative Ophthalmol. Visual Sci., vol. 53, no. 9, pp. 5527–5535,
Aug. 2012.
[11] S. N. Abdullah, Vaegan, M. Y. Boon, and T. Maddess, “Contrastresponse functions of the multifocal steady-state VEP (MSV),” Clin.
Neurophysiol., vol. 123, no. 9, pp. 1865–1871, Sep. 2012.
[12] G. G. Celesia, M. Brigell, R. Gunnink, and H. Dang, “Spatial frequency
evoked visuograms in multiple sclerosis,” Neurology, vol. 42, no. 5,
pp. 1067–1070, May 1992.
[13] S. Tobimatsu, S. Tashima-Kurita, M. Nakayama-Hiromatsu, and
M. Kato, “Clinical relevance of phase of steady-state VEPs to
P100 latency of transient VEPs,” Electroencephalogr. Clin. Neurophysiol./Evoked Potentials Sect., vol. 80, no. 2, pp. 89–93, Mar. 1991.
[14] H. Abe, S. Hasegawa, M. Takagi, T. Yoshizawa, and T. Usui, “Temporal
modulation transfer function of vision by pattern visual evoked potentials
in patients with optic neuritis,” Ophthalmologica, vol. 207, no. 2,
pp. 94–99, 1993.
[15] A. J. Thompson et al., “Diagnosis of multiple sclerosis: 2017 revisions
of the McDonald criteria,” Lancet Neurol., vol. 17, no. 2, pp. 162–173,
Feb. 2018.
[16] Y. Wang, Y.-T. Wang, and T.-P. Jung, “Visual stimulus design for highrate SSVEP BCI,” Electron. Lett., vol. 46, no. 15, pp. 1057–1058, 2010.
[17] M. Nakanishi, Y. Wang, Y.-T. Wang, Y. Mitsukura, and T.-P. Jung,
“Generating visual flickers for eliciting robust steady-state visual evoked
potentials at flexible frequencies using monitor refresh rate,” PLoS ONE,
vol. 9, no. 6, Jun. 2014, Art. no. e99235.
[18] C. A. Kothe and S. Makeig, “BCILAB: A platform for brain–
computer interface development,” J. Neural Eng., vol. 10, no. 5, 2013,
Art. no. 056014.
[19] Y. Wang, X. Gao, and S. Gao, “Computational modeling and application
of steady-state visual evoked potentials in brain–computer interfaces,”
Sci. Suppl., vol. 350, no. 6256, pp. 43–46, 2015.
[20] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao,
“High-speed spelling with a noninvasive brain–computer interface,”
Proc. Nat. Acad. Sci. USA, vol. 112, no. 44, pp. E6058–E6067,
Nov. 2015.
[21] Y. Wang, R. Wang, X. Gao, B. Hong, and S. Gao, “A practical vepbased brain-computer interface,” IEEE Trans. Neural Syst. Rehabil. Eng.,
vol. 14, no. 2, pp. 234–239, Feb. 2006.
[22] M. Jozefowicz-Korczynska and A. M. Pajor, “Evaluation of the smooth
pursuit tests in multiple sclerosis patients,” J. Neurol., vol. 258, no. 10,
pp. 1795–1800, Oct. 2011.
[23] N. Lizak, M. Clough, L. Millist, T. Kalincik, O. B. White, and
J. Fielding, “Impairment of smooth pursuit as a marker of early multiple
sclerosis,” Frontiers Neurol., vol. 7, p. 206, Nov. 2016.
[24] D. B. Liston, L. R. Wong, and L. S. Stone, “Oculometric assessment
of sensorimotor impairment associated with TBI,” Optometry Vis. Sci.,
vol. 94, no. 1, pp. 51–59, 2017.
