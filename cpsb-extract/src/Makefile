# Define SUBSTR
EMPTY:=
SPACE:=$(EMPTY) $(EMPTY)
SEP = $(subst 1,1 ,$(subst 2,2 ,$(subst 3,3 ,$(subst 4,4 ,$(subst 5,5 ,$(subst 6,6 ,$(subst 7,7 ,$(subst 8,8 ,$(subst 9,9 ,$(subst 0,0 , $(1) ))))))))))
SUBSTR = $(strip $(subst $(SPACE),,$(wordlist $(1), $(2), $(call SEP, $(3)))))

# Define MONTH_CONVERTER
MONTH_CONVERTER = $(strip $(subst 01,jan,$(subst 02,feb,$(subst 03,mar,$(subst 04,apr,$(subst 05,may,$(subst 06,jun,$(subst 07,jul,$(subst 08,aug,$(subst 09,sep,$(subst 10,oct,$(subst 11,nov,$(subst 12,dec,$(1))))))))))))))

# Define INV_MONTH_CONVERTER
INV_MONTH_CONVERTER = $(strip $(subst jan,01,$(subst feb,02,$(subst mar,03,$(subst apr,04,$(subst may,05,$(subst jun,06,$(subst 07,jul,$(subst 08,aug,$(subst 09,sep,$(subst 10,oct,$(subst 11,nov,$(subst 12,dec,$(1))))))))))))))

FOLDER=../input ../output 
START_DATE?=197601
END_DATE?=202009
START_YEAR:= $(call SUBSTR,1,4,$(START_DATE))
START_MONTH:= $(call SUBSTR,5,6,$(START_DATE))
END_YEAR:= $(call SUBSTR,1,4,$(END_DATE))
END_MONTH:= $(call SUBSTR,5,6,$(END_DATE))
MONTHS_NUM=01 02 03 04 05 06 07 08 09 10 11 12
YEARA_NUM=$(shell seq $(START_YEAR) $(END_YEAR))
ALL_DATES1=$(foreach year, $(YEARA_NUM), $(foreach month, $(MONTHS_NUM), $(year)$(month)))
ALL_DATES2=$(shell seq $(START_DATE) $(END_DATE))
ALL_DATES=$(filter $(ALL_DATES1), $(ALL_DATES2))
ALL_DATES_2DIG_YEAR=$(foreach date, $(ALL_DATES), $(call SUBSTR, 3,4,$(date)))
ALL_DATES_2DIG_MONTH=$(foreach date, $(ALL_DATES), $(call MONTH_CONVERTER, $(call SUBSTR, 5,6,$(date))))
ALL_DATES_IN_FILENAMES=$(join $(ALL_DATES_2DIG_MONTH),$(ALL_DATES_2DIG_YEAR))
OUTPUT= $(foreach date, $(ALL_DATES), ../output/cps$(date).csv)

all: set_sources $(OUTPUT)

set_sources:
	$(eval SOURCE:= $(shell bash -c 'read -p "Which source do you want to download Basic Monthly CPS data from? [1] nber.org [2] census.gov [3] mixed:" source; echo $$source'))


$(FOLDER):
	mkdir $@

../input/cpsb%.raw: | ../input
	$(eval YEAR = $(call SUBSTR, 1,4,$*))
	$(eval FILENAME_STEM = $(call MONTH_CONVERTER, $(call SUBSTR, 5,6,$*))$(call SUBSTR, 3,4,$*))
ifeq ($(SOURCE),1)
	@wget -c https://data.nber.org/cps-basic2/raw/cpsb$*.raw -P ../input
else ifeq ($(SOURCE),2)
	@if [ $* -lt 199400 ] ; then echo "Census.gov does not support data downloading for files prior to Janurary 1994! Please try downloading from another source." && exit 1; fi
	wget -c https://www2.census.gov/programs-surveys/cps/datasets/$(YEAR)/basic/$(FILENAME_STEM)pub.zip -P ../input
	unzip -p ../input/$(FILENAME_STEM)pub.zip > $@ && rm ../input/$(FILENAME_STEM)pub.zip
else 
	@if [ $* -gt 199400 ] ; then \
		wget -c https://www2.census.gov/programs-surveys/cps/datasets/$(YEAR)/basic/$(FILENAME_STEM)pub.zip -P ../input ; \
		unzip -p ../input/$(FILENAME_STEM)pub.zip > $@ && rm ../input/$(FILENAME_STEM)pub.zip ; \
	else \
		wget -c https://data.nber.org/cps-basic2/raw/cpsb$*.raw -P ../input ; \
	fi
endif

../output/cps%.csv: match_extract.py ../input/cpsb%.raw | ../output
	python $< $*

clean:
	rm -f *.log
	rm -rf $(FOLDER)
