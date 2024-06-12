require "tennis"

RSpec.describe "Tennis" do
  [
    {srv: 0, rcv: 0, score: "love all"},
    {srv: 1, rcv: 0, score: "15 love"},
    {srv: 2, rcv: 0, score: "30 love"},
    {srv: 3, rcv: 0, score: "40 love"},
    {srv: 0, rcv: 1, score: "love 15"},
    {srv: 0, rcv: 2, score: "love 30"},
    {srv: 0, rcv: 3, score: "love 40"},
    {srv: 2, rcv: 2, score: "30 all"},
    {srv: 3, rcv: 2, score: "40 30"},
  ].each do |args|
    it "for score server: #{args[:srv]} receiver: #{args[:rcv]} = #{args[:score]}" do
      tennis = Tennis.new
      args[:srv].times { tennis.point_server }
      args[:rcv].times { tennis.point_receiver }
      expect(tennis.score).to eq args[:score]
    end
  end
end

