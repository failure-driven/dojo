class SubstringContext
  def initialize(text)
    @text = text
  end

  def find(string)
    # @text "the dog the fox"
    text_to_array = @text.split(' ')
    # text to array == ["the", "dog", "teh", "fox"]
    # input string "the fox"
    strings = string.split(' ')
    # strings == ["the", "fox"]
    indexes_of_string = []
    strings.each do |string|
      # for "the" then for "fox"
      indexes_of_string.push(*text_to_array.each_index.select{|i| text_to_array[i] == string})
      # indexes_of_string [] round 1 [0, 2] for "the" round 2 [0, 2, 3] "fox"
    end

    # [0, 1, 3, 4, 15, 16, 20]
    # padding = 1 word each side
    # 0..5
    # 14..17
    #  19..21
    last_index = -9999 # this is crap will limit us to not having more than 10,000 words surrowunding
    output = []
    indexes_of_string.map do |index|
      number_of_words = 3
      puts output.inspect
      if index - last_index <= 2
        number_of_words =  3 + (index - last_index) # only 2 matching words next to each other
        output[output.length - 1] = get_string_context(text_to_array, index - 1 - (index - last_index), number_of_words)
        next
      end
      last_index = index
      if index == 0
        output << get_string_context(text_to_array, index, 2)
      elsif index == text_to_array.length-1
        output << get_string_context(text_to_array, index - 1, 2)
      else
        output << get_string_context(text_to_array, index - 1, number_of_words)
      end
    end.compact
    output
  end

  def get_string_context(text_to_array, start_index, number_of_words)
    text_to_array.slice(start_index, number_of_words).join(' ')
  end


end
