from os import system
import re

def compile(wiz, js, data):
    if 'render_id' not in data:
        return js

    app_id = data['app_id']
    app_namespace = data['app_namespace']
    render_id = data['render_id']
    namespace = data['namespace']
    
    kwargsstr = "{$ kwargs $}"
    dicstr = "{$ dicstr $}"
    branch = wiz.branch()

    fs = wiz.__wiz__.framework.model("wizfs", module="wiz").use(f"wiz/yarn/src")
    component = ''
    p = re.compile('export[\s]+default[\s]+([a-zA-Z]+);?')
    try:
        _search = p.search(js)
        component = _search[1]
    except Exception as e:
        return ''
    if component == '':
        return ''
    o = "{"
    e = "}"
    js = f"""
    function init_{component}() {o}
        let wiz = season_wiz.load('{app_id}', '{namespace}', '{app_namespace}', '{render_id}');
        wiz.branch = '{branch}';
        wiz.data = wiz.kwargs = wiz.options = JSON.parse(atob('{kwargsstr}'));
        wiz.dic = wiz.DIC = JSON.parse(atob('{dicstr}'));

        return wiz;
    {e};

    {js}
    """
    fs.write(f"{component}.jsx", js)

    return js

def after_compile(wiz, js, data):

    p = re.compile('export[\s]+default[\s]+([a-zA-Z]+);?')
    try:
        _search = p.search(js)
        component = _search[1]
    except Exception as e:
        print(js)
        print("Do not found Component")
        return ''
    if component == '':
        return ''
    
    js = f"""
    {js};
    ReactDOM.render(<{component} />, document.querySelector("#root"));
    """
    fs = wiz.__wiz__.framework.model("wizfs", module="wiz").use(f"wiz/yarn/src")
    fs.write(f"{component}.jsx", js)
    args = {
        "COMPONENT": component,
        "BRANCH": wiz.branch(),
        "THEME": wiz.render_theme.split("/")[0],
    }
    args_arr = []
    for key in args:
        val = args[key]
        args_arr.append(f"{key}={val}")
    args_str = " ".join(args_arr)
    system(f"cd yarn && {args_str} yarn run build")
