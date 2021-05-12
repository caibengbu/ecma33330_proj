FOLDER= ../input ../output/
DATES= $(shell ls ../../cpsb-extract/output/*.csv 2> /dev/null | cut -c 30-35)
CPS_DTA_INPUTS=$(foreach date, $(DATES), ../input/cps$(date).csv)
FIRST_DATE=$(firstword $(DATES))
LAST_DATE=$(lastword $(DATES))
ALL_DATES_BUT_FIRST=$(filter-out $(FIRST_DATE),$(DATES))
ALL_DATES_BUT_LAST=$(filter-out $(LAST_DATE),$(DATES))
DATE_PAIR=$(join $(ALL_DATES_BUT_LAST), $(addprefix _, $(ALL_DATES_BUT_FIRST)))

FLOW_FILENAMES=$(foreach date_pair, $(DATE_PAIR), ../output/flow$(date_pair).txt)

all: ../output/flows.txt

$(FOLDER):
	mkdir $@

../input/cps%.csv: | ../input
	ln -s ../../cpsb-extract/output/$(@F) $@

../output/merg%.csv: match_merge.py $(CPS_DTA_INPUTS) | ../output
	python $< $(subst _, ,$*)

../output/flow%.txt: match_flow.py ../output/merg%.csv | ../output
	python $^ $(subst _, ,$*)

../output/flows.txt: $(FLOW_FILENAMES) | ../output
	cat ../output/flow*_*.txt > $@

clean:
	rm -f *.log
	rm -rf $(FOLDER)