class Headline  :
    """
    Headline class to define headline objects
    """

    def __init__(self,title,description,content,urlToImage,url,category,id):
        self.title = title
        self.description = description
        self.content = content
        self.urlToImage = urlToImage
        self.url = url
        self.category = category
        self.id = id

class Sources :
    
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        
        

class Article:

    def __init__(self,id,name,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.url = url
        self.description = description

        self.content = content
