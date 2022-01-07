import re

def compile(wiz, js, data):
    if 'render_id' not in data:
        return js

    app_id = data['app_id']
    app_namespace = data['app_namespace']
    render_id = data['render_id']
    namespace = data['namespace']

    o = "{"
    e = "}"
    kwargsstr = "{$ kwargs $}"
    dicstr = "{$ dicstr $}"
    branch = wiz.branch()

    p = re.compile('export[\s]+default[\s]+([a-zA-Z]+)')
    component = ''
    try:
        component = p.match(js).group(1)
    except:
        pass

    js = f"""{js};
    ReactDOM.render(<{component} />, document.getElementById('{namespace}'));
    """
    js = f"""
    function __init_{render_id}() {o}
        let wiz = season_wiz.load('{app_id}', '{namespace}', '{app_namespace}', '{render_id}');
        wiz.branch = '{branch}';
        wiz.data = wiz.kwargs = wiz.options = JSON.parse(atob('{kwargsstr}'));
        wiz.dic = wiz.DIC = JSON.parse(atob('{dicstr}'));

        {js};
    {e}; 
    __init_{render_id}();
    """

    return js