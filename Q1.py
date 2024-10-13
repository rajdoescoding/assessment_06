def search_query_completions(search_history, partialQuery):
    suggestions = [query for query in search_history if query.startswith(partialQuery)]
    return suggestions

search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

partialQuery = input("Enter your partial search query: ")
suggestions = search_query_completions(search_history, partialQuery)

print("Suggestions:")
for suggestion in suggestions:
    print(suggestion)