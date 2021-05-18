FOLDER=../input ../output
all: ../output/short_emp.txt ../output/emp.txt ../output/unemp.txt

$(FOLDER):
	mkdir $@

../output/LNS%.txt: blsdata-retrieve.py | ../output
	python $<

../output/short_emp.txt: ../output/LNS13008396.txt | ../output
	cp $< $@

../output/unemp.txt: ../output/LNS13000000.txt | ../output
	cp $< $@

../output/emp.txt: ../output/LNS12000000.txt | ../output
	cp $< $@