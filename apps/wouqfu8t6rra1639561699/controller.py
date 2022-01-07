### get request query
### wiz.request.query(<KEY>, <DEFAULT_VALUE>)
# data = wiz.request.query() # get all queries as dict type
# value = wiz.request.query("key", "test") # get `key` value, if not exist in query, return default value
# value = wiz.request.query("key", True) # if default value is True, this key required

### load text from dictionary
# hello = dic("hello")
# title = dic("title.text")

### use selected controller
# controller.custom_function()

### use segments
### Route: /board/<category>/list
### View URI: /board/notice/list
# segment = framework.request.segment

### Build view variables, you can use
# kwargs['message'] = "Hello, World!"
