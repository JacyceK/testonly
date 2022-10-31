from yt_concate.pipeline.steps.getvideolist import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight()

    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)

if __name__ == '__main__':
    main()