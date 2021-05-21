FOLDER= ../input ../output
INPUT=$(foreach direction, ei eu ie iu ue ui, ../input/$(direction)M_rate.txt) ../input/LNS14000000.txt
OUTPUT=$(foreach plot_type, urate_ei urate_eu urate_ie urate_iu urate_ue urate_ui, ../output/$(plot_type).dat) $(foreach plot_type, urate_ei urate_eu urate_ie urate_iu urate_ue urate_ui, ../output/$(plot_type)_fig5.png)
all: $(OUTPUT)

$(FOLDER):
	mkdir $@

../output/%.dat: plot.py $(INPUT) | ../output
	python $<

../output/%_fig5.png: plot.py $(INPUT) | ../output
	python $<

../input/LNS14000000.txt: | ../input
	@if [ -e ../../blsdata-retrieve/output/$(@F) ] ; then ln -s ../../blsdata-retrieve/output/$(@F) $@ ; else exit 1; fi

../input/%M_rate.txt: | ../input
	@if [ -e ../../three-states/output/$(@F) ] ; then ln -s ../../three-states/output/$(@F) $@ ; else exit 1; fi
