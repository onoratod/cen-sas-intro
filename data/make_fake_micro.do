// Create fake data


global out "/Users/danny_onorato/Documents/SASUniversityEdition/myfolders"

clear
set obs 200

gen pik = _n 

gen rand = runiform()
sort rand
gen mom_pik = _n

drop rand
gen rand = runiform()
sort rand
gen dad_pik = _n
drop rand

tostring pik mom_pik dad_pik, format("%03.0f") replace

gen rand = runiform()
replace mom_pik = "" if rand < 0.6
drop rand

gen rand = runiform()
replace dad_pik = "" if rand < 0.6 & ~missing(mom_pik)
drop rand

gen kid_married_2015 = runiform() > 0.3

foreach par in mom dad {
	gen `par'_inc_2000 = rnormal(25000, 10000)
	
	gen rand = runiform()
	replace `par'_inc_2000 = . if rand < 0.1
	drop rand
}



export delimited using "${out}/fake_micro.txt", delim(tab) replace quote

