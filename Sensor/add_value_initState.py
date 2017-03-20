#!/usr/bin/python

# Import the ISStreamer module
from ISStreamer.Streamer import Streamer


def send_value(t):
    # Streamer constructor, this will create a bucket called Python Stream Example
    # you'll be able to see this name in your list of logs on initialstate.com
    # your access_key is a secret and is specific to you, don't share it!
    streamer = Streamer(bucket_name="Temperature Perros-Guirec", bucket_key="VFSWQRTVFX56", access_key="TpxF1xIFECwXn4XuGsGYvHHAhLY1kJHU")
    streamer.log("temp", t)
    streamer.log("temperature Perros-Guirec", t)
    # Once you're finished, close the stream to properly dispose
    streamer.close()

    return

