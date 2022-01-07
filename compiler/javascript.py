import re

def babel():
    pass

def cond_str(js, data):
    app_namespace = data['app_namespace']
    render_id = data['render_id']

    o = "{"
    e = "}"

    p = re.compile('export[\s]+default[\s]+([a-zA-Z]+);?')
    component = ''
    try:
        _search = p.search(js)
        js = js.replace(_search[0], "")
        component = _search[1]
    except:
        pass
    is_react = 'true' if len(component) > 0 else 'false'
    if is_react == 'false':
        return f"""
            {js};
            try {o}
                app.controller('{render_id}', wiz_controller); 
            {e} catch (e) {o}
                try {o}
                    app.controller('{render_id}', ()=> {o} {e} ); 
                {e} catch (e) {o}{e}
            {e} 
        """
    # const _{component}_children = Array.from(document.getElementById('{app_namespace}').children).map((child, i) => {o}
    #     const T = (props) => {o}
    #         return (
    #             <div
    #                 dangerouslySetInnerHTML={o}{o} __html:child.outerHTML {e}{e} 
    #             />
    #         );
    #     {e}
    #     console.log(T.props)
    #     return <T />;
    # {e});
    str_react = f"""
        {js}
        const __html = document.getElementById('{app_namespace}').innerHTML;
        const __c = () => {o}
            return (
                <div dangerouslySetInnerHTML={o}{o} __html:__html {e}{e} />
            );
        {e}
        const {component}_children = <__c />;
        console.log({component}_children)
        const _{component} = React.cloneElement(<{component} />, {o}wiz{e}, {component}_children);
        ReactDOM.render(_{component}, document.getElementById('{app_namespace}'));
    """
    
    res_str = f"""
    if({is_react} && React && ReactDOM && Babel) {o}
        {str_react}
    {e}
    """
    return res_str

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

    js_str = cond_str(js, data)

    js = f"""
    function __init_{render_id}() {o}
        let wiz = season_wiz.load('{app_id}', '{namespace}', '{app_namespace}', '{render_id}');
        wiz.branch = '{branch}';
        wiz.data = wiz.kwargs = wiz.options = JSON.parse(atob('{kwargsstr}'));
        wiz.dic = wiz.DIC = JSON.parse(atob('{dicstr}'));

        {js_str}
    {e};
    __init_{render_id}();
    """
    # if({is_react} && React && ReactDOM && Babel) {o}
    #     const elmt = document.querySelector("script[data-bundle-target='true']");
    #     let html = elmt.innerHTML;
    #     html += "{app_namespace}";
    #     elmt.innerHTML = html;
    # {e}
    # else {o}
    #     __init_{render_id}();
    # {e}

    return js