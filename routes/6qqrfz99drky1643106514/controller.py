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

### render app
# wiz.response.render("main")
# wiz.response.render("app_namespace")
# wiz.response.render("<url_pattern_1>", "<app_namespace>", key="value", key2="value2")
# wiz.response.render("<url_pattern_2>", "<app_namespace>", key="value", key2="value3")
wiz.response.render("widget.react.testapp")
wiz.response.status(200)