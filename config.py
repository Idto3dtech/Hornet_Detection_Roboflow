import json

with open('roboflow_config.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["KdNVXu0fIn7H8yhfAJ8j"]
    ROBOFLOW_MODEL = config["asian-hornet-detection-a6ael-aogji/2"]
    ROBOFLOW_SIZE = config["584"]
    LOCAL_SERVER = config["false"]
    DATASET_NAME = config["asian-hornet-detection-a6ael-aogji"]
    LAPLACIAN_THRESHOLD = config["300"]
    CONFIDENCE_THRESHOLD = config["0.4"]

if not LOCAL_SERVER:
    infer_url = "".join([
        "https://detect.roboflow.com/" + ROBOFLOW_MODEL,
        "?api_key=" + ROBOFLOW_API_KEY,
        "&name=YOUR_IMAGE.jpg"
    ])
else:
    infer_url = "".join([
        "http://127.0.0.1:9001/" + ROBOFLOW_MODEL,
        "?api_key=" + ROBOFLOW_API_KEY,
        "&name=YOUR_IMAGE.jpg"
    ])

# Construct the URL
image_upload_url = "".join([
    "https://api.roboflow.com/dataset/", DATASET_NAME, "/upload",
    "?api_key=", ROBOFLOW_API_KEY,
    "&name=rabbit.jpg",
    "&split=train"
])
