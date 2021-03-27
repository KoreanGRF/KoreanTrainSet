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
for code_name in trainList:
    trainListData[code_name] = []

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

# Parse all language files
langData = {}
languageFiles = glob.iglob(_ROOT + 'lang/*.lng', recursive=True)
for _langFile in languageFiles:
    _lang = os.path.splitext(os.path.basename(_langFile))[0]
    langData[_lang] = parse_lang(_lang)


# Get string language file
def get_string(string_id, lang):
    global langData
    string_val = ''
    if string_id in langData[lang]:
        return langData[lang][string_id]
    else:
        if string_id in langData['english']:
            return langData['english'][string_id]
    return ''


# Find all *.pnml files
print('  Cropping purchase image ... ', end='')
pnmlFiles = glob.iglob(_ROOT + '**/*.pnml', recursive=True)
for file_name in pnmlFiles:
    f = open(file_name, 'r')
    pnml_content = f.read()

    # Find purchase image block
    rst = re.finditer('spriteset\(set_(.+?)_purchase,(?:\s+)"(.+?)"\) {', pnml_content)
    for r in rst:
        sprite_name      = r.group(1)
        sprite_file_name = r.group(2)

        print(sprite_name, end=', ')

        # Slice only template definition
        _from = r.end()
        _to   = pnml_content.find('}', _from+1)
        if _to == -1:
            continue

        # Get template name
        template_block = pnml_content[_from:_to].strip()
        _from = template_block.find('(')
        _to   = template_block.find(')')
        template_name = template_block[0:_from].strip()
        
        # Get coordinates
        template_coords = template_block[_from+1:_to]
        coords = [None, None, None, None, None, None]
        coords_input = re.split(',\s*', template_coords)
        coords[:len(coords_input)] = coords_input
        x = coords[0]
        y = coords[1]
        w = coords[2]
        h = coords[3]
        # t = coords[4]   # Not used in this file
        # l = coords[5]   # Not used in this file

        # tmpl_metro_purchase()
        if template_name == 'tmpl_metro_purchase':
            x = 0
            y = 0
            w = 50
            h = 15
        
        # tmpl_purchase_for_singlehead(x, y), tmpl_purchase_for_dualhead(x, y)
        elif template_name == 'tmpl_purchase_for_singlehead' or template_name == 'tmpl_purchase_for_dualhead':
            w = 50
            h = 15

        # tmpl_purchase_detail(x, y, w, h, t, l)
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        # Check image size
        if isinstance(w, int) and isinstance(h, int) and w > 0 and h > 0:
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
            code_name = re.sub(r"K([2-8])X00", r"K\1x00", code_name)

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
    <tr data-veh_id="{{code_name}}">
        <td class="refit">{{refit}}</td>
        <td class="name">{{string}}</td>
        <td class="speed">{{speed}}</td>
        <td class="speed_designed">{{speed_designed}}</td>
        <td class="capacity">{{capacity}}</td>
        <td class="power">{{power}}</td>
        <td class="weight">{{weight}}</td>
        <td class="introduction">{{introduction}}</td>
    </tr>"""

# Generate doc file by language
for _lang in list(langData.keys()):
    output = "<table class=\"ko_train_set\">"
    print('  Generate ' + _lang + ' document')
    for code_name in trainListData:
        _spec = trainList[code_name]

        # Get name
        string = get_string('STR_' + code_name + '_NAME', _lang).replace('[KTS] ', '')

        # Get variables
        speed          = str(_spec[0]) + ' km/h' if _spec[0] is not None and _spec[0] > 0 else ''
        speed_designed = str(_spec[1]) + ' km/h' if _spec[1] is not None and _spec[1] > 0 else ''
        capacity       = str(_spec[4])           if _spec[4] is not None and _spec[4] > 0 else ''
        power          = str(_spec[6]) + ' kW'   if _spec[6] is not None and _spec[6] > 0 else ''
        weight         = str(_spec[7]) + ' t'
        introduction   = str(_spec[8][0])        if _spec[8] is not None                  else ''

        # Change variables
        append = template
        append = append.replace('{{code_name}}', code_name.upper())
        append = append.replace('{{string}}', string)
        append = append.replace('{{speed}}', speed)
        append = append.replace('{{speed_designed}}', speed_designed)
        append = append.replace('{{capacity}}', capacity)
        append = append.replace('{{power}}', power)
        append = append.replace('{{weight}}', weight)
        append = append.replace('{{introduction}}', introduction)

        # Append all refittable vehicles
        refit = ""
        for sprite_name in trainListData[code_name]:
            refit += '<img src="./_static/' + sprite_name + '.png" alt="' + string + '">\n'

        # Append a train
        append = append.replace('{{refit}}', refit.strip().replace('\n', '<br />'))
        output += append

    # Write a doc file
    f = open(_ROOT + "generated/download_page/" + _lang + ".html", "w")
    f.write(output + "\n</table>")
    f.close()
