require "tennis"

RSpec.describe "Tennis" do
  it "starts a game with love all" do
    tennis = Tennis.new
    expect(tennis.score).to eq "love all"
  end
  it "if server wins a point, the score is 15 love" do
    tennis = Tennis.new
    "someone creates point server method"
    tennis.point_server
    expect(tennis.score).to eq "15 love"
  end
end

