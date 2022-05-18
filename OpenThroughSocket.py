import socket
import re
import ssl
import io

class OpenThroughSocket:
    def __init__(self, content):
        self.content = content

    def getLinks(self):
        urls = []
        results = re.findall("\/.*\.(?:png|jpg)", self.content)
        for y in results:
            if 'https://' not in y:
                y = 'https://andys.md' + y
            urls.append(y)
        urls = list(set(urls))
        self.links_to_images = urls


        return self.links_to_images
