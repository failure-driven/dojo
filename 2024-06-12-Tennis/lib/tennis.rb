class Tennis
  DEFAULT_SCORES = %w[love 15 30 40]

  def initialize
    @score = 0
    @score_receiver = 0
  end

  def score
    output = [DEFAULT_SCORES[@score], DEFAULT_SCORES[@score_receiver]]
    output = [output[0], "all"] if output.uniq.count == 1
    output.join(" ")
  end

  def point_server
    @score += 1
  end

  def point_receiver
    @score_receiver += 1
  end
end