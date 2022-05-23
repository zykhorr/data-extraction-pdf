from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from lxml import html
import re
import pandas as pd


def convert2html(filename):
    output = StringIO()
    with open(filename+'.pdf', 'rb') as pdf_file:
        extract_text_to_fp(pdf_file, output, laparams=LAParams(), output_type='html', codec=None)
    with open(filename+'.html', 'a') as html_file:
        html_file.write(output.getvalue())

    raw_html = output.getvalue()
    tree = html.fromstring(raw_html)
    divs = tree.xpath('.//div')

    return divs


def extract_data(divs, left1, left2, top1, top2):
    content_list = []
    for div in divs:
        div_style = div.get('style')

        try:
            left = int(re.findall(r'left:([\d]+)px', div_style)[0])
            top = int(re.findall(r'top:([\d]+)px', div_style)[0])

            if left1 <= left <= left2 and (top1 <= top <= top2):
                content = str(div.text_content())
                content_list.append(content)

        except IndexError:
            continue

    return content_list


def split_remove(content_list):
    new_list = []
    for value in content_list:
        in_value = value.split('\n')

        for v in in_value:
            if v != '':
                new_list.append(v)

    return new_list


if __name__ == '__main__':
    divs = convert2html('pdf1')
    header_data = extract_data(divs, 420, 420, 110, 179)
    value_data = extract_data(divs, 478, 478, 111, 111)
    headers = split_remove(header_data)
    values = split_remove(value_data)
    df = pd.DataFrame(data=[values], columns=[headers])
    df.to_csv('pdf1.csv', index=False)

    print(df)
