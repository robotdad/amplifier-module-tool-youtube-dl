"""
Amplifier YouTube-DL Tool Module

Download audio and video from YouTube with metadata extraction.
"""

from .audio_utils import AudioExtractor
from .core import VideoInfo, VideoLoader
from .youtube_tool import YouTubeDLTool

__all__ = ["YouTubeDLTool", "VideoInfo", "VideoLoader", "AudioExtractor"]
