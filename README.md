# Split Youtube Chapters

An example of the timestamps file format:

    0:00 - Intro hello how to approach this video
    1:50 - MODULE 0 START (TensorFlow deep learning fundamentals)
    1:53 - [Keynote] 1. What is deep learning?
    6:31 - [Keynote] 2. Why use deep learning?
    16:10 - [Keynote] 3. What are neural networks?
    26:33 - [Keynote] 4. What is deep learning actually used for?
    35:10 - [Keynote] 5. What is and why use TensorFlow?
    43:05 - [Keynote] 6. What is a tensor?
    46:40 - [Keynote] 7. What we're going to cover
    51:12 - [Keynote] 8. How to approach this course
    56:45 - 9. Creating our first tensors with TensorFlow
    1:15:32 - 10. Creating tensors with tf Variable
    1:22:40 - 11. Creating random tensors
    1:32:20 - 12. Shuffling the order of tensors
    1:42:00 - 13. Creating tensors from NumPy arrays

It will also work when chapter names and timestamps are separated with whitespaces instead of hyphens (-).

## 📦 Build the Docker Image

Clone the repository, navigate to the folder containing the `Dockerfile`, and run:

```bash
docker build -t yourusername/split_youtube_chapters:v1.0 .

Replace yourusername and v1.0 with your preferred image name and tag.

▶️ Run the Container
Place your video file and timestamps.txt inside an input folder on your local machine (e.g., D:/MyVideos/input). Then run the container with:

```bash
docker run -it ^
  -v "D:/MyVideos/input":/app/input ^
  -v "D:/MyVideos/output":/app/output ^
  yourusername/split_youtube_chapters:v1.0

Inside the container, provide the paths when prompted:

```bash
Path to the video file: /app/input/your_video.mp4  
Path to the timestamps file: /app/input/timestamps.txt
The split video clips will be saved in the local output folder you mounted (e.g., D:/MyVideos/output).