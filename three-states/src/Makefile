FOLDER= ../input ../output
all: $(foreach direction, ei eu ie iu ue ui, ../output/$(direction)_M.dat)

$(FOLDER):
	mkdir $@

../output/%_M.dat: three-state-M.wls ../input/%.txt | ../output
	./$<

../input/%.txt: | ../input
	@if [ -e ../../flow-seasonal-adjustment/output/$(@F) ] ; then ln -s ../../flow-seasonal-adjustment/output/$(@F) $@ ; else exit 1; fi

