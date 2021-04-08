START_DATE?=197601
END_DATE?=202012
START_YEAR:= $(shell echo $(START_DATE) | cut -c 1-4)
START_MONTH:= $(shell echo $(START_DATE) | cut -c 5-6)
END_YEAR:= $(shell echo $(END_DATE) | cut -c 1-4)
END_MONTH:= $(shell echo $(END_DATE) | cut -c 5-6)
MONTHS_NUM=01 02 03 04 05 06 07 08 09 10 11 12
YEARA_NUM=$(shell seq $(START_YEAR) $(END_YEAR))
ALL_DATES1=$(foreach year, $(YEARA_NUM), $(foreach month, $(MONTHS_NUM), $(year)$(month)))
ALL_DATES2=$(shell seq $(START_DATE) $(END_DATE))
ALL_DATES=$(filter $(ALL_DATES1), $(ALL_DATES2))
CPSB_FILENAMES=$(foreach date, $(ALL_DATES), cpsb$(date))


all: $(CPSB_FILENAMES)
cpsb%:
	@if [ $(shell wget -q --spider https://data.nber.org/cps-basic2/raw/cpsb$*.raw; echo $$?) -eq 0 ]; then echo "cpsb file is checked available for date $*" ; else echo "cpsb file doesn't exist for date $*" && exit 1; fi 