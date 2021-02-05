PROJECT := dojo

default: usage

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

# TODO: check that EDITOR is set
.PHONY: setup_co_authors
setup_co_authors:
	echo "✨\n\nCo-authored-by: Michael Milewski <saramic@gmail.com>" >> .git/.gitmessage && ${EDITOR} .git/.gitmessage && git config commit.template .git/.gitmessage

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
	stat -f "%m%t%Sm %N" ~/.lolcommits/**/*.gif | sort -rn | head -1 | cut -f2- | sed "s/.*20[0-9][0-9] //" | sed "s/^/<img style=\"width:70%;\" src=\"/" | sed "s/.*/&\">/" > ${HOME}/temp_single_lolcommitters.html && open ${HOME}/temp_single_lolcommitters.html

.PHONY: all_the_lols
all_the_lols:
	ls -t ~/.lolcommits/**/*.gif | sed "s/^/<img src=\"/" | sed "s/.*/&\">/" > ${HOME}/temp_lolcommitters.html && open ${HOME}/temp_lolcommitters.html

