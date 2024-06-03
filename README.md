# dojo

coding dojo - because pairing on code is so much better.

## Setup

  to list options

  ```
  make
  ```

  start a ruby rspec project

  ```
  make project name=awesome-problem

    # which will attempt to
    mkdir awesome-problem
    cd awesome-problem
    bundle init
    vi Gemfile
    # and add
      gem "rspec"
      gem "guard-rspec"

    bundle
    bundle exec rspec --init
    bundle exec guard init rspec

    # add this to spec/spec_helper.rb to require all ruby files in /lib
    # require all the lib files
    Dir[
      File.join(File.expand_path(File.dirname(__FILE__)), "..", "lib", "**", "*.rb")
    ].each { |f| require f }

    # run the tests
    bundle exec rspec

  # all that will be left to do is
  cd awesome-problem-one

  # run the tests
  bundle exec rspec

  # run the tests in watch mode
  bundle exec guard
  ```

**Commit Awesome**

- Co-authored-by

  ```
  make setup_co_authors

  git mob --list
  git mob saramic   # mob with github username

  # stored in
  cat ~/.git-coauthors

  # and apply to template in
  cat ~/.gitcommit
  ```

- Lolcommits

  ```
  make setup_lolcommits

    # which basically will
    gem install lolcommits
    lolcommits --enable --delay 1 --animate 6 --fork

  # show last lol
  make last_lol

  # show all the lols
  make all_the_lols

  # disable with
  make disable_lolcommits
  ```

## Projects

- [2021-02-07-substring_context](./2021-02-07-substring_context/)

