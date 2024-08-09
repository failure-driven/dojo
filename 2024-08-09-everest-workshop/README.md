# Pairing and TDD

Pair Programming (& mob/ensemble) and Test Driven Development (Design)

# Online setup

http://cyber-dojo.org

## Notes

- icebreakers
    - new olympic sport
    - what we want to get out of today
- background pairing and TDD
    - how do you introduce people to it

BDD naming - characteristic testing - gold master

- patterns
    - share control
    - baby steps - keep validating
- anti-patterns
    - "watch the master"

- round the room fizz-buzz
- TDD cycle
    1. list of ideas (slicing!)
    2. ❌ write a failing test
    3. ✅ make it pass
    4. ♻️ refactor? - code - tests
    5. goto 2 (sometimes 1)
- Expectations
    - integrate TDD, contracts, TBD
- mobbing
    - driver is only typing
    - the mob dictates what to do, there is a master navigator to always defer
      to if too many people are talking

## Ruby setup

## setup
```sh
bundle init # generates a blank Gemfile
bundle add rspec            # adds rspec to Gemfile
bundle exec rspec --init    # configures spec/spec_helper.rb etc
bundle exec rspec
```

## first test

```sh
mkdir lib
touch lib/demo_ruby.rb
touch spec/demo_ruby_spec.rb
bundle exec rspec
# add --format documentation to .rspec file
bundle exec rspec
```

## runner

```sh
# create a directory for a runner script, ./bin
mkdir bin

# Create a demo script that runs ruby, loads our class
# NOTE: the '$' below is escaped '\$' to be able to cut and paste below code
# but it is only a '$' in the file

cat <<EOF > ./bin/demo.rb
#!/usr/bin/env ruby

\$LOAD_PATH << File.join(__dir__, "../lib")

require 'demo_ruby'

puts 'hi'
EOF

# make it executable
chmod +x bin/demo.rb

# run it
bin/demo.rb
```

## Typescript setup

make a directory in your git repo of choice
```sh
mkdir 2023_Leet_Learning/yet-another-code-kata
cd 2023_Leet_Learning/yet-another-code-kata
```

Setup npm with jest for testing
NOTE: _this assumes you have `jq` installed, you can install with
      `brew install jq`_
```sh
npm init --yes

echo $(jq '.scripts.test="jest"' package.json) | jq . \
    | > package_new.json && mv package{_new,}.json

npm install --save-dev jest typescript @types/jest
```

Install and configure babel to deal with imports and modules etc
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

Now you should be able to run tests and no tests to be found
```sh
npm test
```

Create a test file
```sh
cat <<EOF > yet-another-code-kata.test.ts
import yetAnotherCodeKata from './yet-another-code-kata';

describe("yet another code kata", () => {
  it("returns true, as there is always another code kata", () => {
    expect(yetAnotherCodeKata()).toEqual(true);
  });
});
EOF
```

That will fail ❌ [🅁 🄴 🄳 ], so let's create a simple implementation
```sh
cat <<EOF > yet-another-code-kata.ts
export default () => true;
EOF
```

Tests should now pass ✅ [🄶 🅁 🄴 🄴 🄽 ]
```sh
npm test
```

You can also run them in --watch mode to watch for file changes
```sh
npm test -- --watch
```

now it's time to commit
```sh
git add .
git commit -m "😍 amazing code kata setup, thanks MM"
```
and there you go, now write the code you want!!! ♻️  [🅁 🄴 🄵 🄰 🄲 🅃 🄾 🅁 ]

