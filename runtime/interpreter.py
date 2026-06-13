from py_mini_racer import py_mini_racer
import json


class JSRuntime:

    def __init__(self):
        self.ctx = py_mini_racer.MiniRacer()

    def execute(self, code):

        wrapped_code = f"""
        var output = [];

        var console = {{
            log: function(...args) {{
                output.push(args.join(" "));
            }}
        }};

        {code}

        JSON.stringify(output);
        """

        try:
            result = self.ctx.eval(wrapped_code)

            outputs = json.loads(result)

            for line in outputs:
                print(line)

        except Exception as e:
            print(f"JavaScript Runtime Error: {e}")