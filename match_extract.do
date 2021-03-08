if `1' <= 199505 {
    clear
    infix gestfips 93-94 double hrhhid 1-12 str hrsersuf 75-76 line 147-148 mis 63-64 age 122-123 race 139-140 sex 129-130 status 180-181 str dur 407-409 double fweight 613-622 double lweight 593-602 llind 69-70 educ 137-138 mar 125-126 str ind 436-438 str occu 439-441 using `1'.raw
    generate z=real(hrsersuf)
    replace z=0 if hrsersuf=="-1"
    replace z=1 if hrsersuf=="A"
    replace z=2 if hrsersuf=="B"
    replace z=3 if hrsersuf=="C"
    replace z=4 if hrsersuf=="D"
    replace z=5 if hrsersuf=="E"
    replace z=6 if hrsersuf=="F"
    replace z=7 if hrsersuf=="G"
    replace z=8 if hrsersuf=="H"
    replace z=9 if hrsersuf=="I"
    replace z=10 if hrsersuf=="J"
    replace z=11 if hrsersuf=="K"
    replace z=12 if hrsersuf=="L"
    replace z=13 if hrsersuf=="M"
    replace z=14 if hrsersuf=="N"
    replace z=15 if hrsersuf=="O"
    replace z=16 if hrsersuf=="P"
    replace z=17 if hrsersuf=="Q"
    replace z=18 if hrsersuf=="R"
    replace z=19 if hrsersuf=="S"
    replace z=20 if hrsersuf=="T"
    replace z=21 if hrsersuf=="U"
    replace z=22 if hrsersuf=="V"
    replace z=23 if hrsersuf=="W"
    replace z=24 if hrsersuf=="X"
    replace z=26 if hrsersuf=="Y"
    replace z=25 if hrsersuf=="Z"
    generate double hh=gestfips*100000000000000+hrhhid*100+z
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
    drop hrhhid gestfips hrsersuf
}

if `1' <= 200212 & `1' > 199505 {
    infix double hrhhid 1-15 str hrsersuf 75-76 line 147-148 mis 63-64 age 122-123 race 139-140 sex 129-130 status 180-181 str dur 407-409 double fweight 613-622 double lweight 593-602 llind 69-70 educ 137-138 mar 125-126 str ind 436-438 str occu 439-441 using `1'.raw
    generate z=real(hrsersuf)
    replace z=0 if hrsersuf=="-1"
    replace z=1 if hrsersuf=="A"
    replace z=2 if hrsersuf=="B"
    replace z=3 if hrsersuf=="C"
    replace z=4 if hrsersuf=="D"
    replace z=5 if hrsersuf=="E"
    replace z=6 if hrsersuf=="F"
    replace z=7 if hrsersuf=="G"
    replace z=8 if hrsersuf=="H"
    replace z=9 if hrsersuf=="I"
    replace z=10 if hrsersuf=="J"
    replace z=11 if hrsersuf=="K"
    replace z=12 if hrsersuf=="L"
    replace z=13 if hrsersuf=="M"
    replace z=14 if hrsersuf=="N"
    replace z=15 if hrsersuf=="O"
    replace z=16 if hrsersuf=="P"
    replace z=17 if hrsersuf=="Q"
    replace z=18 if hrsersuf=="R"
    replace z=19 if hrsersuf=="S"
    replace z=20 if hrsersuf=="T"
    replace z=21 if hrsersuf=="U"
    replace z=22 if hrsersuf=="V"
    replace z=23 if hrsersuf=="W"
    replace z=24 if hrsersuf=="X"
    replace z=26 if hrsersuf=="Y"
    replace z=25 if hrsersuf=="Z"
    generate double hh=hrhhid*100+z
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
    drop hrhhid hrsersuf
}

if `1' > 200212 {
    infix double hrhhid 1-15 str hrsersuf 75-76 line 147-148 mis 63-64 age 122-123 race 139-140 sex 129-130 status 180-181 str dur 407-409 double fweight 613-622 double lweight 593-602 llind 69-70 educ 137-138 mar 125-126 str ind 856-859 str occu 860-863 using `1'.raw
    generate z=real(hrsersuf)
    replace z=0 if hrsersuf=="-1"
    replace z=1 if hrsersuf=="A"
    replace z=2 if hrsersuf=="B"
    replace z=3 if hrsersuf=="C"
    replace z=4 if hrsersuf=="D"
    replace z=5 if hrsersuf=="E"
    replace z=6 if hrsersuf=="F"
    replace z=7 if hrsersuf=="G"
    replace z=8 if hrsersuf=="H"
    replace z=9 if hrsersuf=="I"
    replace z=10 if hrsersuf=="J"
    replace z=11 if hrsersuf=="K"
    replace z=12 if hrsersuf=="L"
    replace z=13 if hrsersuf=="M"
    replace z=14 if hrsersuf=="N"
    replace z=15 if hrsersuf=="O"
    replace z=16 if hrsersuf=="P"
    replace z=17 if hrsersuf=="Q"
    replace z=18 if hrsersuf=="R"
    replace z=19 if hrsersuf=="S"
    replace z=20 if hrsersuf=="T"
    replace z=21 if hrsersuf=="U"
    replace z=22 if hrsersuf=="V"
    replace z=23 if hrsersuf=="W"
    replace z=24 if hrsersuf=="X"
    replace z=26 if hrsersuf=="Y"
    replace z=25 if hrsersuf=="Z"
    generate double hh=hrhhid*100+z
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
    drop hrhhid hrsersuf
}

compress
save cps`1'.dta