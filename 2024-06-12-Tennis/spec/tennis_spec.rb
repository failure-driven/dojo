require "tennis"

RSpec.describe "Tennis" do
  it "starts a game with love all" do
    tennis = Tennis.new
    expect(tennis.score).to eq "love all"
  end
end