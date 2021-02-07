require "spec_helper"

RSpec.describe SubstringContext do
  it "returns an empty array when there is no context" do
    substring_context = SubstringContext.new("The quick brown fox jumps over the lazy dog")
    expect(substring_context.find("zebra")).to be_empty
  end

  it "returns the word before and after a found substring" do
    substring_context = SubstringContext.new("The quick brown fox jumps over the lazy dog")
    expect(substring_context.find("quick")).to eq(["The quick brown"])
  end

  it "returns multiple contexts for multiple matches" do
    substring_context = SubstringContext.new("The quick brown fox jumps over the quick dog")
    expect(substring_context.find("quick")).to eq(["The quick brown", "the quick dog"])
  end

  xit "returns a join context when there is less than 2 words between found contexts" do
    substring_context = SubstringContext.new(
      "The quick brown fox jumps over the lazy dog",
    )
    expect(
      substring_context.find(%w[quick brown]),
    ).to eq(["The quick brown fox"])
  end

  xit "returns the whole input if all the substrings overlap" do
    substring_context = SubstringContext.new(
      "The quick brown fox jumps over the lazy dog",
    )
    expect(
      substring_context.find(%w[quick fox over lazy]),
    ).to eq(["The quick brown fox jumps over the lazy dog"])
  end

  xit "returns the begginning and end as expected" do
    substring_context = SubstringContext.new(
      "The quick brown fox jumps over the lazy dog",
    )
    expect(
      substring_context.find("The dog"),
    ).to eq(["The quick", "lazy dog"])
  end

  it "returns the begginning" do
    substring_context = SubstringContext.new(
      "The quick brown fox jumps over the lazy dog",
    )
    expect(
      substring_context.find("The"),
    ).to eq(["The quick"])
  end 
  
  it "returns the end" do
    substring_context = SubstringContext.new(
      "The quick brown fox jumps over the lazy dog",
    )
    expect(
      substring_context.find("dog"),
    ).to eq(["lazy dog"])
  end 

  # chage from +-1 word to number of characters
end
