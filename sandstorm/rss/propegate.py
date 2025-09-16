#! /bin/python3

file = open("feed.xml", "r")
feed = file.read()
file.close()

location = feed.find("<item>")

template = open("itemtemplate.xml", "r")
template_string = template.read()
template.close()

feed_split = feed.split("<item>", 1)

feed_split.insert(1, template_string + "\n")
feed_split.insert(2, "      <item>")

feed = "\n".join(feed_split)

file = open("feed.xml", "w")
file.write(feed)
