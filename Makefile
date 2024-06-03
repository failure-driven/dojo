PROJECT := dojo

default: usage

# terminal colors
RED     = \033[0;31m
GREEN   = \033[0;32m
YELLOW  = \033[0;33m
BLUE    = \033[0;34m
MAGENTA = \033[0;35m
BOLD    = \033[1m
RESET   = \033[0m

.PHONY: usage
usage:
	bin/makefile/usage

.PHONY: new_ruby_dojo
new_ruby_dojo:
	bin/makefile/new-ruby-dojo $(or $(name),$(error Must specify name: "make new_ruby_dojo name=awesome-dojo"))

.PHONY: rubocop_fix_all
rubocop_fix_all:
	bundle exec rubocop -A .

.PHONY: prettier_ruby
prettier_ruby:
	bin/makefile/prettier-ruby

.PHONY: setup_co_authors
setup_co_authors:
	@command -v git-mob &> /dev/null || \
		npm install --global git-mob
	@echo "${GREEN}✅ git-mob installed${RESET}"
	@git config --global git-mob-config.github-fetch true
	git mob --list

# TODO: check that EDITOR is set
.PHONY: setup_co_authors-manually
setup_co_authors-manually:
	echo "✨\n\nCo-authored-by: Michael Milewski <saramic@gmail.com>" >> \
		.git/.gitmessage && \
		${EDITOR} .git/.gitmessage && \
		git config commit.template .git/.gitmessage

# TODO: make sure dependencies like ffmpeg are installed via brew
.PHONY: setup_lolcommits
setup_lolcommits:
	brew install imagemagick ffmpeg
	gem install lolcommits
	lolcommits --enable --delay 1 --animate 6 --fork

.PHONY: disable_lolcommits
disable_lolcommits:
	lolcommits --disable

.PHONY: last_lol
last_lol:
	stat -f "%m%t%Sm %N" ~/.lolcommits/**/*.gif | \
		sort -rn | head -1 | cut -f2- | \
		sed "s/.*20[0-9][0-9] //" | \
		sed "s/^/<img style=\"width:70%;\" src=\"/" | \
		sed "s/.*/&\">/" > \
		${HOME}/temp_single_lolcommitters.html && \
		open ${HOME}/temp_single_lolcommitters.html

.PHONY: all_the_lols
all_the_lols:
	ls -t ~/.lolcommits/**/*.gif | \
		sed "s/^/<img src=\"/" | \
		sed "s/.*/&\">/" > \
		${HOME}/temp_lolcommitters.html && \
		open ${HOME}/temp_lolcommitters.html

