# dojo

coding dojo - because pairing on code is so much better.

## Simple setup

### Python

make sure you have python

```sh
# check we have mise to manage runtimes
mise --version

# setup recent python
mise use python@3.12.11

# check you have a recent python
python --version
Python 3.12.11
```

create a directory for today's dojo

```sh
mkdir "$(date +'%Y-%m-%d')-mars-rover-py"

ls -lrt

cd 2025-09-03-mars-rover-py
```

create virtual environment

```sh
# -m mod : run library module as a script (terminates option list)
python -m venv .venv
# alternatively could call it something like `pytest-env`
# with:
#   python -m venv pytest-env

# activate the virtual environemnt
source .venv/bin/activate
```

install a test framework

```sh
# generate a requirements.txt file of required modules
cat <<EOF > requirements.txt
pytest
EOF
pip install -r requirements.txt
```

generate a test file

```sh
cat <<EOF > test_capitalize.py
def capital_case(x):
       return x.capitalize()

def test_capital_case():
       assert capital_case('semaphore') == 'Semaphore'
EOF
```

run the test

```sh
pytest
# in verbose mode
pytest -vvv
```

finally to leave the virtual env run

```sh
deactivate
```

add a build script `mise.toml` or similar

```sh
cp ../mise.toml .
mise run
```

### Ruby

setup a directory and `RSpec` tests

```sh
# setup directory
mkdir demo-code-kata
cd demo-code-kata
asdf local ruby 3.3.4       # latest at time of writing

# add rspec test suite
bundle init                 # generates a blank Gemfile
bundle add rspec            # adds rspec to Gemfile
bundle exec rspec --init    # configures spec/spec_helper.rb etc

# add --format documentation to .rspec file
sed -i.bak 'a\
  --format documentation' .rspec && rm .rspec.bak

bundle exec rspec
```

Create a test file

```sh
cat <<EOF > spec/yet_another_code_kata_spec.rb
# frozen_string_literal: true

require 'yet_another_code_kata'

RSpec.describe YetAnotherCodeKata do
  it('returns true, as there is always another code kata') do
    yet_another_code_kata = YetAnotherCodeKata.new
    expect(yet_another_code_kata.run).to eq true
  end
end
EOF
```

```sh
bundle exec rspec
```

That will fail ❌ [🅁 🄴 🄳 ], so let's create a simple implementation

```sh
mkdir lib
cat <<EOF > lib/yet_another_code_kata.rb
# frozen_string_literal: true

class YetAnotherCodeKata
  def run()= true
end
EOF
```

### Javascript

setup `Jest` tests

```sh
cd demo-code-kata
asdf local nodejs 20.10.0

npm init --yes

# if you haven't already
# brew install jq
# add jest to package.json runner scripts (requires jq)
echo $(jq '.scripts.test="jest"' package.json) | jq . \
    | > package_new.json && mv package{_new,}.json

npm install --save-dev jest typescript @types/jest
```

write a test

```sh
cat <<EOF > yet-another-code-kata.test.js
import yetAnotherCodeKata from './yet-another-code-kata';

describe("yet another code kata", () => {
  it("returns true, as there is always another code kata", () => {
    expect(yetAnotherCodeKata()).toEqual(true);
  });
});
EOF
```

```sh
npm test
```

this will fail
```error
SyntaxError: Cannot use import statement outside a module
```

can be fixed using bable (or type: module and .mjs files)

```sh
npm install --save-dev @babel/preset-env

cat <<EOF > babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {targets: {node: 'current'}}],
  ],
};
EOF
```

The test still fails ❌ [🅁 🄴 🄳 ], so let's create a simple implementation

```sh
cat <<EOF > yet-another-code-kata.js
export default () => true;
EOF
```

you can run tests in watch mode

```sh
npm test -- --watch
```

### Typescript

on top of what is in javascript, setup typescript

```sh
npm install --save-dev @babel/preset-env @babel/preset-typescript

cat <<EOF > babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {targets: {node: 'current'}}],
    '@babel/preset-typescript',
  ],
};
EOF
```

change your test and implementation to `.ts` endings from `.js`.

---

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

