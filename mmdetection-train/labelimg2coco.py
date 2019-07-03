import os
import xml.etree.ElementTree as ET
import xmltodict
import json
from xml.dom import minidom
from collections import OrderedDict

def generateVOC2Json(rootDir, xmlFiles, jsonFile):
    attrDict = dict()
    attrDict["categories"] = [{"supercategory": "defect", "id": 1, "name": "aeroplane"},
                              {"supercategory": "defect", "id": 2, "name": "bicycle"},
                              {"supercategory": "defect", "id": 3, "name": "bird"},
                              {"supercategory": "defect", "id": 4, "name": "boat"},
                              {"supercategory": "defect", "id": 5, "name": "bottle"},
                              {"supercategory": "defect", "id": 6, "name": "bus"},
                              {"supercategory": "defect", "id": 7, "name": "car"},
                              {"supercategory": "defect", "id": 8, "name": "cat"},
                              {"supercategory": "defect", "id": 9, "name": "chair"},
                              {"supercategory": "defect", "id": 10, "name": "cow"},
			      {"supercategory": "defect", "id": 11, "name": "diningtable"},
                              {"supercategory": "defect", "id": 12, "name": "dog"},
                              {"supercategory": "defect", "id": 13, "name": "horse"},
                              {"supercategory": "defect", "id": 14, "name": "motorbike"},
                              {"supercategory": "defect", "id": 15, "name": "person"},
                              {"supercategory": "defect", "id": 16, "name": "pottedplant"},
                              {"supercategory": "defect", "id": 17, "name": "sheep"},
                              {"supercategory": "defect", "id": 18, "name": "soft"},
                              {"supercategory": "defect", "id": 19, "name": "train"},
                              {"supercategory": "defect", "id": 20, "name": "tvmonitor"},
                              {"supercategory": "defect", "id": 21, "name": "truck"},
			      {"supercategory": "defect", "id": 22, "name": "tricar"},
                              {"supercategory": "defect", "id": 23, "name": "backmirror"},
                              {"supercategory": "defect", "id": 24, "name": "paperbox"},
                              {"supercategory": "defect", "id": 25, "name": "lightcover"},
                              {"supercategory": "defect", "id": 26, "name": "windglass"},
                              {"supercategory": "defect", "id": 27, "name": "hungs"},
                              {"supercategory": "defect", "id": 28, "name": "anusigns"},
                              {"supercategory": "defect", "id": 29, "name": "entrylisence"},
                              {"supercategory": "defect", "id": 30, "name": "safebelt"},
                              {"supercategory": "defect", "id": 31, "name": "plate"},
                              {"supercategory": "defect", "id": 32, "name": "carlight"},
                              {"supercategory": "defect", "id": 33, "name": "cartopwindow"},
			      {"supercategory": "defect", "id": 34, "name": "carrier"},
                              {"supercategory": "defect", "id": 35, "name": "newersign"},
                              {"supercategory": "defect", "id": 36, "name": "wheel"},
                              {"supercategory": "defect", "id": 37, "name": "layon"},
                              {"supercategory": "defect", "id": 38, "name": "bigplate"},
                              {"supercategory": "defect", "id": 39, "name": "traffic cone"},
                              {"supercategory": "defect", "id": 40, "name": "stroller"},
                              {"supercategory": "defect", "id": 41, "name": "wheelchair"},
                              {"supercategory": "defect", "id": 42, "name": "trolley"}
                              ]


    images = list()
    annotations = list()
    for root, dirs, files in os.walk(rootDir):
        image_id = 0
        for file in xmlFiles:
            image_id = image_id + 1
            if file in files:
                # image_id = image_id + 1
                annotation_path = os.path.abspath(os.path.join(root, file))

                # tree = ET.parse(annotation_path)#.getroot()
                image = dict()
                doc = xmltodict.parse(open(annotation_path).read())
                image['file_name'] = file.split('.')[0] + '.jpg'
                image['height'] = int(doc['annotation']['size']['height'])
                image['width'] = int(doc['annotation']['size']['width'])
                image['id'] = image_id
                images.append(image)

                print("File Name: {} and image_id {}".format(file, image_id))

                id1 = 1
                if 'object' in doc['annotation']:
                    objects = doc['annotation']['object']
                    if isinstance(objects, OrderedDict):
                        obj = objects
                        objects = list()
                        objects.append(obj)

                    for obj in objects:
                        for value in attrDict["categories"]:
                            annotation = dict()
                            if str(obj['name']) == value["name"]:
                                # annotation["segmentation"] = []
                                annotation["iscrowd"] = 0
                                annotation["image_id"] = image_id
                                x = int(obj["bndbox"]["xmin"])
                                y = int(obj["bndbox"]["ymin"])
                                w = int(obj["bndbox"]["xmax"]) - x + 1
                                h = int(obj["bndbox"]["ymax"]) - y + 1
                                annotation["bbox"] = [x, y, w, h]
                                annotation["area"] = float(w * h)
                                annotation["category_id"] = value["id"]
                                annotation["ignore"] = 0
                                annotation["segmentation"] = [[x, y, x, (y + h - 1), (x + w - 1), (y + h - 1), (x + w - 1), y]]
                                annotation["id"] = id1
                                id1 += 1

                                annotations.append(annotation)
                else:
                    print("File: {} doesn't have any object".format(file))
            else:
                print("File: {} not found".format(file))
    attrDict["images"] = images
    attrDict["annotations"] = annotations
    attrDict["type"] = "instances"
    jsonString = json.dumps(attrDict)

    with open(jsonFile, "w") as f:
        f.write(jsonString)

    print("Completed. ")


File = "trainval.txt"

XMLFiles = list()
with open(File, "r", encoding='UTF-8') as f:
    for line in f:
        fileName = line.strip()
        print(fileName)
        XMLFiles.append(fileName + ".xml")

rootDir = "Annotations"
jsonFile = "train2019.json"
if os.path.exists(jsonFile):
    os.remove(jsonFile)

generateVOC2Json(rootDir, XMLFiles, jsonFile)
