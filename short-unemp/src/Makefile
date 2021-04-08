FOLDER= ../input ../output/
DATES= $(shell ls ../../cpsb-extract/output/*.dta | cut -c 30-35)
SHORT_UNEMP_BY_YEAR= $(foreach date, $(DATES), ../output/short_unemp_$(date).txt)

all: ../output/short_unemp_ts.txt

$(FOLDER):
	mkdir $@

../input/cps%.dta: | ../input
	ln -s ../../cpsb-extract/output/$(@F) $@

../output/short_unemp_%.txt: gen_shortemp.do ../input/cps%.dta | ../output
	stata-se -e $< $*

../output/short_unemp_ts.txt: $(SHORT_UNEMP_BY_YEAR) | ../output
	cat ../output/short_unemp_*.txt > $@

