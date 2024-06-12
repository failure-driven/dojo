class Tennis
  def initialize
    @something = false
  end

  def score
    return "15 love" if @something

    "love all"
  end

  def point_server
    @something = true
  end
end