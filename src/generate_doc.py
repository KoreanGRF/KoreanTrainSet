"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""
import glob
import re
import os
import spec
from PIL import Image

_ROOT = os.path.dirname(os.path.abspath(__file__))[:-3]

for file_name in glob.iglob(_ROOT + '**/*.pnml', recursive=True):
	f = open(file_name, 'r')
	pnml_content = f.read()

	# Find purchase block
	rst = re.finditer('spriteset\(set_(.+?)_purchase,(?:\s+)"(.+?)"\) \{\n\s+(tmpl_purchase(?:.*?)\(0, (\d+)(, (\d+), (\d+), (\-[0-9]+), (\-[0-9]+))?\)|tmpl_metro_purchase\(\))\n}', pnml_content)

	for r in rst:
		code_name = r.group(1)
		sprite_file_name = r.group(2)
		print(' Cropping purchase image of ' + code_name + ' in ./' + file_name.replace(_ROOT, ''))
		
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

		if w > 0 and h > 0:
			img = Image.open(_ROOT + sprite_file_name[2:])
			
			# Check if valid image
			if img.size[0] == 0 or img.size[1] == 0:
				print('Image is not valid')
				continue
			purchase_img = img.crop((x, y, x+w, y+h))
			purchase_img.save(_ROOT + 'generated/download_page/_static/' + code_name + '.png', 'png')
		else:
			print('Purchase image is not cropped for some reason.')
			print(r, 'x=' + str(x) + ', y=' + str(y) + ', w=' + str(w) + ', h=' + str(h))
