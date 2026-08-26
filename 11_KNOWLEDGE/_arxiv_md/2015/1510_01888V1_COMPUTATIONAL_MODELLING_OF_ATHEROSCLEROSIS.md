---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1510.01888v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1510.01888v1_Computational_Modelling_of_Atherosclerosis

> Source: 1510.01888v1_Computational_Modelling_of_Atherosclerosis.pdf

> Pages: 39

---


## Page 1


Computational+Modelling+of+Atherosclerosis+
+
Andrew+Parton1,+Victoria+McGilligan1,+Maurice+O’Kane2,+Francina+R+
Baldrick1,+Steven+Watterson1*+
+
1Northern+Ireland+Centre+for+Stratified+Medicine,+Ulster+University,+CLTRIC,+Altnagelvin+Hospital+
Campus,+Derry,+Co+Londonderry,+Northern+Ireland,+BT47+6SB+
2Department+of+Clinical+Chemistry,+Altnagelvin+Hospital,+Western+Health+and+Social+Care+Trust,+
Londonderry,+Northern+Ireland,+BT47+6SB+
*Corresponding+author+
+
+
Author+description+
+
Andrew+Parton+is+a+doctoral+student+at+the+Northern+Ireland+Centre+for+Stratified+Medicine,+Ulster+
University.+His+interests+are+in+using+computational+approaches+to+stratify+patients+with+
cardiovascular+disease.+
+
Victoria+McGilligan+is+an+Assistant+Professor+at+the+Northern+Ireland+Centre+for+Stratified+Medicine,+
Ulster+University.+Her+interests+are+in+inflammatory+biomarkers+for+disease+risk+in+personalized+
medicine.+
+
Maurice+O’Kane+is+a+consultant+chemical+pathologist+in+the+Western+Health+and+Social+Care+Trust+at+
Altnagelvin+Hospital.+His+interests+are+in+dyslipidaemia+and+clinical+decisionLmaking.+
+
Francina+R+Baldrick+is+an+Assistant+Professor+at+the+Northern+Ireland+Centre+for+Stratified+Medicine,+
Ulster+University.+Her+interests+are+in+biomarkers+for+the+role+of+nutrition+in+disease.+
+
Steven+Watterson+is+an+Assistant+Professor+at+the+Northern+Ireland+Centre+for+Stratified+Medicine,+
Ulster+University.+His+interests+are+in+computational+modelling+of+cholesterol+metabolism+and+
cardiovascular+disease.+
+
+
+


## Page 2


Key+Points+
• 
Atherosclerosis+is+a+disorder+that+emerges+from+a+combination+of+dynamic+processes,+making+
it+well+suited+to+computational+modelling.+
• 
Atherosclerosis+has+been+modelled+to+a+range+of+levels+of+detail+in+recent+work.+
• 
There+have+been+relatively+few+studies+of+plaque+rupture+and+thrombosis+with+most+work+
focussing+on+atheroma+formation.+
• 
Many+elements+of+atherosclerosis+have+not+yet+been+modelled+which+we+describe.+
• 
This+is+the+first+review+to+bring+together+the+latest+work+in+the+area.+
+


## Page 3


Computational+Modelling+of+Atherosclerosis+
+
Andrew+Parton1,+Victoria+McGilligan1,+Maurice+O’Kane2,+Francina+R+
Baldrick1,+Steven+Watterson1*+
+
1Northern+Ireland+Centre+for+Stratified+Medicine,+Ulster+University,+CLTRIC,+Altnagelvin+Hospital+
Campus,+Derry,+Co+Londonderry,+Northern+Ireland,+BT47+6SB+
2Department+of+Clinical+Chemistry,+Altnagelvin+Hospital,+Western+Health+and+Social+Care+Trust,+
Londonderry,+Northern+Ireland,+BT47+6SB+
*Corresponding+author+
+
+
Atherosclerosis+is+one+of+the+principle+pathologies+of+cardiovascular+disease+with+blood+cholesterol+a+
significant+ risk+ factor.+ +The+ World+ Health+ Organisation+ estimates+ that+ approximately+ 2.5+ million+
deaths+occur+annually+due+to+the+risk+from+elevated+cholesterol+with+39%+of+adults+worldwide+at+
future+ risk.+ + Atherosclerosis+ emerges+ from+ the+ combination+ of+ many+ dynamical+ factors,+ including+
haemodynamics,+ endothelial+ damage,+ innate+ immunity+ and+ sterol+ biochemistry.+ + Despite+ its+
significance+to+public+health,+the+dynamics+that+drive+atherosclerosis+remain+poorly+understood.+As+a+
disease+that+depends+on+multiple+factors+operating+on+different+length+scales,+the+natural+framework+
to+apply+to+atherosclerosis+is+mathematical+and+computational+modelling.+A+computational+model+
provides+an+integrated+description+of+the+disease+and+serves+as+an+in#silico+experimental+system+from+
which+ we+ can+ learn+ about+ the+ disease+ and+ develop+ therapeutic+ hypotheses.+ Although+ the+ work+
completed+in+this+area+toLdate+has+been+limited,+there+are+clear+signs+that+interest+is+growing+and+
that+a+nascent+field+is+establishing+itself.++This+paper+discusses+the+current+state+of+modelling+in+this+
area,+bringing+together+many+recent+results+for+the+first+time.++We+review+the+work+that+has+been+
done,+ discuss+ its+ scope+ and+ highlight+ the+ gaps+ in+ our+ understanding+ that+ could+ yield+ future+
opportunities.+
!!


## Page 4


Introduction!
Cardiovascular+disease+(CVD)+is+the+primary+cause+of+death+globally+[1]+and+contributes+to+morbidity+
and+mortality+more+than+any+other+disorder+in+the+western+world+[2].+In+2012,+CVD+was+responsible+
for+ 31%+ of+ deaths+ worldwide,+ 47%+ of+ all+ deaths+ within+ Europe+ and+ 40%+ of+ all+ deaths+ within+ the+
European+Union+[3,+4].+CVD+covers+a+collection+of+disorders+that+can+be+split+into+atherosclerotic+and+
nonLatherosclerotic+ categories+ [1].+ Atherosclerotic+ CVD+ includes+ cerebrovascular+ disease+ [5],+
coronary+artery+disease+[6]+and+peripheral+vascular+disease+[7],+and+it+is+responsible+for+the+majority+
of+instances+of+CVD+with+a+2012+estimate+attributing+71%+of+all+CVD+to+atherosclerotic+forms+[4].++
At+least+75%+of+all+CVDLrelated+deaths+occur+in+low+and+middleLincome+countries+[3].+In+China,+more+
than+4%+of+the+gross+national+income+is+directly+spent+on+the+treatment+of+CVD+[8]+and+in+the+EU,+it+is+
estimated+that+CVD+costs+the+economy+approximately+€196+billion+per+year+[4].+Improvements+in+
atherosclerosis+and+CVD+treatment+therefore+have+the+potential+to+make+a+dramatic+impact,+not+only+
on+the+quality+of+care+available,+but+also+on+the+economics+of+healthcare.++
CVD+ is+ predominantly+ an+ age+ related+ condition.+ Coronary+ heart+ disease+ in+ men+ occurs+ five+ times+
more+ frequently+ in+ 80++ year+ old+ patients+ than+ similar+ patients+ in+ the+ 40L59+ age+ group+ [9].+ It+ is+
predicted+that+the+global+population+aged+60++will+rise+from+11%+in+the+year+2000+[10]+to+22%+in+
2050,+ making+ atherosclerosis+ a+ significant+ future+ public+ health+ concern.+ + Comorbidities+ that+ drive+
CVD,+such+as+diabetes+[11],+are+set+to+grow+with+a+global+increase+of+55%+in+cases+projected+between+
2013+ and+ 2035+ [12].+ The+ current+ and+ growing+ global+ risk+ of+ morbidity+ and+ mortality+ from+
atherosclerosis+and+the+economic+burden+of+treatment+therefore+make+atherosclerosis+an+important+
area+of+future+research.+
Despite+ the+ growing+ importance+ of+ atherosclerosis+ and+ its+ implications+ for+ public+ health,+ its+
pathogenesis+is+not+fully+understood+[13].+Traditionally,+atherosclerosis+was+viewed+as+a+buildLup+of+
lipids+(including+cholesterol)+within+the+innermost+layer+of+the+artery+wall+(the+tunica#intima)+[14].++


## Page 5


However,+ our+ understanding+ has+ since+ developed+ and+ atherosclerotic+ CVD+ is+ now+ predominantly+
viewed+ as+ a+ chronic+ inflammatory+ condition,+ advanced+ by+ lipid+ buildLup+ and+ triggered+ by+ innate+
immune+responses+[13,+15].+++
Atherosclerosis+emerges+as+the+results+of+multiple+dynamical+cell+processes.+Damage+to+endothelial+
cells+[16]+recruits+monocytes+to+the+site+of+inflammation+via+interL+and+intraLcellular+signalling+[17].+
Monocytes+ migrate+ into+ the+ artery+ wall+ [18],+ alongside+ lipoproteins,+ before+ differentiating+ into+
macrophages+and+phagocytosing+oxidised+low+density+lipoproteins+(oxLDL)+[19,+20].+The+migration+
rate+of+these+cells+and+particles+is+dependent+upon+haemodynamics+[21]+and+vascular+mechanical+
stress+ [22].+ The+ accumulation+ of+ cholesterolLladen+ macrophages+ within+ the+ artery+ wall+ leads+ to+
plaque+formation+[23].+
Studies+aimed+at+understanding+atherosclerosis+need+to+be+broad+in+scope+and+integrative+in+nature.++
The+ appropriate+ framework+ in+ which+ to+ consider+ emergent+ dynamical+ behaviour+ of+ this+ type+ is+
mathematical+ and+ computational+ modelling.+ A+ comprehensive+ programme+ of+ mathematical+
modelling+ and+ simulation+ can+ provide+ many+ benefits.+ + Principally,+ it+ yields+ a+ framework+ for+
therapeutic+hypothesis+generation+and+for+in#silico+drug+target+identification+with+the+potential+to+
streamline+the+drug+development+pipeline.++This+framework+can+be+applied+across+populations+or+can+
be+ tuned+ to+ describe+ individual+ patients+ or+ patient+ groups+ as+ part+ of+ a+ programme+ of+ stratified,+
personalised+and+precision+medicine+[24].++
Mathematical+and+computational+models+can+take+a+range+of+forms.++Ordinary+differential+equations+
(ODEs)+[25],+partial+differential+equations+(PDEs)+[25]+and+stochastic+ordinary+differential+equations+
(SODEs)+[26],+alongside+binary+[27]+and+multivalued+[28]+logic+have+all+been+used+to+model+pathway+
dynamics.+Process+algebras+such+as+pi+[29]+and+kappa+[30]+calculus+have+been+used+to+capture+the+
structure+of+pathway+systems,+in+particular+addressing+the+exponential+growth+in+possible+network+
configurations+ to+ be+ considered+ as+ the+ number+ of+ pathway+ components+ increases+ [31,+ 32].++


## Page 6


Statistical+models+that+infer+pathway+structure+have+been+used+to+generate+hypotheses+from+existing+
datasets+[33,+34].+++
Computational+biology+approaches+have+previously+been+applied+in+studies+of+a+range+of+dynamical+
disease+ processes.+ Examples+ include+ studies+ of+ Alzheimer’s disease+ in+ which+ the+ pathways+ that+
mediate+brain+energy+metabolism+have+been+elucidated+[35],+studies+of+diabetes+in+which+models+of+
diagnostic+ testing+ have+ been+ developed+ along+ with+ models+ of+ the+ physiological+ mechanisms+
associated+with+disease+[36]+and+studies+of+breast+cancer+in+which+biomarkers+have+been+identified+
for+ the+ stratification+ of+ patient+ treatment+ [37].+ + Furthermore,+ computational+ models+ have+ been+
applied+to+pathway+systems+such+as+nuclear+factor+kappa+beta+(NFLκB)+signalling+[38],+macrophage+
processing+[39],+human+metabolism+[40]+and+iron+metabolism+[41].++In+one+of+the+more+ambitious+
computational+ studies+ of+ recent+ years,+ the+ first+ computational+ model+ of+ whole+ cell+ activity+ has+
appeared+describing+Mycoplasma#genitalium#[42].+++
+MachineLreadable+ standards+ for+ model+ representation+ have+ been+ developed+ to+ assist+ model+
development+ and+ model+ reuse.+ + These+ standards+ have+ stimulated+ the+ creation+ of+ pathway+
informatics+tools+and+have+made+models+independent+of+the+software+tools+used+to+create+them.+In+
particular,+ the+ Systems+ Biology+ Markup+ Language+ (SBML)+ [43,+ 44]+ and+ CellML+ [45]+ file+ formats+
capture+ ODE+ models+ describing+ the+ kinetics+ of+ pathway+ interactions+ and+ the+ Systems+ Biology+
Graphical+Notation+Markup+Language+(SBGNLML)+[46,+47]+encodes+diagrams+of+pathway+function+in+a+
biologically+ meaningful+ file+ format.+ + The+ Minimum+ Information+ Requested+ in+ the+ Annotation+ of+
Biochemical+ Models+ (MIRIAM)+ [48]+ and+ Minimum+ Information+ About+ a+ Simulation+ Experiment+
(MIASE)+[49]+standards+describe+model+annotation+and+use+respectively,+and+online+repositories+of+
SBML+files+have+been+introduced+to+facilitate+model+reuse+[50].+
Previously,+cholesterol+biosynthesis+and+the+impact+of+therapeutic+interventions+have+been+modelled+
in+a+series+of+computational+studies+[51–55]+and+the+role+of+lipid+metabolism+and+CVD+in+aging+has+
been+reviewed+[56].++However,+no+review+has+yet+brought+together+the+significant+volume+of+recent+


## Page 7


work+ completed+ on+ computational+ modelling+ of+ atherosclerosis.+ + This+ paper+ reviews+ the+ current+
state+ of+ this+ important+ nascent+ field,+ describing+ the+ work+ completed+ to+ date,+ discussing+ the+
approaches+taken+and+highlighting+the+gaps+in+our+understanding.+++
+


## Page 8


The!pathophysiology!of!atherosclerosis!
In+ Figure+ 1,+ we+ see+ a+ representation+ of+ the+ processes+ that+ lead+ to+ atherosclerosis+ [13,+ 57,+ 58].+
Damage+ to+ the+ endothelial+ layer+ of+ the+ artery+ wall+ triggers+ an+ inflammatory+ response+ in+ which+
monocytes,+TLlymphocytes+and+other+immune+cells+are+recruited+to+the+region+of+damage.++These+
cells+penetrate+the+endothelial+layer,+reaching+the+tunica#intima,+along+with+low+density+lipoprotein+
(LDL)+and+highLdensity+lipoprotein+(HDL)+particles.+Stimulated+by+the+presence+of+interferon+gamma+
(IFNLγ)+ and+ macrophage+ colony+ stimulating+ factor+ (MLCSF),+ monocytes+ differentiate+ into+
macrophages+ once+ they+ have+ entered+ the+ artery+ wall.+ While+ embedded+ within+ the+tunica# intima,+
both+LDL+and+HDL+become+oxidized+by+free+oxygen+radicals.+Macrophages+will+phagocytose+oxidized+
LDL+(oxLDL),+but+not+oxidized+HDL.+Macrophages+heavily+loaded+with+oxLDL+transform+into+foam+cells+
that+eventually+undergo+apoptosis.++The+resulting+mass+of+debris+embedded+in+the+tunica#intima+is+
known+as+an+atheroma.+Foam+cells,+along+with+endothelial+cells,+secrete+monocyte+chemoattractant+
proteinL1+(MCPL1)+to+recruit+more+monocytes+to+the+site+of+inflammation.+Naïve+T+cells+contained+
within+the+artery+wall+differentiate+into+individual+T+cell+types+that+can+secrete+IFNLγ.+Smooth+muscle+
cells+(SMCs)+are+also+recruited+into+the+tunica#intima+where+they+undergo+apoptosis+and+contribute+
to+the+formation+of+a+fibrous+cap+in+the+artery+wall.++This+accumulation+of+cells+and+debris+can+cause+a+
swelling+of+the+artery+wall+that+restricts+blood+flow,+leading+to+stenosis.++If+the+fibrous+cap+ruptures,+
the+buildLup+in+the+tunica#intima+is+released+into+the+blood+stream+increasing+the+risk+of+blockages+
downstream.++Further+complications+can+occur+including+clotting+at+the+site+of+the+atheroma+where+a+
thrombus+forms+further+impeding+blood+flow.+++
Computational!modelling!
Blood%flow%dynamics%
Vascular+damage+is+a+key+trigger+for+the+onset+of+atherosclerosis+that+can+be+induced+by+factors+such+
as+hypertension+[59],+smoking+[60]+and+oxidative+stress+[61].++The+elastic+properties+of+arteries+under+
hypertensive+pressure+have+been+modelled+previously+[62].+Obstructions+to+blood+flow+are+known+to+


## Page 9


be+atherogenic+[63]+and+it+has+been+shown+that+this+is+in+part+attributable+to+the+turbulent+blood+
flow+likely+to+be+induced+downstream+[21,+22,+64–66].++
A+number+of+computational+ studies+have+modelled+the+dynamics+of+blood+flow+(haemodynamics)+
and+ its+ relationship+ to+ vascular+ structure.+ NavierLStokes+ equations+ are+ typically+ used+ to+ describe+
blood+flow+through+arterial+structures+[62–64,+66–82]+under+the+assumption+that+blood+flows+as+a+
Newtonian+fluid,+an+approximation+that+can+be+violated+by+its+viscosity+and+granularity.+However,+
NavierLStokes+ systems+ are+ well+ studied+ and+ are+ therefore+ represent+ a+ powerful+ framework+ for+
computational+analysis.++Arterial+wall+shear+stress+(WSS)+is+widely+used+as+a+model+output+that+serves+
as+a+marker+for+atherosclerotic+prone+regions+within+an+artery+[21,+66,+67,+69–73,+76,+78–86].+How+
WSS+impairs+endothelial+function+is+not+well+known,+although+its+physiological+significance+has+been+
demonstrated+[22].++TwoLdimensional+and+threeLdimensional+models+of+a+YLshaped+arterial+branch+
[66,+70,+71,+80,+83,+85–87]+have+been+created+along+with+linear+artery+models+[64,+67,+68,+70–75,+78,+
81,+ 88,+ 89].+ + Lower+ dimensional+ models+ are+ less+ physiologically+ accurate,+ but+ they+ provide+ the+
authors+ with+ more+ computationally+ amenable+ frameworks+ in+ which+ to+ demonstrate+ important+
principles,+such+as+plaque+stability+[64]+and+the+impact+of+stenosis+[67].+
Inflammation+is+thought+to+be+driven+by+the+penetration+of+the+arterial+wall+by+LDL,+which+in+some+
cases+is+taken+to+be+a+function+of+the+wall+shear+stress,+demonstrating+that+an+arterial+branch+can+be+
a+focal+point+for+atheroma+formation+[66,+70,+71,+80,+81,+83,+85,+86].+As+well+as+WSS,+it+has+been+
shown+that+inflammation+is+related+to+blood+viscosity,+inlet+flow+rate+and+the+geometry+of+the+artery+
[73].+
Simpler+ abstract+ models+ of+ this+ process+ have+ been+ developed+ that+ are+ less+ physiologically+
descriptive,+but+that+enable+more+powerful+mathematical+approaches+to+be+employed.++They+have+
been+used+to+describe+atherosclerosis+as+a+bistable+system+for+simple+arterial+geometries+[84],+to+
develop+haemodynamic+models+in+order+to+explore+the+turbulence+downstream+of+an+atherosclerotic+


## Page 10


constriction+in+two+dimensions+[88]+and+to+describe+haemodynamics+and+plaque+formation+as+a+test+
case+for+novel+numerical+methods+[90].++
LDL%concentration%in%the%artery%lumen%
The+ turnover+ of+ LDL+ in+ the+ blood+ plays+ an+ important+ role+ as+ a+ primary+ factor+ that+ affects+ LDL+
penetration+of+the+tunica#intima#in+many+models+of+atherosclerosis.+Plasma+LDL+levels+have+been+
modelled+as+constant+[71,+77,+80,+87],+or+as+a+variable+[68,+70,+71,+74,+78,+81,+85,+90,+91]+where+the+
system+dynamics+are+typically+governed+by+a+series+of+convectionLdiffusion+equations,+or+part+of+a+
combined+mass+flow+[82].++
LDL%penetration%of%the%tunica%intima%%
The+process+through+which+LDL+passes+into+the+tunica#intima+has+been+modelled+at+a+range+of+levels.++
The+simplest+approaches+consider+this+to+be+a+mathematical+function+of+arterial+WSS+[92]+or+constant+
[77,+87,+90,+91,+93,+94].+Some+simply+ignore+LDL+penetration,+instead+considering+only+LDL+in+the+
tunica#intima+[84]+or+combining+cells,+proteins+and+other+macromolecules+into+one+mixed+quantity+
[95].+More+sophisticated+approaches+have+considered+diffusion+[68,+74,+78,+82,+85,+96,+97]+and+have+
modelled+the+artery+wall+as+a+semiLpermeable+membrane+by+utilising+KedemLKatchalsky+equations+
[67,+71,+81,+98,+99].+LDL+penetration+appears+to+be+considered+as+a+boundary+to+many+models+and+
the+description+of+its+uptake+reflects+the+scope+of+the+model+proposed.++
LDL%oxidation%and%the%role%of%HDL%
A+range+of+approaches+have+been+taken+to+describe+LDL+oxidation+inside+the+tunica#intima+and+they+
are+ coupled+ to+ LDL+ penetration+ to+ differing+ extents.+ + Many+ studies+ consider+ the+ synthesis+ and+
turnover+ of+ oxLDL+ directly+ [68,+ 71,+ 80,+ 81,+ 84,+ 86,+ 87,+ 90,+ 91,+ 93,+ 94,+ 96–98,+ 100,+ 101].+ In+ some,+
oxidation+of+LDL+is+a+modelled+reaction+[68,+71,+80,+81,+86,+87,+90,+91,+93,+94,+96,+97]+whereas+in+
others+it+is+taken+to+be+a+process+that+is+driven+by+factors+such+as+monocyte+recruitment+[84]+or+is+
modelled+ as+ a+ constant+ [100,+ 101].+ Intermediate+ stages+ of+ the+ oxidation+ process+ have+ been+


## Page 11


considered+ by+ modelling+ the+ number+ of+ unoxidized+ antioxidant+ molecules+ attached+ to+ each+ LDL+
particle+[94].+
The+role+of+HDL+has+been+incorporated+into+a+portion+of+these+studies.++In+particular,+it+has+been+
modelled+as+competing+for+free+radicals+and+suppressing+inflammatory+signalling+in+the+tunica#intima+
[91,+94,+97]+and+as+having+an+atheroprotective+effect+on+foam+cells+[96,+101].+
Elsewhere,+the+interplay+between+LDL,+HDL,+oxidising+free+radicals+and+antioxidant+vitamins+C+and+E+
have+been+studied+[94]+with+predictions+of+comparable+atheroprotective+power+between+HDL+and+
vitamin+C.+
Monocyte%recruitment%and%chemoattractants%
Monocyte+recruitment+has+been+modelled+as+related+to+shear+stress+and+the+rate+of+LDL+penetration+
[84].++The+existence+of+monocytes+in+the+lumen+has+rarely+been+considered+[68],+but+several+studies+
have+modelled+the+turnover+of+monocytes+in+the+tunica#intima+[68,+84,+91,+102,+103].++Elsewhere,+the+
process+of+monocyte+recruitment+and+differentiation+has+also+been+simplified+and+incorporated+into+
one+step+governing+macrophage+turnover,+where+this+is+linked+to+driving+factors+such+as+shear+stress,+
diffusion+and+LDL+penetration+[67,+80,+81,+86,+90,+93,+96–101].+++
Similarly,+the+turnover+of+MCPL1+as+a+chemoattractant+has+been+described+explicitly+in+some+studies+
[96,+97]+and+grouped+together+with+other+chemoattractants+including+interleukinL1+(ILL1)+and+MLCSF+
in+other+studies+[68,+86,+90,+91,+93,+99,+104].++One+study+has+shown+that+exposure+to+radiation+leads+
to+enhanced+levels+of+MCPL1+and+is+therefore+atherogenic+[103].++However,+in+many+studies+the+role+
of+chemoattractants+has+been+ignored.+++
Monocyte%to%macrophage%differentiation%
The+differentiation+of+monocytes+to+macrophages+has+been+incorporated+into+a+number+of+studies,+
although+many+simplify+this+step+by+considering+both+populations+as+one+group+on+the+grounds+that+


## Page 12


differentiation+occurs+on+a+time+scale+too+short+to+be+significant+[67,+71,+100].+Where+differentiation+
has+been+modelled+it+is+presented+with+mass+action+kinetics+[68,+84,+91,+103].+
Foam%cell%formation%and%the%phagocytosis%of%oxidised%LDL%
The+transformation+of+macrophages+to+foam+cells+due+to+the+phagocytosis+of+oxLDL+is+a+critical+stage+
in+the+formation+of+atheroma+that+has+been+included+in+many+studies.+These+are+typically+modelled+
as+a+combination+of+mass+action+and+MichaelisLMenten+terms+[67,+68,+80,+81,+84,+86,+96,+97,+100,+
101],+and+in+some+cases+reverse+cholesterol+efflux+is+included+in+the+model+[96,+101,+105].+Many+
studies,+however,+omit+foam+cell+formation+as+a+step,+instead+taking+the+volume+of+macrophages+
recruited+to+be+representative+of+atheroma+formation+[91,+93,+98,+102,+104].++
T%cell%recruitment%and%the%role%of%interferon=gamma%(IFN=γ)%
The+ role+ of+ T+ cells+ in+ coordinating+ the+ inflammatory+ response+ has+ rarely+ been+ included+ in+
computational+studies.+Where+they+have+been+included+as+a+factor,+T+cells+yield+IFNLγ+that+modulates+
macrophage+ differentiation+ [91,+ 96,+ 97,+ 103]+ and+ are+ themselves+ modelled+ as+ being+ activated+ by+
interleukin+12+(ILL12)+[96,+97],+although+it+has+been+shown+experimentally+that+T+cells+can+also+be+
activated+by+ILL1+[106]+and+IFNLγ+[107].++
Proliferation%of%smooth%muscle%cells%
Along+with+foam+cells+and+cell+debris,+SMCs+contribute+to+the+formation+of+atheroma+[13].++However+
this+ factor+ has+ rarely+ been+ incorporated+ into+ models.+ + Where+ it+ has+ been+ incorporated,+ SMC+
recruitment+occurs+in+response+to+MCPL1,+platelet+derived+growth+factor+(PDGF)+and+extracellular+
matrix+(ECM)+either+modelled+explicitly+as+factors+[96,+97]+or+as+a+generic+recruitment+process+[68,+
90,+91,+93].+One+study+in+particular+has+focused+on+the+interplay+between+SMCs+and+PDGF+identifying+
bistability+in+SMCLdriven+atheroma+formation+[108].++


## Page 13


Plaque%rupture%and%thrombosis%
The+rupture+of+atheroma+has+been+modelled,+establishing+a+criterion+for+atheroma+instability+that+
takes+the+form+of+a+solution+to+a+third+order+nonLlinear+ODE+[88].+Separate+studies+have+established+
stability+by+evaluating+the+eigenvalues+of+a+perturbed+system+[93]+and+by+calculating+the+mean+time4
to4rupture#of+atheroma+formation+[102].+The+WSS+upon+an+atheroma+has+been+calculated+as+a+trigger+
for+rupture+and+this+model+has+been+modified+to+incorporate+the+effects+of+abnormal+axial+GLforces+
[89].++Relevant+models+have+been+produced+that+describe+thrombus+formation+in+the+absence+[109]+
and+presence+of+shear+blood+flow+[64,+110].++
Discussion!
The+models+described+here+are+summarised+in+Table+1.++The+majority+of+the+work+presented+has+been+
published+in+the+last+10+years,+demonstrating+that+computational+modelling+of+atherosclerosis+is+a+
developing+field+with+growing+support.++These+studies+operate+at+a+range+of+levels+of+abstraction+and+
have+ variable+ scope.+ + However,+ they+ have+ all+ been+ produced+ as+ separate+ bespoke+ computational+
models+with+little+capacity+for+reuse+by+the+wider+modelling+community.++The+adoption+of+community+
modelling+standards+such+as+SBML+[43,+44]+and+SBGNLML+[46,+47]+would+enable+the+community+to+
progress+ together+ on+ the+ development+ of+ atherosclerosis+ modelling+ and+ it+ would+ be+ a+ valuable+
exercise+to+translate+the+most+biologically+detailed+models+[68,+81]+into+these+community+standards.++
Online+databases,+such+as+BioModels+[50,+111,+112]+and+the+Physiome+Model+Repository+2+(PMR2)+
[113],+ contain+ computational+ models+ of+ biological+ processes.+ + Such+ databases+ facilitate+ the+
codification+of+our+understanding+and,+critically,+enable+models+to+be+reused+and+built+upon+as+our+
knowledge+ advances.+ However,+ no+ models+ of+ atherosclerosis+ currently+ exist+ within+ these+
repositories,+although+systems+biology+representations+of+the+cardiovascular+system+[114]+and+statin+
pharmacokinetics+[115]+are+available.+


## Page 14


The+integration+of+models+developed+by+different+authors+is+likely+to+be+a+significant+future+
challenge.++The+introduction+of+an+online+platform+that+presents+networks+of+pathway+diagrams+using+
SBGN+standards+and+enables+users+to+select+individual+pathways+or+groups+of+pathways+to+study+in+
isolation+or+to+be+downloaded+for+offline+use,+using+SBGNLML+and+SBML+standards,+would+facilitate+
model+reuse,+maximising+the+value+gained+from+their+construction+and+enabling+the+research+
community+to+develop+a+coordinated+consensus+around+the+pathway+biology+more+rapidly.++Such+a+
platform+would+not+be+limited+to+atherosclerosis+but+could+be+applied+more+broadly+across+pathway+
biology.+++
Factors%not%yet%modelled%
There+are+many+components+of+atherosclerosis+that+to+date+have+not+been+modelled.+With+accurate+
parameterisation+each+would+increase+the+comprehensiveness+and+accuracy+of+our+understanding+of+
atherosclerosis+as+a+dynamical+process.+Triglyceride+rich+lipoproteins+contribute+to+plaque+buildLup+
with+some+studies+showing+that+they+trigger+foam+cell+formation+through+mechanisms+that+bypass+
LDL+oxidation+[116–118].+Elsewhere,+it+has+been+proposed+that+categories+of+HDL+and+their+relative+
proportions+may+be+more+important+than+the+absolute+abundance+of+HDL+[57,+119],+suggesting+that+
models+ could+ be+ adapted+ to+ incorporate+ a+ HDL+ profile+ that+ influences+ oxidation+ and+ reverse+
cholesterol+efflux.++It+has+also+been+shown+that+HDL+can+inhibit+the+recruitment+of+monocytes+and+
subsequently+reduce+atherogenesis+[120]+suggesting+further+interactions+to+model.++Clinically,+it+has+
been+ suggested+ that+ LDL+ particle+ number+ is+ a+ stronger+ risk+ factor+ for+ atherosclerosis+ than+ the+
abundance+of+LDLLbound+cholesterol,+implying+that+future+models+should+include+a+description+of+the+
cholesterol+load+of+lipoproteins+as+well+as+their+abundance+[121].++In+addition,+the+role+of+neutrophils+
[122],+ nitrous+ oxide+ [57],+ B+ cells+ [123],+ heat+ shock+ proteins+ [124,+ 125],+ sterol+ regulatory+ element+
binding+ protein+ (SREBP)+ mediated+ regulation+ [54],+ various+ cell+ signalling+ proteins+ such+ as+ NRLP3+
[126],++and+miRNAs+[127]+have+not+been+modelled+in+this+context.+++


## Page 15


By+ far+ the+ majority+ of+ work+ to+ date+ has+ been+ on+ the+ buildLup+ of+ atheroma.+ + Some+ studies+ have+
addressed+the+mechanisms+through+which+atheroma+rupture,+but+they+are+in+a+significant+minority.++
Very+little+work+has+been+done+on+the+consequences+of+rupture,+such+as+thrombus+formation.++This+
presents+ a+ potential+ direction+ for+ the+ field+ that+ is+ highly+ relevant+ to+ patient+ treatment+ as+ most+
patients+at+risk+of+CVD+are+only+identified+after+a+cardiovascular+event+has+occurred.++
Computational%modelling%in%therapy%development%
The+ application+ of+ computational+ modelling+ to+ therapy+ development+ in+ atherosclerosis+ has+ been+
historically+poor.++It+is+possible+to+predict+both+the+efficacy+of+a+drug+and+its+potential+side+effects+
[128–130]+ and+ there+ is+ growing+ interest+ in+ areas+ of+ combinatorial+ drug+ design+ [131]+ to+ optimise+
treatment.++Such+approaches+have+been+demonstrated+for+the+role+of+statins+in+the+reduction+of+LDL+
levels+in+plasma+along+with+dietary+changes+[51,+97].++Computational+biology+can+also+be+used+to+
identify+potential+molecular+targets+for+drugs+and+has+been+used+to+reduce+the+high+attrition+rate+of+
drug+discovery+[133].++However,+these+technologies+have+yet+to+be+exploited+to+their+full+potential.++
Finite+ element+ and+ analytical+ methods+ have+ been+ employed+ to+ model+ the+ interaction+ between+ a+
stent+and+artery+wall+when+widening+constricted+arteries+during+angioplasty+[134,+135].+
Creating+more+comprehensive+models+of+atherosclerosis+has+the+potential+to+improve+the+efficiency+
of+therapy+development+with+benefits+for+both+the+patient+and+the+commercial+vendor.++However,+
obtaining+ accurate+ parameterisations+ for+ the+ models+ is+ a+ fundamental+ challenge.+ + The+ lack+ of+
appropriate+ published+ experimental+ data+ is+ a+ critical+ obstacle+ to+ generating+ high+ confidence+
predictive+models.+++
Difficulties%in%model%generation%
Developing+a+comprehensive+predictive+model+of+atherogenesis+comes+with+many+challenges.+Our+
knowledge+ of+ the+ processes+ involved+ has+ increased+ significantly+ in+ recent+ years+ with+ the+
development+of+genomic+technologies+such+as+genome+wide+association+studies+(GWAS)+[136].+As+
atherosclerosis+is+a+cardiovascular+condition+that+affects+critical+circulatory+systems,+studying+human+


## Page 16


atheroma+poses+logistical+and+ethical+problems+as+access+to+live+atherosclerotic+tissue+is+limited+and+
disturbances+ risk+ triggering+ plaque+ rupture.+ Consequently,+ data+ is+ limited.+ Animal+ studies+ of+
atherosclerosis+do+exist+for+mouse,+rabbit+and+pig+[137]+and+profiling+has+been+conducted+for+plaque+
material+removed+in+carotid+endarterectomy+[138].+
The+limited+data+available+obstructs+studies+of+atheroma+at+the+macro+scale+and+of+the+molecular+
biology+involved.+As+a+result,+establishing+biologically+relevant+kinetic+parameters+that+can+be+used+to+
simulate+ pathway+ dynamics+ is+ challenging+ and+ comprehensive+ parameterisations+ for+ the+
pathogenesis+ of+ atherosclerosis+ are+ not+ available+ in+ the+ public+ domain.+ As+ a+ consequence,+ some+
studies+ have+ resorted+ to+ estimating+ parameters+ for+ models,+ based+ on+ expert+ opinion+ or+ inferred+
from+other+cell+processes.+
It+ is+ likely+ that+ approximate+ values+ can+ be+ obtained+ for+ a+ number+ of+ the+ parameters+ required+ by+
using+recombinant+proteins+and+in#vitro+studies.++However,+recreating+the+environment+of+the+tunica#
intima+and+quantifying+its+impact+on+the+parameterisation+in+order+to+obtain+physiological+values+will+
be+challenging+[139–141].+
Conclusion!
Computational+modelling+of+atherosclerosis+presents+an+opportunity+to+contribute+to+the+reduction+
of+the+global+burden+of+CVD.+++By+introducing+accurate+and+quantitative+models+of+atherosclerosis,+
we+can+create+an+in#silico+experimental+system+with+the+potential+not+only+to+displace+in#vivo+and+in#
vitro+experimentation+but+also+to+enable+us+to+study+details+that+cannot+be+measured+in#vivo#or#in#
vitro.+ However+ this+ necessitates+ a+ physiologically+ accurate+ parameterisation+ and+ such+ data+ is+ not+
currently+available+in+a+comprehensive+form.++
Historically,+little+work+has+been+completed+developing+computational+modelling+of+atherosclerosis,+
although+recent+years+have+seen+a+clear+growth+of+interest+and+the+formation+of+a+nascent+field.++


## Page 17


Here+we+have+gathered+together+and+reviewed+the+recent+results+with+a+view+to+identifying+where+
the+gaps+in+our+understanding+lie+and+where+progress+can+be+made.+++
Most+of+the+work+completed+in+this+area+to+date+has+focussed+on+the+inflammatory+response+and+the+
shear+stress+of+the+artery+wall+and+has+involved+modelling+at+a+range+of+levels+of+abstraction.+++
The+majority+of+work+has+focused+on+describing+atheroma+formation+and+few+studies+have+addressed+
the+mechanics+of+plaque+rupture+and+its+subsequent+consequences.+++In+most+cases,+models+follow+
the+ canonical+ understanding+ of+ atherosclerosis:+ LDL+ penetration+ and+ oxidation,+ monocyte+
recruitment+and+differentiation+and+foam+cell+formation.++However,+many+additional+factors+remain+
outside+this+canonical+picture+that+are+known+to+contribute+to+atherosclerosis+and+there+currently+
exist+ opportunities+ to+ explore+ their+ role+ in+ the+ dynamics+ of+ this+ disease+ through+ computational+
modelling.+
+
Acknowledgements!
We+would+like+to+acknowledge+and+thank+Eliza+Yankova+(University+of+Ulster)+for+her+assistance+with+
Figure+1+(The+pathophysiology+of+atherosclerosis).+
+
+


## Page 18


References!
1++
World+Health+Organisation+L+Mendis+S+Norrving+B+editors+PP.+Global+Atlas+on+Cardiovascular+
Disease+Prevention+and+Control.+
http://whqlibdoc.who.int/publications/2011/9789241564373_eng.pdf?ua=1+(3+August+2015,+
date+last+accessed)+
2++
Singh+RB,+Mengi+SA,+Xu+YJ,+et#al.+Pathogenesis+of+atherosclerosis:+A+multifactorial+process.+Exp#
Clin#Cardiol+2002;7:40–53.+
3++
World+Health+Organisation.+Cardiovascular+Diseases+Fact+Sheet.++
http://www.who.int/mediacentre/factsheets/fs317/en/+(3+August+2015,+date+last+accessed)+
4++
Nichols+M,+LuengoLFernandez+R,+Leal+J+et#al..+European+Cardiovascular+Disease+Statistics+2012.+
http://www.escardio.org/static_file/Escardio/PressLmedia/pressLreleases/2013/EUL
cardiovascularLdiseaseLstatisticsL2012.pdf+(3+August+2015,+date+last+accessed)+
5++
Postiglione+A,+Napoli+C.+Hyperlipidaemia+and+atherosclerotic+cerebrovascular+disease.+Curr#
Opin#Lipidol+1995;6:236–42.+
6++
Hansson+G.+Inflammation,+atherosclerosis,+and+coronary+artery+disease.+N#Engl#J#Med+
2005;353:1685–95.+
7++
Hussein+AA,+Uno+K,+Wolski+K,+et#al.+Peripheral+arterial+disease+and+progression+of+coronary+
atherosclerosis.+J#Am#Coll#Cardiol+2011;57:1220–5.+
8++
World+Heart+Federation.+Urbanization+and+Cardiovascular+Disease+Fact+Sheet.+
http://www.worldLheartLfederation.org/press/factLsheets/urbanizationLandLcardiovascularL
disease/+(3+August+2015,+date+last+accessed)+
9++
Mozaffarian+D,+Benjamin+EJ,+Go+AS,+et#al.+Heart+Disease+and+Stroke+StatisticsLL2015+Update:+A+
Report+From+the+American+Heart+Association.+Circulation+2015;131:29L322.+
10++
World+Health+Organisation.+Facts+about+aging.+http://www.who.int/ageing/about/facts/en/+
(3+August+2015,+date+last+accessed)+
11++
Grundy+SM,+Benjamin+IJ,+Burke+GL,+et#al.+Diabetes+and+cardiovascular+disease:+a+statement+for+
healthcare+professionals+from+the+American+Heart+Association.+Circulation+1999;100:1134–
46.+
12++
International+Diabetes+Federation.+IDF+Diabetes+Atlas,+6th+Edn.+
http://www.idf.org/diabetesatlas+(3+August+2015,+date+last+accessed)+
13++
Weber+C,+Noels+H.+Atherosclerosis:+current+pathogenesis+and+therapeutic+options.+Nat#Med+
2011;17:1410–22.+
14++
Libby+P,+Lichtman+A,+Hansson+G.+Immune+Effector+Mechanisms+Implicated+in+Atherosclerosis:+
From+Mice+to+Humans.+Immunity.+2013;38:1092–104.+
15++
Joris+I,+Majno+G.+Atherosclerosis+and+inflammation.+Adv#Exp#Med#Biol+1978;104:227–43.+


## Page 19


16++
Viggers+RF,+Wechezak+AR,+Sauvage+LR.+An+apparatus+to+study+the+response+of+cultured+
endothelium+to+shear+stress.+J#Biomech#Eng+1986;108:332–7.+
17++
Boisvert+WA.+Modulation+of+atherogenesis+by+chemokines.+Trends#Cardiovasc.#Med.+
2004;14:161–5.+
18++
Kraemer+R.+Regulation+of+cell+migration+in+atherosclerosis.+Curr#Atheroscler#Rep+2000;2:445–
52.+
19++
Yoshida+H,+Kisugi+R.+Mechanisms+of+LDL+oxidation.+Clin.#Chim.#Acta.+2010;411:1875–82.+
20++
Schrijvers+DM,+De+Meyer+GRY,+Herman+AG,+et#al.+Phagocytosis+in+atherosclerosis:+Molecular+
mechanisms+and+implications+for+plaque+progression+and+stability.+Cardiovasc#Res+
2007;73:470–80.+
21++
Glagov+S,+Zarins+C,+Giddens+DP,+et#al.+Hemodynamics+and+atherosclerosis.+Insights+and+
perspectives+gained+from+studies+of+human+arteries.+Arch.#Pathol.#Lab.#Med.+1988;112:1018–
31.+
22++
Cunningham+KS,+Gotlieb+AI.+The+role+of+shear+stress+in+the+pathogenesis+of+atherosclerosis.+
Lab#Invest+2005;85:9–23.+
23++
Blum+A,+Miller+HI.+The+role+of+inflammation+in+atherosclerosis.+Isr#J#Med#Sci+1996;32:1059–65.+
24++
Auffray+C,+Hood+L.+Editorial:+Systems+biology+and+personalized+medicine+L+the+future+is+now.+
Biotechnol#J+2012;7:938–9.+
25++
Aldridge+BB,+Burke+JM,+Lauffenburger+DA,+et#al.+Physicochemical+modelling+of+cell+signalling+
pathways.+Nat#Cell#Biol+2006;8:1195–203.+
26++
Meng+TC,+Somani+S,+Dhar+P.+Modeling+and+simulation+of+biological+systems+with+stochasticity.+
In#Silico#Biol+2004;4:293–309.+
27++
Watterson+S,+Marshall+S,+Ghazal+P.+Logic+models+of+pathway+biology.+Drug#Discov.#Today.+
2008;13:447–56.+
28++
Watterson+S,+Ghazal+P.+Use+of+logic+theory+in+understanding+regulatory+pathway+signaling+in+
response+to+infection.+Future#Microbiol+2010;5:163–76.+
29++
Guerriero+ML,+Prandi+D,+Priami+C,+et#al.+Process+Calculi+Abstractions+for+Biology.+In:+
Algorithmic#Bioprocesses.+2009.+463–86.+
30++
Feret+J,+Danos+V,+Krivine+J,+et#al.+Internal+coarseLgraining+of+molecular+systems.+Proc#Natl#Acad#
Sci#U#S#A+2009;106:6453–8.+
31++
Pedersen+M,+Plotkin+G.+A+language+for+biochemical+systems.+In:+Lecture#Notes#in#Computer#
Science#(including#subseries#Lecture#Notes#in#Artificial#Intelligence#and#Lecture#Notes#in#
Bioinformatics).+2008.+63–82.+
32++
Kwiatkowska+MZ,+Heath+JK.+Biological+pathways+as+communicating+computer+systems.+J#Cell#
Sci+2009;122:2793–800.+


## Page 20


33++
Vert+JP.+Reconstruction+of+Biological+Networks+by+Supervised+Machine+Learning+Approaches.+
In:+Elements#of#Computational#Systems#Biology.+2010.+165–88.+
34++
Grzegorczyk+M,+Husmeier+D,+Edwards+KD,+et#al.+Modelling+nonLstationary+gene+regulatory+
processes+with+a+nonLhomogeneous+Bayesian+network+and+the+allocation+sampler.+
Bioinformatics+2008;24:2071–8.+
35++
Lewis+NE,+Schramm+G,+Bordbar+A,+et#al.+LargeLscale+in+silico+modeling+of+metabolic+
interactions+between+cell+types+in+the+human+brain.+Nat#Biotechnol+2010;28:1279–85.+
36++
Ajmera+I,+Swat+M,+Laibe+C,+et#al.+The+impact+of+mathematical+modeling+on+the+understanding+
of+diabetes+and+related+complications.+CPT#Pharmacometrics#Syst#Pharmacol+2013;2:e54.+
37++
Faratian+D,+Goltsov+A,+Lebedeva+G,+et#al.+Systems+biology+reveals+new+strategies+for+
personalizing+cancer+medicine+and+confirms+the+role+of+PTEN+in+resistance+to+trastuzumab.+
Cancer#Res+2009;69:6713–20.+
38++
Nelson+DE,+Ihekwaba+AE,+Elliott+M,+et#al.+Oscillations+in+NFLkappaB+signaling+control+the+
dynamics+of+gene+expression.+Science+2004;306:704–8.+
39++
Raza+S,+McDerment+N,+Lacaze+PA,+et#al.+Construction+of+a+large+scale+integrated+map+of+
macrophage+pathogen+recognition+and+effector+systems.+BMC#Syst#Biol+2010;4:63.+
40++
Thiele+I,+Swainston+N,+Fleming+RM,+et#al.+A+communityLdriven+global+reconstruction+of+human+
metabolism.+Nat#Biotechnol+2013;31:419–25.+
41++
Mitchell+S,+Mendes+P.+A+computational+model+of+liver+iron+metabolism.+PLoS#Comput#Biol+
2013;9:e1003299.+
42++
Karr+JR,+Sanghvi+JC,+Macklin+DN,+et#al.+A+wholeLcell+computational+model+predicts+phenotype+
from+genotype.+Cell+2012;150:389–401.+
43++
Hucka+M,+Finney+A,+Sauro+HM,+et#al.+The+systems+biology+markup+language+(SBML):+a+medium+
for+representation+and+exchange+of+biochemical+network+models.+Bioinformatics+
2003;19:524–31.+
44++
Finney+A,+Hucka+M.+Systems+biology+markup+language:+Level+2+and+beyond.+Biochem#Soc#
Trans+2003;31:1472–3.+
45++
Cuellar+AA,+Lloyd+CM,+Nielsen+PF,+et#al.+An+overview+of+CellML+1.1,+a+biological+model+
description+language.+Simulation4Transactions#Soc#Model#Simul#Int+2003;79:740–7.+
46++
Le+Novere+N,+Hucka+M,+Mi+H,+et#al.+The+Systems+Biology+Graphical+Notation.+Nat#Biotechnol+
2009;27:735–41.+
47++
Van+Iersel+MP,+Villéger+AC,+Czauderna+T,+et#al.+Software+support+for+SBGN+maps:+SBGNLML+
and+LibSBGN.+Bioinformatics+2012;28:2016–21.+
48++
Le+Novère+N,+Finney+A,+Hucka+M,+et#al.+Minimum+information+requested+in+the+annotation+of+
biochemical+models+(MIRIAM).+Nat#Biotechnol+2005;23:1509–15.+


## Page 21


49++
Waltemath+D,+Adams+R,+Beard+DA,+et#al.+Minimum+information+about+a+simulation+
experiment+(MIASE).+PLoS#Comput#Biol+2011;7.+
50++
Le+Novere+N,+Bornstein+B,+Broicher+A,+et#al.+BioModels+Database:+a+free,+centralized+database+
of+curated,+published,+quantitative+kinetic+models+of+biochemical+and+cellular+systems.+
Nucleic#Acids#Res+2006;34:D689–91.+
51++
Bhattacharya+BS,+Sweby+PK,+Minihane+AM,+et#al.+A+mathematical+model+of+the+sterol+
regulatory+element+binding+protein+2+cholesterol+biosynthesis+pathway.+J#Theor#Biol+
2014;349:150–62.+
52++
Mazein+A,+Watterson+S,+Hsieh+WY,+et#al.+A+comprehensive+machineLreadable+view+of+the+
mammalian+cholesterol+biosynthesis+pathway.+Biochem#Pharmacol+2013;86:56–66.+
53++
Watterson+S,+Guerriero+ML,+Blanc+M,+et#al.+A+model+of+flux+regulation+in+the+cholesterol+
biosynthesis+pathway:+Immune+mediated+graduated+flux+reduction+versus+statinLlike+led+
stepped+flux+reduction.+Biochimie+2013;95:613–21.+
54++
Lu+H,+Talbot+S,+Robertson+KA,+et#al.+Rapid+proteasomal+elimination+of+3LhydroxyL3L
methylglutarylLCoA+reductase+by+interferonLgamma+in+primary+macrophages+requires+
endogenous+25Lhydroxycholesterol+synthesis.+Steroids+Published+Online+First:+2015.+
55++
Mc+Auley+MT,+Wilkinson+DJ,+Jones+JJ,+et#al.+A+wholeLbody+mathematical+model+of+cholesterol+
metabolism+and+its+ageLassociated+dysregulation.+BMC#Syst#Biol+2012;6:130.+
56++
Mc+Auley+MT,+Mooney+KM.+Computationally+Modeling+Lipid+Metabolism+and+Aging:+A+MiniL
review.+Comput#Struct#Biotechnol#J+2015;13:38–46.+
57++
Douglas+G,+Channon+KM.+The+pathogenesis+of+atherosclerosis.+Medicine#(Baltimore)+
2014;42:480–4.+
58++
Lusis+AJ.+Atherosclerosis.+Nature+2000;407:233–41.+
59++
Alexander+RW.+Hypertension+and+the+Pathogenesis+of+Atherosclerosis :+Oxidative+Stress+and+
the+Mediation+of+Arterial+Inflammatory+Response:+A+New+Perspective.+Hypertension.+
1995;25:155–61.+
60++
Powell+JT.+Vascular+damage+from+smoking:+disease+mechanisms+at+the+arterial+wall.+Vasc#Med+
1998;3:21–8.+
61++
Harrison+D,+Griendling+KK,+Landmesser+U,+et#al.+Role+of+oxidative+stress+in+atherosclerosis.+Am#
J#Cardiol+2003;91:7A+–+11A.+
62++
Goriely+A,+Vandiver+R.+On+the+mechanical+stability+of+growing+arteries.+IMA#J#Appl#Math#
(Institute#Math#Its#Appl+2010;75:549–70.+
63++
Nabel+EG,+Ganz+P,+Gordon+JB,+et#al.+Dilation+of+normal+and+constriction+of+atherosclerotic+
coronary+arteries+caused+by+the+cold+pressor+test.+Circulation+1988;77:43–52.+
64++
Li+ZY,+Howarth+SPS,+Tang+T,+et#al.+How+critical+is+fibrous+cap+thickness+to+carotid+plaque+
stability?+A+flowLplaque+interaction+model.+Stroke+2006;37:1195–9.+


## Page 22


65++
Resnick+N,+Yahav+H,+ShayLSalit+A.+Fluid+shear+stress+and+the+vascular+endothelium:+for+better+
and+for+worse.+Prog#Biophys#Mol#Biol+2003;81:177–99.+
66++
Stroud+JS,+Berger+SA,+Saloner+D.+Numerical+analysis+of+flow+through+a+severely+stenotic+carotid+
artery+bifurcation.+J#Biomech#Eng+2002;124:9–20.+
67++
Tomaso+G+Di,+DiazLZuccarini+V,+PichardoLAlmarza+C.+A+Multiscale+Model+of+Atherosclerotic+
Plaque+Formation+at+Its+Early+Stage.+IEEE#Trans#Biomed#Eng+2011;58:3460–3.+
68++
Cilla+M,+Peña+E,+Martínez+MA.+Mathematical+modelling+of+atheroma+plaque+formation+and+
development+in+coronary+arteries.+J#R#Soc#Interface+2014;11:20130866.+
69++
Ethier+CR.+Computational+modeling+of+mass+transfer+and+links+to+atherosclerosis.+Ann#Biomed#
Eng+2002;30:461–71.+
70++
Filipovic+N,+Kojic+M.+Computer+simulations+of+blood+flow+with+mass+transport+through+the+
carotid+artery+bifurcation.+Theor#Appl#Mech+2004;31:1–33.+
71++
Filipovic+N,+Meunier+N,+Fotiadis+D,+et#al.+ThreeLdimensional+Numerical+Simulation+of+Plaque+
Formation+in+the+Arteries.+Computational#Surgery#and#Dual#Training.+2014;257L264+
72++
Johnston+BM,+Johnston+PR,+Corney+S,+et#al.+NonLNewtonian+blood+flow+in+human+right+
coronary+arteries:+Transient+simulations.+J#Biomech+2006;39:1116–28.+
73++
Liu+B,+Tang+D.+Computer+Simulations+of+Atherosclerotic+Plaque+Growth+in+Coronary+Arteries.+
Mol#Cell#Biomech+2010;7:193–202.+
74++
Olgac+U,+Kurtcuoglu+V,+Poulikakos+D.+Computational+modeling+of+coupled+bloodLwall+mass+
transport+of+LDL:+effects+of+local+wall+shear+stress.+Am#J#Physiol#Heart#Circ#Physiol+
2008;294:H909–19.+
75++
Rappitsch+G,+Perktold+K,+Pernkopf+E.+Numerical+Modelling+of+ShearLDependent+Mass+Transfer+
in+Large+Arteries. International#Journal#for#Numerical#Methods#in#Fluids+1997;857:847–57.+
76++
Sun+N,+Wood+NB,+Hughes+AD,+et#al.+FluidLwall+modelling+of+mass+transfer+in+an+axisymmetric+
Stenosis:+Effects+of+shearLdependent+transport+properties.+Ann#Biomed#Eng+2006;34:1119–28.+
77++
Ai+L,+Vafai+K.+A+coupling+model+for+macromolecule+transport+in+a+stenosed+arterial+wall.+Int#J#
Heat#Mass#Transf+2006;49:1568–91.+
78++
Wada+S,+Koujiya+M,+Karino+T.+Theoretical+study+of+the+effect+of+local+flow+disturbances+on+the+
concentration+of+lowLdensity+lipoproteins+at+the+luminal+surface+of+endLtoLend+anastomosed+
vessels.+Med#Biol#Eng#Comput+2002;40:576–87.+
79++
Wang+HH.+Analytical+models+of+atherosclerosis.+Atherosclerosis+2001;159:1–7.+
80++
Calvez+V,+Ebde+A.+Mathematical+modelling+of+the+atherosclerotic+plaque+formation.+ESAIM#
Proc+2010;:1–16.+
81++
Vincent+Calvez++Nicolas+Meunier,+Annie+Raoult+and+Gabriela+Rusnakova+JGH.+Mathematical+
and+numerical+modelling+of+early+atherosclerotic+lesions.+ESAIM#Proc+2010;30:1–14.+


## Page 23


82++
Quarteroni+A,+Veneziani+A,+Zunino+P.+Mathematical+and+Numerical+Modeling+of+Solute+
Dynamics+in+Blood+Flow+and+Arterial+Walls.+SIAM+J.+Numer.#Anal.+2002;39:1488–511.+
83++
Bosnić+Z,+Vračar+P,+Radovi+MD,+et#al.+Mining+data+from+hemodynamic+simulations+for+
generating+prediction+and+explanation+models.+IEEE#Trans#Inf#Technol#Biomed+2012;16:248–
54.+
84++
Bulelzai+MA,+Dubbeldam+JL.+Long+time+evolution+of+atherosclerotic+plaques.+J#Theor#Biol+
2012;297:1–10.+
85++
Gabriel+SA,+Ding+Y,+Feng+Y,+et#al.+DepositionLdriven+Growth+in+Atherosclerosis+Modelling.+19th+
Australasian#Fluid#Mechanics#Conference.+2014;:2–5.+
86++
Silva+T,+Sequeira+A,+Santos+RF,+et#al.+Mathematical+Modeling+of+Atherosclerotic+Plaque+
Formation+Coupled+with+a+NonLNewtonian+Model+of+Blood+Flow.+Conf#Pap#Med+2013;2013:1–
14.+
87++
Gessaghi+VC,+Raschi+MA,+Tanoni+DY,+et#al.+Growth+model+for+cholesterol+accumulation+in+the+
wall+of+a+simplified+3D+geometry+of+the+carotid+bifurcation.+Comput#Methods#Appl#Mech#Eng+
2011;200:2117–25.+
88++
Green+J,+Waters+S,+Cummings+L,+et#al.+Atherosclerotic+plaque+rupture.+UK#MMSG#Nottingham#
2002.+Published+Online+First:+2002.+http://www.mathsLinLmedicine.org/uk/2002/plaqueL
rupture/report.pdf+(3+August+2015,+date+last+accessed)+
89++
Deepa+TK,+Binu+LS,+Sukesh+AK.+Modelling+Blood+Flow+and+Analysis+of+Atherosclerotic+Plaque+
Rupture+under+GLForce.+2009#3rd#Int#Conf#Bioinforma#Biomed#Eng+2009;:1–4.+
90++
Girke+S,+Klofkorn+R,+Ohlberger+M.+Efficient+Parallel+Simulation+of+Atherosclerotic+Plaque+
Formation+Using+Higher+Order+Discontinuous+Galerkin+Schemes.+Finite#Vol.#Complex#Appl.#VII4
Elliptic,#Parabol.#Hyperbolic#Probl.+2014;:Volume+78,+pp+617–25.+
91++
McKay+C,+McDee+S,+Mottram+N,+et#al.+Towards+a+Model+of+Atherosclerosis.+Univ#Strat+
2005;:1–29.+
92++
Calvez+V,+Ebde+A,+Meunier+N,+et#al.+Mathematical+modelling+of+the+atherosclerotic+plaque+
formation.+ESAIM#Proc+2010;30:1–14.+
93++
Ibragimov+AI,+McNeal+CJ,+Ritter+LR,+et#al.+A+mathematical+model+of+atherogenesis+as+an+
inflammatory+response.+Math#Med#Biol+2005;22:305–33.+
94++
Cobbold+CA,+Sherratt+JA,+Maxwell+SR.+Lipoprotein+oxidation+and+its+significance+for+
atherosclerosis:+a+mathematical+approach.+Bull#Math#Biol+2002;64:65–95.+
95++
Prosi+M,+Zunino+P,+Perktold+K,+et#al.+Mathematical+and+numerical+models+for+transfer+of+lowL
density+lipoproteins+through+the+arterial+walls:+a+new+methodology+for+the+model+set+up+with+
applications+to+the+study+of+disturbed+lumenal+flow.+J#Biomech+2005;38:903–17.+
96++
Friedman+A,+Hao+W.+A+Mathematical+Model+of+Atherosclerosis+with+Reverse+Cholesterol+
Transport+and+Associated+Risk+Factors.+Bull#Math#Biol+Published+Online+First:+2014.+


## Page 24


97++
Hao+W,+Friedman+A.+The+LDLLHDL+profile+determines+the+risk+of+atherosclerosis:+a+
mathematical+model.+PLoS#One+2014;9:e90497.+
98++
Filipovic+N,+Teng+Z,+Radovic+M,+et#al.+Computer+simulation+of+threeLdimensional+plaque+
formation+and+progression+in+the+carotid+artery.+Med#Biol#Eng#Comput+2013;51:607–16.+
99++
Filipovic+N,+Fotiadis+D,+Pelosi+W,+et#al.+Experimental+and+computer+model+of+plaque+formation+
in+the+artery.+10th#Int#Work#Biomed#Eng#BioEng#2011+2011;:1–4.+
100++
Ougrinovskaia+A,+Thompson+RS,+Myerscough+MR.+An+ODE+model+of+early+stages+of+
atherosclerosis:+mechanisms+of+the+inflammatory+response.+Bull#Math#Biol+2010;72:1534–61.+
101++
Cohen+A,+Myerscough+MR,+Thompson+RS.+AtheroLprotective+effects+of+High+Density+
Lipoproteins+(HDL):+An+ODE+model+of+the+early+stages+of+atherosclerosis.+Bull#Math#Biol+
2014;76:1117–42.+
102++
Zohdi+TI,+Holzapfel+GA,+Berger+SA.+A+phenomenological+model+for+atherosclerotic+plaque+
growth+and+rupture.+J#Theor#Biol+2004;227:437–43.+
103++
Little+MP,+Gola+A,+Tzoulaki+I.+A+model+of+cardiovascular+disease+giving+a+plausible+mechanism+
for+the+effect+of+fractionated+lowLdose+ionizing+radiation+exposure.+PLoS#Comput#Biol+2009;5.+
104++
El+Khatib+N,+Génieys+S,+Volpert+V.+Atherosclerosis+Initiation+Modeled+as+an+Inflammatory+
Process.+Math#Model#Nat#Phenom+2007;2:126–41.+
105++
Zhang+S,+Ritter+LR,+Ibragimov+AI.+Foam+cell+formation+in+atherosclerosis:+HDL+and+macrophage+
reverse+cholesterol+transport.+Discret#Contin#Dyn#Syst#4#Ser#S+2013;:825–35.+
106++
Lichtman+AH,+Chin+J,+Schmidt+JA,+et#al.+Role+of+interleukin+1+in+the+activation+of+T+lymphocytes.+
Proc#Natl#Acad#Sci#U#S#A+1988;85:9699–703.+
107++
McLaren+JE,+Ramji+DP.+Interferon+gamma:+A+master+regulator+of+atherosclerosis.+Cytokine#
Growth#Factor#Rev.+2009;20:125–35.+
108++
Fok+PLW.+Mathematical+model+of+intimal+thickening+in+atherosclerosis:+vessel+stenosis+as+a+
free+boundary+problem.+J#Theor#Biol+2012;314:23–33.+
109++
Xue+C,+Friedman+A,+Sen+CK.+A+mathematical+model+of+ischemic+cutaneous+wounds.+Proc#Natl#
Acad#Sci#U#S#A+2009;106:16782–7.+
110++
Guy+RD,+Fogelson+AL,+Keener+JP.+Fibrin+gel+formation+in+a+shear+flow.+Math#Med#Biol+
2007;24:111–30.+
111++
Chelliah+V,+Juty+N,+Ajmera+I,+et#al.+BioModels:+tenLyear+anniversary.+Nucleic#Acids#Res+
2015;43:D542–8.+
112++
Li+C,+Donizelli+M,+Rodriguez+N,+et#al.+BioModels+Database:+An+enhanced,+curated+and+
annotated+resource+for+published+quantitative+kinetic+models.+BMC#Syst#Biol+2010;4:92.+
113++
Yu+T,+Lloyd+CM,+Nickerson+DP,+et#al.+The+Physiome+Model+Repository+2.+Bioinformatics+
2011;27:743–4.+


## Page 25


114++
Shaw+GM,+Chase+JG,+Starfinger+C,+et#al.+Modelling+the+cardiovascular+system.#Crit.#Care#
Resusc.+2007;9:264–9.+
115++
Bucher+J,+Riedmaier+S,+Schnabel+A,+et#al.+A+systems+biology+approach+to+dynamic+modeling+
and+interLsubject+variability+of+statin+pharmacokinetics+in+human+hepatocytes.+BMC#Syst#Biol+
2011;5:66.+
116++
Gotto+AM.+Triglyceride+as+a+risk+factor+for+coronary+artery+disease.+Am#J#Cardiol+1998;82:25.+
117++
Talayero+BG,+Sacks+FM.+The+role+of+triglycerides+in+atherosclerosis.+Curr#Cardiol#Rep+
2011;13:544–52.+
118++
Le+NA,+Walter+MF.+The+role+of+hypertriglyceridemia+in+atherosclerosis.+Curr.#Atheroscler.#Rep.+
2007;9:110–5.+
119++
Umaerus+M,+Rosengren+B,+Fagerberg+B,+et#al.+HDL2+interferes+with+LDL+association+with+
arterial+proteoglycans:+a+possible+atheroLprotective+effect.+Atherosclerosis+2012;225:115–20.+
120++
Umemoto+T,+Han+CY,+Mitra+P,+et#al.+Apolipoprotein+AI+and+highLdensity+lipoprotein+have+antiL
inflammatory+effects+on+adipocytes+via+cholesterol+transporters:+ATPLbinding+cassette+AL1,+
ATPLbinding+cassette+GL1,+and+scavenger+receptor+BL1.+Circ#Res+2013;112:1345–54.+
121++
Otvos+JD,+Mora+S,+Shalaurova+I,+et#al.+Clinical+implications+of+discordance+between+lowLdensity+
lipoprotein+cholesterol+and+particle+number.+J#Clin#Lipidol+2011;5:105–13.+
122++
Hartwig+H,+Silvestre+Roig+C,+Daemen+M,+et#al.+Neutrophils+in+atherosclerosis.+A+brief+overview.+
Hamostaseologie+2014;35.+
123++
Perry+HM,+Bender+TP,+McNamara+CA.+B+cell+subsets+in+atherosclerosis.+Front#Immunol+
2012;3:373.+
124++
Xu+Q,+Metzler+B,+Jahangiri+M,+et#al.+Molecular+chaperones+and+heat+shock+proteins+in+
atherosclerosis.+Am#J#Physiol#Hear#Circ#Physiol+2012;302:506–14.+
125++
Kilic+A,+Mandal+K.+Heat+shock+proteins:+pathogenic+role+in+atherosclerosis+and+potential+
therapeutic+implications.+Autoimmune#Dis+2012;2012:502813.+
126++
Xiao+H,+Lu+M,+Yang+T,+et#al.+SREBP2+Activation+of+NLRP3+Inflammasome+in+Endothelium+
Mediates+HemodynamicLInduced+Atherosclerosis+Susceptibility.+Circulation+2013;128:632–42.+
127++
NazariLJahantigh+M,+Egea+V,+Schober+A,+et#al.+MicroRNALspecific+regulatory+mechanisms+in+
atherosclerosis.+J#Mol#Cell#Cardiol+Published+Online+First:+2014.+
128++
Tatonetti+NP,+Liu+T,+Altman+RB.+Predicting+drug+sideLeffects+by+chemical+systems+biology.+
Genome#Biol+2009;10:238.+
129++
Wang+K,+Sun+J,+Zhou+S,+et#al.+Prediction+of+DrugLTarget+Interactions+for+Drug+Repositioning+
Only+Based+on+Genomic+Expression+Similarity.+PLoS#Comput#Biol+2013;9.+


## Page 26


130++
Yang+L,+Wang+K,+Chen+J,+et#al.+Exploring+offLtargets+and+offLsystems+for+adverse+drug+reactions+
via+chemicalLprotein+interactome+L+clozapineLinduced+agranulocytosis+as+a+case+study.+PLoS#
Comput#Biol+2011;7.+
131++
Sun+X,+Vilar+S,+Tatonetti+NP.+HighLthroughput+methods+for+combinatorial+drug+discovery.+Sci#
Transl#Med+2013;5:205rv1.+
132++
Eussen+SR,+Rompelberg+CJ,+Klungel+OH,+et#al.+Modelling+approach+to+simulate+reductions+in+
LDL+cholesterol+levels+after+combined+intake+of+statins+and+phytosterols/Lstanols+in+humans.+
Lipids#Health#Dis+2011;10:187.+
133++
Chua+HN,+Roth+FP.+Discovering+the+targets+of+drugs+via+computational+systems+biology.+J#Biol#
Chem+2011;286:23653–8.+
134++
Holzapfel+GA,+Gasser+TC,+Ogden+RW.+A+new+constitutive+framework+for+arterial+wall+
mechanics+and+a+comperative+study+of+material+models.+J#Elast+2000;61:1–48.+
135++
Eftaxiopoulos+DA,+Atkinson+C.+A+nonlinear,+anisotropic+and+axisymmetric+model+for+balloon+
angioplasty.+Proc#R#Soc#A#Math#Phys#Eng#Sci+2005;461:1097–128.+
136++
Schunkert+H,+König+IR,+Kathiresan+S,+et#al.+LargeLscale+association+analysis+identifies+13+new+
susceptibility+loci+for+coronary+artery+disease.+Nat#Genet+2011;43:333–8.+
137++
Getz+GS,+Reardon+CA.+Animal+models+of+Atherosclerosis.+Arterioscler.+Thromb.+Vasc.+Biol.+
2012;32:1104–15.+
138++
Verhoeven+BA,+De+Vries+JP,+Pasterkamp+G,+et#al.+Carotid+atherosclerotic+plaque+characteristics+
are+associated+with+microembolization+during+carotid+endarterectomy+and+procedural+
outcome.+Stroke+2005;36:1735–40.+
139++
Yang+M,+Chesterman+CN,+Chong+BH.+Recombinant+PDGF+enhances+megakaryocytopoiesis+in+
vitro.+Br#J#Haematol+1995;91:285–9.+
140++
Rollins+BJ,+Walz+A,+Baggiolini+M.+Recombinant+human+MCPL1/JE+induces+chemotaxis,+calcium+
flux,+and+the+respiratory+burst+in+human+monocytes.+Blood+1991;78:1112–6.+
141++
Santoli+D,+Yang+YC,+Clark+SC,+et#al.+Synergistic+and+antagonistic+effects+of+recombinant+human+
interleukin+(IL)+3,+ILL1+alpha,+granulocyte+and+macrophage+colonyLstimulating+factors+(GLCSF+
and+MLCSF)+on+the+growth+of+GMLCSFLdependent+leukemic+cell+lines.+J#Immunol+
1987;139:3348–54.+
142++
SchulzeLBauer+CAJ,+Mörth+C,+Holzapfel+GA.+Passive+biaxial+mechanical+response+of+aged+
human+iliac+arteries.+J#Biomech#Eng+2003;125:395–406.+
143++
Ahmed+SA,+Giddens+DP.+Velocity+measurements+in+steady+flow+through+axisymmetric+
stenoses+at+moderate+Reynolds+numbers.+J#Biomech+1983;16:505–16.+
144++
Meyer+G,+Merval+R,+Tedgui+A.+Effects+of+pressureLinduced+stretch+and+convection+on+lowL
density+lipoprotein+and+albumin+uptake+in+the+rabbit+aortic+wall.+Circ#Res+1996;79:532–40.+


## Page 27


145++
Boussel+L,+Arora+S,+Rapp+J,+et#al.+Atherosclerotic+plaque+progression+in+carotid+arteries:+
monitoring+with+highLspatialLresolution+MR+imagingLLmulticenter+trial.+Radiology+
2009;252:789–96.+
146++
Kirpalani+A,+Park+H,+Butany+J,+et#al.+Velocity+and+wall+shear+stress+patterns+in+the+human+right+
coronary+artery.+J#Biomech#Eng+1999;121:370–5.+
147++
Myers+JG,+Moore+JA,+Ojha+M,+et#al.+Factors+influencing+blood+flow+patterns+in+the+human+right+
coronary+artery.+Ann#Biomed#Eng+2001;29:109–20.+
148++
Huang+Y,+Rumschitzki+D,+Chien+S,+et#al.+A+fiber+matrix+model+for+the+filtration+through+
fenestral+pores+in+a+compressible+arterial+intima.+Am#J#Physiol+1997;272:H2023–39.+
149++
Yuan+F,+Chien+S,+Weinbaum+S.+A+new+view+of+convectiveLdiffusive+transport+processes+in+the+
arterial+intima.+J#Biomech#Eng+1991;113:314–29.+
150++
Friedman+MH,+Ehrlich+LW.+Effect+of+spatial+variations+in+shear+on+diffusion+at+the+wall+of+an+
arterial+branch.+Circ#Res+1975;37:446–54.+
151++
Ishibashi+H,+Sunamura+M,+Karino+T.+Flow+patterns+and+preferred+sites+of+intimal+thickening+in+
endLtoLend+anastomosed+vessels.+Surgery+1995;117:409–20.+
152++
BuduLGrajdeanu+P,+Schugart+RC,+Friedman+A,+et#al.+A+mathematical+model+of+venous+
neointimal+hyperplasia+formation.+Theor#Biol#Med#Model+2008;5:2.+
153++
Hecht+F.+New+development+in+freefem+.+J#Numer#Math+2012;20:251–65.+
154++
Cheng+C,+Van+Haperen+R,+De+Waard+M,+et#al.+Shear+stress+affects+the+intracellular+distribution+
of+eNOS:+Direct+demonstration+by+a+novel+in+vivo+technique.+Blood+2005;106:3691–8.+
155++
Cheng+C,+Tempel+D,+Van+Haperen+R,+et#al.+Atherosclerotic+lesion+size+and+vulnerability+are+
determined+by+patterns+of+fluid+shear+stress.+Circulation+2006;113:2744–53.+
156++
Dhooge+A,+Govaerts+W,+Kuznetsov+YA.+MATCONT:+A+MATLAB+package+for+numerical+
bifurcation+analysis+of+ODEs.+ACM#Trans#Math#Softw+2003;29:141–64.+
157++
Chen+J,+Lu+XY.+Numerical+investigation+of+the+nonLNewtonian+blood+flow+in+a+bifurcation+
model+with+a+nonLplanar+branch.+J#Biomech+2004;37:1899–911.+
158++
Yang+N,+Vafai+K.+Modeling+of+lowLdensity+lipoprotein+(LDL)+transport+in+the+arteryLeffects+of+
hypertension.+Int#J#Heat#Mass#Transf+2006;49:850–67.+
159++
Weller+HG,+Tabor+G.+A+tensorial+approach+to+computational+continuum+mechanics+using+
objectLoriented+techniques.+Comput#Phys+1998;12:620–31.+
160++
Dedner+A,+Klöfkorn+R,+Nolte+M,+et#al.+A+generic+interface+for+parallel+and+adaptive+
discretization+schemes:+Abstraction+principles+and+the+DuneLFem+module.+Comput#
(Vienna/New#York)+2010;90:165–96.+


## Page 28


161++
Neužil+J,+Thomas+SR,+Stocker+R.+Requirement+for,+promotion,+or+inhibition+by+αLtocopherol+of+
radicalL+induced+initiation+of+plasma+lipoprotein+lipid+peroxidation.+Free#Radic#Biol#Med+
1996;22:57–71.+
162++
Lovren+F,+Pan+Y,+Quan+A,+et#al.+MicroRNAL145+targeted+therapy+reduces+atherosclerosis.+
Circulation+2012;126.+
163++
Feig+JE,+Rong+JX,+Shamir+R,+et#al.+HDL+promotes+rapid+atherosclerosis+regression+in+mice+and+
alters+inflammatory+properties+of+plaque+monocyteLderived+cells.+Proc#Natl#Acad#Sci#U#S#A+
2011;108:7166–71.+
164++
Schiopu+A,+Frendéus+B,+Jansson+B,+et#al.+Recombinant+Antibodies+to+an+Oxidized+LowLDensity+
Lipoprotein+Epitope+Induce+Rapid+Regression+of+Atherosclerosis+in+ApobecL1L/L/LowLDensity+
Lipoprotein+ReceptorL/L+Mice.+J#Am#Coll#Cardiol+2007;50:2313–8.+
165++
Cushing+SD,+Berliner+JA,+Valente+AJ,+et#al.+Minimally+modified+low+density+lipoprotein+induces+
monocyte+chemotactic+protein+1+in+human+endothelial+cells+and+smooth+muscle+cells.+Proc#
Natl#Acad#Sci#U#S#A+1990;87:5134–8.+
166++
Shi+Q,+Vandeberg+JF,+Jett+C,+et#al.+Arterial+endothelial+dysfunction+in+baboons+fed+a+highL
cholesterol,+highLfat+diet.+Am#J#Clin#Nutr+2005;82:751–9.+
167++
Stadius+ML,+Rowan+R,+Fleischhauer+JF,+et#al.+Time+course+and+cellular+characteristics+of+the+
iliac+artery+response+to+acute+balloon+injury.+An+angiographic,+morphometric,+and+
immunocytochemical+analysis+in+the+cholesterolLfed+New+Zealand+white+rabbit.+Arterioscler#
Thromb+1992;12:1267–73.+
168++
Roy+S,+Biswas+S,+Khanna+S,+et#al.+Characterization+of+a+preclinical+model+of+chronic+ischemic+
wound.+Physiol#Genomics+2009;37:211–24.++
 
+


## Page 29


Table&1&
A"summary"of"the"mathematical"models"of"atherosclerosis"referenced"within"this"review.""
These"models"are"reproducible"as"their"governing"equations"are"explained"in"the"cited"references."
First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
Goriely"[62]"
On"the"mechanical"
stability"of"growing"
arteries"
2010"
A"coronary"artery"
modelled"as"an"
incompressible"2D
layer"cylindrical"
structure"was"used"
to"study"the"
arterial"response"to"
stress"
Related"to"
experimental"data"
Compared"to"
experimental"data"
obtained"by"
SchulzeDBauer"et"al."
[142]"
None"mentioned"
Li"[64]"
How"critical"is"
fibrous"cap"
thickness"to"carotid"
plaque"stability?"A"
flowDplaque"
interaction"model"
2006"
A"model"of"a"
stenotic"carotid"
artery"was"used"to"
relate"fibrous"cap"
thickness"to"WSS"
Use"a"combination"
of"estimated"and"
experimentally"
validated"
parameters"
"
The"authors"claim"
that"the"model"fits"
well"within"the"
current"literature,"
however"no"
references"are"
given"to"
substantiate"this"
claim"
FEMLAB"was"used"
for"model"
construction,"SPSS"
was"used"to"
analyse"this"model"
Stroud"[66]"
Numerical"analysis"
of"flow"through"a"
severly"stenotic"
carotid"artery"
bifurcation"
2002"
A"model"of"a"
carotid"artery"
bifurcation"is"used"
to"study"pulsatile"
and"steady"blood"
flow"
Related"to"
experimental"data"
Compared"to"
experimental"data"
obtained"by"Ahmed"
and"Giddens"[143]"
None"mentioned"
Quarteroni"[82]"
Mathematical"and"
numerical"
2002"
Proposed"two"
models"of"an"
Parameter"source"
unclear"
None"
None"mentioned"


## Page 30


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
modeling"of"solute"
dynamics"in"blood"
flow"and"arterial"
walls"
arterial"bifurcation"
to"study"mass"
transfer"
"
"
Di"Tomaso"[67]""
A"Multiscale"Model"
of"Atherosclerotic"
Plaque"
Formation"at"Its"
Early"Stage"
2011"
Built"a"multiDscale"
model"of"
atherosclerosis"to"
include"mass"
transfer,"LDL"
oxidation"and"foam"
cell"formation"
Use"a"combination"
of"estimated"and"
experimentally"
validated"
parameters"
"
The"model"was"
compared"with"
experimental"data"
taken"from"Meyer"
et#al.#[144]"and"
against"the"model"
produced"by"Olgac"
et#al.#[74]"
None"mentioned"
Cilla"[68]"
Mathematical"
modelling"of"
atheroma"plaque"
formation"and"
development"in"
coronary"arteries"
2013"
Uses"a"standard"left"
descending"
coronary"artery"
model"to"study"
plaque"growth"
Taken"from"
experimental"data"
and"other"
mathematical"
models"
Parts"of"the"model"
correspond"with"
experimental"data"
such"as"Meyer"et#
al.#[144],#however"
appropriate"
experimental"data"
to"cover"the"entire"
model"is"not"
currently"available."
COMSOL"
Multiphysics"
Filipovic"[70]"
Computer"
simulations"of"
blood"flow"with"
mass"transport"
through"the"carotid"
artery"bifurcation"
2004"
Proposed"a"
simulation"of"mass"
transport"to"allow"
physicians"to"study"
individual"patients"
Parameter"source"
unclear"
The"authors"claim"
that"the"model"fits"
well"within"the"
current"literature,"
however"no"
references"are"
given"to"
substantiate"this"
claim"
None"mentioned"


## Page 31


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
Filipovic"[71]""
ARTreat"Project:"
ThreeDDimensional"
Numerical"
Simulation"of"
Plaque"Formation"
and"Development"
in"the"Arteries"
2012"
Presented"a"3D"
model"of"plaque"
formation"and"
development"
Parameters"were"
experimentally"
established"
through"a"rabbit"
animal"model"
Plaque"progression"
within"the"model"
has"been"validated"
against"
experimental"data"
taken"from"Boussel"
et#al.#[145]"
None"mentioned"
Johnston"[72]"
NonDNewtonian"
blood"flow"in"
human"right"
coronary"arteries:"
Transient"
simulations"
2005"
Used"right"coronary"
artery"models"to"
study"pulsatile"
blood"flow"
Experimentally"
observed"
Findings"were"
validated"against"
experimental"data"
taken"from"
Kirpalani"et#al."
[146]"&"Myers"et#
al.#[147]"
CFDDACE"
Liu"[73]"
Computer"
Simulations"of"
Atherosclerotic"
Plaque"Growth"in"
Coronary"Arteries"
2010"
Uses"model"of"a"
stenosisDfree"
curved"human"
coronary"artery"to"
study"plaque"
growth"
Experimentally"
observed"
None"
COMSOL"
Multiphysics"
Olgac"[74]"
Computational"
modeling"of"
coupled"bloodDwall"
mass"transport"of"
LDL:"effects"of"local"
wall"shear"stress"
2008"
Developed"a"model"
of"a"stenosed"
coronary"artery"to"
study"the"effects"of"
WSS"on"mass"
transport"
Experimentally"
observed"
Related"to"
experimental"data"
Meyer"et#al."[144],"
Huang"et#al."[148],"
Yuan"et#al."[149]"
COMSOL"
Multiphysics"
Rappitsch"[75]"
Numerical"
Modelling"of"ShearD
Dependent"Mass"
Transfer"in"Large"
Arteries"
1997"
Used"a"curvedD
tubeDartery"model"
to"study"blood"flow"
and"lipoprotein"
transport"processes"
Use"a"combination"
of"estimated"and"
experimentally"
validated"
parameters"
"
Validated"against"
Friedman"et#al."
[150]"
None"mentioned"


## Page 32


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
"
"
"
Sun"[76]"
FluidDwall"
modelling"of"mass"
transfer"in"an"
axisymmetric"
Stenosis:"Effects"of"
shearDdependent"
transport"
properties"
2006"
Studies"the"
influence"of"WSS"
on"mass"transport"
Use"a"combination"
of"estimated"and"
experimentally"
validated"
parameters"
Compared"to"
experimental"data"
taken"from"rabbit"
aortic"walls"Meyer"
et#al."[144]"
None"mentioned"
Ai"[77]"
A"coupling"model"
for"macromolecule"
transport"in"a"
stenosed"arterial"
wall"
2006"
A"model"of"a"
stenosed"artery"is"
used"to"study"lipid"
transfer"
Experimentally"
validated"
Compared"to"other"
mathematical"
models,"with"
arguments"as"to"
why"their"
parameter"set"is"
more"accurate"
FIDAP"
Wada"[78]"
Theoretical"study"
of"the"effect"of"
local"flow"
disturbances"on"the"
concentration"of"
lowDdensity"
lipoproteins"at"the"
luminal"surface"of"
endDtoDend"
anastomosed"
vessels."
2002"
Femoral"artery"
model"is"used"to"
study"the"
relationship"
between"intimal"
thickness"and"the"
endothelial"surface"
level"of"LDL"
Parameters"were"
taken"from"
experimental"data"
or"estimated"
Compared"to"
experimental"data"
taken"from"
Ishibashi"et#al.#
[151]"
Star"LT""
Calvez"[80]"
Mathematical"
modelling"of"the"
atherosclerotic"
2009"
Developed"a"2D"
geometry"
modelling"the"
Parameters"are"
taken"from"other"
mathematical"
None"
FreeFem++"[153]"


## Page 33


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
plaque"formation."
carotid"artery"to"
demonstrate"
plaque"formation,"
based"on"the"
model"of"El"Khatib"
et#al.#[104]"
"
models,"relating"to"
atherosclerosis"
[104]"and"
hyperplasia"[152]"
Calvez"[81]"
Mathematical"and"
numerical"
modelling"of"early"
atherosclerotic"
lesions"
2010"
Expanded"on"their"
previous"model"
[80]"to"include"a"
model"of"lesion"
growth"
Parameters"were"
taken"from"
experimental"data"
or"estimated"
Experiments"
published"by"Cheng"
et#al.#[154,"155]#
were"reproduced"
and"were"used"to"
validate"the"model"
FreeFem++"[153]"
Bosnić"[83]"
Mining"data"from"
hemodynamic"
simulations"for"
generating"
prediction"and"
explanation"
models."
2012"
Built"a"prototype"of"
a"system"that"could"
predict"locations"of"
increased"WSS"
from"artery"models"
Parameter"source"
unclear"
Presents"a"series"of"
methods"to"
estimate"accuracy"
of"the"model,"and"
relates"these"to"
experimental"data"
None"mentioned"
Bulelzai"[84]"
Long"time"
evolution"of"
atherosclerotic"
plaques"
2011"
Present"a"series"of"
ODEs"for"the"
concentrations"of"
particular"elements"
of"atheromae.""
Taken"from"
experimental"data"
and"other"
mathematical"
models"[91]"
Compared"to"
mathematical"
model"of"Zohdi"et#
al.#[102]"
MATCONT"[156]"
Gabriel"[85]"
DepositionDdriven"
Growth"in"
Atherosclerosis"
Modelling."
2014"
A"simplified"
bifurcating"artery"is"
used"to"model"LDL"
flux"into"the"intima"
Taken"from"
experimental"data"
None"
ANSYS"Fluent"
Silva"[86]"
Mathematical"
Modeling"of"
Atherosclerotic"
2013"
Built"a"2D"carotid"
artery"bifurcation"
to"study"plaque"
Taken"from"other"
mathematical"
models"[157]"
None"
COMSOL"
Multiphysics"


## Page 34


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
Plaque"Formation"
Coupled"with"a"
NonDNewtonian"
Model"of"blood"
Flow"
formation"with"a"
nonDNewtonian"
model"of"blood"
flow"
Gessaghi"[87]"
Growth"model"for"
cholesterol"
accumulation"in"
the"wall"of"a"
simplified"3D"
geometry"of"the"
carotid"bifurcation"
2011"
A"3D"model"of"a"
carotid"artery"
bifurcation"is"used"
to"study"the"influx,"
efflux,"oxidation"
and"phagocytosis"
of"LDL"
Taken"from"
experimental"data"
Compared"with"
data"obtained"from"
Yang"et#al.[158].#
However,"authors"
comment"that"not"
enough"
experimental"data"
exists"to"fully"
validate"the"model."
OpenFOAM"[159],"
Netgen""
Green"[88]"
Atherosclerotic"
plaque"rupture"
2002"
A"model"of"a"
straight,"stenotic"
2D"artery"is"used"to"
study"
atherosclerotic"
plaque"rupture."
Parameter"source"
unclear"
None"
AUTO"
Deepa"[89]"
Modelling"Blood"
Flow"and"Analysis"
of"Atherosclerotic"
Plaque"Rupture"
under"GDForce"
2009"
A"1D"arterial"model"
was"used"to"study"
the"rupture"of"
plaques"under"gD
force"
Sources"have"not"
been"cited"for"
parameter"values"
None"
MATLAB"
Girke"[90]"
Efficient"Parallel"
Simulation"of"
Atherosclerotic"
Plaque"Formation"
Using"Higher"Order"
Discontinuous"
Galerkin"Schemes"
2014"
Girke"et#al.#built"a"
mathematical"
model"based"on"
the"works"of"
Ibragimov"et#al."
[93]"and"Calvez"et#
al.#[81]#to"
Taken"from"
experimental"data"
None"
DUNEDFEM"[160]"


## Page 35


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
demonstrate"the"
use"of"the"compact"
discontinuous"
galerkin"method"
(CDG2)"in"
discretizing"
relevant"equations"
McKay"[91]"
Towards"a"Model"
of"Atherosclerosis"
2005"
Proposed"a"
mathematical"
model"to"cover"
mass"transfer,"
oxidation,"immune"
cell"activation"and"
plaque"growth"
Taken"from"other"
mathematical"
models,"or"
estimated"by"
domain"experts"
None"
None"mentioned"
Ibragimov"[93]"
A"mathematical"
model"of"
atherogenesis"as"an"
inflammatory"
response"
2005"
Created"a"series"of"
ODEs"to"study"the"
concentrations"of"
cell"groups"over"
time"
Primarily"estimated"
due"to"lack"of"
relevant"data"
None"
FEMLAB"
Cobbold"[94]"
Lipoprotein"
Oxidation"and"its"
Significance"for"
Atherosclerosis:"a"
Mathematical"
Approach"
2002"
Built"a"series"of"
ODEs"to"study"
lipoprotein"
oxidation"
Taken"from"
experimental"data"
Compared"to"an"
experiment"
performed"by"
Neužil"et#al.#[161]"
None"mentioned"
Prosi"[95]"
Mathematical"and"
numerical"models"
for"transfer"of"low"
density"
lipoproteins"
through"the"arterial"
walls:"a"new"
2004"
Built"multiple"
models"of"
lipoprotein"transfer"
in"order"to"
maximse"the"
accuracy"of"their"
prediction"
Taken"from"
experimental"data"
Experimentally"
validated"against"
Meyer"et#al.#[144]"
None"mentioned"


## Page 36


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
methodology"for"
the"model"set"up"
with"applications"to"
the"study"of"
disturbed"lumenal"
flow"
Friedman"[96]"
A"Mathematical"
Model"of"
Atherosclerosis"
with"Reverse"
Cholesterol"
Transport"and"
Associated"Risk"
Factors"
2014"
Expands"on"the"
previous"model"by"
the"same"group"
[97]"to"include"
reverse"cholesterol"
transport"
Taken"from"
experimental"data"
and"from"other"
mathematical"
models"[97]"
Validated"
qualitatively"
against"
experimental"data"
(e.g."[162–164])"
None"mentioned"
Hao"[97]"
The"LDLDHDL"profile"
determines"the"risk"
of"atherosclerosis:"
a"mathematical"
model"
2014"
Developed"a"series"
of"PDEs"to"model"
the"concentration"
of"a"series"of"cells"
and"
macromolecules"
contained"within"
an"atheroma,"and"
related"this"
information"to"
plaque"growth"
Taken"from"
experimental"data"
or"estimated"
None"
MATLAB"
Filipovic"[99]"
Experimental"and"
computer"model"of"
plaque"formation"
in"the"artery"
2011"
Built"a"model"of"
plaque"formation"
based"on"a"pig"left"
anterior"
descending"
coronary"artery"
Taken"from"
experimental"data,"
or"estimated"where"
data"was"
unavailable."
Reproduced"an"
experiment"by"
Cheng"et#al."[155]"
and"compared"the"
results"to"their"
model"of"plaque"
formation"
None"explained"


## Page 37


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
Ougrinovskaia"
[100]"
An"ODE"model"of"
early"stages"of"
atherosclerosis:"
mechanisms"of"the"
inflammatory"
response"
2010"
Developed"a"series"
of"ODEs"to"model"
mass"transfer"and"
foam"cell"formation"
Estimated"
Behaviour"relates"
to"qualitative"data,"
but"model"has"not"
been"compared"to"
quantitative"data"
MATLAB,"XPPAUTO"
Cohen"[101]"
AtheroDprotective"
effects"of"High"
Density"
Lipoproteins"(HDL):"
An"ODE"model"of"
the"early"stages"of"
atherosclerosis"
2014"
Expanded"on"their"
previous"model"
[100]"to"include"
HDL"and"reverse"
cholesterol"
transport"
Taken"from"
experimental"data"
Noted"that"the"
behaviour"of"their"
model"corresponds"
with"an"experiment"
performed"by"Feig"
et#al.#[163]"
None"mentioned"
Zohdi"[102]"
A"
phenomenological"
model"for"
atherosclerotic"
plaque"growth"and"
rupture"
2004"
Built"a"series"of"
equations"to"study"
plaque"growth"and"
lesion"rupture"
Taken"from"
experimental"data,"
or"estimated"where"
data"was"
unavailable."
None"
None"mentioned"
Little"[103]"
A"model"of"
cardiovascular"
disease"giving"a"
plausible"
mechanism"for"the"
effect"of"
fractionated"lowD
dose"ionizing"
radiation"exposure"
2009"
Built"a"series"of"
equations"to"study"
the"effect"of"small"
radiation"doses"to"
atherosclerosis"and"
CVD"
Taken"from"
experimental"data"
Sections"of"this"
model"are"
validated"by"
matching"with"
experimental"data"
published"by"
Cushing"et#al."[165]"
and"Shi"et#al.#[166]"
None"mentioned"
El"Khatib"[104]"
Atherosclerosis"
Initiation"Modeled"
as"an"Inflammatory"
Process"
2007"
Built"a"series"of"
reactionDdiffusion"
equations"by"
grouping"together"
Estimated"
None"
COMSOL"
Multiphysics"


## Page 38


First"Author"
Title"
Year"
Form"
Parameters"
Validation"
Tools"
all"cytokines"and"
immune"cells"
involved"
Zhang"[105]"
Foam"cell"
formation"in"
atherosclerosis:"
HDL"and"
macrophage"
reverse"cholesterol"
transport"
2013"
Expanded"on"the"
model"of"Ibragimov"
et#al.#[93]#by"
focusing"on"the"
role"of"HDL"and"
reverse"cholesterol"
transport"
Taken"from"
experimental"data"
and"from"other"
mathematical"
models"[94]"
None"
None"mentioned"
Fok"[108]"
Mathematical"
model"of"intimal"
thickening"in"
atherosclerosis:"
vessel"stenosis"as"a"
free"boundary"
problem"
2012"
Focuses"on"SMC"
migration"and"the"
role"of"PDGF"
Taken"from"
experimental"data"
Compared"to"
experimental"data"
taken"from"New"
Zealand"white"
rabbits"Stadius"et#
al."[167]"
None"mentioned"
Xue"[109]"
A"mathematical"
model"of"ischemic"
cutaneous"wounds"
2009"
Xue"et#al.#
developed"a"series"
of"PDEs"to"model"
ischemic"dermal"
wounds"
A"combination"of"
experimentally"
validated"and"
estimated"
parameters"are"
used"
Compared"to"
experimental"data"
established"by"Roy"
et#al.#[168]"
Livermore"Solver"
Guy"[110]"
Fibrin"gel"formation"
in"a"shear"flow"
2007"
Presents"a"model"
of"fibrin"formation"
in"a"damaged"blood"
vessel"
A"combination"of"
experimentally"
validated"and"
estimated"
parameters"are"
used"
None"
None"mentioned"


## Page 39


Figure"
1:"
The"
pathophysiology"of"atherosclerosis.""Low"density"lipoproteins"(LDL)"transfer"into"the"artery"wall"at"a"site"of"endothelial"damage."Arterial"wall"
shear"stress"(WSS)"and"its"relationship"to"lipoprotein"transfer"into"the"artery"wall"has"been"studied"by"Liu"et#al."Lipoproteins"pass"into"the"
artery"wall"at"a"rate"dependent"on"WSS,"lipoprotein"diffusivity"and"lipoprotein"concentration,"as"modeled"by"Sun"et#al."After"entering"the"
intima,"lipoproteins"become"oxidized"upon"contact"with"free"oxygen"radicals,"a"process"that"has"been"modeled"by"Cobbold"et#al."Monocytes"
are"recruited"to"the"site"of"inflammation"via"MCPD1"(modeled"by"Cilla"et#al.)"and"pass"into"the"intima"before"differentiating"into"macrophages"
(Bulelzai" et# al.)," catalyzed" by" TDCell" produced" IFNDγ" (Hao" et# al.)." Macrophages" phagocytose" oxidized" LDL" within" the" artery" wall," forming"
cholesterolDladen"foam"cells"(Zhang"et#al.)."Foam"cells"secrete"MCPD1,"which"recruits"more"monocytes"to"the"lesion,"and"PDGF,"which"recruits"
smooth"muscle"cells"(SMCs)"into"the"intima"(Fok"et#al.)."
Smooth muscle cell
PDGF
MCP-1
Monocyte
MCP-1
IFN-γ
T cell
LUMEN
TUNICA
INTIMA
SMC proliferation
Fok et al. (2012)
T cell concentration
Hao et al. (2012)
Monocyte differentiation
Bulelzai et al. (2011)
Arterial wall shear stress
Liu et al. (2010)
Monocyte recruitment
Cilla et al. (2013)
LDL
LDL
LDL
LDL
LDL transfer into tunica intima
Sun et al. (2006)
LDL
O
O O
O
Foam cell
Macrophage
Foam cell formation
Zhang et al. (2013)
oxLDL
HDL
oxHDL
Lipoprotein oxidation
Cobbold et al. (2002)
HDL and RTC
Cohen et al. (2014)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1510_01888v1_computational_modelling_of_atherosclerosis
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2015/1510_01888V1_COMPUTATIONAL_MODELLING_OF_ATHEROSCLEROSIS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
