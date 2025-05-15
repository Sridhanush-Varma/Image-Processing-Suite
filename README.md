# Image Processing Suite

A powerful and user-friendly image processing application that provides various image manipulation and enhancement features. Built with Python and popular image processing libraries.

## 🚀 Features

### Basic Operations
- Image loading and saving in multiple formats (PNG, JPG, JPEG, BMP)
- Resize and rotate images
- Crop functionality
- Flip (horizontal/vertical)

### Enhancement Tools
- Brightness adjustment
- Contrast manipulation
- Gamma correction
- Sharpness control
- Blur effects (Gaussian, Motion)
- Noise reduction

### Filters
- Grayscale conversion
- Black & White threshold
- Sepia tone
- Edge detection (Sobel, Canny)
- Emboss effect
- Negative image

### Advanced Features
- Histogram equalization
- Color balance
- Red-eye removal
- Image compression
- Watermark addition
- Batch processing

## 🛠️ Technical Stack

- **Python 3.8+**
- **Libraries:**
  - OpenCV (cv2)
  - NumPy
  - Pillow (PIL)
  - scikit-image
  - matplotlib

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/username/image-processing-suite.git

# Navigate to project directory
cd image-processing-suite

# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For Unix/MacOS:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

## 🚦 Getting Started

```python
from image_processor import ImageProcessor

# Initialize processor
processor = ImageProcessor('path/to/image.jpg')

# Apply operations
processor.adjust_brightness(1.2)
processor.apply_gaussian_blur(radius=2)
processor.save_image('output.jpg')
```

## 📂 Project Structure

```
image-processing-suite/
├── src/
│   ├── __init__.py
│   ├── image_processor.py
│   ├── filters.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_processor.py
├── examples/
│   └── demo_images/
├── requirements.txt
└── README.md
```

## 💻 Usage Examples

```python
# Basic image enhancement
processor = ImageProcessor('input.jpg')
processor.auto_enhance()
processor.save_image('enhanced.jpg')

# Apply multiple filters
processor.grayscale()
processor.adjust_contrast(1.5)
processor.apply_edge_detection()
processor.save_image('filtered.jpg')

# Batch processing
processor.batch_process(
    input_dir='input_folder',
    output_dir='output_folder',
    operations=['grayscale', 'sharpen']
)
```

## ⚙️ Configuration

Default settings can be modified in `config.yaml`:
```yaml
default_quality: 95
max_image_size: 4096
supported_formats: ['jpg', 'png', 'bmp']
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📢 Attribution Requirement

If you use this project in any form (website, app, service, or derivative code), you **must** include the following attribution in your documentation, website footer, or credits page:

> Created by Sridhanush Varma – [https://github.com/Sridhanush-Varma/Image-Processing-Suite](https://github.com/Sridhanush-Varma/Image-Processing-Suite)

Thank you for respecting the work that went into this project! 💻✨


## 🎯 Future Improvements

- [ ] GUI implementation
- [ ] Additional filters and effects
- [ ] Video processing capabilities
- [ ] AI-powered image enhancement
- [ ] Cloud storage integration
- [ ] Batch processing optimization

## 📧 Contact

Project Link: [https://github.com/Sridhanush-Varma/Image-Processing-Suite](https://github.com/Sridhanuhs-Varma/Image-Processing-Suite)

## 🙏 Acknowledgments

- OpenCV Documentation
- Python Pillow Contributors
- scikit-image Community
