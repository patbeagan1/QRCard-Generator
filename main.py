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
        f.write("<body class=\"flex-container\">")
        write_css(f)
        write_single_item(f, items)
        f.write("</body>")
        f.write("</html>")


def write_css(f):
    f.write("""
<style>
img {
    max-height: 150px;     
    max-width: 150px;     
}
img.qr {
    height: 150px;     
    width: 150px;     
}
.flex-container {
    display: inline-flex;
    flex-wrap: wrap;
    background-color: white;
}       
.flex-container > a {
    text-align: center;
    border-radius: 10px;
    overflow: hidden;
    background-color: #ffffff;
    margin: 10px;
    overflow-wrap: break-word;
    break-inside: avoid;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 10px 0 rgba(0, 0, 0, 0.19);
}
a > div {
    break-inside: avoid;
}
div > p {
    text-align: left;
}
p{
    inline-size: 280px;
    margin: 2px 10px 2px 10px;
}
.img-row {
    display: inline-flex;
    border-bottom: 1px solid #cfcfcf
}
.img-sizer {
    width: 150px;
    background: #eeeeee;
}
.centered-element {
    margin: 0;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
}
</style>
""")


def write_single_item(f, items):
    for index, each in enumerate(items):
        f.write(f"""
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
""")


if __name__ == '__main__':
    os.makedirs(build_dir, exist_ok=True)
    for i in sys.argv[1:]:
        items = read_items(i)
        create_qr_codes(items)
        write_to_file(items)
