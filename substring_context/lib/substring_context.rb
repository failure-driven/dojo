class SubstringContext
  def initialize(text)
    @text = text
  end

  def find(string)
    text_to_array = @text.split(' ')
    indexes_of_string = text_to_array.each_index.select{|i| text_to_array[i] == string}
    indexes_of_string.map do |index|
      if index == 0
        "#{text_to_array[index]} #{text_to_array[index + 1]}"
      elsif index == text_to_array.length-1
        "#{text_to_array[index - 1]} #{text_to_array[index]}"
      else
        text_to_array.slice(index - 1, 3).join(' ')
      # "#{text_to_array[index - 1]} #{text_to_array[index]} #{text_to_array[index + 1]}"
      end
    end
  end

  
end
