
# Task 2 – Segment Images and Videos

### (a) Segment a list of local images
- Write code to segment multiple images from a local folder.
- Refer to Ultralytics segmentation docs for code snippets: https://docs.ultralytics.com/tasks/segment/

### (b) Get a video snippet
- Download a short, appropriate video from YouTube or social media.
- Ensure the video content is respectful.

### (c) Split the video into frames
Use `ffmpeg` to extract frames at regular intervals:

```bash
ffmpeg -i input_video.mp4 -vf "fps=5" frames/frame_%04d.jpg
```

This extracts 5 frames per second and saves them in the `frames/` folder.

### (d) Segment extracted frames
- Apply YOLO segmentation on each frame.
- Save the output in a separate folder, e.g., `segmented_frames/`.

### (e) Reconstruct video from segmented frames
Use `ffmpeg` to stitch segmented frames back into a video:

```bash
ffmpeg -framerate 5 -i segmented_frames/frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p output_video_segmented.mp4
```

---

## Have fun and good luck!
