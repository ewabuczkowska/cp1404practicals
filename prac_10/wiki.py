"""
CP1404 - Practical 10 - Wikipedia
"""
import wikipedia

search = input("Enter page title: ")
while search:
    try:
        page = wikipedia.page(search, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        print()
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
        print()
    except wikipedia.exceptions.PageError:
        print(f'Page id "{search}" does not match any pages. Try another id!\n')
    search = input("Enter page title: ")
print("Thank you.")