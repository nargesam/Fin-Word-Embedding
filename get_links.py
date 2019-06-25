
import wikipediaapi
import os
cwd = os.getcwd()
print(cwd)

links = []
cont = []
alltext = []

# opening a file, get the link or the title and add it to a list
with open("Category-Social.txt") as openfile:
    for line in openfile:
        # title = line[18:]
        # cont.append(title)
        for part in line.split():
            if "https" in part:
                links.append(part)


print(len(links))

# for getting the page content base on page title
# for title in con:
#     page = wikipedia.page(title)
#     alltext.append(page.content)


# save link and title of pages 
with open('category-social-links.txt', 'w') as w:
# with open('category-social-title.txt', 'w') as w:
    # w.write(content)
    for link in links:
        w.write(link)
        w.write('\n')


