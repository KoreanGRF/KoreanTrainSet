SHELL               := /bin/bash
NMLC                ?= nmlc

# C compiler
CC                  ?= cc
CC_FLAGS            ?= -C -E -nostdinc -x c-header
CP_FLAGS            ?= $(shell [ "$(OSTYPE)" = "Darwin" ] && echo "-rfX" || echo "-rf")
CC_USER_FLAGS       ?=

# Configurations
-include Makefile.config

# Settings for Bananas (TODO)
# BANANAS_INI = bananas.ini
# MUSA        = musa
# MUSA_FLAGS  =

### Version
# $REPO_VERSION	$REPO_ISODATE	$REPO_MODIFIED	$REPO_HASH	$REPO_ISTAG	$REPO_ISSTABLETAG
VERSION_INFO        ?= "$(shell ./findversion.sh)"
REPO_VERSION        ?= $(shell echo ${VERSION_INFO} | cut -f1)   # Version
REPO_ISODATE        ?= $(shell echo ${VERSION_INFO} | cut -f2)   # Date
REPO_MODIFIED       ?= $(shell echo ${VERSION_INFO} | cut -f3)   # Is modified
REPO_HASH           ?= $(shell echo ${VERSION_INFO} | cut -f4)   # Hash
REPO_ISSTABLETAG    ?= $(shell echo ${VERSION_INFO} | cut -f5)   # Is stable

# Disable default syuffixes rule
.SUFFIXES:

# File names
DIR_NAME            ?= $(shell echo "$(REPO_NAME) $(REPO_VERSION)" | xargs | sed s/\ /_/g)
GRF_FILE            ?= $(BASE_FILENAME).grf
NML_FILE            ?= $(BASE_FILENAME).nml
NFO_FILE            ?= $(BASE_FILENAME).nfo
PNML_FILE           ?= $(BASE_FILENAME).pnml
TAG_FILE            ?= custom_tags.txt
DOC_FILE            ?= docs/readme.txt docs/license.txt docs/changelog.txt

GRF_GENERATE        ?= $(BASE_FILENAME).grf
NML_GENERATE        ?= $(BASE_FILENAME).nml
NFO_GENERATE        ?= $(BASE_FILENAME).nfo
PNML_GENERATE       ?= $(BASE_FILENAME).pnml
TAR_GENERATE        ?= $(BASE_FILENAME).tar
TAG_GENERATE        ?= custom_tags.txt
DOC_GENERATE        ?= $(DOC_FILE)
BUNDLE_FILES        ?= $(GRF_FILE) $(DOC_FILE)

# target 'all' must be first target
all: $(GRF_GENERATE) $(DOC_GENERATE) bundle_tar
	@echo $(REPO_VERSION)

# Generate *.grf
$(GRF_GENERATE): $(NML_GENERATE) $(TAG_GENERATE)
	@echo "[NMLC] $@"
	@ $(NMLC) -c --custom-tags="./$(TAG_FILE)" --lang-dir="./lang/" "./$(NML_FILE)" --grf="./$(GRF_FILE)" --nml="./$(NML_FILE)"
clean::
	@echo "[CLEAN GRF]"
	@-rm -rf $(GRF_FILE)

# Generate *.nml from *.pnml
$(NML_GENERATE): $(PNML_GENERATE)
	@echo "[CPP] $@"
	@ cc -D VERSION=$(VERSION) $(CC_USER_FLAGS) $(CC_FLAGS) -o $(NML_FILE) $(PNML_FILE)
clean::
	@echo "[CLEAN NML]"
	@-rm -rf $(NML_FILE)

$(NFO_GENERATE):
clean::
	@echo "[CLEAN NFO]"
	@-rm -rf $(NFO_FILE)


# Generate *.txt from *.ptxt
%.txt: %.ptxt $(GRF_GENERATE)
	@echo "[DOC] $@"
	@ cat $< \
		| sed -e "s/{{\VERSION}}/$(VERSION)/" \
		> $@
#		| sed -e "s/$(REPLACE_GRFID)/$(GRF_ID)/" \
#		| sed -e "s/$(REPLACE_REVISION)/$(NEWGRF_VERSION)/" \
#		| sed -e "s/$(REPLACE_FILENAME)/$(DIR_NAME)/" \

# Make a directory
mkdir: $(DIR_NAME)
$(DIR_NAME): $(GRF_GENERATE) $(DOC_GENERATE) 
	@echo "[BUNDLE] $@"
	@ if [ -e $@ ]; then rm -rf $@; fi
	@ mkdir $@
	@ -for i in $(BUNDLE_FILES); do cp $(CP_FLAGS) $$i $@; done
#	@ if [ -f $(BANANAS_INI) ]; then sed 's/^version *=.*/version = $(FILE_VERSION_STRING)/' $(BANANAS_INI) > $@/bananas.ini; fi

# Make custom_tags.txt
$(TAG_GENERATE):
	@echo "[TAG] $@"
	@echo "VERSION        :$(VERSION)" > $@
	@echo "RECENT_UPDATED :$(RECENT_UPDATED)" >> $@
	@echo "AUTHOR_WEBSITE :$(AUTHOR_WEBSITE)" >> $@
	@echo "AUTHOR_EMAIL   :$(AUTHOR_EMAIL)" >> $@
clean::
	@echo "[CLEAN TAG]"
	@-rm -rf $(TAG_FILE)

# Make a bundle
bundle: bundle_tar
bundle_tar: $(DIR_NAME).tar
$(DIR_NAME).tar: $(DIR_NAME)
	@echo "[BUNDLE TAR] $@"
	@ tar -cf $@ $^ --exclude=bananas.ini
clean::
	@echo "[CLEAN BUNDLE]"
	@-rm -rf $(shell echo "$(REPO_NAME)*" | xargs | sed s/\ /_/g)