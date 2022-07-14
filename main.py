import os
import sys
import subprocess

build_dir = "build"


def read_items(filename: str):
    with open(filename, "r") as f:
        readlines = f.readlines()
        return [i.split(",") for i in readlines]


def in_build_dir(filename: str):
    return "{0}/{1}".format(build_dir, filename)


def get_qr_output_file_name(index: int):
    return f"out-{index}.png"


def create_qr_codes(items):
    for index, value in enumerate(items):
        subprocess.run(["qrencode",
                        "-o",
                        in_build_dir(get_qr_output_file_name(index)),
                        value[0]])


def write_to_file(items):
    with open(in_build_dir("index.html"), "w") as f:
        f.write("<html>")
        f.write("<body>")
        f.write("<div class=\"masonry\">")
        write_css(f)
        write_single_item(f, items)
        f.write("</div>")
        f.write("""<div style="width: 8.5in; background: yellow">hello world</div>""")
        f.write("</body>")
        f.write("</html>")


def write_css(f):
    f.write("""
<style>
img {
    max-height: 1in;     
    max-width: 1in;     
}
img.qr {
    height: 1in;     
    width: 1in;     
}
.masonry {
    display: inline-block;
    flex-wrap: wrap;
    background-color: white;
    column-count: 4;
    column-gap: 0px;
    padding-bottom: 20px;
}       
.masonry > div > a {
    width: 2in;
    display: flex;
    text-align: center;
    overflow: hidden;
    background-color: #ffffff;
    margin: 8px;
    overflow-wrap: break-word;
    break-inside: avoid;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.1), 0 4px 4px 0 rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    border: 1px solid #aaaaaa;
}
div > a {
    break-inside: avoid;
}
a > div {
    width: 2in;
}
div > p {
    text-align: left;
}
p {
    font-size: 0.8em;
    inline-size: 1.8in;
    margin: 2px 10px 2px 10px;
}
.img-row {
    display: inline-flex;
    border-bottom: 1px solid #cfcfcf
}
.img-sizer {
    width: 1in;
    background: #eeeeee;
}
.centered-element {
    margin: 0;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
}
@media only screen and (min-width: 8.401in) { .masonry { column-count: 4; } }
@media only screen and (min-width: 6.378in) and (max-width: 8.400in) { .masonry { column-count: 3; } }
@media only screen and (min-width: 4.251in) and (max-width: 6.377in) { .masonry { column-count: 2; } }
@media only screen and (min-width: 0in) and (max-width: 4.25in) { .masonry { column-count: 1; } }
.card-wrapper {
    width: 2in;
    display: inline-block;
}
</style>
""")


def write_single_item(f, items):
    for index, each in enumerate(items):
        f.write(f"""
<div class="card-wrapper">
    <a href="{each[0]}">
        <div>
            <div class="img-row">
                <div class="img-sizer">
                    <img class="centered-element" src="{each[1]}"/> 
                </div>
                <img class="qr" src="{get_qr_output_file_name(index)}"/>
            </div>
            <p>{each[0]}</p>
        </div>
    </a>
</div>
""")


if __name__ == '__main__':
    os.makedirs(build_dir, exist_ok=True)
    for i in sys.argv[1:]:
        items = read_items(i)
        create_qr_codes(items)
        write_to_file(items)
