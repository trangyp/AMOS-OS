---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.07695v1
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1902.07695v1_Chip-based_frequency_combs_sources_for_optical_coherence_tomography

> Source: 1902.07695v1_Chip-based_frequency_combs_sources_for_optical_coherence_tomography.pdf

> Pages: 10

---


## Page 1


Chip-based frequency combs sources for optical coherence tomography 
Xingchen Ji,1,2 Alexander Klenner,3 Xinwen Yao,1 Yu Gan, 1 Alexander L. Gaeta,3 
Christine P. Hendon1 and Michal Lipson1,* 
1Department of Electrical Engineering, Columbia University, New York, NY 10027 
2School of Electrical and Computer Engineering, Cornell University, Ithaca, NY 14853  
3Department of Applied Physics and Applied Mathematics, Columbia University, New York, NY 10027 
*ml3745@columbia.edu 
 
Abstract 
The Optical coherence tomography (OCT) is a powerful interferometric imaging technique widely used in medical 
fields such as ophthalmology, cardiology and dermatology, for which footprint and cost are becoming increasingly 
important. Here we present a platform for miniaturized sources for OCT based on chip-scale lithographically-
defined microresonators. We show that the proposed platform is compatible with standard commercial spectral 
domain (SD) OCT systems and enable imaging of human tissue with an image quality comparable to the one 
achieved with tabletop commercial sources. This platform provides a path towards fully integrated OCT systems. 
 
Optical coherence tomography (OCT) is a non-invasive imaging modality that provides depth-resolved, high-
resolution images of tissue microstructures in real-time. OCT has been widely demonstrated in medical fields such 
as ophthalmology and cardiology1. Recently, great efforts have been spent on the development of on-chip OCT 
components in order to enable OCT systems with small footprint and cost2–6. These efforts have leveraged recent 
advances in photonic integration on-chip including the beam splitter, reference arm, sampling arm and 
spectrometer2–6. However, the degree of miniaturization of the OCT system based on the miniaturization of these 
components is limited, since these systems still rely on an external, tabletop light source such as a superluminescent 
diode (SLD) or swept source laser that cannot be easily integrated with current photonics on a silicon platform.  
 
Here we introduce a platform for a miniaturized OCT source based on chip-scale lithographically-defined 
microresonators. These microresonators are fabricated using traditional microelectronic processes. When optically 
pumped with a single continuous-wave laser source they can generate broadband frequency combs, consisting of 
discrete lines with a frequency spacing determined by the geometry of the resonator. Such frequency combs have


## Page 2


been demonstrated in numerous chip-scale platforms including silica7–10, silicon11,12, silicon nitride13–15, aluminum 
nitride16, crystalline fluorides17,18, diamond19 and AlGaAs20 in the past decade.  
 
Our platform is based on ultra-low loss silicon nitride resonator generated frequency combs13–15,21. This resonator 
platform when integrated with semiconductor amplifiers, has recently been shown to enable highly efficient 
broadband frequency comb generation on-chip22. Silicon nitride (Si3N4) combines the beneficial properties of a wide 
transparency range covering the entire OCT imaging window, a high nonlinear refractive index (𝑛2 = 2.4 ×
10−19 m2/W),23 and semiconductor mass manufacturing compatibility. Si3N4 frequency combs have recently been 
recently generated using a reflective semiconductor amplifier as a pump source enabling a millimeter sized 
electrically pumped source22. Fig 1 shows an artist’s view of a chip-scale OCT system consisting of lithographically 
defined components all on a single chip, where the Si3N4 microresonator acts as a light source. Fig 1 inset shows the 
recently demonstrated hybrid approach for achieving chip-scale mm-size electrically pumped microresonator 
combs22. 
 
In order to enable a large imaging range using the optical comb as an OCT source of at least 2 mm (comparable with 
commercial OCT imaging range), we design the combs with a small spectral line spacing of 0.21 nm (corresponding 
to 38 GHz) using a large microresonator with a perimeter of 1.9 mm (see the Supplementary Materials). This 
perimeter is at least an order of magnitude larger than traditional high confinement micro-resonators14,24,25. In order 
to achieve sufficient optical power build up and enable comb generation in such a large cavity8,26, we rely on the 
extremely low loss platform recently demonstrated27. The ultra-low loss of 3 dB/m compensates for the large mode 
volume and enables frequency combs generation with 120 nm bandwidth. In order to generate the combs with broad 
bandwidth and high conversion efficiency, ideal for OCT imaging, we ensure that the combs generation process 
does not induce soliton states with characteristic hyperbolic secant spectrum, by tuning of the cavity resonance 
relative to the pump frequency using a microheater co-fabricated with the resonator28–30. Figure 2A shows the 
fabricated on-chip resonator. Figure 2B shows the generated frequency comb spectra using a ring resonator based on 
waveguides with 7301500 nm cross section. The measured power in these frequency combs lines is 42 mW with 
pump power of 142 mW corresponding to 30% conversion efficiency.


## Page 3


Using the microresonator platform, we acquire OCT images of human tissue with chip-based frequency combs and 
show that the platform is compatible with a standard commercial SD-OCT system31 . These images were achieved 
using a standard SD-OCT system (Thorlabs Telesto I), where the SLD was simply replaced by the chip-based 
frequency combs. Since the system is not optimized for our combs, the imaging capability is a lower bound limit. 
Figures 3-4 show ex vivo OCT images of human breast and coronary artery samples imaged with our microresonator 
frequency comb source using a commercial SD-OCT system31. The human breast tissue was obtained from 
Columbia University Tissue Bank32, and the human heart was obtained via the national disease research 
interchange33. Figure 3 compares images recorded using our microresonator frequency comb and a commercial SLD 
which has similar performance to the generated combs (see the Supplementary Materials). The Hematoxylin and 
Eosin (H&E) stained histology is provided as the reference for both the breast and two arteries in cardiovascular 
system, coronary artery and aorta. Different tissue types, including stromal tissue, adipose tissue and milk duct are 
delineated in both B-scans by comparing with the corresponding histology analysis. Figure 4A shows a stitched 
frequency-comb-based OCT image of a human left anterior descending artery (LAD) in comparison with the H&E 
histology in Figure 4B. Figure 4C shows a stitched frequency-comb-based OCT image of a human aorta in 
comparison with the H&E histology in Figure 4D. OCT B-scans were stitched using the method previously used in 
cervical imaging31. In the red inset, a gradually decreasing trend of backscattering can be visualized within the 
transition region from a fibrous region to the media. The blue inset in Figure 4 reveals a typical pattern of a 
fibrocalcific plaque3, where a layer of signal-rich fibrous cap is on the top of calcium, a signal-poor region with a 
sharply delineated border. Importantly, overlying the fibrocalcific plaque region, we can see a transition from dense 
fibrous cap a region with a thinner fibrous cap for unstable plaque structure. The green inset in Figure 4 shows the 
visualization of large calcification region, the deposit of calcium. Figures 3 and 4 show the potential to visualize 
critical features within human breast and cardiovascular samples by integrating the chip-based frequency combs into 
an OCT system. 
 
We have demonstrated the viability of chip-based frequency comb platform as light sources for OCT systems a key 
step toward fully integrated chip-scale OCT systems. The different building blocks needed in order to realize an 
integrated OCT system including a chip-scale beam splitter, reference arm, sampling arm and spectrometer have


## Page 4


already been demonstrated recently and can be integrated on the same chip as the microresonator2–6 enabling the 
miniaturization and lower cost of OCT systems. 
 
In addition to enabling highly integrated sources, Si3N4 microresonator combs exhibit a bandwidth that is determined 
by the waveguide geometry alone and not limited by the optical power13,30, in contrast to traditional OCT sources 
based on SLD sources with limited bandwidth at high optical powers due to gain narrowing. With waveguide 
dispersion engineering and a spectrometer designed for the combs, this platform could enable high axial resolution 
and high penetration depth.  
 
Methods 
Device fabrication 
Starting from a silicon wafer, a 4-µm-thick oxide layer is grown for the bottom cladding. Silicon nitride (Si3N4) is 
deposited using low-pressure chemical vapor deposition (LPCVD) in two steps. After Si3N4 deposition, we deposit a 
silicon dioxide (SiO2) hard mask using plasma enhanced chemical vapor deposition (PECVD). We pattern our 
devices with JEOL 9500 electron beam lithography. Ma-N 2403 electron-beam resist is used to write the pattern, 
and the nitride film is etched in an inductively coupled plasma reactive ion etcher (ICP RIE) using a combination of 
CHF3, N2, and O2 gases. After stripping the resist and oxide mask, we anneal the devices at 1200°C in an argon 
atmosphere for 3 hours to remove residual N-H bonds in the Si3N4 film. We clad the devices with 500 nm of high 
temperature silicon dioxide (HTO), deposited at 800°C, and followed by 2.5 µm of SiO2 using PECVD. Chemical 
Mechanical Polishing (CMP) and multipass lithography technique can be applied to further reduce sidewall 
scattering losses27. Above the waveguide cladding, we fabricate integrated microheaters by sputtering platinum and 
using a lift-off approach. We integrated micro-heaters on our device to control the cavity resonance by temperature 
tuning, which enables the use of a simple compact single-frequency pump laser diode to generate frequency 
combs15,34. 
 
Measurements 
As the presence of the pump within the comb spectrum limits the dynamic range of the detection, we use a filtering 
setup based on a free-space grating and pin to fully attenuate the pump power. The setup is shown in the


## Page 5


Supplementary Materials. This filtering setup can be replaced by a customized fiber-based filter or an on-chip filter 
to miniaturize the size of the setup in the future. We directly plug the comb source into a commercial system 
(Thorlabs Telesto I) to acquire images. The schematic of the OCT system is shown in the Supplementary Materials. 
An optical circulator with an isolation of -40dB is added to protect the commercial console. The incident light from 
the comb source is routed to the Michelson interferometer, and the backscattered signals from both interferometer 
arms are directed back to the spectrometer. 
 
Using the frequency combs combined with the commercialized SD-OCT system, we are able to acquire OCT images. 
The images are reconstructed in real-time from the raw spectral data generated by the system, following standard 
OCT signal processing steps, including background subtraction, linear-k interpolation, apodization, and dispersion 
compensation. The acquisition rate is 28 kHz currently limited by the CCD line rate. The total acquisition time of an 
image for the SLD and the chip comb images is the same (35msec). The sensitivity of the OCT system is defined by 
the minimal sample reflectivity at which the signal to noise ratio reaches unity35. It is measured to be 98 dB at an A-
line rate of 28 kHz with the frequency comb source. The sensitivity can be further increased by suppressing the 
noise due to the laser-chip coupling via packaging36.  
 
Acknowledgements 
The authors would like to thank Charles Marboe for his histopathological assistance. This work was performed in 
part at the Cornell NanoScale Facility, a member of the National Nanotechnology Coordinated Infrastructure 
(NNCI), which is supported by the National Science Foundation (ECCS-1542081). The authors acknowledge 
support from the Defense Advanced Research Projects Agency (N66001-16-1-4052), the Air Force Office of 
Scientific Research (FA9550-15-1-0303), the National Science Foundation (2016-EP-2693-A, CCF-1640108) and 
the National Institute of Health (1DP2HL127776-01). X.J. acknowledges the China Scholarship Council for 
financial support.


## Page 6


Author contributions  
X.J. prepared the manuscript in discussion with all authors. X.J., A.K. and X.Y. designed and performed the 
experiments. X.J. fabricated the devices. A.K. performed theoretical modelling and simulations. X.Y. and Y.G. 
performed the OCT measurements and data analysis. M.L., C.P.H. and A.L.G. supervised the project. 
 
References 
1. 
Huang, D. et al. Optical coherence tomography. Sci. N. Y. NY 254, 1178 (1991). 
2. 
Akca, B. I. et al. Miniature spectrometer and beam splitter for an optical coherence tomography on a silicon 
chip. Opt. Express 21, 16648 (2013). 
3. 
Yurtsever, G. et al. Photonic integrated Mach-Zehnder interferometer with an on-chip reference arm for optical 
coherence tomography. Biomed. Opt. Express 5, 1050 (2014). 
4. 
Chang, L. et al. Chip based common-path optical coherence tomography system with an on-chip microlens and 
multi-reference suppression algorithm. Opt. Express 24, 12635 (2016). 
5. 
Schneider, S. et al. Optical coherence tomography system mass-producible on a silicon photonic chip. Opt. 
Express 24, 1573 (2016). 
6. 
Eggleston, M. S. et al. 90dB Sensitivity in a Chip-Scale Swept-Source Optical Coherence Tomography System. 
2 (2018). 
7. 
Kippenberg, T. J., Holzwarth, R. & Diddams, S. A. Microresonator-based optical frequency combs. Science 
332, 555–559 (2011). 
8. 
Kippenberg, T. J., Spillane, S. M. & Vahala, K. J. Kerr-Nonlinearity Optical Parametric Oscillation in an 
Ultrahigh- Q Toroid Microcavity. Phys. Rev. Lett. 93, (2004). 
9. 
Del’Haye, P. et al. Optical frequency comb generation from a monolithic microresonator. Nature 450, 1214–
1217 (2007). 
10. Suh, M.-G., Yang, Q.-F., Yang, K. Y., Yi, X. & Vahala, K. J. Microresonator soliton dual-comb spectroscopy. 
Science 354, 600–603 (2016). 
11. Kuyken, B. et al. An octave-spanning mid-infrared frequency comb generated in a silicon nanophotonic wire 
waveguide. Nat. Commun. 6, 6310 (2015).


## Page 7


12. Miller, S. A. et al. Low-loss silicon platform for broadband mid-infrared photonics. Optica 4, 707 (2017). 
13. Okawachi, Y. et al. Octave-spanning frequency comb generation in a silicon nitride chip. Opt. Lett. 36, 3398–
3400 (2011). 
14. Pfeiffer, M. H. P. et al. Octave-spanning dissipative Kerr soliton frequency combs in Si_3N_4 microresonators. 
Optica 4, 684 (2017). 
15. Xue, X. et al. Mode-locked dark pulse Kerr combs in normal-dispersion microresonators. Nat. Photonics 9, 
594–600 (2015). 
16. Jung, H., Xiong, C., Fong, K. Y., Zhang, X. & Tang, H. X. Optical frequency comb generation from aluminum 
nitride microring resonator. Opt. Lett. 38, 2810 (2013). 
17. Wang, C. Y. et al. Mid-infrared optical frequency combs at 2.5 μm based on crystalline microresonators. Nat. 
Commun. 4, 1345 (2013). 
18. Grudinin, I. S., Yu, N. & Maleki, L. Generation of optical frequency combs with a CaF 2 resonator. Opt. Lett. 
34, 878–880 (2009). 
19. Hausmann, B. J. M., Bulu, I., Venkataraman, V., Deotare, P. & Lončar, M. Diamond nonlinear photonics. Nat. 
Photonics 8, 369–374 (2014). 
20. Pu, M., Ottaviano, L., Semenova, E. & Yvind, K. Efficient frequency comb generation in AlGaAs-on-insulator. 
Optica 3, 823 (2016). 
21. Miller, S. et al. On-chip frequency comb generation at visible wavelengths via simultaneous second- and third-
order optical nonlinearities. Opt. Express 22, 26517 (2014). 
22. Stern, B., Ji, X., Okawachi, Y., Gaeta, A. L. & Lipson, M. Battery-operated integrated frequency comb 
generator. Nature 562, 401–405 (2018). 
23. Ikeda, K., Saperstein, R. E., Alic, N. & Fainman, Y. Thermal and Kerr nonlinear properties of plasma-deposited 
silicon nitride/silicon dioxide waveguides. Opt. Express 16, 12987–12994 (2008). 
24. Karpov, M., Pfeiffer, M. H. P., Liu, J., Lukashchuk, A. & Kippenberg, T. J. Photonic chip-based soliton 
frequency combs covering the biological imaging window. Nat. Commun. 9, (2018). 
25. Trocha, P. et al. Ultrafast optical ranging using microresonator soliton frequency combs. Science 359, 887–891 
(2018).


## Page 8


26. Matsko, A. B., Savchenkov, A. A., Strekalov, D., Ilchenko, V. S. & Maleki, L. Optical hyperparametric 
oscillations in a whispering-gallery-mode resonator: Threshold and phase diffusion. Phys. Rev. A 71, (2005). 
27. Ji, X. et al. Ultra-low-loss on-chip resonators with sub-milliwatt parametric oscillation threshold. Optica 4, 619 
(2017). 
28. Ferdous, F. et al. Spectral line-by-line pulse shaping of on-chip microresonator frequency combs. Nat. 
Photonics 5, 770–776 (2011). 
29. Herr, T. et al. Universal formation dynamics and noise of Kerr-frequency combs in microresonators. Nat. 
Photonics 6, 480–487 (2012). 
30. Coen, S., Randle, H. G., Sylvestre, T. & Erkintalo, M. Modeling of octave-spanning Kerr frequency combs 
using a generalized mean-field Lugiato–Lefever model. Opt. Lett. 38, 37–39 (2013). 
31. Gan, Y. et al. Analyzing three-dimensional ultrastructure of human cervical tissue using optical coherence 
tomography. Biomed. Opt. Express 6, 1090–1108 (2015). 
32. Yao, X. et al. Visualization and tissue classification of human breast cancer images using ultrahigh-resolution 
OCT. Lasers Surg. Med. 49, 258–269 (2017). 
33. Gan, Y., Tsay, D., Amir, S. B., Marboe, C. C. & Hendon, C. P. Automated classification of optical coherence 
tomography images of human atrial tissue. J. Biomed. Opt. 21, 101407–101407 (2016). 
34. Joshi, C. et al. Thermally controlled comb generation and soliton modelocking in microresonators. Opt. Lett. 41, 
2565–2568 (2016). 
35. Leitgeb, R., Hitzenberger, C. K. & Fercher, A. F. Performance of fourier domain vs. time domain optical 
coherence tomography. Opt. Express 11, 889–894 (2003). 
36. Komljenovic, T. et al. Heterogeneous Silicon Photonic Integrated Circuits. J. Light. Technol. 34, 20–35 (2016).


## Page 9


Fig 1. Artist view of a fully integrated OCT systems with frequency combs light source. The frequency combs light 
source is formed by a reflective semiconductor optical amplifier chip fully integrated with an ultra-low loss Si3N4 
microresonator (Inset). The interferometer, including beam splitter, reference arm, sampling arm and spectrometer is 
integrated on the same chip. A mircolens and MEMS based scanning mirror can be attached to emit and collect and 
backscattered light from the sample6. 
 
 
Fig 2. Device image and measured spectrum. (A) Microscopy image of the silicon nitride on-chip microresonator. A 
platinum heater is fabricated over a large portion of the cavity and allows electric contact via the pads. (B) Measured 
frequency comb spectrum generated using the silicon nitride microresonators. Inset shows line spacing of 0.21 nm. 
 
100	μm
Pump
Output
Platinum	
Heaters
Waveguide
(A)
(B)


## Page 10


Fig 3. OCT images comparsion. OCT C-scans of human breast tissue taken with (A) the frequency comb source, (B) 
a single SLD source, and OCT B-scans of the same tissue taken with (C) the frequency comb source (marked by the 
blue arrow) and (D) a single SLD source (marked by the yellow arrow), respectively, corresponded with (E) the 
H&E staining slide. Different features and tissue types, such as stromal tissue, adipose tissue and milk duct, are 
delineated in both B-scans. 
 
Fig 4. Frequency-comb-based OCT images. Stitched frequency-comb-based OCT B-scans of human coronary artery 
(A) and aorta (C) with corresponding H&E histology of coronary artery (B) and aorta (D).  Critical features are 
observed, including delineation of the fibrous cap, calcium, and layered structure of intima and media are depicted 
within OCT images.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1902_07695v1_chip_based_frequency_combs_sources_for_optical_coherence_tomography
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1902_07695V1_CHIP_BASED_FREQUENCY_COMBS_SOURCES_FOR_OPTICAL_COHERENCE_TOMOGRAPHY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
