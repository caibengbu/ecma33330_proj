FOLDER= ../input ../output/
OUTPUT= $(addprefix ../output/, $(addsuffix .txt, eu ei ue ui ie iu))

all: $(OUTPUT)

$(FOLDER):
	mkdir $@

../input/flows.txt: | ../input
	@if [ -e ../../cps-merge/output/$(@F) ] ; then ln -s ../../cps-merge/output/$(@F) $@ ; else exit 1; fi

../output/%.txt: match_sa.py ../input/flows.txt | ../output
	python $<

clean:
	rm -f *.log
	rm -rf $(FOLDER)