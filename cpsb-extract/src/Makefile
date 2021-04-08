FOLDER=../input ../output 
START_DATE?=197601
END_DATE?=202009
START_YEAR:= $(shell echo $(START_DATE) | cut -c 1-4)
START_MONTH:= $(shell echo $(START_DATE) | cut -c 5-6)
END_YEAR:= $(shell echo $(END_DATE) | cut -c 1-4)
END_MONTH:= $(shell echo $(END_DATE) | cut -c 5-6)
MONTHS_NUM=01 02 03 04 05 06 07 08 09 10 11 12
YEARA_NUM=$(shell seq $(START_YEAR) $(END_YEAR))
ALL_DATES1=$(foreach year, $(YEARA_NUM), $(foreach month, $(MONTHS_NUM), $(year)$(month)))
ALL_DATES2=$(shell seq $(START_DATE) $(END_DATE))
ALL_DATES=$(filter $(ALL_DATES1), $(ALL_DATES2))
OUTPUT= $(foreach date, $(ALL_DATES), ../output/cps$(date).dta)

all: $(OUTPUT)

$(FOLDER):
	mkdir $@

../input/cpsb%.raw: | ../input
	wget https://data.nber.org/cps-basic2/raw/cpsb$*.raw -P ../input

../output/cps%.dta: match_extract.do ../input/cpsb%.raw | ../output
	stata-se -e $< $*

../output/short_ts.dta: empty_short_ts.do | ../output
	stata-se -e $<

