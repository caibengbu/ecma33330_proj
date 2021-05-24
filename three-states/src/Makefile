FOLDER= ../input ../output
INPUT=$(foreach direction, ei eu ie iu ue ui, ../input/$(direction).txt)
OUTPUT=$(foreach direction, ei eu ie iu ue ui, ../output/$(direction)_M.dat)
all: $(OUTPUT)

$(FOLDER):
	mkdir $@

../output/%_M.dat: three-state.py $(INPUT) | ../output
	python $<

../input/%.txt: | ../input
	@if [ -e ../../flow-seasonal-adjustment/output/$(@F) ] ; then ln -s ../../flow-seasonal-adjustment/output/$(@F) $@ ; else exit 1; fi

clean:
	rm -rf $(FOLDER)

