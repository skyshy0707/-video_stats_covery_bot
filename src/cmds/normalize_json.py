import argparse
import asyncio
import json

from core import schemes
from db import dao


async def load_records(file: str):
    with open(file, "r") as file:
        data = json.loads(file.read())
        videos = data.get("videos")

        for video in videos:
            video = schemes.Video(**video)
            await dao.create_creator(id=video.creator_id)
            await dao.create_video(video)
            for snapshot in video.snapshots:
                await dao.create_snapshot(snapshot)


parser = argparse.ArgumentParser(
    description="json_data_normalize"
)
parser.add_argument("filename")

if __name__ == "__main__":
    args = parser.parse_args()
    asyncio.run(load_records(args.filename))