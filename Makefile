# MATER MAKEFILE

START_DATE?=197601
END_DATE?=202009

export START_DATE END_DATE

all:
	#$(MAKE) -C cpsb-check-availability/src
	$(MAKE) -C cpsb-extract/src
	$(MAKE) -C cps-merge/src
	$(MAKE) -C short-unemp/src
	$(MAKE) -C flow-seasonal-adjustment/src