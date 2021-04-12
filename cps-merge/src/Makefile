FOLDER= ../input ../output/
DATES= $(shell ls ../../cpsb-extract/output/*.dta | cut -c 30-35)
CPS_DTA_INPUTS=$(foreach date, $(DATES), ../input/cps$(date).dta)
FIRST_DATE=$(firstword $(DATES))
LAST_DATE=$(lastword $(DATES))
ALL_DATES_BUT_FIRST=$(filter-out $(FIRST_DATE),$(DATES))
ALL_DATES_BUT_LAST=$(filter-out $(LAST_DATE),$(DATES))
DATE_PAIR=$(join $(ALL_DATES_BUT_LAST), $(addprefix _, $(ALL_DATES_BUT_FIRST)))

FLOW_FILENAMES=$(foreach date_pair, $(DATE_PAIR), ../output/flow$(date_pair).txt)

all: ../output/flows.txt
.INTERMEDIATE: $(FLOW_FILENAMES)

$(FOLDER):
	mkdir $@

../input/cps%.dta: | ../input
	ln -s ../../cpsb-extract/output/$(@F) $@

../output/merg%.dta: match_merge.do $(CPS_DTA_INPUTS) | ../output
	stata-se -e $< $(subst _, ,$*)

../output/flow%.txt: match_flow.do ../output/merg%.dta | ../output
	stata-se -e $^ $(subst _, ,$*)

../output/flows.txt: $(FLOW_FILENAMES) | ../output
	cat ../output/flow*.txt > $@

clean:
	rm *.log
	rm -r $(FOLDER)