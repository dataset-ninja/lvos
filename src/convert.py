# from dataset_tools.convert import unpack_if_archive
# import src.settings as s
# from urllib.parse import unquote, urlparse
# from supervisely.io.fs import get_file_name, get_file_size
import supervisely as sly
import os
import cv2
import random
import colorsys
import numpy as np
import imagesize
from glob import glob
import json
import tqdm

# def download_dataset(teamfiles_dir: str) -> str:
#     """Use it for large datasets to convert them on the instance"""
#     api = sly.Api.from_env()
#     team_id = sly.env.team_id()
#     storage_dir = sly.app.get_data_dir()

#     if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
#         parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
#         file_name_with_ext = os.path.basename(parsed_url.path)
#         file_name_with_ext = unquote(file_name_with_ext)

#         sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
#         local_path = os.path.join(storage_dir, file_name_with_ext)
#         teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

#         fsize = api.file.get_directory_size(team_id, teamfiles_dir)
#         with tqdm(
#             desc=f"Downloading '{file_name_with_ext}' to buffer...",
#             total=fsize,
#             unit="B",
#             unit_scale=True,
#         ) as pbar:
#             api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
#         dataset_path = unpack_if_archive(local_path)

#     if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
#         for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
#             local_path = os.path.join(storage_dir, file_name_with_ext)
#             teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

#             if not os.path.exists(get_file_name(local_path)):
#                 fsize = api.file.get_directory_size(team_id, teamfiles_dir)
#                 with tqdm(
#                     desc=f"Downloading '{file_name_with_ext}' to buffer...",
#                     total=fsize,
#                     unit="B",
#                     unit_scale=True,
#                 ) as pbar:
#                     api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

#                 sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
#                 unpack_if_archive(local_path)
#             else:
#                 sly.logger.info(
#                     f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
#                 )

#         dataset_path = storage_dir
#     return dataset_path


# def count_files(path, extension):
#     count = 0
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(extension):
#                 count += 1
#     return count


# def create_oc_dict(dataset_path):
#     subdatasets = [f.path for f in os.scandir(dataset_path) if f.is_dir]
#     for idx, subds_path in enumerate(subdatasets):
#         subds_name = os.path.basename(subds_path)
#         subds_path = os.path.join(subds_path, "JPEGImages")
#         subfolders = [os.path.basename(f.path) for f in os.scandir(subds_path) if f.is_dir()]
#         for i, subfolder in enumerate(subfolders):
#             # obj_class = sly.ObjClass(name="", geometry_type=sly.Bitmap, color=random_color())
#             values = classes_map.setdefault(subds_name, {}).setdefault(subfolder, [])
#             values.append("class_name_1")
#             # values.append(sly.VideoObject(obj_class))
#             # obj_classes_meta.extend([obj_class])


# classes_map = {
#     "test": {
#         "058oeZ2p": ["microphone"],
#         "58jpr19X": ["motorboat"],
#         "5NImTLT6": ["cue ball"],
#         "5VwnMLaz": ["kangaroo"],
#         "6mNj04tC": ["fish"],
#         "711gAS21": ["baby shark"],
#         "7im4LEcb": ["panda"],
#         "81Oju1e7": ["person"],
#         "8kv99Cop": ["person", "surfboard"],
#         "AIv9mv7T": ["sheep"],
#         "aSNxf5ms": ["person"],
#         "B9fFIrgq": ["basketball"],
#         "bDv75KJl": ["giraffe"],
#         "ealukzgh": ["baby elephant"],
#         "FmzvB44A": ["zebra"],
#         "GchnEETZ": ["que ball"],
#         "GmfSNNa3": ["skateboard"],
#         "gUca15ef": ["monkey"],
#         "gw84JOqH": ["gorilla"],
#         "Gz3GEPPC": ["basketball"],
#         "HQ2UJdrW": ["person", "que ball"],
#         "irsQQbUO": ["car"],
#         "JefVS4hq": ["sheep"],
#         "Kz1wgslb": ["person"],
#         "LWVlKBlK": ["frisbee"],
#         "MI0uwoMt": ["que ball"],
#         "Oj1z5fO0": ["baby zebra"],
#         "PhiOlFlA": ["person", "person"],
#         "PQPOuFNO": ["fighter jet", "fighter jet"],
#         "qeD7QcDW": ["lion"],
#         "R3UJGYwy": ["microphone"],
#         "R4xwHrdP": ["sheep"],
#         "RCgebO9V": ["person"],
#         "shW04XAm": ["person"],
#         "T4pEUdxQ": ["giraffe"],
#         "T9woxlyM": ["person", "person"],
#         "tAyQIobn": ["zebra"],
#         "TVfoBiU2": ["elephant"],
#         "UBITNvZb": ["person", "umbrella"],
#         "UtEnRpiP": ["cup"],
#         "UykV25jo": ["person"],
#         "vlKROEmy": ["car", "car"],
#         "w3XiaDdm": ["cur ball"],
#         "xL5OHe3Y": ["person"],
#         "Y6tOZtQV": ["cue ball"],
#         "yfzVCnvU": ["fish"],
#         "YHUoFe2u": ["giraffe"],
#         "YMRntd88": ["tiger"],
#         "yWnanBID": ["fish"],
#         "yxCvN6OJ": ["frisbee"],
#     },
#     "train": {
#         "0qiJ95fE": ["car"],
#         "0sfNjoxO": ["person", "surfboard"],
#         "1aIerTPX": ["motorboat"],
#         "1Bz1hUWb": ["person", "skateboard"],
#         "1Cs9eroK": ["bear"],
#         "1ZjnVUCR": ["giraffe"],
#         "26Q5crVV": ["person"],
#         "2fiwgaIN": ["giraffe"],
#         "2K6Fl595": ["car"],
#         "2pMiy6eH": ["person", "kite"],
#         "2vt1LoVz": ["baby"],
#         "38445wgB": ["goat"],
#         "3Y3D5llb": ["person"],
#         "4B5Yhjx3": ["fighter jet"],
#         "4QfDSwLI": ["person", "umbrella"],
#         "5twR3usf": ["car"],
#         "5vhETIqa": ["motorboat"],
#         "5wjt5SL1": ["sailboat"],
#         "65DBEapy": ["motorbike"],
#         "6A1OmuOM": ["person"],
#         "73odGVzM": ["sheep"],
#         "7pURsJK1": ["person"],
#         "8O5opvsQ": ["giraffe"],
#         "8oE0wDAF": ["bicycle"],
#         "8TrHEtoY": ["car"],
#         "8xvF6EwY": ["car"],
#         "9AjqzjeF": ["person"],
#         "9DvvNIo8": ["kangaroo"],
#         "9fAADSRD": ["person"],
#         "a67jsI9o": ["motorboat"],
#         "AZCzuD65": ["person"],
#         "bGscYB9F": ["person", "skateboard"],
#         "BmjKtOYM": ["motorboat"],
#         "C5Fy1dMd": ["motorbike"],
#         "c5i9QGyC": ["car"],
#         "CMwJ6uGh": ["kangaroo"],
#         "d6D5mjyW": ["kid"],
#         "EBsWTunP": ["person", "surfboard"],
#         "et9PpeEO": ["warship"],
#         "EZJnoj9u": ["person"],
#         "fcUOEAIv": ["elephant"],
#         "fQVilF4a": ["kid", "umbrella"],
#         "FWdWToxr": ["bear"],
#         "goBLKpz1": ["tiger"],
#         "hP6JJw8p": ["person", "kid"],
#         "hpzholup": ["person", "kid"],
#         "HYo3SdRN": ["elephant"],
#         "HYxp6TRq": ["kite"],
#         "I4LB4YMo": ["person"],
#         "iFk0iwmQ": ["kite"],
#         "IgnZEtEk": ["sailboat"],
#         "IkXZMC5o": ["person", "basketball"],
#         "jjsLuuoN": ["person"],
#         "Kibc9L9k": ["cue ball"],
#         "KlhduiNN": ["monkey"],
#         "KuZcFWzo": ["corn duster"],
#         "KVfDKpDH": ["lion"],
#         "lL7u6APJ": ["person", "person"],
#         "LuW1amTA": ["tiger"],
#         "lwZsQteO": ["car"],
#         "M2yxKpVR": ["baby"],
#         "md6PGONo": ["person", "umbrella"],
#         "ML7rr9vL": ["person", "motorbike"],
#         "MQgiTlie": ["person"],
#         "n1APyt91": ["kite"],
#         "n5nz1xJi": ["umbrella"],
#         "n7nWyjSa": ["bear"],
#         "NNkYxBvO": ["elephant"],
#         "nWK3ga8b": ["person", "kite"],
#         "o5diSyjE": ["person", "surfboard"],
#         "okdEUp4G": ["car"],
#         "Ou8mekrW": ["person", "skateboard"],
#         "PEyHFztC": ["kid", "kid"],
#         "PWbTG2c7": ["motorboat"],
#         "Qap2pPBC": ["elephant"],
#         "qI9iVBp4": ["elephant"],
#         "qK05GHIN": ["bear cub"],
#         "QSCXmdjb": ["car"],
#         "qSL6X2A2": ["kid", "kid"],
#         "r1droTMS": ["person"],
#         "r2dmXYRk": ["baby monkey"],
#         "R9vNG4Ho": ["baby", "toy motorbike"],
#         "rLXm1lSX": ["motorboat"],
#         "Rmwyr11U": ["kangaroo"],
#         "rNs16dCv": ["person", "surfboard"],
#         "rUOsJ0qK": ["person", "surfboard"],
#         "saQ7JfTQ": ["motorboat"],
#         "sBWHgEwJ": ["baby giraffe"],
#         "sfSEiJgA": ["person", "surfboard"],
#         "STkgoC15": ["person", "basketball"],
#         "TkEbZ87A": ["tiger"],
#         "TldqmxbE": ["motorboat"],
#         "tUkFCYL6": ["car"],
#         "u9ZlyjGI": ["fighter jet"],
#         "UfWJI2YV": ["kite"],
#         "UrKAenln": ["fighter jet"],
#         "urruYOTY": ["lion"],
#         "v81zWb2C": ["cue ball"],
#         "w5XzZXEE": ["person"],
#         "wAHVI3BV": ["tiger"],
#         "WmNwuMQx": ["person", "basketball"],
#         "wNpKciYV": ["car"],
#         "wnwkQ4jM": ["lion"],
#         "WuWp4Oq3": ["car"],
#         "XfbRshfV": ["person", "person"],
#         "xfH7II2g": ["person"],
#         "XkFsOwfw": ["car"],
#         "xrqrzFnL": ["lion"],
#         "Y0WMiBdR": ["person"],
#         "y2Ai61Xm": ["bear"],
#         "Yprjyg9u": ["fighter jet"],
#         "yWPaUTDz": ["person"],
#         "yYZUeb48": ["kite"],
#         "yzDaKIdv": ["person", "kite"],
#         "ZeODULHT": ["tiger"],
#         "ZKKwNxKA": ["fighter jet"],
#         "ZL56eLoQ": ["car"],
#         "zPkZoeOu": ["person", "surfboard"],
#         "zuL99fYA": ["motorboat"],
#         "zx8dtV5J": ["car"],
#     },
#     "valid": {
#         "0tCWPOrc": ["person", "surfboard"],
#         "3nsHQkEK": ["cue ball"],
#         "3Zf4NFzn": ["fighter jet"],
#         "48f9Llhg": ["giraffe"],
#         "49TNsJzk": ["bear cub"],
#         "7BcOR5aJ": ["cue ball"],
#         "7K7WVzGG": ["person", "person"],
#         "8lxxCA5h": ["zebra"],
#         "8MfWMkrt": ["sheep"],
#         "9mBuSvT2": ["bear"],
#         "aFytsETk": ["cup"],
#         "aT6JIUVU": ["sheep"],
#         "bl6VuRYE": ["baby elephant"],
#         "cjD5WPSv": ["giraffe"],
#         "cUD1dwuP": ["person", "person"],
#         "D4AgqLQL": ["sheep"],
#         "d83wYdy0": ["car"],
#         "dtHbJvYy": ["fish"],
#         "EWCZAcdt": ["person", "skateboard"],
#         "f4DjwV55": ["kangaroo"],
#         "FFMl5yqs": ["football"],
#         "FiRTBMg2": ["flag", "flag"],
#         "gdqCcvs2": ["frisbee"],
#         "Gy1gwYZD": ["basketball"],
#         "HNrCxhwd": ["cue ball"],
#         "ikcMMycg": ["football"],
#         "JGG6MrhF": ["fish"],
#         "K3OUeINk": ["microphone"],
#         "KfcCU1ma": ["kite", "kite"],
#         "kozmQMck": ["tiger"],
#         "KPDIQo5u": ["person", "person"],
#         "MKnlVo6x": ["monkey"],
#         "N6CONZUW": ["zebra"],
#         "NFbsxmYE": ["lion"],
#         "nfcT3owb": ["fish"],
#         "pMntJwSQ": ["frisbee"],
#         "q1MSEBkh": ["basketball"],
#         "Q3kk9fuH": ["cueball"],
#         "raql9H7f": ["person", "person"],
#         "rUaDdVmD": ["motorboat"],
#         "ScFTYisJ": ["baby elephant"],
#         "v3uNUctx": ["fish"],
#         "Vh9NwLSn": ["skateboard"],
#         "VhwRKgVS": ["person", "surfboard"],
#         "vJ8W2TO5": ["baby zebra"],
#         "vjG0jbkQ": ["person", "umbrella"],
#         "x3nD3QQ9": ["motorbike"],
#         "X5U0z8VI": ["panda"],
#         "xpI7xRWN": ["microphone"],
#         "yExgitit": ["sheep"],
#     },
# }

# def get_objclass_list_and_update_map(classes_map):
#     unique_values = set()

#     for subdict in classes_map.values():
#         for values_list in subdict.values():
#             unique_values.update(values_list)

#     obj_class_mapping = {
#         value: sly.ObjClass(name=value, geometry_type=sly.Bitmap, color=random_color())
#         for value in unique_values
#     }

#     # Replace strings in the original dictionary
#     for key, subdict in classes_map.items():
#         for subkey, values_list in subdict.items():
#             obj_class_instances = [obj_class_mapping[value] for value in values_list]
#             classes_map[key][subkey] = obj_class_instances

#     obj_class_list = list(obj_class_mapping.values())

#     return obj_class_list


def separate_masks(mask_path):
    mask = cv2.imread(mask_path)

    hsv_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)

    color_ranges = {
        "green": (np.array([40, 50, 50]), np.array([80, 255, 255])),
        "red": (np.array([0, 50, 50]), np.array([10, 255, 255])),
        "yellow": (np.array([20, 100, 100]), np.array([30, 255, 255])),
        "blue": (np.array([110, 50, 50]), np.array([130, 255, 255])),
        "pink": (np.array([150, 50, 50]), np.array([170, 255, 255])),
    }

    grayscale_masks = []

    for lower, upper in color_ranges.values():
        color_mask = cv2.inRange(hsv_mask, lower, upper)

        cv2.destroyAllWindows()
        grayscale_mask = convert_mask_to_binary(color_mask)

        grayscale_masks.append(grayscale_mask)

    return grayscale_masks


def convert_mask_to_binary(mask):
    if isinstance(mask, str):
        mask = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)

    retval, binary_mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

    cv2.destroyAllWindows()

    return binary_mask


def create_ann(img_path, tag_values, obj_count):
    path_parts = img_path.split(os.sep)
    ann_path = os.path.join(
        dataset_path,
        path_parts[7],
        "Annotations",
        path_parts[9],
        (sly.fs.get_file_name(img_path) + ".png"),
    )
    split_tag_value, captions = tag_values
    split_tag = sly.Tag(subds_tag_meta, split_tag_value)

    width, height = imagesize.get(img_path)
    labels = []
    if os.path.exists(ann_path):
        if obj_count > 1:
            tags = [sly.Tag(id_tag_meta, (oc + 1)) for oc in range(obj_count)]
            masks = separate_masks(ann_path)
            for i, (mask, tag) in enumerate(zip(masks, tags)):
                if np.unique(mask).size == 2:
                    caption_tag = sly.Tag(caption_tag_meta, captions[i])
                    label = sly.Label(
                        geometry=sly.Bitmap(mask), obj_class=obj_class, tags=[tag, caption_tag]
                    )
                    labels.append(label)
        else:
            mask = convert_mask_to_binary(ann_path)
            if np.unique(mask).size == 2:
                caption_tag = sly.Tag(caption_tag_meta, captions[0])
                id_tag = sly.Tag(id_tag_meta, 1)
                label = sly.Label(sly.Bitmap(mask), obj_class, tags=[id_tag, caption_tag])
                labels.append(label)
    return sly.Annotation((height, width), labels, [split_tag])


def random_color():
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return [r, g, b]


def extract_captions(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)

    result_dict = {}

    for key, value in data.get("videos", {}).items():
        if "objects" in value and isinstance(value["objects"], dict) and value["objects"]:
            captions = [obj["caption"] for obj in value["objects"].values()]

            result_dict[key] = captions

    return result_dict


def count_objects(json_path):

    with open(json_path, "r") as file:
        data = json.load(file)

    result_dict = {}

    for key, value in data.get("videos", {}).items():
        if "objects" in value and isinstance(value["objects"], dict):
            num_objects = len(value["objects"])

            result_dict[key] = num_objects

    return result_dict


dataset_path = "/mnt/c/users/german/documents/videodataset"

subds_tag_meta = sly.TagMeta("sequence", sly.TagValueType.ANY_STRING)
caption_tag_meta = sly.TagMeta("caption", sly.TagValueType.ANY_STRING)
id_tag_meta = sly.TagMeta("id", sly.TagValueType.ANY_NUMBER)

obj_class = sly.ObjClass("object", sly.Bitmap, [0, 255, 0])


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    dataset_names = {"test": "test", "train": "train", "val": "valid"}

    meta = sly.ProjectMeta(
        obj_classes=[obj_class], tag_metas=[subds_tag_meta, caption_tag_meta, id_tag_meta]
    ).to_json()
    project = api.project.create(workspace_id, project_name)
    api.project.update_meta(project.id, meta)

    for ds_name, ds_path in dataset_names.items():
        dataset = api.dataset.create(project.id, ds_name)
        subfolders = [
            f.path
            for f in os.scandir(os.path.join(dataset_path, ds_path, "JPEGImages"))
            if f.is_dir()
        ]
        json_path = os.path.join(dataset_path, (ds_path + "_expression_meta.json"))
        captions = extract_captions(json_path)
        count_dict = count_objects(json_path)
        # print(count_dict)
        pbar = tqdm.tqdm(total=len(subfolders), desc=f"Processing {ds_name} dataset...")
        for subfolder in subfolders:
            subfolder_name = os.path.basename(subfolder)
            img_paths = glob(os.path.join(subfolder, "*.jpg"))
            # progress = sly.Progress("Create dataset: {}".format(subfolder_name), len(img_paths))
            for img_paths_batch in sly.batched(img_paths):
                img_names_batch = [
                    (subfolder_name + "_" + sly.fs.get_file_name_with_ext(img_path))
                    for img_path in img_paths_batch
                ]
                img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_paths_batch)
                img_ids = [img_info.id for img_info in img_infos]
                tag_values = (subfolder_name, captions.get(subfolder_name))
                anns = [
                    create_ann(img_path, tag_values, count_dict.get(subfolder_name))
                    for img_path in img_paths_batch
                ]
                api.annotation.upload_anns(img_ids, anns)
            pbar.update(1)
        pbar.close()
    return project
