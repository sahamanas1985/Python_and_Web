import difflib

def get_similarity(string1, string2):
  # Get the ratio of similarity between the two strings
  similarity = difflib.SequenceMatcher(None, string1, string2).ratio()

  # Calculate the percentage of similarity
  percentage = similarity * 100

  return percentage

# Test the function
string1 = "This is a test string"
string2 = "This is a test string!"

print(get_similarity(string1, string2)) # Output: 95.65217391304348
