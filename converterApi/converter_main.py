from pathlib import Path

from converterApi.compile_page import compile_page
from converterApi.util.file_utils import clear_detect_dir
from converterApi.util.get_parameters import label_txt_to_list
from converterApi.yolov5 import detect

ROOT = Path(__file__).resolve().parents[0]  # Project root directory


def converter_run(test_image_path):
    clear_detect_dir()

    # Detecting classes on uploaded sketch image
    weight_path = Path(ROOT, 'yolov5/last.pt')

    detect.run(source=test_image_path, weights=weight_path, conf_thres=0.75, save_txt=True, save_conf=True)  # Detecting classes on uploaded sketch

    # Reading results from label file to label_list
    label_str = "yolov5/runs/detect/exp/labels/" + test_image_path.split("/")[1].split(".")[0] + ".txt"
    result_label_path = Path(ROOT, label_str)

    labels_list = label_txt_to_list(result_label_path)

    compile_page(labels_list)
