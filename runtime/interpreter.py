from py_mini_racer import py_mini_racer
import json


class JSRuntime:

    def __init__(self):
        self.ctx = py_mini_racer.MiniRacer()

    def execute(self, code):

        wrapped_code = f"""
var output = [];

function formatArgs(args) {{
    return args.map(arg =>
        arg === null
            ? "null"
            : typeof arg === "object"
                ? JSON.stringify(arg)
                : String(arg)
    ).join(" ");
}}

var console = {{
    log: function(...args) {{
        output.push(formatArgs(args));
    }},

    error: function(...args) {{
        output.push(formatArgs(args));
    }},

    warn: function(...args) {{
        output.push(formatArgs(args));
    }},

    info: function(...args) {{
        output.push(formatArgs(args));
    }}
}};

{code}

JSON.stringify(output);
"""

        try:
            result = self.ctx.eval(wrapped_code)

            if result:
                outputs = json.loads(result)

                for line in outputs:
                    print(line)

        except Exception as e:
            print(f"JavaScript Runtime Error: {e}")