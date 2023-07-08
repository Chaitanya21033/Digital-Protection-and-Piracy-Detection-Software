import cv2

def add_watermark(input_video, output_video, watermark_text, start_time, end_time):
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    frame_number = 0
    start_frame_number = int(start_time * fps)
    end_frame_number = int(end_time * fps)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if start_frame_number <= frame_number <= end_frame_number:
            cv2.putText(frame, watermark_text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        out.write(frame)
        frame_number += 1

    cap.release()
    out.release()

add_watermark(".\\input.mp4", ".\\output.mp4", "My Watermark", 10, 12)
