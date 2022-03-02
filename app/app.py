from flask import Flask, render_template

app = Flask(
    __name__,
    instance_relative_config=False,
    static_folder='static',
    template_folder='templates'
)

'''
when referencing a link url use url_for(function_name)
'''


@app.route('/')
@app.route('/home')
def home():
    '''Route to the home page'''
    nav = [
        {'name': 'HTML', 'memo': 'HTML Cheatsheet',
            'url': 'htm', 'img': 'static/img/htm.png'},
        {'name': 'Python', 'memo': 'Python Cheatsheet',
            'url': 'python', 'img': 'static/img/Python.png'},
        {'name': 'CSS', 'memo': 'CSS Cheatsheet',
            'url': 'css', 'img': 'static/img/css.png'},
        {'name': 'JavaScript', 'memo': 'JavaScript Cheatsheet',
            'url': 'js', 'img': 'static/img/js.png'},
        {'name': 'jQuery', 'memo': 'jQuery Cheatsheet',
            'url': 'jQuery', 'img': 'static/img/jquery.png'},
        {'name': 'MySQL', 'memo': 'MySQL Cheatsheet',
            'url': 'sql', 'img': 'static/img/sql.png'},
        {'name': 'C++', 'memo': 'C++ Cheatsheet',
            'url': 'cpp', 'img': 'static/img/cpp.png'},
        {'name': 'Julia', 'memo': 'Julia Cheatsheet',
            'url': 'julia', 'img': 'static/img/julia.png'},
    ]

    return render_template(
        'home.html',
        description='A simple go to reference of knowledge - Code AutoBiography',
        nav=nav
    )


@app.route('/cpp')
def cpp():
    '''Route to the c++ page'''
    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Control Structures & Loops', 'url': 'cpp/loops.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'Data Types & Variables', 'url': 'cpp/data.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'Arrays', 'url': 'cpp/arrays.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'Loops & Control Structures', 'url': 'cpp/loops.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'Pointers & Memory', 'url': 'cpp/pointers.html'},
        {'id': "headingSeven", 'data': 'collapseSeven',
            'heading': 'Functions', 'url': 'cpp/functions.html'},
        {'id': "headingEight", 'data': 'collapseEight',
            'heading': 'Object Oriented Programming', 'url': 'cpp/oop.html'},
        {'id': "headingNine", 'data': 'collapseNine',
            'heading': 'Handling Classes Externally', 'url': 'cpp/class.html'},
        {'id': "headingTen", 'data': 'collapseTen',
            'heading': 'Arrow Member Selection', 'url': 'cpp/member_select.html'},
        {'id': "headingThirteen", 'data': 'collapseThirteen',
            'heading': 'Member Initialisers', 'url': 'cpp/member_init.html'},
        {'id': "headingFourteen", 'data': 'collapseFourteen',
            'heading': 'Composition', 'url': 'cpp/composition.html'},
        {'id': "headingFifteen", 'data': 'collapseFifteen',
            'heading': 'Friend Functions', 'url': 'cpp/friend.html'},
        {'id': "headingSixteen", 'data': 'collapseSixteen',
            'heading': 'Constants', 'url': 'cpp/const.html'},
        {'id': "headingSeventeen", 'data': 'collapseSeventeen',
            'heading': 'This Keyword', 'url': 'cpp/this.html'},
        {'id': "headingEighteen", 'data': 'collapseEighteen',
            'heading': 'Operator Overloading', 'url': 'cpp/opp_overload.html'},
        {'id': "headingNineteen", 'data': 'collapseNineteen',
            'heading': 'Inheritance', 'url': 'cpp/inherit.html'},
        {'id': "headingTwenty", 'data': 'collapseTwenty',
            'heading': 'Types Of Inheritance', 'url': 'cpp/inherit_types.html'},
        {'id': "headingTwentyOne", 'data': 'collapseTwentyOne',
            'heading': 'Polymorphism', 'url': 'cpp/poly.html'},
        {'id': "headingTwentyTwo", 'data': 'collapseTwentyTwo',
            'heading': 'Virtual Functions', 'url': 'cpp/virtFunc.html'},
        {'id': "headingTwentyThree", 'data': 'collapseTwentyThree',
            'heading': 'Function Templates', 'url': 'cpp/funcTemp.html'},
        {'id': "headingTwentyFour", 'data': 'collapseTwentyFour',
            'heading': 'Class Templates', 'url': 'cpp/classTemp.html'},
        {'id': "headingTwentyFive", 'data': 'collapseTwentyFive',
            'heading': 'Template Specialisation', 'url': 'cpp/tempSpec.html'},
        {'id': "headingTwentySix", 'data': 'collapseTwentySix',
            'heading': 'Exception Handling', 'url': 'cpp/exceptions.html'},
        {'id': "headingTwentySeven", 'data': 'collapseTwentySeven',
            'heading': 'File Handling', 'url': 'cpp/files.html'},
        {'id': "headingTwentyEight", 'data': 'collapseTwentyEight',
            'heading': 'Things To Note', 'url': 'cpp/note.html'},

    ]

    return render_template(
        'cpp/cpp.html',
        title='C++',
        description='Code AutoBiography of C & C++',
        block=block
    )


@app.route('/python')
def python():
    '''Route to the python page'''
    operator = [
        {"sign": "**", "description": "Exponentiation"},
        {"sign": "~, +, -", "description": "Complement, plus, minus"},
        {"sign": "*, /, %, //",
            "description": "Multiply, division, modulus, floor division"},
        {"sign": ">>, <<", "description": "Right and left bitwise shift"},
        {"sign": "&", "description": "Bitwise AND"},
        {"sign": "^", "description": "Bitwise exclusive OR"},
        {"sign": "|", "description": "Bitwise OR"},
        {"sign": "", "description": "in, not in, is not, is"},
        {"sign": "<, >, <=, >=, !=, ==",
            "description": "Less than, greater than, less than or equal to, greater than ot equal, not equal, equal to"},
        {"sign": "not", "description": "Boolean \'NOT\'"},
        {"sign": "and", "description": "Boolean \'AND\'"},
        {"sign": "or", "description": "Boolean \'OR\'"},
        {"sign": "=, +=, -=, %=, /=, //=, *=, **=",
            "description": "Assignment operators"},
    ]

    sets = [
        {"sign": "|", "description": "Union"},
        {"sign": "&", "description": "Intersection"},
        {"sign": "-", "description": "Difference - gets items in the first set that is not in the second"},
        {"sign": "^", "description": "Symmetric difference - gets items in either sets but not both"}
    ]

    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Control Structures & Loops', 'url': 'python/loops.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'Data Structures', 'url': 'python/data.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'Functions & Modules', 'url': 'python/func.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'Raising Expections & Error Handling', 'url': 'python/err.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'File Handling', 'url': 'python/file.html'},
        {'id': "headingSeven", 'data': 'collapseSeven',
            'heading': 'Object Oriented Programming', 'url': 'python/oop.html'},
        {'id': "headingEight", 'data': 'collapseEight',
            'heading': 'Regular Expressions', 'url': 'python/re.html'},
        {'id': "headingNine", 'data': 'collapseNine',
            'heading': 'Packaging', 'url': 'python/pack.html'},
        {'id': "headingTen", 'data': 'collapseTen',
            'heading': 'Things To Note', 'url': 'python/note.html'}
    ]

    return render_template(
        'python/py.html',
        title='Python',
        description='Code AutoBiography of Python',
        block=block,
        operator=operator,
        sets=sets
    )


@app.route('/htm')
def htm():
    '''Route to the html page'''
    tags = [
        {"tag": "!-- --", "description": "Defines a comment"},
        {"tag": "!DOCTYPE html", "description": "Defines a document type"},
        {"tag": "a", "description": "Defines a hyperlink"},
        {"tag": "abbr", "description": "Defines an abbreviation"},
        {"tag": "address", "description": "Defines contact information for the author or owner of a document"},
        {"tag": "area", "description": "Defines an area inside an image-map"},
        {"tag": "article", "description": "Defines an article"},
        {"tag": "aside", "description": "Defines a content aside from page content"},
        {"tag": "audio", "description": "Defines a sound content"},
        {"tag": "b", "description": "Defines a bold text"},
        {"tag": "base", "description": "Specifies the target URL/target for all relative URLs in a document"},
        {"tag": "bdi", "description": "Isolates a part of text that might be formatted in a different from other text outside it"},
        {"tag": "bdo", "description": "Overides the current text direction"},
        {"tag": "blockquote",
            "description": "Defines a section that is quoted from another source"},
        {"tag": "body", "description": "Defines the document's body"},
        {"tag": "br", "description": "Defines a line break"},
        {"tag": "button", "description": "Defines a clickable button"},
        {"tag": "canvas",
            "description": "Used to draw graohics on the fly via scripting(usually javascript)"},
        {"tag": "caption", "description": "Defines a table caption"},
        {"tag": "cite", "description": "Defines the title of a work"},
        {"tag": "code", "description": "Defines a piece of computer code"},
        {"tag": "col", "description": "Specifies cloumn property for each column within a <colgroup> element"},
        {"tag": "colgroup", "description": "Specifies a group of one or more columns in a table for formatting"},
        {"tag": "datalist", "description": "Specifies a list of pre-defined options for input controls"},
        {"tag": "dd", "description": "Defines a description/value of a term in a description list"},
        {"tag": "del", "description": "Defines text that has been deleted from a document"},
        {"tag": "details", "description": "Defines additional details that the user can view or hide"},
        {"tag": "dfn", "description": "Represents the defining instance of a term"},
        {"tag": "dialog", "description": "Defines a dialog box or window"},
        {"tag": "div", "description": "Defines a section in a document"},
        {"tag": "dl", "description": "Defines a description list"},
        {"tag": "dt", "description": "Defines a term/name in a description list"},
        {"tag": "em", "description": "Defines emphasized text"},
        {"tag": "embed",
            "description": "Defines a container for an external(non-HTML) application"},
        {"tag": "fieldset", "description": "groups related elements in a form"},
        {"tag": "figcaption", "description": "Defines a caption for a <figure> element"},
        {"tag": "figure", "description": "Specifies self-contained conntent"},
        {"tag": "footer", "description": "Defines a footer for a document or section"},
        {"tag": "form", "description": "Defines an HTML form for user input"},
        {"tag": "h1 ... h6", "description": "Defines HTML headings"},
        {"tag": "head", "description": "Defines information about the document"},
        {"tag": "header", "description": "Defines a header for a document or a section"},
        {"tag": "hr", "description": "Defines a horizontal line - a thematic change in content"},
        {"tag": "html", "description": "Defines the root of an HTML document"},
        {"tag": "i", "description": "Defines italicised text"},
        {"tag": "iframe", "description": "Defines an inline frame"},
        {"tag": "img", "description": "Defines an image"},
        {"tag": "input", "description": "Defines an input control"},
        {"tag": "ins", "description": "Defines a text that has been inserrted into s document"},
        {"tag": "kbd", "description": "Defines keyboard input"},
        {"tag": "keygen",
            "description": "Defines a key-pair generator field (for forms)"},
        {"tag": "label", "description": "Defines a label for a input field"},
        {"tag": "legend", "description": "Defines a caption for <fieldset> element"},
        {"tag": "li", "description": "Defines a list item"},
        {"tag": "link", "description": "Defines a relationship between a document and anexternal resource"},
        {"tag": "main", "description": "Specifies the main content of a document"},
        {"tag": "map", "description": "Defines a client-side image map"},
        {"tag": "mark", "description": "Defines highlighted text"},
        {"tag": "menu", "description": "Defines a list of menu/commands"},
        {"tag": "menuitem", "description": "Defines a command that a user can invoke in a popup menu"},
        {"tag": "meta", "description": "Defines metadata about an HTML document"},
        {"tag": "meter", "description": "Defines a scalar measurement within a known range"},
        {"tag": "nav", "description": "Defines navigation links"},
        {"tag": "noscript", "description": "defines an alternate content for users that do not support client-side scripts"},
        {"tag": "object", "description": "Defines an embedded object"},
        {"tag": "ol", "description": "Defines an ordered list"},
        {"tag": "optgroup",
            "description": "Defines a group of related options in a dropdown list"},
        {"tag": "option", "description": "Defines an option in a dropdown list"},
        {"tag": "output", "description": "Defines the result of a calculation"},
        {"tag": "p", "description": "Defines a paragraph"},
        {"tag": "param", "description": "Defines a parameter for an object"},
        {"tag": "picture", "description": "Defines a container for multiple image resources"},
        {"tag": "pre", "description": "Defines pre-formatted text"},
        {"tag": "progress", "description": "Represents the progress of a task"},
        {"tag": "q", "description": "Defines a short quotation"},
        {"tag": "rp", "description": "Defines what to show in browsers tha do not support ruby annotations"},
        {"tag": "samp", "description": 'Defines a sample output from a computer program'},
        {"tag": "script", "description": "Defines a client-side script"},
        {"tag": "section", "description": "Defines a section in a document"},
        {"tag": "select", "description": "Defines a dropdown list"},
        {"tag": "small", "description": "Defines a smaller text"},
        {"tag": "source",
            "description": "Defines multiple media sources for media elements (<audio> & <video>)"},
        {"tag": "span", "description": "Defines a section in a document"},
        {"tag": "strong", "description": "Defines important text"},
        {"tag": "sub", "description": "Defines a subscripted text"},
        {"tag": "summary", "description": "Defines a visible heading for <details> element"},
        {"tag": "sup", "description": "Defines a superscripted text"},
        {"tag": "svg", "description": "defines a container for SVG graphics"},
        {"tag": "table", "description": "Defines a table"},
        {"tag": "tbody", "description": "Groups the body content in a table"},
        {"tag": "td", "description": "Defines a cell in a table"},
        {"tag": "textarea", "description": "Defines a multiline text input control"},
        {"tag": "tfoot", "description": "Groups the footer content in a table"},
        {"tag": "th", "description": "Defines a header cell in a table"},
        {"tag": "thead", "description": "Groups the header content in a table"},
        {"tag": "time", "description": "Deines date/time"},
        {"tag": "title", "description": "Defines a title for the document"},
        {"tag": "tr", "description": "Defines a row in a table"},
        {"tag": "track",
            "description": "Defines text tracks for madia elements (<audio> & <video>)"},
        {"tag": "u", "description": "Underlines text"},
        {"tag": "ul", "description": "Defines an unordered list"},
        {"tag": "var", "description": "Defines a variable"},
        {"tag": "video", "description": "Defines a video content"},
        {"tag": "wbr", "description": "Defines a possible line break"}
    ]

    lists = [
        {"eg_1": "color", "eg_2": "tel"},
        {"eg_1": "date", "eg_2": "name"},
        {"eg_1": "datetime", "eg_2": "time"},
        {"eg_1": "datetime-local", "eg_2": "text"},
        {"eg_1": "email", "eg_2": "password"},
        {"eg_1": "url", "eg_2": "radio"},
        {"eg_1": "week", "eg_2": "checkbox"},
        {"eg_1": "month", "eg_2": "submit"},
        {"eg_1": "number", "eg_2": "range"},
        {"eg_1": "search", "eg_2": "radio"},
        {"eg_1": "submit", "eg_2": "checkbox"}
    ]

    attr = [
        {"eg_1": "form", "eg_2": "list"},
        {"eg_1": "max", "eg_2": "min"},
        {"eg_1": "formaction", "eg_2": "multiple"},
        {"eg_1": "formenctype", "eg_2": "placeholder"},
        {"eg_1": "formnovalidate", "eg_2": "required"},
        {"eg_1": "formtarget", "eg_2": "step"},
        {"eg_1": "height", "eg_2": "width"},
        {"eg_1": "autofocus", "eg_2": "pattern"},
    ]

    specs = [
        {"code": "&amp; &#38;", "display": "Ampersand(&)"},
        {"code": "&gt; &#62", "display": "Greater than(>)"},
        {"code": "&lt; &#60", "display": "Less than(<)"},
        {"code": "&quot; &#34", "display": "Quotation marks(\"\")"},
        {"code": "&copy; &#169", "display": "Copyright"},
        {"code": "&reg; &#174", "display": "Registered"},
        {"code": "&trade; &#8482", "display": "Trademark"},
        {"code": "&nbsp; &#160", "display": "Non-breaking space"}

    ]

    target = [
        {"value": "_blank", "description": "Opens in a new browser window"},
        {"value": "_parent", "description": "Open in the parent frame or window"},
        {"value": "_self", "description": "Opens in the current window. Target is set to this value by default."},
        {"value": "_top", "description": "Opens in the topmost frame, thus replacing the contents of the window"},
        {"value": "<iframe_name>",
            "description": "Opens in an iframe element with the matching name attribute"}
    ]

    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Layout Structure', 'url': 'html/layout.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'Tags Reference', 'url': 'html/tags.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'Input Types & Its Attributes', 'url': 'html/input.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'Special Characters', 'url': 'html/special.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'Things To Note', 'url': 'html/note.html'}
    ]

    return render_template(
        'html/htm.html',
        title='HTML',
        description='Code AutoBiography of HTML',
        block=block,
        tags=tags,
        lists=lists,
        attr=attr,
        specs=specs,
        target=target
    )


@app.route('/js')
def js():
    '''Route to javascript page'''
    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Symbols & Operators', 'url': 'js/symbol.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'Variables & Data Structures', 'url': 'js/variable.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'Concatenation & String Functions', 'url': 'js/concat.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'Arrays', 'url': 'js/array.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'Objects', 'url': 'js/object.html'},
        {'id': "headingSeven", 'data': 'collapseSeven',
            'heading': 'JSON', 'url': 'js/json.html'},
        {'id': "headingEight", 'data': 'collapseEight',
            'heading': 'Conditionals & Loops', 'url': 'js/loops.html'},
        {'id': "headingNine", 'data': 'collapseNine',
            'heading': 'Functions', 'url': 'js/func.html'},
        {'id': "headingTen", 'data': 'collapseTen',
            'heading': 'Popup Boxes', 'url': 'js/pop.html'},
        {'id': "headingEleven", 'data': 'collapseEleven',
            'heading': 'Object Oriented Programming', 'url': 'js/oop.html'},
        {'id': "headingTwelve", 'data': 'collapseTwelve',
            'heading': 'The Math Object', 'url': 'js/math.html'},
        {'id': "headingThirteen", 'data': 'collapseThirteen',
            'heading': 'The Date Object', 'url': 'js/date.html'},
        {'id': "headingFourteen", 'data': 'collapseFourteen',
            'heading': 'Promises', 'url': 'js/promise.html'},
        {'id': "headingFiftteen", 'data': 'collapseFiftteen',
            'heading': 'Async & Await', 'url': 'js/async.html'},
        {'id': "headingSixteen", 'data': 'collapseSixteen',
            'heading': 'The this Keyword', 'url': 'js/this.html'},
        {'id': "headingSeventeen", 'data': 'collapseSeventeen',
            'heading': 'Regular Expressions', 'url': 'js/regex.html'},
        {'id': "headingEighteen", 'data': 'collapseEighteen',
            'heading': 'Events', 'url': 'js/event.html'},
        {'id': "headingNineteen", 'data': 'collapseNineteen',
            'heading': 'Manipulating The DOM', 'url': 'js/dom.html'},
        {'id': "headingTwenty", 'data': 'collapseTwenty',
            'heading': 'Things To Note', 'url': 'js/note.html'},
    ]
    return render_template(
        'js/js.html',
        title='JavaScript',
        description='Code AutoBiography of JavaScript',
        block=block
    )


@app.route("/jQuery")
def jQuery():
    '''Route to jQuery page'''
    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Selectors', 'url': 'jquery/select.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'The attr() method', 'url': 'jquery/attr.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'The html() method', 'url': 'jquery/html.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'The text() method', 'url': 'jquery/text.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'The val() method', 'url': 'jquery/val.html'},
        {'id': "headingSeven", 'data': 'collapseSeven',
            'heading': 'Class Methods', 'url': 'jquery/class.html'},
        {'id': "headingEight", 'data': 'collapseEight',
            'heading': 'The css() method', 'url': 'jquery/css.html'},
        {'id': "headingNine", 'data': 'collapseNine',
            'heading': 'Sizing Methods', 'url': 'jquery/size.html'},
        {'id': "headingTen", 'data': 'collapseTen',
            'heading': 'Parent & Child Methods', 'url': 'jquery/parent.html'},
        {'id': "headingEleven", 'data': 'collapseEleven',
            'heading': 'Handling Events', 'url': 'jquery/event.html'},
        {'id': "headingTwelve", 'data': 'collapseTwelve',
            'heading': 'Things To Note', 'url': 'jquery/note.html'},
    ]
    return render_template(
        'jquery/jquery.html',
        title='jQuery',
        description='Code AutoBiography of jQuery',
        block=block
    )


@app.route('/sql')
def sql():
    '''Route to SQL page'''
    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Show Keyword', 'url': 'sql/show.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'Select Keyword', 'url': 'sql/select.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'Distinct Keyword', 'url': 'sql/distinct.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'Limit Keyword', 'url': 'sql/limit.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'Order By Keyword', 'url': 'sql/order.html'},
        {'id': "headingSeven", 'data': 'collapseSeven',
            'heading': 'Where Keyword', 'url': 'sql/where.html'},
        {'id': "headingEight", 'data': 'collapseEight',
            'heading': 'Operators', 'url': 'sql/operators.html'},
        {'id': "headingNine", 'data': 'collapseNine',
            'heading': 'Concat Function', 'url': 'sql/concat.html'},
        {'id': "headingTen", 'data': 'collapseTen',
            'heading': 'Sub Queries', 'url': 'sql/sub.html'},
        {'id': "headingEleven", 'data': 'collapseEleven',
            'heading': 'Joining Tables', 'url': 'sql/join.html'},
        {'id': "headingTwelve", 'data': 'collapseTwelve',
            'heading': 'Set Operations', 'url': 'sql/set.html'},
        {'id': "headingThirteen", 'data': 'collapseThirteen',
            'heading': 'Inserting Data', 'url': 'sql/insert.html'},
        {'id': "headingFifteen", 'data': 'collapseFifteen',
            'heading': 'Updating Data', 'url': 'sql/update.html'},
        {'id': "headingSixteen", 'data': 'collapseSixteen',
            'heading': 'Creating Tables', 'url': 'sql/table.html'},
        {'id': "headingSeventeen", 'data': 'collapseSeventeen',
            'heading': 'Constraints', 'url': 'sql/constraint.html'},
        {'id': "headingEighteen", 'data': 'collapseEighteen',
            'heading': 'Views', 'url': 'sql/view.html'},
        {'id': "headingNineteen", 'data': 'collapseNineteen',
            'heading': 'Things To Note', 'url': 'sql/note.html'}
    ]
    return render_template(
        'sql/sql.html',
        title='MySQL',
        description='Code AutoBiography of MySQL',
        block=block
    )


@app.route('/react')
def react():
    '''Route to react js page'''
    return render_template(
        'react.html',
        title='React',
        description='Code AutoBiography of React js'
    )


@app.route('/css')
def css():
    '''Route to css page'''
    block = [
        {'id': "headingTwo", 'data': 'collapseTwo',
            'heading': 'Vertical Align', 'url': 'css/valign.html'},
        {'id': "headingThree", 'data': 'collapseThree',
            'heading': 'Text Styling', 'url': 'css/text.html'},
        {'id': "headingFour", 'data': 'collapseFour',
            'heading': 'White Spaces', 'url': 'css/space.html'},
        {'id': "headingFive", 'data': 'collapseFive',
            'heading': 'Positioning Elements', 'url': 'css/position.html'},
        {'id': "headingSix", 'data': 'collapseSix',
            'heading': 'Table & Border Styling', 'url': 'css/border.html'},
        {'id': "headingSeven", 'data': 'collapseSeven',
            'heading': 'Backgroung Styling', 'url': 'css/background.html'},
        {'id': "headingEight", 'data': 'collapseEight',
            'heading': 'List Styling', 'url': 'css/list.html'},
        {'id': "headingNine", 'data': 'collapseNine',
            'heading': 'Box Shadow', 'url': 'css/shadow.html'},
        {'id': "headingTen", 'data': 'collapseTen',
            'heading': '@Font-face Rule', 'url': 'css/font.html'},
        {'id': "headingEleven", 'data': 'collapseEleven',
            'heading': 'Pseudo Classes', 'url': 'css/class.html'},
        {'id': "headingTwelve", 'data': 'collapseTwelve',
            'heading': 'Linear & Radial Gradients', 'url': 'css/gradient.html'},
        {'id': "headingThirteen", 'data': 'collapseThirteen',
            'heading': 'Transitions', 'url': 'css/transition.html'},
        {'id': "headingFourteen", 'data': 'collapseFourteen',
            'heading': 'Transformations', 'url': 'css/transform.html'},
        {'id': "headingFifteen", 'data': 'collapseFifteen',
            'heading': 'Animations', 'url': 'css/animate.html'},
        {'id': "headingSixteen", 'data': 'collapseSixteen',
            'heading': 'Filters', 'url': 'css/filter.html'},
        {'id': "headingSeventeen", 'data': 'collapseSeventeen',
            'heading': 'Things To Note', 'url': 'css/note.html'},
    ]

    return render_template(
        'css/css.html',
        title='CSS',
        description='Code AutoBiography of CSS',
        block=block
    )


@app.route('/flask')
def pyflask():
    '''Route to flask page'''
    return render_template(
        'flask.html',
        title='Flask',
        description='Code AutoBiography of Flask'
    )


@app.route("/julia")
def julia():
    '''Route to julia page'''
    return render_template(
        'julia/julia.html',
        title='Julia',
        description='Code AutoBiography of Julia'
    )



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
