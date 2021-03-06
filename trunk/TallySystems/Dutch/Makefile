# @todo kiniry 16 Aug 2005 - Remove jmlc_junit separate compilation
# and classfile directory as it is no longer necessary with JML 5.
# Modified 2007, Systems Research Group, University College Dublin

RELEASE = v2.0
BASE	= usermanual
BIBTEXOPT = 
BIBWARN = 'LaTeX Warning: Citation'
REFWARN = 'Rerun to get cross-references'
LATEXMAX = 6
FIGSCALE = 0.5
JMLVERSION = 5.5

# CLASSPATH components

CORECP	= src
#CORECP	= src:specs
SPECS = specs
#SPECS = ../../specs
JMLSPECS = /usr/local/Java/JML-$(JMLVERSION)/specs
JARS = ../../infrastructure/jars
SOURCEPATH = $(CORECP):$(JMLSPECS):$(SPECS)
JMLCP	= $(JARS)/jmlruntime.jar:$(JARS)/jmljunitruntime.jar:$(JARS)/jml-release.jar:$(SPECS)
JUNITCP	= $(JARS)/junit.jar
JCECP	= $(JARS)/bcprov-jdk14-129.jar
FOPCP	= $(JARS)/fop.jar
MISCCP	= $(JARS)/avalon-framework-4.2.0.jar:$(JARS)/batik.jar
CHECKSTYLECP	= $(JARS)/checkstyle-optional-4.3.jar:$(JARS)/checkstyle-all-4.3.jar
ESCJAVA2CP = $(JARS)/esctools2.jar

# local variables for build process

jml ?= /usr/local/Java/bin/jml
javac ?= /usr/bin/javac
jmlrac ?= /usr/local/Java/bin/jmlrac
jmlc ?= /usr/local/Java/bin/jmlc --oldSemantics
jmldoc ?= /usr/local/Java/bin/jmldoc
jmlunit ?= /usr/local/Java/bin/jmlunit

basedocdir = doc
srcpath = src
specpath =	specs
buildpath =	build
jmlc_path =	jmlc
jmlunit_path =	jmlunit
interesting_path = interesting
jmlc_jmlunit_path =	jmlc_jmlunit
jmlc_interesting_path = jmlc_interesting

ESCPATH = /usr/local/Java/bin
escjava = $(ESCPATH)/escjava2 -source 1.4 -vclimit 2500000
#export ESCTOOLS_ROOT=$(ESCPATH)
export SIMPLIFY=/usr/local/Java/ESCJava2/Simplify-1.5.4.macosx

# Various CLASSPATH constructions

BASE_CLASSPATH	= $(CORECP):$(JCECP):$(FOPCP):$(MISCCP):$(JUNITCP):$(JMLCP)
JAVAC_CLASSPATH	= $(buildpath):$(BASE_CLASSPATH)
JMLC_CLASSPATH	= $(jmlc_path):$(BASE_CLASSPATH)
JUNIT_CLASSPATH	= $(jmlc_jmlunit_path):$(BASE_CLASSPATH)
INTERESTING_CLASSPATH = $(jmlc_interesting_path):$(BASE_CLASSPATH)
ESCJAVA_CLASSPATH	= $(CORECP):$(JCECP):$(FOPCP):$(MISCCP):$(JUNITCP):$(JMLCP):$(ESCJAVA2CP)
UNIT_TEST_CLASSPATH	= $(jmlc_jmlunit_path):$(buildpath):$(JCECP):$(FOPCP):$(MISCCP):$(JUNITCP):$(JMLCP)
INTERESTING_UNIT_TEST_CLASSPATH = $(jmlc_interesting_path):$(buildpath):$(JCECP):$(FOPCP):$(MISCCP):$(JUNITCP):$(JMLCP)
CHECKSTYLE_CLASSPATH	= $(CORECP):$(CHECKSTYLECP)

javapat	=	$(srcpath)/sos/koa/*java
javafiles =	$(wildcard $(srcpath)/sos/koa/*java)
core_javafiles =	$(srcpath)/sos/koa/Candidate.java \
			$(srcpath)/sos/koa/CandidateList.java \
			$(srcpath)/sos/koa/District.java \
			$(srcpath)/sos/koa/KiesKring.java \
			$(srcpath)/sos/koa/KiesLijst.java \
			$(srcpath)/sos/koa/VoteSet.java
koa_constants = $(srcpath)/sos/koa/KOAConstants.java
readme_file = koa/README.TXT
version_file = VERSION.TXT
usermanual_dir = usermanual
usermanual_tex = $(usermanual_dir)/usermanual.tex
usermanual_pdf = $(usermanual_dir)/usermanual.pdf
usermanual_ps = $(usermanual_dir)/usermanual.ps
adapter_files =	$(wildcard $(srcpath)/sos/koa/*Adapter.java)
jmlunitpat =	$(jmlunit_path)/sos/koa/*java
jmlunitfiles =	$(wildcard $(jmlunit_path)/sos/koa/*java)
generated_jmlunitfiles	=	$(wildcard $(jmlunit_path)/sos/koa/*_JML_Test.java)
interestingpat =	$(interesting_path)/sos/koa/*java
interestingfiles =	$(wildcard $(interesting_path)/sos/koa/*java)
generated_interestingfiles	=	$(wildcard $(interesting_path)/sos/koa/*_JML_Test.java)
classfiles =	$(foreach javafile,$(javafiles),\
		$(subst .java,.class,$(javafile)))
javadoc =	javadoc
javadocflags =	-version -author -private -source 1.4
jmldocflags =	-version -author -private --source 1.4
javadocdir =	$(basedocdir)/javadocs
jmldocdir =	$(basedocdir)/jmldocs

main_memory_use =	-ms256M -mx256M
rac_memory_use =	-ms256M -mx320M
test_memory_use	=	-ms256M -mx1024M

copyright = "SOA<br />&copy; 2004 SoS Group<br />All Rights Reserved"

# implicit rules for paper documentation generation

%.ps: %.gif
	giftopnm $< | pnmtops -noturn > $@
%.ps: %.fig
	fig2dev -L ps $< > $@
%.eps: %.fig
	fig2dev -L eps $< > $@
%.pdf: %.fig
	fig2dev -L pdf $< > $@
%.pdf: %.eps
	epstopdf $< > $@
.pdf_t: %.pstex_t
	sed 's/\.pstex/\.pdf/g' $< > $@
%.pdftex: %.tex
	sed 's/\.pstex_t/\.pdf_t/g' $< > $@
%.pstex: %.fig
	fig2dev -L pstex -m $(FIGSCALE) $< > $@
%.pstex_t: %.fig
	fig2dev -L pstex_t -m $(FIGSCALE) -p `basename $< .fig`.pstex $< > $@
%.ps: %.dvi
	dvips -D600 -Ppdf $< -o $@

%.aux: %.tex
	latex $*

%.dvi: %.tex
	latex $<
	if grep $(BIBWARN) $*.log >/dev/null; \
	then bibtex $(BIBTEXOPT) $*; latex $<; latex $<; fi
	RUNS=$(LATEXMAX); \
	while [ $$RUNS -gt 0 ] ; do \
		if grep $(REFWARN) $*.log > /dev/null; \
		then latex $< ; else break; fi; \
		RUNS=`expr $$RUNS - 1`; \
	done

%.pdf: %.ps
	ps2pdf $<

# identification of phony targets

.PHONY: all build escjava test ps pdf spellcheck \
	classes jmlc jmlc_jmlunit jmlunit jmlunit_classes \
	jmlc_interesting interesting interesting_classes \
	escjava2-typecheck escjava2 escjava2-current escjava2-core \
	main main-jmlrac jml-junit-tests jmlrac-tests interesting-tests \
	source_docs javadoc jmldoc checkstyle \
	clean clean_other_stamps clean_classes clean_jmlc \
	clean_jmlcjunit clean_jmlunit clean_jmlcintersting clean_interesting \
	clean_javadoc clean_jmldoc

# targets

all:	build source_docs test # escjava distr

build:	classes jml jmlc jmlunit_classes interesting_classes

escjava:	escjava2-typecheck escjava2

test:	jmlrac-tests interesting-tests

# paper documentation-related

ps:	$(BASE).ps

$(BASE).dvi:	$(BASE).tex\
		$(BASE).bbl

$(BASE).bbl:	$(BASE).aux\
		$(BASE).bib
		bibtex $(BIBTEXOPT) $(BASE)

$(BASE).ps:		$(BASE).dvi

$(BASE).pdf:	$(BASE).ps
		ps2pdf13 $(BASE).ps

pdf:		$(BASE).pdf

ps:		$(BASE).ps

spellcheck:
		aspell --lang=american --master=american -t -c $(BASE).tex
#aspell --lang=british --master=british -t -c $(BASE).tex

# targets related to building software

classes:	classes.stamp

classes.stamp:	$(javafiles)
	@mkdir -p $(buildpath)
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	$(javac) -g -d $(buildpath) -source 1.4 $(javapat) && \
	touch classes.stamp

jml:	jml.stamp

jml.stamp:	$(javafiles)
	$(jml) --classpath $(JMLC_CLASSPATH) \
	  --sourcepath $(SOURCEPATH) \
	  --Quiet --source 1.4 -A -a $(javapat) && \
	touch jml.stamp

jmlc:	jmlc.stamp jml.stamp

jmlc.stamp:	$(javafiles)
	@mkdir -p $(jmlc_path)
	$(jmlc) --classpath $(JMLC_CLASSPATH) \
		--sourcepath $(SOURCEPATH) \
		--destination $(jmlc_path) \
		--Quiet --source 1.4 -A -a $(javapat) && \
	touch jmlc.stamp

# jml-junit

jmlc_jmlunit: jmlc_jmlunit.stamp

jmlc_jmlunit.stamp:	$(javafiles)
	@mkdir -p $(jmlc_jmlunit_path)
	$(jmlc) --classpath $(JUNIT_CLASSPATH) \
		--sourcepath $(SOURCEPATH) \
		--destination $(jmlc_jmlunit_path) \
		--Quiet --source 1.4 -A -a $(javapat) && \
	touch jmlc_jmlunit.stamp

jmlunit:	jmlc_jmlunit jmlunit.stamp

jmlunit.stamp:	$(javafiles)
	@mkdir -p $(jmlunit_path)
	$(jmlunit) --classpath $(JAVAC_CLASSPATH) \
		--destination $(jmlunit_path) \
		--sourcepath $(SOURCEPATH) \
		--package --source 1.4 \
		--testLevel=2 $(core_javafiles) && \
	touch jmlunit.stamp

jmlunit_classes:	jmlunit jmlunit_classes.stamp

jmlunit_classes.stamp:	$(jmlunitfiles)
	mkdir -p $(jmlc_jmlunit_path)
	export CLASSPATH=$(JUNIT_CLASSPATH);\
	$(javac) -g -d $(jmlc_jmlunit_path) -source 1.4 $(jmlunitpat) && \
	touch jmlunit_classes.stamp

# interestingness testing

jmlc_interesting: jmlc_interesting.stamp

jmlc_interesting.stamp:	$(javafiles)
	@mkdir -p $(jmlc_interesting_path)
	$(jmlc) --classpath $(INTERESTING_CLASSPATH) \
		--sourcepath $(SOURCEPATH) \
		--destination $(jmlc_interesting_path) \
		--Quiet --source 1.4 -A -a $(javapat) && \
	touch jmlc_interesting.stamp

interesting:	jmlc_interesting interesting.stamp

interesting.stamp:	$(javafiles)
	@mkdir -p $(interesting_path)
	$(jmlunit) --classpath $(JAVAC_CLASSPATH) \
		--useGenerator \
		--destination $(interesting_path) \
		--sourcepath $(SOURCEPATH) \
		--package --source 1.4 \
		--testLevel=2 $(core_javafiles) && \
	touch interesting.stamp

interesting_classes:	interesting interesting_classes.stamp

interesting_classes.stamp:	$(jmlunitfiles)
	mkdir -p $(jmlc_interesting_path)
	export CLASSPATH=$(INTERESTING_CLASSPATH);\
	$(javac) -g -d $(jmlc_interesting_path) -source 1.4 $(interestingpat) && \
	touch interesting_classes.stamp

# targets related to checking software

escjava2-typecheck:	escjava2-typecheck.stamp

escjava2-typecheck.stamp:	$(javafiles)
	export CLASSPATH=$(ESCJAVA_CLASSPATH);\
	$(escjava) -typecheck $(javapat) && \
	touch escjava2-typecheck.stamp

escjava2:	escjava2.stamp

escjava2.stamp:	$(javafiles)
	export CLASSPATH=$(ESCJAVA_CLASSPATH);\
	$(escjava) $(javapat) && \
	touch escjava2.stamp

# Class         LOC	Total   Passed  Failed  Status
#-------------------------------------------------------
# Candidate     368	15	13	2	87%
# CandidateList 276	15	4	11
# District	189	9	9	0	100%
# KiesKring	249	18	12	6
# KiesLijst	207	13	9	4
# VoteSet	269	11	0	11

# /afs/sos/build/ESCTools/ESCTools/Escjava/escj

escjava2-current:
	export CLASSPATH=$(ESCJAVA_CLASSPATH);\
	$(escjava) -bootclasspath $(BOOTCP) \
		src/sos/koa/Task.java

escjava2-core:
	export CLASSPATH=$(ESCJAVA_CLASSPATH);\
	$(escjava) -bootclasspath $(BOOTCP) \
		$(core_javafiles)

checkstyle.stamp:
	export CLASSPATH=$(CHECKSTYLE_CLASSPATH); \
	java com.puppycrawl.tools.checkstyle.Main \
		-c sos-group.xml $(core_javafiles)

checkstyle:	checkstyle.stamp

# executing the program

main: classes
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java $(main_memory_use) sos.koa.MenuPanel

main-jmlrac: jmlc
	export CLASSPATH=$(JMLC_CLASSPATH);\
	$(jmlrac) $(rac_memory_use) sos.koa.MenuPanel

jml-junit-tests:	classes jmlunit_classes
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	jml-junit $(test_memory_use) sos.koa.KiesKring_JML_Test

jmlrac-tests:	classes jmlunit_classes
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.Candidate_JML_Test
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.CandidateList_JML_Test
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.District_JML_Test
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.KiesKring_JML_Test
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.KiesLijst_JML_Test
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.VoteSet_JML_Test

interesting-tests:	classes interesting_classes
	export CLASSPATH=$(INTERESTING_UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.Candidate_JML_Test
	export CLASSPATH=$(INTERESTING_UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.CandidateList_JML_Test
	export CLASSPATH=$(INTERESTING_UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.District_JML_Test
	export CLASSPATH=$(INTERESTING_UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.KiesKring_JML_Test
	export CLASSPATH=$(INTERESTING_UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.KiesLijst_JML_Test
	export CLASSPATH=$(INTERESTING_UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.VoteSet_JML_Test

jmlrac-tests-current:	classes jmlunit_classes
	export CLASSPATH=$(UNIT_TEST_CLASSPATH);\
	$(jmlrac) $(test_memory_use) sos.koa.VoteSet_JML_Test

viewpdf-test:	classes
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=acroread sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=acrobat sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=GPdf sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=kpdf sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=Kghostview sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=gv sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=ggv sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=xpdf sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java -DPdfViewer=gs sos.koa.ViewPdf
	export CLASSPATH=$(JAVAC_CLASSPATH);\
	java sos.koa.ViewPdf samples/KOA_rapport.pdf doc/040213_uitnodigingsbrief_aan_Univ_Nijmegen.pdf

# generating source-based documentation

source_docs:	javadoc # jmldoc

javadoc:	javadoc.stamp

javadoc.stamp:	$(javafiles) $(srcpath)/sos/koa/package.html $(basedocdir)/overview.html
	mkdir -p $(javadocdir); \
	export CLASSPATH=$(BASE_CLASSPATH);\
	$(javadoc) -d $(javadocdir) $(javadocflags) \
	-sourcepath .:$(srcpath):$(jdksrcpath) \
	-overview $(basedocdir)/overview.html \
	-doctitle "SOA: The SoS/KOA Vote Recount System" \
	-header $(copyright) \
	-footer $(copyright) \
	-subpackages sos.koa; \
	touch javadoc.stamp

jmldoc:		jmldoc.stamp

jmldoc.stamp:	$(javafiles) $(srcpath)/sos/koa/package.html $(basedocdir)/overview.html
	mkdir -p $(jmldocdir); \
	export CLASSPATH=$(BASE_CLASSPATH);\
	$(jmldoc) -d $(jmldocdir) $(jmldocflags) \
	-sourcepath .:$(SOURCEPATH):$(jdksrcpath) \
	-overview $(basedocdir)/overview.html \
	-doctitle "SOA: The SoS/KOA Vote Recount System" \
	-header $(copyright) \
	-footer $(copyright) \
	sos.koa;
	touch jmldoc.stamp


release:
	sed -i -e "s/^\(.* RELEASE = \)\(.*\)/\1\"$(RELEASE)\";/" $(koa_constants)
	sed -i -e "s/^\(.*\)\(%%%RELEASE\)/\\\date{Release\ $(RELEASE)}\2/" $(usermanual_tex)
	#svn commit $(usermanual_tex) $(koa_constants)
	cd $(usermanual_dir); make pdf
	echo '$(RELEASE)' > $(version_file)
	date >> $(version_file)

distr: distr.stamp

distr.stamp: release classes clean_distr usermanual
	mkdir -p distr/tmp
	mkdir -p distr/koa
	mkdir -p distr/koa/lib
	mkdir -p distr/koa/doc
	cp -r xml distr/tmp
	cp -r build/* distr/tmp
	jar -J-Xmx256M -mcf MANIFEST.MF distr/koa/koa.jar -C distr/tmp .
	rm -rf distr/tmp
	cp $(JCECP) distr/koa/lib/
	cp jars/avalon-framework.jar distr/koa/lib
	cp jars/batik.jar distr/koa/lib
	cp jars/fop.jar distr/koa/lib
	cp $(usermanual_pdf) distr/koa/doc
	cd distr/koa; jar -i koa.jar
	cd distr; zip koa.zip koa/koa.jar koa/lib/*
	touch distr.stamp

src_distr: src_distr.stamp 

src_distr.stamp: distr clean_src_distr
	mkdir -p distr/koa/src/sos/koa
	mkdir -p distr/koa/doc/javadocs
	mkdir -p distr/koa/doc/jmldocs
	cp src/sos/koa/*.java distr/koa/src/sos/koa
	cp src/sos/koa/*.html distr/koa/src/sos/koa
	cp -r doc/javadocs/* distr/koa/doc/javadocs
	cp -r doc/jmldocs/* distr/koa/doc/jmldocs
	cp doc/koa.css distr/koa/doc 
	cp doc/overview.html distr/koa/doc 
	cp ChangeLog distr/koa
	cp $(version_file) distr/koa
	cd jars; cp -r src ../distr/koa/lib/
	rm -rf distr/koa/lib/src/CVS
	cat README.header > distr/$(readme_file)
	cd distr; zip -r koa.zip koa/
	cd distr; echo '' >> $(readme_file)
	cd distr; echo 'The binaries:' >> $(readme_file)
	cd distr; echo '----' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'jar' >> $(readme_file)
	cd distr; echo '' >> $(readme_file)
	cd distr; echo 'The documentation:' >> $(readme_file)
	cd distr; echo '----' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'docs' | grep -v 'html' |grep -v 'sos' |grep -v 'package' |grep -v 'resources' | grep -v 'stylesheet' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'pdf' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'package' | grep 'src' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'Change' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'README' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'VERSION' >> $(readme_file)
	cd distr; echo '' >> $(readme_file)
	cd distr; echo 'The sources:' >> $(readme_file)
	cd distr; echo '----' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'src'|grep 'sos/koa' |grep -v 'java'|grep -v 'html' >> $(readme_file)
	cd distr; unzip -l koa.zip |grep 'src'|grep 'lib' >> $(readme_file)
	cat README.footer >> distr/$(readme_file)
	cd distr; zip -r koa.zip $(readme_file)
	touch src_distr.stamp

usermanual:	usermanual.stamp

usermanual.stamp:	
	cd $(usermanual_dir); make pdf
	touch usermanual.stamp

# targets related to cleaning up

clean:	clean_javadoc clean_jmldoc clean_classes clean_jml clean_jmlc \
	clean_jmlunit clean_jmlcjunit clean_interesting clean_jmlcinteresting \
	clean_other_stamps clean_distr clean_src_distr clean_usermanual
	rm -f $(BASE).dvi $(BASE).ps $(BASE).pdf
	rm -f *.log *.bbl *.blg *.aux *.out
	rm -f *.pstex *.pstex_t *.pdf *.pdf_t *.pdftex
	rm -f *.bak

clean_other_stamps:
	rm -f escjava2-typecheck.stamp escjava2.stamp checkstyle.stamp

clean_classes:
	rm -rf distr $(buildpath)/* classes.stamp jmlunit_classes.stamp

clean_jml:
	rm -rf jml.stamp

clean_jmlc:
	rm -rf $(jmlc_path)/* jmlc.stamp

clean_jmlcjunit:
	rm -rf $(jmlc_jmlunit_path)/* jmlc_jmlunit.stamp

clean_jmlunit:
	rm -f $(generated_jmlunitfiles) jmlunit.stamp

clean_jmlcinteresting:
	rm -rf $(jmlc_interesting_path)/* jmlc_interesting.stamp

clean_interesting:
	rm -f $(generated_interestingfiles) interesting.stamp

clean_javadoc:
	rm -rf $(javadocdir)/*.html \
		$(javadocdir)/sos* \
		$(javadocdir)/com* \
		$(javadocdir)/images \
		$(javadocdir)/package-list \
		$(javadocdir)/stylesheet.css \
		javadoc.stamp

clean_jmldoc:
	rm -rf $(jmldocdir)/*.html \
		$(jmldocdir)/sos* \
		$(jmldocdir)/com* \
		$(jmldocdir)/images \
		$(jmldocdir)/package-list \
		$(jmldocdir)/stylesheet.css \
		jmldoc.stamp

clean_distr:
	rm -rf distr

clean_src_distr:
	rm -rf src_distr.stamp

clean_usermanual:
	rm -rf usermanual.stamp
