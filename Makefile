# MASTER MAKEFILE

START_DATE?=197601
END_DATE?=202009

export START_DATE END_DATE

all:
	#$(MAKE) -C cpsb-check-availability/src
	$(MAKE) -C cpsb-extract/src
	$(MAKE) -C cps-merge/src
	$(MAKE) -C short-unemp/src
	$(MAKE) -C flow-seasonal-adjustment/src
	$(MAKE) -C three-states/src
	$(MAKE) -C plot/src

clean:
	$(MAKE) -C cpsb-extract/src clean
	$(MAKE) -C cps-merge/src clean
	$(MAKE) -C short-unemp/src clean
	$(MAKE) -C flow-seasonal-adjustment/src clean
	$(MAKE) -C three-states/src clean
	$(MAKE) -C plot/src clean
