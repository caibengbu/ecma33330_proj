FOLDER=../input ../output
START_DATE?=197601
END_DATE?=202009
all: ../output/adjusted_short_unemp.png ../output/LNS13008396.txt ../output/LNS12000000.txt ../output/LNS13000000.txt ../output/LNS14000000.txt

$(FOLDER):
	mkdir $@

../output/LNS%.txt: blsdata-retrieve.py | ../output
	python $< $(START_DATE) $(END_DATE)

../input/short_unemp_ts.txt: | ../input
	@if [ -e ../../short-unemp/output/$(@F) ] ; then ln -s ../../short-unemp/output/$(@F) $@ ; else exit 1; fi

short-unemp-x13.spc: sa_short_emp_from_CPSdata.py ../input/short_unemp_ts.txt
	python $<

short-unemp-x13.d11: short-unemp-x13.spc
	x13as $(basename $@)

../output/adjusted_short_unemp.png: u-v-f-s.py ../output/LNS13008396.txt ../output/LNS12000000.txt ../output/LNS13000000.txt short-unemp-x13.d11 | ../output
	python $<

clean:
	rm -f short-unemp-x13.*
	rm -f data.dat
	rm -rf ../input ../output