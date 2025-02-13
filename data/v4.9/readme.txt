Miguel Hilario (hilario@arizona.edu)
Armin Sorooshian (armin@arizona.edu)
The University of Arizona

v4: Retrieval now reads OPC data directly from DASH_SAMP_PARAM_RESAMP files (RESAMP made by Cassidy Soloff)
	- 4.9: 
		- Decreased initial guess of wet Dp in retrieve_GF to 2*dry Dp (formerly 2.5*dry Dp in v4.8) to test sensitivity of GF on initial guess.
	- 4.8:
		- Increased initial guess of wet Dp in retrieve_GF to 2.5*dry Dp (dp_wet_guess = dp_dry*2.5) to avoid wet and dry fractions being stuck at initial conditions.
	- 4.7: 
		- Increased SEMS Dp resolution of calibration surface to improve GF retrievals at SEMS Dp < 200 nm.
		- Enforced minimum (0) and maximum (1) for wet and dry fractions in GF retrieval.
		- Made wet Dp guess increment smaller in GF retrieval (dp_wet_guess += dp_wet_diff/(2*(j+1))).
	- 4.6: Implemented linear weighting on OPC Dps in GF retrieval to improve peak finding. 
		- 20250211: I think v4.5 (exponential weighting) is better. So disregard this version.
	- 4.5: Updated GF retrieval to use exponentially-weighted percentiles instead of single OPC peak. This should help with GF bifurcation.
	- 4.4: Increased smoothing on calibration surface, increased HO hi_dp_mask (from 1.2 to 1.3). Additional QA on which scans are part of the calibration surfaces.
	- 4.3: Updated calibration surfaces with higher resolution and additional QA (removed bad scans).
	- 4.2: Adjusted HOPC hi_dp_mask from 1.5 to 1.2 to exclude doubly charged peaks from peak finding.
	- 4.1: Adjusted HOPC hi_dp_mask from 2 to 1.5 to exclude doubly charged peaks from peak finding.
	- 4.0: retrieval now reads OPC data from RESAMP file
v3: Assorted improvements in retrieval
	- 3.8: Reduced guess increment more than in v3.7 to improve stability of retrieve_GF function. 
		- Set wet Dp guess increment to Dp_wet_diff/j where j is the iteration number so that increment becomes smaller over time.
	- 3.7: Changed guess increment in retrieve_GF function to reduce GF oscillation and improve chance of convergence. I'm hoping this will address the GF bifurcation issue.
	- 3.6: Cropped both HO and DO calibration surfaces to resolve lingering RI issues (1.3-1.4). Limts are DO RI = 1.39-2, HO RI = 1.30s-2.
	- 3.5: Updated mask_dist() to remove doubly-charged peaks in HOPC data.
	- 3.4: Updated mask_dist() so min_cnts applies only to SEMS_Dp  <= 450 nm. This is to preserve coarse mode retrieval
	- 3.3: Cropped calibration surface to remove unrealistic RI. Calibration surfaces now span RI = 1.33-2 (water, black carbon).
	- 3.2: Corrected handling of OPC data when SEMS Dp = 350 nm (mask_dist function in dash_functions.py). Done on 20250123.
	- 3.1: Added filter for minimum counts after masking OPC distributions for relevant size range. Note that mask Dp did not include Dp = 350 nm. This was corrected in v3.2.
	- 3.0
v2: Period-specific calibration surface used in retrieval
	- Early Spring: applied to flights between 240528-240605 using calibration data collected between 230922-240214.
	- Late Spring: applied to flights between 240606-240617 using calibration data collected between 240612-240614.
	- Summer: applied to flights between 240722-240815 using calibration data collected between 240723-240913.
v1: Retrieval used one calibration surface that included all calibration data collected between 230922-240913.