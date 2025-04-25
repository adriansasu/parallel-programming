# Paralel programming with Python. Image editing

Clone the project and mkdir /input_images and /output_images, in the root

To generate mock images and edit, you need to have installed the following packages (and check python version)

```python
  python --version

  python -m pip install Pillow

  pip install tqdm
```

Run to generate images:

```python
python generate_samples.py
```

Run to edit images:

```python
python image_pipeline.py
```

Or with custom editing (custom blur & resize:)

```python
python image_pipeline.py --size 128 128 --blur 4.5
```
