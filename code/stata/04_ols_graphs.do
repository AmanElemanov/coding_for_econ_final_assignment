*Import data
use "data/derived/immunization.dta", clear

*Is the standard of living positively correlated with immunization rate?
reg imm lngdppc
//Yes, countries that have 1% higher GDP per capita tend to have approximately 0.06 percentage points higher immunization rate among children, other things being equal.

reg imm lngdppc lnpop imm_above_mean

*Plotting the variables and saving graphs
hist gdppc
graph export gdppc.png, replace
hist lngdppc
graph export lngdppc.png, replace
hist imm
graph export imm.png, replace

save "data/derived/immunization.dta", replace
