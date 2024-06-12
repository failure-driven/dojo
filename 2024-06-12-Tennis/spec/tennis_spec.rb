require "tennis"

RSpec.describe "Tennis" do
  it "starts a game with love all" do
    tennis = Tennis.new
    0.times { tennis.point_server }
    expect(tennis.score).to eq "love all"
  end

  it "if server wins a point, the score is 15 love" do
    tennis = Tennis.new
    1.times { tennis.point_server }
    expect(tennis.score).to eq "15 love"
  end

  it "if server wins 2 points in a row, the score is 30 love" do
    tennis = Tennis.new
    2.times { tennis.point_server }
    expect(tennis.score).to eq "30 love"
  end

  it "if server wins 3 points in a row, the score is 30 love" do
    tennis = Tennis.new
    3.times { tennis.point_server }
    expect(tennis.score).to eq "40 love"
  end
end

