local filename ../input/cpsb`1'.raw

if `1' <= 197712 {
    infix hh 4-8 hh1 9-12 hh2 25-26 line 94-95 mis 2 age 97-98 race 100 sex 101 status 109 str dur 66-67 double fweight 121-132 educ 103-104 grade 105 mar 99 str ind 88-90 str occu 91-93 using `filename'
    generate double hh3 = hh*1000000+hh1*100+hh2
    generate educ1 = educ-grade+1
    drop hh hh1 hh2 educ
    rename hh3 hh
    rename educ1 educ
    replace dur =" ." if dur =="--"
    replace ind ="." if ind =="---"
    replace occu ="." if occu =="---"
}

if `1' <= 198212 & `1' > 197712{
    infix double hh 4-15 line 94-95 mis 2 age 97-98 race 100 sex 101 status 109 str dur 66-67 double fweight 121-132 educ 103-104 grade 105 mar 99 str ind 88-90 str occu 91-93 using `filename'
    generate educ1 = educ-grade+1
    drop educ
    rename educ1 educ
    replace dur =" ." if dur =="--"
    replace ind ="." if ind =="---"
    replace occu ="." if occu =="---"
}

if `1' <= 198312 & `1' > 198212{
    infix  double hh 4-15 line 94-95 mis 2 age 97-98 race 100 sex 101 status 109 str dur 66-67 double fweight 121-132 educ 103-104 grade 105 mar 99 str ind 524-526 str occu 527-529 using `filename'
    generate educ1 = educ-grade+1
    drop educ
    rename educ1 educ
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
}

if `1' <= 198812 & `1' > 198312{
    infix double hh 4-15 line 541-542 mis 2 age 97-98 race 100 sex 101 status 109 str dur 66-67 double fweight 121-132 educ 103-104 grade 105 mar 99 str ind 524-526 str occu 527-529 using `filename'
    generate educ1 = educ-grade+1
    drop educ
    rename educ1 educ
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
}

if `1' <= 199112 & `1' > 198812{
    infix double hh 145-156 line 264-265 mis 70 age 270-271 race 280 sex 275 status 348 str dur 304-305 double fweight 398-405 double lweight 576-583 llind 584 educ 277-278 grade 279 mar 272 str ind 310-312 str occu 313-315 using `filename'
    generate educ1 = educ-grade+1
    drop educ
    rename educ1 educ
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
}

if `1' <= 199312 & `1' > 199112{
    infix double hh 145-156 line 264-265 mis 70 age 270-271 race 280 sex 275 status 348 str dur 304-305 double fweight 398-405 double lweight 576-583 llind 584 educ 277-278 mar 272 str ind 310-312 str occu 313-315 using `filename'
    replace dur="." if dur=="--"
    replace ind="." if ind=="---"
    replace occu="." if occu=="---"
}

if `1' <= 199505 & `1' > 199312{
    clear
    infix gestfips 93-94 double hrhhid 1-12 str hrsersuf 75-76 line 147-148 mis 63-64 age 122-123 race 139-140 sex 129-130 status 180-181 str dur 407-409 double fweight 613-622 double lweight 593-602 llind 69-70 educ 137-138 mar 125-126 str ind 436-438 str occu 439-441 using `filename'
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
    infix double hrhhid 1-15 str hrsersuf 75-76 line 147-148 mis 63-64 age 122-123 race 139-140 sex 129-130 status 180-181 str dur 407-409 double fweight 613-622 double lweight 593-602 llind 69-70 educ 137-138 mar 125-126 str ind 436-438 str occu 439-441 using `filename'
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
    infix double hrhhid 1-15 str hrsersuf 75-76 line 147-148 mis 63-64 age 122-123 race 139-140 sex 129-130 status 180-181 str dur 407-409 double fweight 613-622 double lweight 593-602 llind 69-70 educ 137-138 mar 125-126 str ind 856-859 str occu 860-863 using `filename'
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

*compress
save ../output/cps`1'.dta
