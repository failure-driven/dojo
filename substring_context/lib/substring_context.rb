class SubstringContext
  def initialize(text)
    @text = text
  end

  def find(search_string)
    text_to_array = @text.split
    indexes_of_string = []
    search_string.split.each do |search_sub_string|
      indexes_of_string.push(*text_to_array.each_index.select { |i| text_to_array[i] == search_sub_string })
    end

    last_index = nil
    output = []
    gap_size = 2 # 2 words before starting a new context sub string
    in_context_sub_string = false
    start_index = nil
    indexes_of_string.map do |index|
      if index - (last_index || index) <= gap_size
        if in_context_sub_string
          last_index = index
          next
        else
          in_context_sub_string = true
          start_index = index.zero? ? 0 : index - 1
        end
      else
        in_context_sub_string = false
        output << get_string_context(text_to_array, start_index, (last_index + 2) - start_index)
        start_index = nil
      end
      last_index = index
    end
    unless indexes_of_string.empty?
      start_index ||= last_index - (gap_size / 2)
      output << get_string_context(text_to_array, start_index, (last_index + 2) - start_index)
    end
    output
  end

  def get_string_context(text_to_array, start_index, number_of_words)
    text_to_array.slice(start_index, number_of_words).join(" ")
  end
end
