class Tennis
  # SCORES = {
  #   0: "love",
  #   1: "15",
  #   2: "30"
  # }
  def initialize
    @score = 0
  end

  def score
    return "love all" if @score == 0
    return "15 love" if @score == 1
    return "30 love" if @score == 2
  end

  def point_server
    @score += 1
  end
end