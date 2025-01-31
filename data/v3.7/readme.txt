v3: Added filter for minimum counts after masking OPC distributions for relevant size range
	- 3.7: Changed guess increment in retrieve_GF function to reduce GF oscillation and improve chance of convergence. I'm hoping this will address the GF bifurcation issue.
	- 3.6: Cropped both HO and DO calibration surfaces to resolve lingering RI issues (1.3-1.4). Limts are DO RI = 1.39-2, HO RI = 1.30s-2.
	- 3.5: Updated mask_dist() to remove doubly-charged peaks in HOPC data.
	- 3.4: Updated mask_dist() so min_cnts applies only to SEMS_Dp  <= 450 nm. This is to preserve coarse mode retrieval
	- 3.3: cropped calibration surface to remove unrealistic RI. Calibration surfaces now span RI = 1.33-2 (water, black carbon).
	- 3.2: corrected handling of OPC data when SEMS Dp = 350 nm (mask_dist function in dash_functions.py). Done 20250123.
	- 3.1: mask Dp did not include Dp = 350 nm. This was changed for 3.2.
v2: Period-specific calibration surface used in retrieval
	- Early Spring: applied to flights between 240528-240605 using calibration data collected between 230922-240214.
	- Late Spring: applied to flights between 240606-240617 using calibration data collected between 240612-240614.
	- Summer: applied to flights between 240722-240815 using calibration data collected between 240723-240913.
v1: Retrieval used one calibration surface that included all calibration data collected between 230922-240913.