"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""
import glob
import re
import os
from spec import *
from PIL import Image

# _ROOT path
_ROOT = os.path.dirname(os.path.abspath(__file__))[:-3]

# Initialise
notInTrainList = []
trainListData = {}

# Parse language file
def parse_lang(lang):
    langData = {}
    f = open(_ROOT + 'lang/' + lang + '.lng', 'r')
    lines = f.readlines()
    for _line in lines:
        _line = _line.strip()
        if _line.startswith('#') or not _line:   # Skip comments
            continue
        _tmp = _line.split(':')
        _key = _tmp[0].strip()
        _val = _tmp[1]
        langData[_key] = _val
    return langData

langData = {
    'english': parse_lang('english'),
    'korean':  parse_lang('korean')
}

# Get string language file
def get_string(string_id, lang):
    global langData
    string_val = ''
    if string_id in langData[lang]:
        return langData[lang][string_id]
    else:
        if string_id in langData['english']:
            return langData['english'][string_id]
    return '<Unknown string>'

print('  Cropping purchase image ... ', end='')

# Find all *.pnml files
for file_name in glob.iglob(_ROOT + '**/*.pnml', recursive=True):
    f = open(file_name, 'r')
    pnml_content = f.read()

    # Find purchase block
    rst = re.finditer('spriteset\(set_(.+?)_purchase,(?:\s+)"(.+?)"\) \{\n\s+(tmpl_purchase(?:.*?)\(0, (\d+)(, (\d+), (\d+), (\-[0-9]+), (\-[0-9]+))?\)|tmpl_metro_purchase\(\))\n}', pnml_content)

    for r in rst:
        sprite_name = r.group(1)         # (eg) 1K_RHEO_FIRST_1
        sprite_file_name = r.group(2)    # (eg) (ROOT)src/metro/seoul1+/1K_RHEO_FIRST_1.png
        print(sprite_name, end=', ')
        # print(' Cropping purchase image of ' + sprite_name + ' in ./' + file_name.replace(_ROOT, ''))
        
        # tmpl_metro_purchse()
        if r.group(3) == 'tmpl_metro_purchse()':
            x = 0
            y = 0
            w = 50
            h = 15
        
        # Locomotive template
        else:
            # tmpl_purchase_detail(0, y, x, h, t, l)
            if r.group(5) != None:
                x = 0
                y = int(r.group(4))
                w = int(r.group(6))
                h = int(r.group(7))
            
            # tmpl_purchase(0, 0)
            else:
                x = 0
                y = 0
                w = 50
                h = 15

        # Check image size
        if w > 0 and h > 0:
            img = Image.open(_ROOT + sprite_file_name[2:])
            
            # Check if valid image
            if img.size[0] == 0 or img.size[1] == 0:
                print('Image is not valid')
                continue

            # Crop purchase image and save into png file
            purchase_img = img.crop((x, y, x+w, y+h))
            
            # Make transparent image
            purchase_img = purchase_img.convert('RGBA')
            datas = purchase_img.getdata()
            newData = []
            for item in datas:
                if item[0] == 0 and item[1] == 0 and item[2] == 255:
                    newData.append((0, 0, 0, 0))
                else:
                    newData.append(item)
            purchase_img.putdata(newData)

            # Save purchase image
            purchase_img.save(_ROOT + 'generated/download_page/_static/' + sprite_name + '.png', 'png')

            # Parse `code_name`
            code_name = os.path.splitext(os.path.basename(file_name))[0]
            code_name = re.sub('(_graphic|_switch)$', '', code_name)
            code_name = code_name.replace("-", "_").upper()
            code_name = re.sub(r"K(7|8)X00", r"K\1x00", code_name)

            # Check if there is a trainList data named `code_name`
            if not code_name in trainList:
                notInTrainList.append(code_name)
            else:
                if not code_name in trainListData:
                    trainListData[code_name] = []
                trainListData[code_name].append(sprite_name)

        else:
            print('Purchase image is not cropped for some reason.')
            print(r, 'x=' + str(x) + ', y=' + str(y) + ', w=' + str(w) + ', h=' + str(h))
print()

# Print warning
for code_name in notInTrainList:
    print(' .. ' + code_name + ' is not in trainList!')

# Make a table
template = """
        <tr data-veh_id="{{code_name}}" data-refittable="{{refittable}}">
            <td class="align-center">{{refit}}</td>
            <td>{{string}}</td>
            <td class="align-center">{{speed}}</td>
            <td class="align-center">{{capacity}}</td>
            <td class="align-center">{{power}}</td>
            <td class="align-center">{{introduction}}</td>
        </tr>"""

for _lang in list(langData.keys()):
    output = "<table>"
    print('  Generating ' + _lang + ' document')
    for code_name in trainListData:
        string = get_string('STR_' + code_name + '_NAME', _lang).replace('[KTS] ', '')
        if len(trainListData[code_name]) > 1:
            refittable = "1"
        else:
            refittable = "0"
        speed        = str(trainList[code_name][0]) if trainList[code_name][0] is not None and trainList[code_name][0] > 0 else ''
        capacity     = str(trainList[code_name][3]) if trainList[code_name][3] is not None and trainList[code_name][3] > 0 else ''
        power        = str(trainList[code_name][5]) + ' kW' if trainList[code_name][5] is not None and trainList[code_name][5] > 0 else ''
        introduction = str(trainList[code_name][6][0])

        append = template
        append = append.replace('{{code_name}}', code_name.upper())
        append = append.replace('{{string}}', string)
        append = append.replace('{{speed}}', speed)
        append = append.replace('{{capacity}}', capacity)
        append = append.replace('{{power}}', power)
        append = append.replace('{{introduction}}', introduction)

        refit = ""
        for sprite_name in trainListData[code_name]:
            refit += '<img src="./_static/' + sprite_name + '.png" alt="' + string + '">\n'

        append = append.replace('{{refit}}', refit.strip().replace('\n', '<br />'))
        output += append

    f = open(_ROOT + "generated/download_page/" + _lang + ".html", "w")
    f.write(output + "</table>")
    f.close()
