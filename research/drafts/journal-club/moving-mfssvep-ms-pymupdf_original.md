# Novel_Moving_Steady-State_Visual_Evoked_Potential_Stimulus_to_Assess_Afferent_and_Efferent_Dysfunction_in_Multiple_Sclerosis

- Source PDF: `C:\Users\Projects\manager-agent\research\paper_candidates\papers\Novel_Moving_Steady-State_Visual_Evoked_Potential_Stimulus_to_Assess_Afferent_and_Efferent_Dysfunction_in_Multiple_Sclerosis.pdf`
- Extraction: `PyMuPDF` page-by-page text fallback
- Verification status: unverified draft

- Page count: 5
- Title metadata: Novel Moving Steady-State Visual Evoked Potential Stimulus to Assess Afferent and Efferent Dysfunction in Multiple Sclerosis
- Author metadata: 

---

## Page 1

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 31, 2023                                 1297

   Novel Moving Steady-State Visual Evoked
    Potential Stimulus to Assess Afferent and
    Efferent Dysfunction in Multiple Sclerosis


                    Masaki Nakanishi   , Senior Member, IEEE, Annalise Miner,
                        Tzyy-Ping Jung   , Fellow, IEEE, and Jennifer Graves


  Abstract— Afferent and efferent visual dysfunction are     Index Terms— Afferent and  efferent  visual pathway,
prominent features of multiple sclerosis (MS). Visual out-   electroencephalogram  (EEG),  electrooculogram  (EOG),
comes have been shown to be robust biomarkers of the   multifocal steady-state visual evoked potential (mfSSVEP),
overall disease state. Unfortunately, precise measurement   multiple sclerosis (MS), virtual reality headset.
of afferent and efferent function is typically limited to ter-
tiary care facilities, which have the equipment and analyti-                                 I. INTRODUCTION
cal capacity to make these measurements, and even then,
only a few centers can accurately quantify both afferent and     NE of the greatest unmet needs in multiple sclerosis
efferent dysfunction. These measurements are currently       (MS) research and clinical care is the ability to quantify            O
unavailable in acute care facilities (ER, hospital floors).   disease burden with highly reproducible and rater-independent
We aimed to develop a moving multifocal steady-state   methods. Significant advancements have been made in mea-
visual evoked potential (mfSSVEP) stimulus to simulta-
                                                               suring visual dysfunction through the use of low-contrast letterneously assess afferent and efferent dysfunction in MS
for application on a mobile platform. The brain-computer   acuity measures, visual evoked potentials (VEP), optical coher-
interface (BCI) platform consists of a head-mounted virtual-   ence tomography (OCT), and efferent oculometrics, but these
reality headset with electroencephalogram (EEG) and elec-   tools are not in widespread use in most MS clinics and often
trooculogram (EOG) sensors. To evaluate the platform,   require support from those with subspecialty training in neuro-
we recruited consecutive patients who met the 2017 MS
                                                         ophthalmology [1]. Most of the equipment  is cumbersomeMcDonald diagnostic criteria and healthy controls for a
pilot cross-sectional study. Nine MS patients (mean age  and immovable. The functional vision measures also typically
32.7 years, SD 4.33) and ten healthy controls (24.9 years,   require performing a correction of refractive error, which most
SD 7.2) completed the research protocol. The afferent mea-   neurologists are not equipped to provide in their offices.
sures based on mfSSVEPs showed a significant difference     Despite the difficulty of conducting extensive, systematic
between the groups (signal-to-noise ratio of mfSSVEPs for
                                                                  visual testing in neurology clinics or acute care settings, thecontrols: 2.50 ± 0.72 vs. MS: 2.04 ± 0.47) after controlling
for age (p = 0.049). In addition, the moving stimulus suc-   visual system has demonstrated an exceptional ability to detect
cessfully induced smooth pursuit movement that can be   demyelinating injury even in those who have no clinical symp-
measured by the EOG signals. There was a trend for worse   toms. Standard full-field VEP has been used to support the
smooth pursuit tracking in cases vs. controls, but this did   diagnosis of MS for over 50 years [2], [3]. In young patients
not reach nominal statistical significance in this small pilot
                                                           with MS, without any detectable exam finding abnormalities,sample. This study introduces a novel moving mfSSVEP
stimulus for a BCI platform to evaluate neurologic visual   latency delays can be seen for saccadic (fast) eye movements
function. The moving stimulus showed a reliable capabil-   that distinguish these patients from healthy controls [4]. Dis-
ity to assess both afferent and efferent visual functions   ruption of smooth pursuit eye movements also distinguishes
simultaneously.                                     MS eyes from controls [5]. The current understanding of the
  Manuscript received 11 July 2022; revised 14 October 2022 and   quantitative relationships between structure and function in the
12 December 2022; accepted 27 December 2022. Date of publica-   visual system far surpasses that of other central nervous system
tion 8 February 2023; date of current version 16 February 2023.   pathways. Thus, the afferent and efferent visual pathways are
This work was supported by the University of California San Diego
Galvanizing Engineering in Medicine Program. (Corresponding author:   well poised to serve as a model system of injury and repair for
Masaki Nakanishi.)                                                 therapeutic investigations and clinical monitoring in MS [6].
  This work involved human subjects or animals in its research. Approval    The majority of MS patients are not diagnosed or cared
of all ethical and experimental procedures and protocols was granted
by the University of California San Diego Human Research Protections   for in clinic settings with advanced visual function testing
Program.                                                                     facilities. A mobile platform that does not require dedicated
  Masaki Nakanishi and Tzyy-Ping Jung are with the Swartz Cen-  room space or a trained technician, such as the one pro-
ter for Computational Neuroscience, Institute for Neural Computation,
University of California San Diego, La Jolla, CA 92093 USA (e-mail:   posed here, would enable more widespread use of quantita-
masaki@sccn.ucsd.edu; jung@sccn.ucsd.edu).                          tive afferent/efferent vision testing in acute care settings and
  Annalise Miner and Jennifer Graves are with the Department of Neu-   non-tertiary care centers.
roscience, University of California San Diego, La Jolla, CA 92093 USA
(e-mail: aeminer@health.ucsd.edu; jgraves@health.ucsd.edu).             Efferent visual function testing is currently only used in
  Digital Object Identifier 10.1109/TNSRE.2023.3243554               observational research settings. Despite its proven ability to

                   This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
                               For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

## Page 2

1298                                            IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 31, 2023



detect dysfunction, quantification of dysfunction has not been
brought to the clinic or trial setting. This situation is largely
due to the lack of technical expertise and immovable equip-
ment needed to perform these measurements. As an example,
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
are  elicited by  rapid  flickering  stimulation,  producing  a
brain response characterized by a quasi-sinusoidal waveform
that has frequency components with constant amplitude and    Fig. 1. A moving multi-focal stimulus. (Top) The stimulus was presented
phase [8]. The technique is faster than standard VEPs and    at the center of a screen and started to move at a constant speed
                                                                          with an angle θ assigned randomly in a 15◦-wide 2-D space. To avoid
less susceptible to  artifacts produced by blinking and eye                                                                        visually-crowded illustration, the fixation point was depicted rather than
movements as well as electromyographic noise contamination,   the multi-focal stimulus in the figure. (Bottom) Participants fixed their
and  it may present a better signal-to-noise ratio [9], [10],   gaze at the center of the stimulus so that it simultaneously elicits multi-
                                                                               focal steady-state visual evoked potentials (mfSSVEPs) and smooth eye
[11], [12], [13], [14]. The current study builds on the prior                                                             movements.
work in glaucoma by adding a moving multi-focal SSVEP
(mfSSVEP) stimulus for assessing both afferent and efferent
visual function simultaneously. The MSight BCI platform   space at a constant speed [8] were implemented and pre-
piloted in this study will greatly facilitate research on the   sented on  a Samsung Odyssey + head-mounted  display
correlations between the afferent and efferent measures in  (HMD). Different frequencies were assigned to each sector,
neurological disease and support the development of new and   ranging from 8  to 11.8 Hz with a frequency  interval of
novel indices of MS-related visual dysfunction. We hypothe-   0.2 Hz. To enhance the signal-to-noise ratio (SNR) in elicit-
sized that SSVEP amplitudes across the frequencies assessed   ing mfSSVEPs, the platform uses a frequency-approximation
would be lower compared to control subjects given the high   approach to render flexible frequencies with a variable number
prevalence of both  clinical and subclinical  afferent injury   of frames in a stimulating period [16], [17]. Two patterns
in MS. We also hypothesized reduced  fidelity of stimulus  (A and B) of visual stimuli, each with 10 of 20 sectors
tracking in the efferent measure based on high rates of efferent   flickered concurrently, were presented separately, to facilitate
visual dysfunction even in those with mild disease course.      the calculation of the SNR (see II-D Data Analysis). For
                                                          example, the stimulus pattern A contained 8 to 11.6 Hz with
                               II. METHODS                        a 0.4 Hz interval and the stimulus pattern B contained 8.2 to
A. Participants                                             11.8 Hz with a 0.4 Hz interval. The fixation target moves in
                                                   2-D space at v = 60◦/s rendered randomly and smoothly on  We offered enrollment to consecutive patients who attended
                                                                 the screen of the HMD (Fig. 1). At the beginning of eachthe University of California San Diego (UCSD) MS Center.
                                                                                     trial, a 2-D moving angle θ was assigned, and the horizontalParticipants with MS had to meet the updated 2017 McDonald
                                                       and the vertical moving speeds were determined based oncriteria for MS [15]. The included participants were exposed
                                                                 the angle. For example, horizontal and vertical speeds canto a variety of MS disease modifying medications including
                                                        be determined as vcos(θ) and vsin(θ), respectively. Once theoral (e.g., dimethyl fumarate, fingolimod) and infusion (e.g.,
                                                              stimulus reached to one of the 15◦-wide boundaries in fourocrelizumab) medications. Age similar healthy controls had no
                                                                     directions, the moving direction was flipped as shown in Fig.1.history of neurological or ophthalmological disease. The study
was approved by UCSD Human Research Protections Program
and all participants provided informed written consent.        C. Data Acquisition
                                          EEG and electrooculogram (EOG) data were measured
B. Visual Stimulus                                          using a BioSemi ActiveTwo EEG system (BioSemi, Inc.). EEG
  Multi-focal visual stimuli consisting of two patterns of   data were recorded with nine Ag/AgCl Electrodes covering the
20 sectors in three concentric rings (subtending 8.4◦, 21◦,   occipital area and an additional one at Cz. EOG electrodes
and 35◦of the visual field) and moving in 15◦-wide 2-D  were placed above the superior orbit and below the inferior

## Page 3

NAKANISHI et al.: NOVEL MOVING STEADY-STATE VISUAL EVOKED POTENTIAL STIMULUS                                                    1299



                                                      where F( f ) indicates the amplitude spectrum at a frequency
                                                               of  f Hz computed by discrete Fourier transform (DFT), and
                                                                                                     ft and  fnt are subsets of stimulus frequencies ranging from
                                                               8.0 to 11.8 Hz containing target and non-target frequencies
                                                                      that are contained in each pattern of visual stimulus  (e.g.,
                                                                  8.0, 8.4, . . . , 11.6 Hz are target and 8.2, 8.6, . . . , 11.8 Hz are
                                                                 non-target frequencies for pattern A). The SNR was quantified
                                                                    for each eye on each participant. To compute an SNR, we first
Fig. 2.   Experimental environment. Participants fixed their gaze at   took an average of 90 5-s data epochs on each condition
the center of the stimulus so that  it simultaneously elicits multi-focal    (i.e., eye and stimulus pattern), obtained amplitude spectra by
steady-state visual evoked potentials (mfSSVEPs) and saccadic eye
                                                            applying DFT to the averaged waveforms, and then computedmovements.
                                                                 the eq (1) using the spectra corresponding to the stimulus
orbit for vertical eye movement and to the left of the left and   patterns A and B. The SNR defined here indicates the changes
right of each eye for horizontal eye movement. The HMD   of frequency components in EEG due to the visual stimulation,
was placed on top of the electrode cap (Fig. 2). The data  which is suitable to measure the abnormality in afferent visual
were digitized with common mode sense (CMS) and driven  pathway [17].
right leg (DRL) electrodes at a sampling rate of 2,048 Hz.   EOG data were also resampled to 256 Hz and converted to
Event triggers that indicated the onsets of visual stimulation   vertical and horizontal EOG (vEOG and hEOG) by subtracting
and horizontal and vertical stimulus position were sent through   the signal obtained from the electrodes placed above superior
the LabStreamingLayer (LSL) [18] to the EEG system. The   orbit and below inferior orbit and right and left of each eye,
participants were asked to sit in a comfortable chair and gaze   respectively. However, the electrode placed above the superior
at a red dot located in the center of the moving visual stimuli.   orbit interfered with the HMD, contaminating the EOG data
They were also instructed to avoid eye blinking during the   with interference noises. As a result, vEOG measurements
5-second visual stimulation. The experiment consisted of three  were excluded from the following analysis. The data were
sessions with stimulus A-pattern and three sessions with stim-   then epoched according to the event triggers. To quantify the
ulus B-pattern for each eye. Each session per eye contained   participants’ efferent tracking function, correlation coefficients
30 6-second trials, including 5 seconds of visual stimulation   between the amplitude of hEOG data and the horizontal tra-
followed by a 1-second short break, totaling 3 minutes. In sum,   jectory of the visual stimulus were computed as eye-tracking
each participant performed 360 trials (i.e., 2 eyes × 2 stimulus   performance.
patterns × 3 sessions × 30 trials/session) of the gazing task.    One-way analysis of covariances (ANCOVAs) were con-
                                                           ducted  to  determine   statistically  significant  differences
                                                       between the MS  participants and the healthy controls onD. Data Analysis
                                                                 the SNR of mfSSVEPs and the eye-tracking performance
  EEG data were first resampled to 256 Hz and re-referenced
                                                                  controlling for age. In other words, the participants’ age was
to the Cz channel. Then, data epochs composed of 9-channel
                                                                 the covariate in the ANCOVA.
5-second mfSSVEPs were extracted from the continuous EEG
data according to the event markers. Considering a latency                                                                                                                  III. RESULTS
delay in the visual system [19], the data epochs were extracted
                                          We  recruited nine MS  participants (mean age: 32.7 ±
in [0.14 5.14]  s, where the time zero indicated stimulus
                                                            4.33 yrs., 66.6 % female) and ten healthy controls (mean age:
onsets. Each EEG epoch was band-pass  filtered using a
                                                            24.9 ± 7.2 yrs., 80 % female). The MS patients exhibited
Chebyshev Type I filter created with MATLAB’s cheb1ord()
                                                           a wide range of disability accumulation, as measured by the
and cheby()  functions. The  filter has  less than 3 dB  of
                                                     Expanded Disability Status Scale (EDSS) scores. MS subjects
ripple in the passband between 6 and 90 Hz, a stopband
                                                       had EDSS scores from 0 (no disability) to 6.5 (needing a
that attenuated by 35 dB below 4 Hz and above 100 Hz to
                                                           walker for ambulation). The averaged disease duration was
preserve the components at the frequencies of interest  (i.e.,
                                                               8.8 years ranging from 0.9 to 24.6 years. Eight MS participants
8, 8.2, . . . , 11.8 Hz with an interval of 0.2 Hz) and their har-
                                                       had a history of clinical optic neuritis and no patients had
monic components [20]. Zero-phase forward and reverse fil-
                                                                   history of an overt clinical efferent abnormality on a bedside
tering was implemented using the filtfilt() function in Matlab.
                                                       exam.
As an afferent measure, we employed the SNR of mfSSVEPs
                                                                     Fig. 3  illustrates examples  of  the amplitude  spectra  of
which was defined as the ratio of the signal power induced by
                                               mfSSVEPs and EOG-based horizontal eye-tracking data col-
the stimuli to that of spontaneous activity [17], [21]. Having
                                                                  lected from a healthy control and an MS participant. Each
the two stimulus patterns  (i.e., A and B), the signals and
                                                           amplitude spectrum was obtained by combining the spec-
noises can be defined as the components corresponding to the
                                                                           tra corresponding to the two visual stimulus patterns  (i.e.,
frequencies that flickered in a pattern and that did not flicker in
                                                                       (a) and (b)). More specifically, the maximum values at each
the other pattern, respectively. Therefore, it can be computed
                                                            frequency  bins  between  the  two  spectra  were  obtained
as follows:
                                                       and used  to draw the  final spectrum shown  in Fig. 3(a).
           P f ∈ft F( f )                  As shown  in  the  figure,  the MS  patient  clearly showed            SNR =                                   (1)                                       ),                     degraded mfSSVEP amplitude across the frequency spectrum           P f ∈fnt F( f

## Page 4

1300                                            IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 31, 2023





Fig. 3.  Examples of (a) the time-series and amplitude spectra of mfSSVEPs and (b) EOG-based eye tracking data collected from a healthy
participant and a MS participant. The frequency range highlighted in gray indicates the frequency range of stimulus frequencies (i.e., 8 - 11.8 Hz).


                                                                    potential stimulus  to simultaneously stimulate both  visual
                                                          systems [22], [23], [24]. This pilot paradigm integrated an
                                         EEG headset with an HMD to create a portable data collection
                                                     method and applied a moving mfSSVEP stimulus to concur-
                                                                    rently assess both afferent and efferent visual pathways in MS
                                                                       patients. Our results demonstrated that mfSSVEP SNR was
                                                                     significantly lower in MS patients than in healthy control eyes,
                                                              suggesting that this approach can be used to assess afferent
                                                                  visual dysfunction in MS eyes.
                                                         These measures  provide  valuable  insight and  potential
                                                           biomarkers for sub-clinical disease activity in the MS pop-
                                                                      ulation. Additionally, this integrated headset’s ability to col-
Fig. 4.  Averaged mfSSVEP SNR (left) and eye-tracking performance
(right) across participants in each group. The error bars indicate stan-   lect multiple measures of visual function underlines its use
dard errors.                                                     as an  efficient and transportable tool for tracking disease
                                                                progression.
and weakly-correlated eye trajectory with the moving stimulus    The  efferent measures based on  the hEOG-based eye-
compared with the healthy control. In Fig. 3(b), the stimulus   tracking performance showed a trend between the two exper-
position and EOG-based eye trajectory were plotted in 2-D   imental groups, but not a nominally statistically significant
spaces. The control eye was able to closely track the stimulus   difference. The small sample size of this pilot study may be
while the MS eye had evident departures from the stimulus  one factor contributing to this. A few participants had apparent
position.                                                          subclinical abnormalities on this efferent testing and this pilot
   Fig. 4 shows the averaged mfSSVEP signal-to-noise ratio   test demonstrated the ability to elicit eye movement responses
(SNR) and eye-tracking performance across eyes  in each   with the novel stimulus. Participants recruited did not have
group. The mean SNR of mfSSVEPs in the control and MS   overt clinical efferent dysfunction on bedside exam, which
groups were 2.54 ± 0.76 and 2.19 ± 0.47, respectively. The  may have impacted the lack of nominal statistical significance
one-way ANCOVA showed that the SNRs of the mfSSVEP in   in this small sample size. It could also reflect the fact that
the control group were significantly higher than those in the  EOG data were largely contaminated by the interferences from
MS group after controlling for participants’ age (F(1,34) =   the head-mounted display because it was placed on top of the
4.18, p = 0.049). The mean eye-tracking performance in the   electrodes. Removal of the vEOG data due to technical artifact
control and MS groups were 68.71 ± 14.16 and 68.33 ± 11.75,  may have obscured the ability to measure the differences in
respectively. Across the MS and controls groups, there was   efferent features between MS participants and healthy controls.
no statistically significant difference in the mean eye-tracking  Newer VR headset models include a built-in video-based eye-
performance after controlling for participants’ age (F(1,34) =   tracker (e.g. HTC Vive Pro Eye); in the future, using such
0.01, p = 0.753) in  this  pilot sample  size, despite some   devices to precisely assess the efferent visual pathway would
extreme differences for some MS participants (Figure 3).      be preferable and will be pursued for the advancement of this
                                                                platform. The overall results of this study demonstrate the
                      IV. DISCUSSION                       importance of re-examining these findings with a larger sample
  This study  provides  preliminary  validation  of  this VR   size and updated technology in order to establish validity and
BCI-based assessment of MS-related visual dysfunction and   revisit the significance of efferent visual pathway measures.
introduced a novel moving evoked potential stimulus. While    It will also be imperative to address potential longitudinal
afferent and  efferent measures have independently shown   changes in these measures in both MS patients and healthy
validity as disease burden outcomes in MS and other neu-   controls, to evaluate the device’s applicability as a reliable
rological diseases, this is the  first use of a moving evoked   marker of MS disease progression.

## Page 5

NAKANISHI et al.: NOVEL MOVING STEADY-STATE VISUAL EVOKED POTENTIAL STIMULUS                                                    1301



                     V. CONCLUSION                              [10]  S. N. Abdullah, N. Aldahlawi, Y. Rosli, Vaegan, M. Y. Boon, and
                                                                                          T. Maddess, “Effect of contrast, stimulus density, and viewing dis-
  This study uses a virtual reality headset with a moving                                                                                    tance on multifocal  steady-state  visual evoked  potentials (MSVs),”
visual flicker stimulus to simultaneously assess afferent and          Investigative Ophthalmol. Visual Sci., vol. 53, no. 9, pp. 5527–5535,
efferent visual functions. The results showed that the proposed        Aug. 2012.
mobile platform could induce and measure both mfSSVEPs    [11]  S. N. Abdullah, Vaegan, M. Y. Boon, and T. Maddess, “Contrast-
                                                                                 response functions of the multifocal steady-state VEP (MSV),” Clin.
and smooth pursuit behavior  in healthy controls and MS         Neurophysiol., vol. 123, no. 9, pp. 1865–1871, Sep. 2012.
patients. In  particular, the SNR of mfSSVEPs in the MS    [12] G. G. Celesia, M. Brigell, R. Gunnink, and H. Dang, “Spatial frequency
patients was significantly lower than that in the healthy con-        evoked visuograms in multiple sclerosis,” Neurology, vol. 42, no. 5,
                                                                                     pp. 1067–1070, May 1992.
trols, indicating a degraded afferent visual function in the    [13]  S.  Tobimatsu,  S.  Tashima-Kurita, M.  Nakayama-Hiromatsu,  and
MS patients. The proposed protocol has a great potential to       M.  Kato,  “Clinical  relevance  of  phase  of  steady-state VEPs  to
facilitate research and the development of a novel diagnostic       P100 latency of transient VEPs,” Electroencephalogr. Clin. Neurophys-
                                                                                      iol./Evoked Potentials Sect., vol. 80, no. 2, pp. 89–93, Mar. 1991.
tool for MS-related visual dysfunction.                                                                               [14] H. Abe, S. Hasegawa, M. Takagi, T. Yoshizawa, and T. Usui, “Temporal
                                                                             modulation transfer function of vision by pattern visual evoked potentials
               ACKNOWLEDGMENT                                                                                           in  patients with  optic  neuritis,” Ophthalmologica,  vol. 207, no.  2,
  The authors would like to thank the generous participants         pp. 94–99, 1993.
who donated their time for this study.                                 [15] A. J. Thompson et al., “Diagnosis of multiple sclerosis: 2017 revisions
                                                                                     of the McDonald criteria,” Lancet Neurol., vol. 17, no. 2, pp. 162–173,
                 REFERENCES                                  Feb. 2018.
                                                                               [16] Y. Wang, Y.-T. Wang, and T.-P. Jung, “Visual stimulus design for high-
 [1]  J. S. Graves et al., “Leveraging visual outcome measures to advance          rate SSVEP BCI,” Electron. Lett., vol. 46, no. 15, pp. 1057–1058, 2010.
     therapy development in neuroimmunologic disorders,” Neurol. Neuroim-    [17] M. Nakanishi, Y. Wang, Y.-T. Wang, Y. Mitsukura, and T.-P. Jung,
     munology Neuroinflammation, vol. 9, no. 2, p. e1126, Mar. 2022.              “Generating visual flickers for eliciting robust steady-state visual evoked
 [2] L. Leocani, S. Guerrieri, and G. Comi, “Visual evoked potentials as a          potentials at flexible frequencies using monitor refresh rate,” PLoS ONE,
     biomarker in multiple sclerosis and associated optic neuritis,” J. Neuro-          vol. 9, no. 6, Jun. 2014, Art. no. e99235.
     Ophthalmology, vol. 38, no. 3, pp. 350–357, Sep. 2018.                  [18] C. A. Kothe and  S.  Makeig, “BCILAB: A  platform  for  brain–
 [3]  J. L. Barton, J. Y. Garber, A. Klistorner, and M. H. Barnett, “The electro-        computer interface development,” J. Neural Eng., vol. 10, no. 5, 2013,
      physiological assessment of visual function in multiple sclerosis,” Clin.          Art. no. 056014.
     Neurophysiol. Pract., vol. 4, pp. 90–96, May 2019.                       [19] Y. Wang, X. Gao, and S. Gao, “Computational modeling and application
 [4] A. Yousef et al., “Subclinical saccadic eye movement dysfunction in         of steady-state visual evoked potentials in brain–computer interfaces,”
      pediatric multiple sclerosis,” J. Child Neurol., vol. 34, no. 1, pp. 38–43,          Sci. Suppl., vol. 350, no. 6256, pp. 43–46, 2015.
      Jan. 2019.                                                                [20] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao,
 [5]  T. Rempe  et  al., “Quantification of smooth  pursuit dysfunction  in        “High-speed  spelling with a noninvasive brain–computer  interface,”
     multiple sclerosis,” Multiple Sclerosis Rel. Disorders, vol. 54, Sep. 2021,         Proc.  Nat. Acad.  Sci. USA,  vol. 112,  no.  44,  pp. E6058–E6067,
      Art. no. 103073.                                                       Nov. 2015.
 [6]  J. Graves and L.  J. Balcer, “Eye disorders in patients with multiple    [21] Y. Wang, R. Wang, X. Gao, B. Hong, and S. Gao, “A practical vep-
      sclerosis: Natural history and management,” Clin. Ophthalmol., vol. 4,        based brain-computer interface,” IEEE Trans. Neural Syst. Rehabil. Eng.,
     pp. 1409–1422, Dec. 2010.                                                          vol. 14, no. 2, pp. 234–239, Feb. 2006.
 [7] M. Nakanishi et al., “Detecting glaucoma with a portable brain-computer    [22] M. Jozefowicz-Korczynska and A. M. Pajor, “Evaluation of the smooth
      interface for objective assessment of visual function loss,” JAMA Oph-          pursuit tests in multiple sclerosis patients,” J. Neurol., vol. 258, no. 10,
      thalmol., vol. 135, no. 6, pp. 550–557, Jun. 2017.                              pp. 1795–1800, Oct. 2011.
 [8]  F. B. Vialatte, M. Maurice, J. Dauwels, and A. Cichocki, “Steady-state    [23] N.  Lizak, M. Clough, L.  Millist,  T.  Kalincik, O. B. White, and
      visually evoked potentials: Focus on essential paradigms and future            J. Fielding, “Impairment of smooth pursuit as a marker of early multiple
      perspectives,” Prog. Neurobiol., vol. 90, pp. 418–438, Apr. 2010.                 sclerosis,” Frontiers Neurol., vol. 7, p. 206, Nov. 2016.
 [9] A. M. Norcia, L. G. Appelbaum,  J. M. Ales, B. R. Cottereau, and    [24] D. B. Liston, L. R. Wong, and L. S. Stone, “Oculometric assessment
     B. Rossion, “The steady-state visual evoked potential in vision research:         of sensorimotor impairment associated with TBI,” Optometry Vis. Sci.,
   A review,” J. Vis., vol. 15, no. 6, p. 4, May 2015.                                 vol. 94, no. 1, pp. 51–59, 2017.
