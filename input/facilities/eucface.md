title: EucFace
long: 150.72446
lat:  -33.6132
typeOf: @facility
full_name: Eucalyptus woodland free-air CO2 enrichment (EucFACE) facility
code: FACE
Description: The Eucalyptus woodland free-air CO2 enrichment (EucFACE) facility is the only one of its kind in the southern hemisphere, and provides unparalleled access for intensive study of canopy and soil processes and native biodiversity in a mature Eucalyptus woodland. EucFACE’s infrastructure is located in native Eucalyptus woodland of the Cumberland Plain in the western part of the Sydney basin. EucFACE was established in 2010 following recommendation to the Commonwealth to understand how rising atmospheric CO2 concentration and CO2 fertilisation affects tree canopy processes and soil and ecosystem function in an Australian native woodland. The experiment is located in the drier and warmer part of the Sydney basin, receiving 800mm rainfall per annum with periodic droughts.
Previous FACE experiments in Australia include OzFACE in Yabulu, Qld and TasFACE in Hobart, Tasmania. However, these previous experiments were conducted with short-stature, herbaceous vegetation whereas the current effort focuses on mature native Australian woodland vegetation. Native woodlands of the Cumberland Plain once covered more than 30% of the Sydney basin but remnants of the Cumberland Plain woodland are now threatened by weed invasion, Sydney's urban sprawl and climate change. The experiment aims to understand C sequestration above and below ground under rising atmospheric CO2 concentrations and under Australian conditions with dynamic changes in water availability within and amongst years.

---





#Data organisation overview

Each of the six 'rings' within eucFACE collects data streaming off automated logger stations (meteorological data, radiative data etc) being generated on different time frequencies. This data may be uploaded into HIEv on a ring per ring basis or in certain scenarios as a single site-wide dataset (see below). In addition to automated facility data, scientific 'projects' operating within eucFACE also collect data on a per project basis. Data relating to that project is marked as so within HIEv. The file naming convention for eucFACE captures this distinction.



#File Naming Convention

Convention: FACE_&lt;PROJECT>_&lt;RING>_&lt;VARIABLE COLLECTION CODE>_&lt;DATA PROCESSING>_&lt;DATE or DATERANGE>[_&lt;VERSION>].&lt;filetype>

(all terms in the filename should be upper case apart from the file ending which should be lower case)

FACE: Official HIE facility code to represent data sourced from the eucFACE facility (all data from the eucFACE facility will be prefixed by use of the code 'FACE'). See all official HIE facility codes here.
&lt;PROJECT>: Which of the official EucFACE projects this data file is associated with. The project code should be used in the filename (capitalized P followed by a 4 digit project number, e.g. P0003, P0012, etc). Details about different projects taking part at eucFACE can be found here. In the event that the data is from automated facility, 'AUTO' can be used for the project code
&lt;RING>: Which ring(s) data has been sourced from. This can include data sourced from a single EucFACE ring, from all rings, or from a subset of rings. It also allows the file to refer to FACE data collected on a non-ring site. Rules on how to label each are in the Ring section below.
&lt;VARIABLE COLLECTION CODE>: A collection code that represents a particular grouping of variables contained within a file. A list of variables contained within different variable collection codes can be found below.
&lt;DATE or DATERANGE>: The date range which a dataset covers (for automated timeseries data for example) or the single date on which a sample, for example, was taken. Note that dates are in the YYYYMMDD format (with a hyphen used to split the start and end date of a date range). Note that in the case of facility data a 'data chunking' date may be used marking on which date the 'chunking' of this file ended/will end (see explanation).
&lt;DATA PROCESSING>: The level of post-processing operated on the data. The definitions of the different levels of post-processing can be found below.
&lt;VERSION>: An optional version number of the form _Vx. This can be utilized when a new version of a file already existing within HIEv has been updated/corrected (maintaining the same data processing level).
&lt;filetype>: The format of the data file. Further information about different file types can be found on the data formats page, found here.

#Examples: 
FACE_AUTO_R3_FLUX_R_20130630.dat - Automated facility data from Ring 3 within the EUCFace facility in the 'chunking' period up to 30th June 2013 and covering variables included in the 'FLUX' category of variables.
FACE_P0005_R346_RAD_L1_20130527.dat - 'RAD' data for the 27th May 2013, created as part of project P0005 within the eucFACE facility, and sourced from rings 3, 4 and 6. The data has been subjected to level one cleaning and processing.
FACE_P0005_R346_RAD_L1_20130527_V2.dat - Corrected version of the above file (due to an error in the cleaning script).

#Ring

'Ring' specifies which of the 6 EucFACE rings have been a source location for the current data file. Data sourced from...
a single ring will use Rx (where x is a single digit from 1 to 6), e.g. R1 for ring 1, R2 for ring 2, etc.
all rings will use RA. 
a subset of rings will use R followed by an ordered list of rings, up to a maximum of 5 rings (when all 6 rings are used 'RA' should be used). So for example:
R12 contains data sourced from rings 1 and 2.
R346 contains data sourced from rings 3, 4 and 6.
R23456 contains data sourced from all rings apart from ring 1.
a EucFACE sampling location outside of the 6 rings will use R0 (R followed by a zero). A description  of the actual sampling location should be added in the metadata in this scenario.

#Variable Collection Codes

Variable collection codes are used to group together a collection of linked variables. Further information about each collection code, and how to request the addition of a new collection code, can be found on the EucFACE collections code page.

Data Processing Codes

The meanings of the different data processing codes used in eucFACE are as follows: 

R   -  Raw Data.               Data that has been directly extracted from an instrument and that has not been subjected to any data cleaning or post-processing
L1 -   Level One Data.      Data that has been cleaned and processed, but in a cursory manner. Some erroneous data may be included.
L2 -   Level Two Data.      Data that has been rigorously cleaned, processed, and checked for quality control. 
L3 -   Level Three Data.    Archive of published datasets. 


For additonal help in uploading eucFACE-related data into HIEv, please see the guidance page
Facility PC data

Initial raw data loaded into HIEv may differ in name from that stored at the facility. The naming convention used by technicians has particular meaning that helps in the management of data at the facility technical level. This naming convention however does not lend itself well to data discovery/management from a general data user perspective. Therefore instead of attempting to force both cases to use the same naming convention, filenames may be converted to the HIEv naming convention before ingestion. A mapping of the original 'technical' name to the HIEv name is kept here, and should the need arise, will allow HIEv data to be traced back to the facility PC. 

#Facility Status History

Details of the operating status of the eucFACE facility including shutdown periods etc can be found here.
