import os
import glob
import argparse
from PIL import Image, ImageFilter
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import current_process
from tqdm import tqdm

def process_image(args):
    image_path, output_dir, size, blur = args
    worker_name = current_process().name

    try:
        with Image.open(image_path) as img:
            img = img.resize(size)
            img = img.convert("L")
            img = img.filter(ImageFilter.GaussianBlur(blur))

            filename = os.path.basename(image_path)
            output_path = os.path.join(output_dir, filename)
            img.save(output_path)
            return filename
    except Exception as e:
        return f"Error with {image_path}: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Parallel Image Processing Pipeline")
    parser.add_argument("--input", default="input_images", help="Input folder")
    parser.add_argument("--output", default="output_images", help="Output folder")
    parser.add_argument("--size", type=int, nargs=2, default=[256, 256], help="Resize dimensions (width height)")
    parser.add_argument("--blur", type=float, default=2.0, help="Blur radius")
    parser.add_argument("--workers", type=int, default=os.cpu_count(), help="Number of parallel processes (default: number of cores)")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    image_paths = glob.glob(os.path.join(args.input, "*.jpg"))
    task_args = [(path, args.output, tuple(args.size), args.blur) for path in image_paths]

    print("\n🎛️  Settings:")
    print(f"Input folder:  {args.input}")
    print(f"Output folder: {args.output}")
    print(f"Image size:    {args.size[0]}x{args.size[1]}")
    print(f"Blur radius:   {args.blur}")
    print(f"Workers:       {args.workers}\n")

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        results = list(tqdm(executor.map(process_image, task_args), total=len(task_args)))

    print(f"\n✅ Done! Processed {len(results)} images. Check the '{args.output}' folder.")

if __name__ == "__main__":
    main()
