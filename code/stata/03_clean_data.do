browse

*Keep only relevant variables
keep year countrycode countryname pop surv imm gdppc lngdppc
browse //Looks like gdppc and lngdppc are string variables because some countries have "NA" in the respective columns
count if gdppc == "NA" | lngdppc == "NA"

*Destring the variables
destring gdppc lngdppc, replace ignore("NA")
di missing(.)
count if missing(gdppc) | missing(lngdppc)

*Drop missing observations
drop if missing(gdppc) | missing(lngdppc)

*Summarize the variables
sum pop, detail
di `r(N)'
di `r(mean)'

sum surv, d
sum imm, d
sum gdppc, d

*Generate a new variable (indicator that immunization rate is above mean)
sum imm, d
gen imm_above_mean = 1
replace imm_above_mean = 0 if imm < `r(mean)'
tab imm_above_mean

*Create logged variables
gen lnpop = ln(pop)
sum lnpop, d
// surv and imm are in percentages, so no need to log them

*Save .dta file
mkdir data/derived/
save "data/derived/immunization.dta", replace
