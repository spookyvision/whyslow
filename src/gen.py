#!/usr/bin/env python
class RS:
    def __init__(self, name):
        self.name = name

    def emit_decl(self, fh):
        fh.write("""
#[derive(Debug)]
struct %s;
""" % self.name)

    def emit_use(self, fh):

        fh.write("""println!("{:?}", %s);\n""" % self.name
                 )


if __name__ == "__main__":
    rss = []
    for i in range(1_000_0):
        r = RS(f"Test{i}")
        rss.append(r)
    with open("main.rs", "w") as fh:
        for r in rss:
            r.emit_decl(fh)
        fh.write("fn main() {\n")
        for r in rss:
            r.emit_use(fh)
        fh.write("}")
